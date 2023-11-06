Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #bai_1.9:tinh tien lai gui tiet kiem
>>> lai_suat_mot_nam=eval(input("Nhap lai suat mot nam="))
Nhap lai suat mot nam=7.6
>>> so_tien_gui=eval(input("Nhap so tien gui="))
Nhap so tien gui=10000000
>>> so_thang_gui=eval(input("Nhap so thang gui="))
Nhap so thang gui=6
>>> tien_lai=(so_tien_gui*so_thang_gui)*(lai_suat_mot_nam/100/12)
... 
>>> tien_von_lai=so_tien_gui+tien_lai
>>> print("tien lai:",tien_lai)
tien lai: 380000.0
>>> print("tien von+lai:",tien_von_lai)
tien von+lai: 10380000.0
