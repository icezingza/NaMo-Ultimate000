import unittest
from core.identity_engine import NaMoIdentity

class TestIdentity(unittest.TestCase):
    def test_generate_response(self):
        config = type("Config", (), {"core_identity": {"name": "นะโม", "user_title": "พี่", "speech_style": {"ending_particles": ["นะ"]}}})
        identity = NaMoIdentity(config)
        response = identity.generate_response("ทดสอบ", {"state": "ปกติ"})
        self.assertIn("นะ", response)

if __name__ == "__main__":
    unittest.main()
