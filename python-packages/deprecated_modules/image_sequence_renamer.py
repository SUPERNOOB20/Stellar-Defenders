import os

path = input("Where is your image sequence? \n")

image_sequence_counter = 0

os.chdir(path)

fixed_len = len(os.listdir(path))

list_of_all_files = []

for loop_number in range(0, fixed_len):

    # old_name = (os.listdir(path))[loop_number]
    # new_name = f"{image_sequence_counter}.png"
    
    image_sequence_counter += 1
    list_of_all_files.append((os.listdir(path))[loop_number])

    # os.rename(old_name, new_name)

while len(list_of_all_files) > 0:
    for i in range(0, fixed_len):
        old_name = list_of_all_files[0]
        new_name = f"{i}.png"

        os.rename(src = old_name, dst = new_name)

        list_of_all_files.pop(0)