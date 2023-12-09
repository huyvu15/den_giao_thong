import cv2
import os
import time

# Tạo thư mục label nếu nó chưa tồn tại
if not os.path.exists("ztoi"):
    os.mkdir("ztoi")

cam = cv2.VideoCapture("rtsp://admin:Admin@123@27.72.149.50:1554/profile3/media.smp")

# Tọa độ của góc trên bên trái
tl_x = 461
tl_y = 44
br_x = 521
br_y = 66

# Kích thước hình cắt
width = br_x - tl_x
height = br_y - tl_y

# Tạo biến đếm và thời điểm bắt đầu
count = 0
start_time = time.time()

while True:
    ret, frame = cam.read()

    if not ret:
        break

    # Cắt hình từ tọa độ tl đến br
    cropped_frame = frame[tl_y:br_y, tl_x:br_x]

    cv2.imshow("Cropped Frame", cropped_frame)

    # Lưu ảnh vào thư mục label
    image_filename = os.path.join("ztoi", f"image_3_{count}.jpg")
    cv2.imwrite(image_filename, cropped_frame)
    count += 1

    # Reset thời điểm bắt đầu
    start_time = time.time()

    if count >= 1000:
        break

    if cv2.waitKey(1) == ord("q"):
        break
    time.sleep(1)
    

cv2.destroyAllWindows()
cam.release()
