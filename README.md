# HTTPLogAnalyze
HTTPLogAnalyze เป็นเครื่องมือวิเคราะห์ log ไฟล์ของ HTTP server (เช่น Apache หรือ Nginx) ที่เขียนด้วยภาษา Python โดยมีเป้าหมายเพื่อช่วยให้ผู้ใช้สามารถตรวจสอบพฤติกรรมการเข้าถึงเว็บไซต์ เช่น IP ที่เข้าถึงบ่อยที่สุด, URL ที่ถูกเรียกมากที่สุด, และช่วงเวลาที่มีการเข้าถึงสูงสุด

🔧 คุณสมบัติหลัก
วิเคราะห์ log ไฟล์ในรูปแบบ Common Log Format (CLF)
แสดง:
IP ที่เข้าถึงบ่อยที่สุด
URL ที่ถูกเรียกมากที่สุด
จำนวน request ต่อชั่วโมง
รองรับการแสดงผลแบบกราฟด้วย Matplotlib

📦 การติดตั้ง

1. Clone repository:
   
		git clone https://github.com/nattakaiwan/HTTPLogAnalyze.git
		cd HTTPLogAnalyze

3. ติดตั้ง dependencies:
   
		pip install -r requirements.txt


🚀 วิธีใช้งาน

		python main.py <path_to_log_file>

ตัวอย่าง:

		python main.py access.log


