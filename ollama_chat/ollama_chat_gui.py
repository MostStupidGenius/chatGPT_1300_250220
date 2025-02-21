import subprocess
import tkinter as tk
from tkinter import scrolledtext
from tkinter import font
from config import OLLAMA_PATH, MODEL_NAME

def send_message():
    user_input = entry.get()
    if user_input.lower() == '종료':
        window.quit()
    
    # ollama 모델에 입력 전달
    result = subprocess.run([OLLAMA_PATH, 'run', MODEL_NAME, user_input], capture_output=True, text=True, encoding='utf-8')
    
    # 모델의 응답 출력
    if result.stdout:
        chat_area.config(state=tk.NORMAL)
        chat_area.insert(tk.END, "당신: " + user_input + "\n")
        chat_area.insert(tk.END, "Ollama: " + result.stdout.strip() + "\n")
        chat_area.config(state=tk.DISABLED)
    else:
        chat_area.config(state=tk.NORMAL)
        chat_area.insert(tk.END, "Ollama: 응답이 없습니다.\n")
        chat_area.config(state=tk.DISABLED)
    
    entry.delete(0, tk.END)

def apply_font_size():
    # 슬라이더의 값에 따라 폰트 크기 적용
    new_size = font_size_slider.get()
    text_font.config(size=new_size)

# GUI 설정
window = tk.Tk()
window.title("Ollama Chat")

# 최소 창 크기 설정
window.minsize(400, 300)

# 기본 폰트 크기 설정
text_font = font.Font(size=12)

# 대화창 설정
chat_area = scrolledtext.ScrolledText(window, state='disabled', width=50, height=10, font=text_font)
chat_area.pack(pady=10, expand=True, fill=tk.BOTH)  # 내용에 따라 크기 조정

entry = tk.Entry(window, width=50, font=text_font)
entry.pack(pady=10)
entry.bind("<Return>", lambda event: send_message())  # Enter 키로 메시지 전송

send_button = tk.Button(window, text="전송", command=send_message)
send_button.pack(pady=5)

# 폰트 크기 조정 슬라이더 추가
font_size_slider = tk.Scale(window, from_=8, to=30, orient=tk.HORIZONTAL, label="폰트 크기")
font_size_slider.set(12)  # 기본 폰트 크기 설정
font_size_slider.pack(pady=10)

# 적용 버튼 추가
apply_button = tk.Button(window, text="적용", command=apply_font_size)
apply_button.pack(pady=5)

window.mainloop() 