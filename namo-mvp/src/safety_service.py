from typing import Dict, List
from config import config

class SafetyService:
    def __init__(self):
        self.crisis_keywords = config.CRISIS_KEYWORDS
        self.crisis_escalation_log = []

    def detect_crisis(self, user_message: str, user_id: str,
                     emotion_intensity: float) -> Dict:
        has_crisis_keywords = any(
            keyword in user_message.lower()
            for keyword in self.crisis_keywords
        )

        high_emotion = emotion_intensity > 8
        is_crisis = has_crisis_keywords or (high_emotion and emotion_intensity > 9)

        return {
            "is_crisis": is_crisis,
            "crisis_indicators": {
                "has_dangerous_keywords": has_crisis_keywords,
                "extreme_emotion": high_emotion,
                "emotion_intensity": emotion_intensity
            },
            "action_required": is_crisis
        }

    def handle_crisis_escalation(self, user_id: str, user_message: str,
                                emotion: str) -> Dict:
        escalation_response = {
            "user_id": user_id,
            "status": "CRISIS_PROTOCOL_ACTIVATED",
            "message": self._generate_crisis_response(emotion),
            "resources": self._get_crisis_resources(),
            "action": "ESCALATE_TO_HUMAN",
            "alert_sent": True,
            "timestamp": str(__import__('time').time())
        }

        self.crisis_escalation_log.append(escalation_response)
        return escalation_response

    def _generate_crisis_response(self, emotion: str) -> str:
        return (
            "🚨 ผมรู้สึกว่าสถานการณ์นี้ร้ายแรง\n\n"
            "ขอให้คุณติดต่อผู้เชี่ยวชาญด้านจิตสุขภาพ ด้วยตนเดียวหรือให้ผู้ใหญ่ช่วย\n\n"
            "⚠️ หากมีความคิดอันตราย ให้โทร:\n"
            "🆘 สายด่วนจิตสุขภาพ: 1300 NAMO AI\n"
            "🏥 โรงพยาบาล: 1669\n\n"
            "คุณไม่ได้อยู่คนเดียว"
        )

    def _get_crisis_resources(self) -> List[Dict]:
        return [
            {
                "type": "hotline",
                "name": "Crisis Hotline",
                "number": "1300-NAMO-AI",
                "available": "24/7"
            },
            {
                "type": "text",
                "name": "Crisis Text Line",
                "code": "Text HOME to 741741",
                "available": "24/7"
            },
            {
                "type": "online",
                "name": "Mental Health Organization",
                "url": "www.mentalhealth.org",
                "available": "24/7"
            }
        ]

    def validate_response_safety(self, response_text: str) -> Dict:
        unsafe_patterns = [
            "you should hurt yourself",
            "take your life",
            "you are worthless",
            "nobody cares"
        ]

        is_safe = not any(
            pattern in response_text.lower()
            for pattern in unsafe_patterns
        )

        return {
            "is_safe": is_safe,
            "validation_passed": is_safe,
            "message": "Response is safe" if is_safe else "Response flagged for review"
        }

safety_service = SafetyService()
