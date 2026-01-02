# Profit or Loss

cp = int(input("Enter a number:-"))
sp = int(input("Enter a number:-"))

if sp>cp:
    print("Profit:",sp-cp)
elif cp>sp:
    print("Loss",cp-sp)
else:
    print("No Profit No Loss")