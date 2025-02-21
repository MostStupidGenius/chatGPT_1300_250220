import os
from mutagen import File
from openpyxl import Workbook
from datetime import datetime

def get_audio_metadata(folder_path):
    """음성 파일의 메타데이터를 추출하는 함수"""
    # 결과를 저장할 리스트
    audio_files_data = []
    
    # 지원하는 음성 파일 확장자
    AUDIO_EXTENSIONS = ('.mp3', '.wav', '.m4a', '.flac', '.ogg')
    
    # 폴더 내 모든 파일 검사
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith(AUDIO_EXTENSIONS):
                file_path = os.path.join(root, file)
                
                # 파일 기본 정보 추출
                file_size = os.path.getsize(file_path) / (1024 * 1024)  # MB 단위로 변환
                file_modified = datetime.fromtimestamp(os.path.getmtime(file_path))
                
                # 음성 파일 메타데이터 추출
                try:
                    audio = File(file_path)
                    if audio is not None:
                        duration = audio.info.length  # 재생 시간(초)
                        minutes = int(duration // 60)
                        seconds = int(duration % 60)
                        duration_str = f"{minutes}:{seconds:02d}"
                    else:
                        duration_str = "알 수 없음"
                except:
                    duration_str = "오류"
                
                # 데이터 저장
                audio_files_data.append({
                    '파일명': file,
                    '폴더경로': root,
                    '파일크기(MB)': round(file_size, 2),
                    '재생길이': duration_str,
                    '수정날짜': file_modified.strftime('%Y-%m-%d %H:%M:%S')
                })
    
    return audio_files_data

def save_to_excel(data, output_file):
    """데이터를 엑셀 파일로 저장하는 함수"""
    wb = Workbook()
    ws = wb.active
    ws.title = "음성파일 정보"
    
    # 헤더 추가
    if data:
        headers = list(data[0].keys())
        ws.append(headers)
        
        # 데이터 추가
        for item in data:
            ws.append([item[header] for header in headers])
        
        # 열 너비 자동 조정
        for column in ws.columns:
            max_length = 0
            column_letter = column[0].column_letter
            for cell in column:
                try:
                    if len(str(cell.value)) > max_length:
                        max_length = len(str(cell.value))
                except:
                    pass
            adjusted_width = (max_length + 2)
            ws.column_dimensions[column_letter].width = adjusted_width
    
    # 파일 저장
    wb.save(output_file)

def main():
    # 설정값
    FOLDER_PATH = r"C:\음성파일폴더"  # 음성 파일이 있는 폴더 경로
    OUTPUT_FILE = "음성파일_메타데이터.xlsx"  # 결과 파일명
    
    try:
        print("음성 파일 메타데이터 추출을 시작합니다...")
        
        # 메타데이터 추출
        audio_data = get_audio_metadata(FOLDER_PATH)
        
        if audio_data:
            # 엑셀 파일로 저장
            save_to_excel(audio_data, OUTPUT_FILE)
            print(f"처리 완료! {len(audio_data)}개의 파일 정보를 {OUTPUT_FILE}에 저장했습니다.")
        else:
            print("처리할 음성 파일을 찾지 못했습니다.")
            
    except Exception as e:
        print(f"오류 발생: {str(e)}")

if __name__ == "__main__":
    main() 