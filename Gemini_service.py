import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def generate_text(prompt):
    if not prompt:
        return ""
    try:
        # 🛠️ แก้ไขตรงนี้: เปลี่ยนจาก gemini-2.5-flash เป็นโมเดลเวอร์ชันล่าสุด
        model = genai.GenerativeModel("gemini-3.5-flash") 
        
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"เกิดข้อผิดพลาด: {str(e)}"
