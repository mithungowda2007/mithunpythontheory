with open("gagan.txt","w") as file:
    file.write("Gagan , Gowda!")

with open("gagan.txt","r") as file:
    content=file.read()
    print(content)