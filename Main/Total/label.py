import numpy as np

# xanh 1, do -1, vang 0

# sang = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
#         1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
#         1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 
#         1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, 
#         -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, 
#         -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, 
#         -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, 0.0, 0.0, 0.0, 0.0,
#         0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

sang = [-1]*44 + [1] *43 + [0] * 13

chieu = [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1, 1, 1, -1, -1, -1,
    -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1, 1,
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, 1, 1, -1, -1, -1, -1, -1,
   -1, -1, -1, -1, 1, 1, 1, -1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1, 1, 1 ]

toi = [ 1, 1, -1, -1, -1, -1, -1, -1, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, -1, -1,
    -1, -1, -1, -1, -1, -1, 1, -1, -1, -1, -1, -1, -1, 1, -1, -1, -1, -1, -1, -1,
    -1, -1, -1, -1, 1, -1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1,
    -1, -1, -1, -1, -1, -1, -1, -1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1 ]

# sang = np.array(sang)
# chieu = np.array(chieu)
# # toi = np.array(toi)
# # sangchieu= np.concatenate((sang, chieu))
# data1 = np.concatenate((sang, chieu)) # 2


anh_sang = [1] * 106 + [-1] * 119 + [0] * 30 # 1

anh_chieu = [-1]*110 + [1] *110 + [0] * 30 # 3

anh_toi = [-1]*200 + [1] *200 + [0] * 102

# anh_sang = np.array(anh_sang)
# anh_chieu = np.array(anh_chieu)
# # anh_toi = np.array(anh_toi)
# # sangchieu1= np.concatenate((anh_sang, anh_chieu))
# # data2 = np.concatenate((sangchieu1,anh_toi))
# data = np.concatenate((anh_sang,data1, anh_chieu, anh_toi))



# print(data)
# print(len(data))


# # Cast the data to integers
# data = data.astype(int)

# my_list = list(data)

# # Save 'data' to a text file as integers
# np.savetxt('label1.txt', data, fmt='%d')

# Gộp các danh sách theo thứ tự
ket_qua = anh_sang + sang + chieu + anh_chieu + anh_toi

# In kết quả
print(ket_qua)
print(len(ket_qua))




