from typing import Dict

class DharmaService:
    def __init__(self):
        self.four_noble_truths = {
            "dukkha": "Suffering exists",
            "samudaya": "Suffering has causes",
            "nirodha": "Suffering can end",
            "magga": "Path to end suffering"
        }

    def apply_four_noble_truths(self, problem: str, emotion: str,
                               intensity: float) -> Dict:
        return {
            "dukkha": self._analyze_dukkha(problem, intensity),
            "samudaya": self._analyze_samudaya(problem, emotion),
            "nirodha": self._analyze_nirodha(problem),
            "magga": self._analyze_magga(problem, emotion),
            "dharmic_path": self._suggest_dharmic_path(emotion, intensity)
        }

    def _analyze_dukkha(self, problem: str, intensity: float) -> Dict:
        return {
            "truth": "ทุกข์นี้มีจริง",
            "validation": f"ความเจ็บปวดของคุณเป็นของจริง (ระดับ {intensity}/10)",
            "dharma_insight": "การยอมรับทุกข์ คือขั้นแรกของการปลดปล่อย",
            "reflection": "คุณรู้สึกถูกต้องที่จะรู้สึกแบบนี้"
        }

    def _analyze_samudaya(self, problem: str, emotion: str) -> Dict:
        cause_patterns = {
            "sadness": "การสูญเสีย การปฏิเสธ การคาดหวังที่ไม่เป็นจริง",
            "anxiety": "ความไม่แน่นอน การพยายามควบคุม การกำหนดจำกัด",
            "anger": "ขอบเขตถูกละเมิด ความรู้สึกไม่เป็นธรรม ความอยุติธรรม",
            "guilt": "ความท้อแท้ ความไม่ยอมรับตนเอง การติเตียน"
        }

        probable_cause = cause_patterns.get(emotion.lower(), "ความต้องการที่ไม่ได้รับ")

        return {
            "truth": "ทุกข์เกิดจากสาเหตุ",
            "probable_cause": probable_cause,
            "dharma_insight": "เมื่อเข้าใจสาเหตุ เราจึงมีพลังเปลี่ยนแปลง",
            "deeper_question": "อะไรคือความปรารถนาที่ยังไม่ได้รับ?"
        }

    def _analyze_nirodha(self, problem: str) -> Dict:
        return {
            "truth": "ทุกข์นี้สามารถสิ้นสุดได้",
            "vision": "คุณอาจไม่สามารถเปลี่ยนแปลงปัญหา แต่คุณสามารถเปลี่ยนแปลงความสัมพันธ์กับมัน",
            "dharma_insight": "การปลดปล่อย คือการปล่อยวางการต่อสู้ ไม่ใช่การยอมแพ้",
            "future_state": "คุณสามารถอยู่ร่วมกับปัญหานี้ได้ โดยไม่ให้มันปกครองใจ"
        }

    def _analyze_magga(self, problem: str, emotion: str) -> Dict:
        eightfold_path = {
            "Right View": "เข้าใจความจริง",
            "Right Intention": "ตั้งใจอย่างสุขมีไมตร",
            "Right Speech": "พูดจาตรวจสอบความจริง",
            "Right Action": "ปฏิบัติตามคุณธรรม",
            "Right Livelihood": "มีชีวิตอย่างสุจริต",
            "Right Effort": "พยายามเพาะเพิ่มสิ่งดี",
            "Right Mindfulness": "สังเกตการณ์ด้วยสติ",
            "Right Concentration": "หมั่นสมาธิ"
        }

        return {
            "truth": "มีทางออก (Noble Eightfold Path)",
            "path": eightfold_path,
            "practical_steps": self._suggest_practical_steps(emotion),
            "dharma_insight": "ทางออกมีอยู่ในทุกช่วงเวลา"
        }

    def _suggest_practical_steps(self, emotion: str) -> list:
        steps = {
            "sadness": [
                "1. ยอมรับความเศร้า (Right View)",
                "2. สมาธิสั้นๆ 5 นาที (Right Concentration)",
                "3. เขียนบันทึกการสูญเสีย (Right Speech to self)",
                "4. ถ้าพร้อม ให้อภัยตัวเอง (Right Action)"
            ],
            "anxiety": [
                "1. สังเกตว่าไม่เป็นจริง (Right View)",
                "2. หายใจลึก 3 ครั้ง (Right Effort)",
                "3. ติดตัวเองกับปัจจุบัน (Right Mindfulness)",
                "4. ทำสิ่งเล็กๆ หนึ่งสิ่ง (Right Action)"
            ],
            "anger": [
                "1. สัญญาของโครธเป็นเสียง (Right View)",
                "2. เดินอย่างรู้สึก (Right Action)",
                "3. ระบายด้วยสติ (Right Speech to self)",
                "4. ปล่อยการต่อสู้ (Right Intention)"
            ]
        }

        return steps.get(emotion.lower(), [
            "1. สังเกตด้วยสติ",
            "2. หายใจเชิงสติ",
            "3. เวลา และการยอมรับ",
            "4. ปล่อยการยึดมั่น"
        ])

    def _suggest_dharmic_path(self, emotion: str, intensity: float) -> str:
        if intensity > 8:
            return "ทุกข์นี้คือการเรียกหา... เรียกหาการเปลี่ยนแปลง เรียกหาจิตสำนึก เรียกหากรรมทีดี"
        elif intensity > 5:
            return "สิ่งที่คุณรู้สึกนี้... คือโอกาส ให้เกิดปัญญา"
        else:
            return "ดำเนินต่อไปด้วยสติ... ยิ่งเบา ยิ่งชาญฉลาด"

dharma_service = DharmaService()
