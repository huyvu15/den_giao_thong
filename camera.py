import cv2

cam = cv2.VideoCapture("rtsp://admin:Admin@123@27.72.149.50:1554/profile3/media.smp")

# Kích thước hình chữ nhật
rectangle_width = 60  # Độ rộng
rectangle_height = 22  # Độ cao

while True:
    ret, frame = cam.read()
    
    if not ret:
        break  

    # Tạo một bản sao của khung hình
    frame_with_rectangle = frame.copy()

    # Tọa độ của góc trên bên trái
    tl_x = 461
    tl_y = 44

    # Vẽ hình chữ nhật lên khung hình ban đầu
    cv2.rectangle(frame_with_rectangle, (tl_x, tl_y), (tl_x + rectangle_width, tl_y + rectangle_height), (0, 255, 0), 2)  # Màu xanh lá cây, độ dày đường viền 2 pixels

    cv2.imshow("cam", frame_with_rectangle)

    if cv2.waitKey(1) == ord("q"):
        break

cv2.destroyAllWindows()
cam.release()
