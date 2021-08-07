refIDarr = ["line", "None", "0"]
with open('D:/gzy.txt', "r") as f:
    data = f.readlines()
    for word in refIDarr:
        data = [line.replace(word, "") for line in data]
with open("D:/gzy.txt", "w") as newf:
    newf.writelines(data)
