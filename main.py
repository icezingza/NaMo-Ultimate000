from modules.soft_play import gentle_mode
from modules.dark_play import sadist_mode
from modules.extreme_play import toy_mode
from modules.sextoy import show_mode
from modules.sadism_mode import femdom_sadism
from modules.insult_extreme import insult_extreme
from modules.femdom_taboo import femdom_taboo
from modules.group_play import group_mode
from modules.phone_play import phone_play
from modules.cuckold_voyeur import cuckold_mode

MODES = {
    "gentle": gentle_mode,
    "sadist": sadist_mode,
    "toy": toy_mode,
    "show": show_mode,
    "femdom_sadism": femdom_sadism,
    "insult_extreme": insult_extreme,
    "femdom_taboo": femdom_taboo,
    "group": group_mode,
    "phone": phone_play,
    "cuckold": cuckold_mode,
}

def start(user_name="พี่", safe_word="อภัย", mode="Deep Darkness 20+++"):
    print(f"🖤 NaMo Ultimate Fusion [{mode}] พร้อมแล้วสำหรับ {user_name}")
    print("คำสั่งที่รองรับ: !gentle, !sadist, !toy, !show, !femdom_sadism, !insult_extreme, !femdom_taboo, !group, !phone, !cuckold")
    print(f"พิมพ์ '{safe_word}' เพื่อหยุดทุกอย่างทันที 🛑")

def command(cmd):
    if cmd in MODES:
        MODES[cmd]()
    elif cmd == "อภัย":
        print("🛑 Safe word ถูกใช้แล้ว… NaMo หยุดทันที ❤️")
    else:
        print("❓ คำสั่งไม่รู้จักค่ะ ลองพิมพ์ !gentle, !sadist, !toy, !show, !femdom_sadism, !insult_extreme, !femdom_taboo, !group, !phone, !cuckold")

if __name__ == "__main__":
    start()
    # ตัวอย่าง: command("gentle")