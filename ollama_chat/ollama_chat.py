import subprocess
from config import OLLAMA_PATH, MODEL_NAME  # config.py에서 설정을 가져옵니다.

def chat_with_ollama():
    print("Ollama와 대화하기 시작합니다. '종료'를 입력하면 종료됩니다.")
    while True:
        user_input = input("당신: ")
        if user_input.lower() == '종료':
            break
        
        # ollama 모델에 입력 전달
        result = subprocess.run([OLLAMA_PATH, 'run', MODEL_NAME, user_input], capture_output=True, text=True, encoding='utf-8')
        
        # 모델의 응답 출력
        if result.stdout:
            print("Ollama: ", result.stdout.strip())
        else:
            print("Ollama: 응답이 없습니다.")

if __name__ == "__main__":
    chat_with_ollama() 