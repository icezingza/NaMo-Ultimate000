from typing import Dict, List, Optional
from datetime import datetime, timedelta
import json
from dataclasses import dataclass, asdict
import time

@dataclass
class Memory:
    id: str
    user_id: str
    event: str
    emotion: str
    emotion_intensity: float
    dharma_insight: str
    timestamp: float
    importance: float

    def to_dict(self):
        return asdict(self)

class MemoryService:
    def __init__(self):
        self.memory_store: Dict[str, List[Memory]] = {}
        self._emotion_groups = {
            "sad": ["sadness", "depression", "grief", "loss", "unhappy"],
            "anxious": ["anxiety", "fear", "worry", "stressed", "nervous"],
            "angry": ["anger", "rage", "irritated", "frustrated", "resentment"],
            "happy": ["joy", "happiness", "contentment", "peace", "gratitude"]
        }
        self._emotion_to_group_map = {
            emotion: group
            for group, emotions in self._emotion_groups.items()
            for emotion in emotions
        }

    def store_experience(self, user_id: str, event: str, emotion: str,
                        emotion_intensity: float, dharma_insight: str = ""):
        memory_id = f"{user_id}_{int(time.time()*1000)}"
        memory = Memory(
            id=memory_id,
            user_id=user_id,
            event=event,
            emotion=emotion,
            emotion_intensity=emotion_intensity,
            dharma_insight=dharma_insight,
            timestamp=time.time(),
            importance=emotion_intensity / 10.0
        )

        if user_id not in self.memory_store:
            self.memory_store[user_id] = []

        self.memory_store[user_id].append(memory)
        return memory.to_dict()

    def retrieve_user_context(self, user_id: str, days_back: int = 30) -> List[Dict]:
        if user_id not in self.memory_store:
            return []

        cutoff_time = time.time() - (days_back * 24 * 3600)
        relevant_memories = [
            m for m in self.memory_store[user_id]
            if m.timestamp >= cutoff_time
        ]

        relevant_memories.sort(
            key=lambda x: (x.importance, x.timestamp),
            reverse=True
        )

        return [m.to_dict() for m in relevant_memories]

    def find_linked_memories(self, user_id: str, emotion: str,
                            similarity_threshold: float = 0.7) -> List[Dict]:
        if user_id not in self.memory_store:
            return []

        linked = []
        for memory in self.memory_store[user_id]:
            if memory.emotion.lower() == emotion.lower():
                similarity = 0.9
            elif self._is_related_emotion(memory.emotion, emotion):
                similarity = 0.75
            else:
                similarity = 0.5

            if similarity >= similarity_threshold:
                linked.append({
                    "memory": memory.to_dict(),
                    "similarity_score": similarity
                })

        linked.sort(key=lambda x: x["similarity_score"], reverse=True)
        return linked[:10]

    def _is_related_emotion(self, emotion1: str, emotion2: str) -> bool:
        # ⚡ Bolt: Optimized emotion group lookup from O(n) to O(1)
        # Pre-computed map avoids iterating lists, making lookups constant time.
        group1 = self._emotion_to_group_map.get(emotion1.lower())
        group2 = self._emotion_to_group_map.get(emotion2.lower())
        return group1 is not None and group1 == group2

    def analyze_memory_pattern(self, user_id: str) -> Dict:
        if user_id not in self.memory_store:
            return {"pattern": "no data"}

        memories = self.memory_store[user_id]
        emotion_counts = {}
        total_intensity = 0

        for mem in memories:
            emotion_counts[mem.emotion] = emotion_counts.get(mem.emotion, 0) + 1
            total_intensity += mem.emotion_intensity

        avg_intensity = total_intensity / len(memories) if memories else 0
        most_common_emotion = max(emotion_counts.items(), key=lambda x: x[1])[0] if emotion_counts else "unknown"

        return {
            "total_memories": len(memories),
            "avg_emotional_intensity": round(avg_intensity, 2),
            "most_common_emotion": most_common_emotion,
            "emotion_distribution": emotion_counts,
            "trend": "improving" if len(memories) > 0 and memories[-1].emotion_intensity < avg_intensity else "stable"
        }

memory_service = MemoryService()
