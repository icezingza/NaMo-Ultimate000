from typing import Dict, List
from memory_service import memory_service

class PersonalizationEngine:
    def __init__(self):
        pass

    def generate_personalized_response(self, user_id: str,
                                      current_emotion: str,
                                      current_intensity: float) -> Dict:
        """
        Generates a personalized response using pre-calculated emotion data.
        Optimization:
        1. Eliminated redundant call to emotion_service.analyze_sentiment (BERT model).
        2. Consolidated multiple memory lookups into a single call.
        """
        # Consolidated memory insights in a single pass
        insights = memory_service.get_user_insights(user_id, current_emotion, days_back=30)
        user_memories = insights['relevant_memories']
        user_pattern = insights['user_pattern']
        linked_memories = insights['linked_memories']

        base_response = self._generate_base_compassion_response(
            current_emotion,
            current_intensity
        )

        personalized_response = self._enhance_with_context(
            base_response,
            user_memories,
            user_pattern,
            linked_memories,
            current_emotion
        )

        return {
            "personalized_response": personalized_response,
            "emotion": current_emotion,
            "intensity": current_intensity,
            "user_pattern": user_pattern,
            "similar_past_experiences": len(linked_memories),
            "recommendations": self._generate_recommendations(
                current_emotion,
                user_pattern,
                current_intensity
            )
        }

    def _generate_base_compassion_response(self, emotion: str,
                                         intensity: float) -> str:
        responses = {
            "sadness": {
                "high": "ความเศร้าที่คุณรู้สึก... มันสำคัญ ผมรับรู้",
                "medium": "ความเศร้านี้คือส่วนหนึ่งของการเป็นมนุษย์",
                "low": "ความเศร้าก็ผ่านไป เหมือนเมฆในท้องฟ้า"
            },
            "anxiety": {
                "high": "ความกังวลมาแรง... ให้ผมอยู่ตรงนี้กับคุณ",
                "medium": "ความกลัวบ่งชี้ว่าคุณเนื้อใจดูแล",
                "low": "ความวิตกกังวลเพียงเล็กน้อย... ลองหายใจลึก"
            },
            "anger": {
                "high": "โครธนี้ถูกต้อง... ขอบเขตถูกละเมิด",
                "medium": "โครธบ่งชี้ว่ามีอะไรต้องเปลี่ยน",
                "low": "ความรำคาญเล็กน้อย... สังเกตแล้วปล่อย"
            },
            "joy": {
                "high": "ความสุขนี้มาจากไหน... ตัวแสง",
                "medium": "ความพึงพอใจนี้... ซาบซึ้งมันไว้",
                "low": "สามารถหาความยินดีเพิ่มในช่วงนี้"
            }
        }

        emotion_key = emotion.lower()
        intensity_key = "high" if intensity > 7 else ("medium" if intensity > 4 else "low")

        return responses.get(emotion_key, {}).get(intensity_key,
            "ผมรับรู้ความรู้สึกของคุณ... พยายามเข้าใจมัน")

    def _enhance_with_context(self, base_response: str,
                             user_memories: List[Dict],
                             user_pattern: Dict,
                             linked_memories: List[Dict],
                             current_emotion: str) -> str:
        enhancements = []

        if linked_memories:
            past_intensity = linked_memories[0]['memory']['emotion_intensity']
            enhancements.append(
                f"เคยผ่านจุดนี้มาแล้ว... และคุณได้มาได้ (ครั้งที่ {len(linked_memories)})"
            )

        if user_pattern.get('trend') == 'improving':
            enhancements.append("ผมเห็นคุณกำลังเพิ่มขึ้น... ตั้งแต่ที่เรารู้จัก")

        if user_memories:
            most_recent = user_memories[0]
            if most_recent.get('dharma_insight'):
                enhancements.append(f"จำไว้: {most_recent['dharma_insight']}")

        enhanced = base_response
        if enhancements:
            enhanced += "\n\n" + "\n".join(enhancements)

        return enhanced

    def _generate_recommendations(self, emotion: str, user_pattern: Dict,
                                 intensity: float) -> List[str]:
        recommendations = []

        if intensity > 7:
            recommendations.append("ลองการหายใจเชิงสติ: หายใจเข้า 4 วินาที หายใจออก 6 วินาที")
            recommendations.append("เขียนบันทึกสิ่งที่รู้สึก (5-10 นาที)")

        if emotion.lower() == "anxiety":
            recommendations.append("ลองการนั่งสมาธิ 5 นาที")
            recommendations.append("ไปเดินสักครู่นึง หรือยืดเหยียด")

        if user_pattern.get('most_common_emotion') == emotion.lower():
            recommendations.append("ดูเหมือนเรื่องนี้ขึ้นมาบ่อย... อาจต้องพูดกับที่ปรึกษา")

        return recommendations

personalization_engine = PersonalizationEngine()
