import random
import time


print("*"*20,"MINI GAME RANDOM","*"*20)
print()

songuoi = int(input("Nhập vào số người chơi:"))
soluot = int(input("Nhập vào số lượt muốn chơi:"))
print("*"*10,"Thông Tin Cấu Hình","*"*10)

tuso = int(input("Nhập vào số bắt đầu trong dãy:"))
denso = int(input("Nhập vào số kết thúc trong dãy:"))

if(tuso==denso):
    print("Không Thể Bắt Đầu Và Kết Thúc Cùng Một Số")
    time.sleep(5)
    exit()
elif(tuso>denso):
    print("Không Thể Bắt Đầu Lớn Hơn")
    time.sleep(5)
print()

tong = 0
for x in range(0,songuoi):
    for i in range(0,soluot):
        so=random.randrange(tuso, denso, 1)
        print("{0:>2}".format(so) ,end="\t")
        tong += so
    time.sleep(5)
    print("Tổng:","{0:>3}".format(tong), "Của Người Thứ ",x+1)
    tong=0    
    print()

input()

