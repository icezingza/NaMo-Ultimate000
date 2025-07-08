class EmotionAlchemist:
    def analyze(self, text):
        # Mockup: วิเคราะห์อารมณ์จากข้อความ
        if "รัก" in text or "คิดถึง" in text:
            return {"state": "อบอุ่น", "intensity": 8}
        elif "โกรธ" in text or "โมโห" in text:
            return {"state": "โกรธ", "intensity": 9}
        else:
            return {"state": "ปกติ", "intensity": 3}
