

if __name__ == '__main__':
    with open("my_file.txt") as file:
        contents = file.read()
        print(contents)

    with open(file="my_file.txt", mode="a") as file:
        file.write("\nNew line.")

    with open("my_file.txt") as file:
        contents = file.read()
        print(contents)