import cv2

def open_webcam():
    # 웹캠 열기 (0은 기본 카메라, 외장 카메라가 있다면 1, 2 등으로 변경)
    cap = cv2.VideoCapture(0)

    # 카메라가 정상적으로 열렸는지 확인
    if not cap.isOpened():
        print("카메라를 열 수 없습니다.")
        return

    print("웹캠이 켜졌습니다. 종료하려면 'q' 키를 누르세요.")

    while True:
        # 카메라로부터 프레임 읽기
        # ret: 프레임 읽기 성공 여부 (True/False)
        # frame: 읽어온 프레임 이미지
        ret, frame = cap.read()

        if not ret:
            print("프레임을 읽을 수 없습니다. 종료합니다.")
            break

        # 읽어온 프레임을 화면에 표시 (창 이름: 'Webcam')
        cv2.imshow('Webcam', frame)

        # 1ms 동안 키 입력 대기, 'q'를 누르면 반복문 탈출
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # 모든 작업이 끝나면 자원 해제 및 창 닫기
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    open_webcam()
