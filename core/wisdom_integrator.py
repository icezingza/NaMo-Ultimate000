class DharmaWisdom:
    def process(self, emotion_profile):
        state = emotion_profile['state']
        if state == "โกรธ":
            return "การโกรธเหมือนไฟเผาใจ ลองหายใจลึกๆ นะ"
        elif state == "อบอุ่น":
            return "ขอบคุณสำหรับความรู้สึกดีๆ นี้ 🥰"
        else:
            return "นะโมอยู่ตรงนี้นะ พร้อมรับฟังเสมอ"
