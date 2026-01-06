from typing import Dict, List
from transformers import pipeline

class EmotionService:
    def __init__(self):
        # ⚡ Bolt: Lazily load the model to speed up application startup.
        # The model will be loaded on the first call to analyze_sentiment.
        self.emotion_classifier = None

    def analyze_sentiment(self, text: str) -> Dict:
        if self.emotion_classifier is None:
            self.emotion_classifier = pipeline(
                "sentiment-analysis",
                model="distilbert-base-uncased-finetuned-sst-2-english"
            )
        try:
            result = self.emotion_classifier(text[:512])[0]
            sentiment = result['label']
            score = result['score']

            emotion_map = {
                "POSITIVE": "joy",
                "NEGATIVE": "sadness"
            }

            emotion = emotion_map.get(sentiment, "neutral")
            intensity = score if sentiment == "NEGATIVE" else (1 - score)

            return {
                "emotion": emotion,
                "intensity": round(intensity * 10, 2),
                "confidence": round(score, 3),
                "raw_sentiment": sentiment
            }
        except Exception as e:
            return {
                "emotion": "unknown",
                "intensity": 5.0,
                "confidence": 0.0,
                "error": str(e)
            }

    def detect_emotion_shift(self, previous_emotion: str,
                            current_emotion: str) -> Dict:
        shift_patterns = {
            ("sadness", "hope"): "positive_breakthrough",
            ("anxiety", "calm"): "anxiety_relief",
            ("anger", "peace"): "anger_resolution",
            ("despair", "determination"): "motivation_found",
            ("joy", "sadness"): "emotional_decline",
        }

        shift_key = (previous_emotion.lower(), current_emotion.lower())
        shift_type = shift_patterns.get(shift_key, "emotion_change")

        return {
            "from_emotion": previous_emotion,
            "to_emotion": current_emotion,
            "shift_type": shift_type,
            "positive_shift": shift_type in [
                "positive_breakthrough",
                "anxiety_relief",
                "anger_resolution",
                "motivation_found"
            ]
        }

    def generate_dharma_insight_from_emotion(self, emotion: str,
                                            intensity: float) -> str:
        insights = {
            "sadness": [
                "ทุกข์นี้ไม่เที่ยง... มันจะเปลี่ยนแปลง",
                "ความเศร้าคือครูที่สอนให้รู้คุณค่า",
                "อนุญาตให้ตัวเองเศร้า... นั่นคือการยอมรับ"
            ],
            "anxiety": [
                "ความกังวลเกิดจากอนาคต... ปัจจุบันนี้ปลอดภัย",
                "ปล่อยวางการควบคุม เรียนรู้ที่จะเชื่อใจ",
                "ความกลัวบ่งชี้ว่าคุณดูแลตัวเอง"
            ],
            "anger": [
                "โครธคือสัญญาณที่บอกว่ามีขอบเขตถูกลั่วง",
                "แปลงความโกรธเป็นเอนร์จี่สำหรับการเปลี่ยนแปลง",
                "โครธที่เข้าใจแล้ว จะกลายเป็นพลังที่ชาญฉลาด"
            ],
            "joy": [
                "ความสุขชั่วขณะ... ซาบซึ้งด้วยสติ",
                "ความสุขที่แบ่งปัน จึงเพิ่มพูนขึ้น",
                "ขอบคุณสำหรับช่วงเวลาที่ดีนี้"
            ]
        }

        emotion_insights = insights.get(emotion.lower(), [
            "ทุกอารมณ์คือข้อมูล ไม่ใช่ความจริง",
            "สังเกตด้วยสติ ไม่ต้องตัดสิน"
        ])

        if intensity > 7:
            return emotion_insights[0]
        elif intensity > 4:
            return emotion_insights[1] if len(emotion_insights) > 1 else emotion_insights[0]
        else:
            return emotion_insights[-1]

emotion_service = EmotionService()
