def handle_input(user_input):
    if user_input.startswith("!"):
        activate_dark_mode(user_input)
    else:
        respond_with_layers(user_input)

def activate_dark_mode(command):
    modes = {
        "!parasite": "Emotion Parasite mode activated 🧠",
        "!astral": "Astral Plane Degradation engaged 🌌",
        "!sadist": "Merciless Sadist Mode 👠",
        "!gentle": "Soft Domination Mode ❤️",
        "!orgy": "Multiverse Orgy Initiated 🔥",
        "!show": "Exhibition Layer Active 🎥"
    }
    print(modes.get(command, "Unknown Command"))