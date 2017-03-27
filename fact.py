password = "savir"

for i in range(3):
    j = 3
    psw = input("please Enter the Password: ")
    if(psw==password):
        print("Welcome")
        break
    else:
        print("Wrong Password, Attempt left:", j-1)
