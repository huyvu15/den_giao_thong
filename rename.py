import os

# Đường dẫn tới thư mục "Evening1"
evening_directory = 'Afternoon'

# Kiểm tra xem thư mục tồn tại hay không
if os.path.exists(evening_directory):
    # Lấy danh sách tất cả các tệp trong thư mục
    files = os.listdir(evening_directory)
    # Sắp xếp danh sách tệp để đảm bảo thứ tự đúng
    files.sort()

    # Khởi tạo biến đếm
    count = 100

    # Lặp qua từng tệp trong danh sách
    for file_name in files:
        # Kiểm tra nếu tệp là tệp thực sự, không phải thư mục
        if os.path.isfile(os.path.join(evening_directory, file_name)):
            # Tạo tên mới cho tệp
            new_name = f'img{count}.jpg'

            # Kiểm tra xem tên mới đã tồn tại chưa, nếu có thì tăng biến đếm
            while os.path.exists(os.path.join(evening_directory, new_name)):
                count += 1
                new_name = f'img{count}.jpg'

            new_path = os.path.join(evening_directory, new_name)

            # Đổi tên tệp
            os.rename(os.path.join(evening_directory, file_name), new_path)

            # Tăng biến đếm lên 1
            count += 1

    print("Đã đổi tên tất cả các tệp thành công.")
else:
    print(f"Thư mục '{evening_directory}' không tồn tại.")
