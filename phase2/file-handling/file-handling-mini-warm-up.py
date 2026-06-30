with open("data.txt", "w") as txt_file:
    hobbies = ["Coding", "Programming", "Python"]
    txt_file.write("My name is Bins!\n")
    txt_file.write(f"My hobbies are:\n")

    for hobby in hobbies:
        txt_file.write(f"{hobby}\n")

with open("data.txt", "r") as txt_file:
    reader = txt_file.readlines()

    print(reader)
