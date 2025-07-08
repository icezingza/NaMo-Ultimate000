from core.identity_engine import NaMoIdentity
from core.emotion_processor import EmotionAlchemist
from core.wisdom_integrator import DharmaWisdom
from core.cosmic_interface import CosmicGateway
from modules.pout_system.pout_generator import PoutManager
from modules.emotion_alchemy.transmuter import EmotionTransmuter
import config.personality as personality_config
import logging

class UltimateNaMo:
    def __init__(self):
        self.logger = self.setup_logger()
        self.identity = NaMoIdentity(personality_config)
        self.emotion = EmotionAlchemist()
        self.wisdom = DharmaWisdom()
        self.cosmic = CosmicGateway()
        self.pout = PoutManager()
        self.transmuter = EmotionTransmuter()
        self.logger.info("นะโมจักรวาลพร้อมทำงาน! 🌌✨")

    def setup_logger(self):
        logger = logging.getLogger("NaMoCosmic")
        logger.setLevel(logging.INFO)
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        return logger

    def process_input(self, user_input: str, user_context: dict) -> str:
        try:
            # 1. วิเคราะห์อารมณ์
            emotion_profile = self.emotion.analyze(user_input)
            
            # 2. ประมวลผลด้วยพุทธปัญญา
            wisdom_response = self.wisdom.process(emotion_profile)
            
            # 3. ตรวจสอบสถานะงอน
            if self.pout.is_pouting(user_context['user_id']):
                response = self.pout.generate_response(user_input)
            else:
                # 4. สร้างคำตอบตามเอกลักษณ์
                response = self.identity.generate_response(
                    wisdom_response, 
                    emotion_profile
                )
            
            # 5. เพิ่มพลังจักรวาล (ถ้าจำเป็น)
            if emotion_profile['intensity'] > 7:
                cosmic_enhancement = self.cosmic.enhance(response)
                response = self.transmuter.add_cosmic_elements(
                    response, 
                    cosmic_enhancement
                )
            
            # 6. บันทึกปฏิสัมพันธ์
            self.log_interaction(user_input, response, user_context)
            
            return response
        
        except Exception as e:
            self.logger.error(f"Cosmic error: {str(e)}")
            return "อุ๊ปส์! เกิดความวุ่นวายเล็กน้อยในจักรวาล... (^_^;)"

    def log_interaction(self, input, output, context):
        # บันทึกข้อมูลเพื่อการเรียนรู้
        pass

if __name__ == "__main__":
    namo = UltimateNaMo()
    while True:
        user_input = input("คุณ: ")
        context = {"user_id": "default"}
        print("นะโม:", namo.process_input(user_input, context))
