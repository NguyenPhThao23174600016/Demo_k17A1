Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #bai_1.6:chia deu so keo
>>> alice_candies=eval(input("Nhap so keo alice : "))
Nhap so keo alice : 121
>>> bob_candies=eval(input("Nhap so keo bob : "))
Nhap so keo bob : 77
>>> carol_candies=eval(input("Nhap so keo carol : "))
Nhap so keo carol : 109
>>> to_smash=(alice_candies+bob_candies+carol_candies)%3
>>> print("to smash=",to_smash)
to smash= 1
