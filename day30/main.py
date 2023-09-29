# catch exceptions and errors

# key error
# index error
# Type error

# try: - Something that might cause an exception
# except: - Do this if there was an exception
# else: Do this if there were no exceptions
# finally: - Do this no matter what happens


# #file not found
# try:
#     file = open("a_file.txt")
#     a_dict = {"Key":"Value"}
#     print(a_dict["dasdAS"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise TypeError("This is an error that I made up.")
#     # file.close()
#     # print("File was closed")

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not be over 3 meters")

bmi = weight / height ** 2
print(bmi)
