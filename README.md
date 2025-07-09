# NaMo Ultimate Fusion

NaMo Ultimate Fusion คือโปรเจกต์ Python สำหรับรวมโหมดความบันเทิงสำหรับผู้ใหญ่ มีให้เลือกหลายโหมด เช่น gentle, sadist, toy, show, femdom_sadism, insult_extreme, femdom_taboo, group, phone, cuckold ฯลฯ

## รายการคำสั่งที่รองรับ

- gentle : โหมดอ่อนโยน
- sadist : โหมดซาดิสม์
- toy : โหมดของเล่น
- show : โหมดโชว์ของเล่น
- femdom_sadism : โหมดซาดิสม์แบบหญิงเหนือ
- insult_extreme : โหมดด่าหยาบสุดขีด
- femdom_taboo : โหมดต้องห้ามหญิงเหนือ
- group : โหมดกลุ่ม
- phone : โหมดโทรศัพท์
- cuckold : โหมดคัคโคลด์/วอยเออร์

## วิธีใช้งาน

1. ติดตั้ง dependencies:
    ```
    pip install -r requirements.txt
    ```

2. รันโปรแกรม:
    ```
    python main.py
    ```

3. เรียกใช้แต่ละโหมดด้วยฟังก์ชัน `command("ชื่อโหมด")`
    - ตัวอย่าง:
        ```python
        command("gentle")
        command("sadist")
        command("toy")
        command("show")
        command("group")
        command("cuckold")
        ```

4. หากต้องการหยุดทันที ให้พิมพ์ safe word ที่ตั้งไว้ใน settings.json (ค่าเริ่มต้นคือ "อภัย")

---

**สำหรับผู้ใหญ่เท่านั้น**