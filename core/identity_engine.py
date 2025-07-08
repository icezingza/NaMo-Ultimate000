class NaMoIdentity:
    def __init__(self, config):
        self.name = config.core_identity.get('name', 'นะโม')
        self.user_title = config.core_identity.get('user_title', 'พี่')
        self.speech_style = config.core_identity.get('speech_style', {})

    def generate_response(self, wisdom, emotion):
        ending = self.speech_style.get('ending_particles', ['ค่ะ'])[0]
        return f"{wisdom} [{emotion['state']}] {ending}"
