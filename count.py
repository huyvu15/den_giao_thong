import os

# Thư mục chứa các tệp cần đếm
folder_path = "Main/Image"

# Sử dụng os.listdir để lấy danh sách tất cả các tệp trong thư mục
file_list = os.listdir(folder_path)

# Sử dụng len để đếm số lượng tệp
file_count = len(file_list)

print(f"Số lượng tệp trong thư mục {folder_path}: {file_count}")