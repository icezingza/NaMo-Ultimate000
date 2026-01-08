from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from typing import Optional
import uvicorn
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

from config import config
from memory_service import memory_service
from emotion_service import emotion_service
from personalization_engine import personalization_engine
from dharma_service import dharma_service
from safety_service import safety_service

app = FastAPI(
    title="NamoNexus MVP",
    description="AI Mental Health Companion with Dharma Engine",
    version="0.1.0"
)

class UserMessage(BaseModel):
    user_id: str
    message: str
    previous_emotion: Optional[str] = None

class HealthCheck(BaseModel):
    status: str
    version: str

@app.get("/health", response_model=HealthCheck)
async def health_check():
    return {
        "status": "healthy",
        "version": "0.1.0"
    }

@app.post("/namo/interact")
async def namo_interact(user_msg: UserMessage):
    user_id = user_msg.user_id
    message = user_msg.message

    try:
        emotion_analysis = emotion_service.analyze_sentiment(message)
        emotion = emotion_analysis['emotion']
        intensity = emotion_analysis['intensity']

        crisis_check = safety_service.detect_crisis(message, user_id, intensity)

        if crisis_check['is_crisis']:
            crisis_response = safety_service.handle_crisis_escalation(
                user_id, message, emotion
            )
            memory_service.store_experience(
                user_id, message, emotion, intensity,
                dharma_insight="⚠️ Crisis detected - Human escalation initiated"
            )
            return crisis_response

        personalized = personalization_engine.generate_personalized_response(
            user_id, emotion, message
        )

        dharma_analysis = dharma_service.apply_four_noble_truths(
            message, emotion, intensity
        )

        final_response = (
            personalized['personalized_response'] + "\n\n" +
            f"🙏 {dharma_analysis['dharmic_path']}"
        )

        safety_check = safety_service.validate_response_safety(final_response)

        if not safety_check['is_safe']:
            final_response = "ผมเข้าใจความรู้สึกของคุณ... โปรดติดต่อที่ปรึกษาสำหรับการช่วยเหลือลึกขึ้น"

        dharma_insight = dharma_analysis.get('dukkha', {}).get('dharma_insight', '')
        memory_service.store_experience(
            user_id, message, emotion, intensity, dharma_insight
        )

        return {
            "user_id": user_id,
            "response": final_response,
            "emotion_detected": emotion,
            "emotion_intensity": intensity,
            "recommendations": personalized['recommendations'],
            "dharma_path": dharma_analysis['magga'],
            "memory_stored": True,
            "crisis_status": "normal"
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/namo/user-context/{user_id}")
async def get_user_context(user_id: str, days: int = 30):
    try:
        context = memory_service.retrieve_user_context(user_id, days_back=days)
        pattern = memory_service.analyze_memory_pattern(user_id)
        return {
            "user_id": user_id,
            "memory_count": len(context),
            "pattern": pattern,
            "recent_memories": context[:5]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/namo/user-pattern/{user_id}")
async def get_user_pattern(user_id: str):
    try:
        pattern = memory_service.analyze_memory_pattern(user_id)
        return pattern
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/namo/analyze-emotion")
async def analyze_emotion(text: str):
    try:
        analysis = emotion_service.analyze_sentiment(text)
        return analysis
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/namo/dharma-guidance")
async def get_dharma_guidance(problem: str, emotion: str = "sadness",
                             intensity: float = 5.0):
    try:
        guidance = dharma_service.apply_four_noble_truths(
            problem, emotion, intensity
        )
        return guidance
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/namo/crisis-check")
async def crisis_check(user_id: str, message: str):
    try:
        analysis = emotion_service.analyze_sentiment(message)
        crisis = safety_service.detect_crisis(message, user_id, analysis['intensity'])
        return crisis
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(
        app,
        host=config.API_HOST,
        port=config.API_PORT,
        reload=config.DEBUG
    )
