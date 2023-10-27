import cv2
import os
import time
import tkinter as tk

# Tạo thư mục label nếu nó chưa tồn tại
if not os.path.exists("label"):
    os.mkdir("label")

cam = cv2.VideoCapture("rtsp://admin:Admin@123@27.72.149.50:1554/profile3/media.smp")

# Kích thước hình chữ nhật
rectangle_width = 60  # Độ rộng
rectangle_height = 22  # Độ cao

# Tạo biến đếm và thời điểm bắt đầu
count = 0
capturing = False

def start_capture():
    global capturing
    capturing = True

def stop_capture():
    global capturing
    capturing = False

root = tk.Tk()
root.title("Image Capture")

start_button = tk.Button(root, text="Start Capture", command=start_capture)
start_button.pack()

stop_button = tk.Button(root, text="Stop Capture", command=stop_capture)
stop_button.pack()

while True:
    ret, frame = cam.read()

    if not ret:
        break

    if capturing:
        # Tạo một bản sao của khung hình
        frame_with_rectangle = frame.copy()

        # Tọa độ của góc trên bên trái
        tl_x = 461
        tl_y = 44

        # Vẽ hình chữ nhật lên khung hình ban đầu
        cv2.rectangle(frame_with_rectangle, (tl_x, tl_y), (tl_x + rectangle_width, tl_y + rectangle_height), (0, 255, 0), 2)  # Màu xanh lá cây, độ dày đường viền 2 pixels

        cv2.imshow("cam", frame_with_rectangle)

        # Tính toán tọa độ của đối tượng trong hình chữ nhật
        x = tl_x
        y = tl_y
        w = rectangle_width
        h = rectangle_height

        # Kiểm tra xem đối tượng có nằm trong hình chữ nhật không
        if x <= tl_x <= x + w and y <= tl_y <= y + h:
            # Lưu ảnh vào thư mục label
            image_filename = os.path.join("label", f"image_{count}.jpg")
            cv2.imwrite(image_filename, frame)
            count += 1

        if count >= 100:
            stop_capture()

    if cv2.waitKey(1) == ord("q"):
        break

    root.update()  # Cập nhật giao diện người dùng

cv2.destroyAllWindows()
cam.release()
