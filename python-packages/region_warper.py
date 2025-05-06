# import os
# print("YOUR DIRECTORY RN:", os.getcwd())
# os.chdir("./game/python-packages")

# print("YOUR DIRECTORY RN, ONCE AGAIN:", os.getcwd())

def set_warp_to(colour_string):
    # if number_of_lines("nexus.txt") < 2:

    change_specified_line_in_a_txt_file("nexus.txt", 0, colour_string)

    print("yay :3")

    return




def change_specified_line_in_a_txt_file(filename, line_number, text):
    file = open(filename, "r", encoding = "utf-8")
    lines = file.readlines()
    lines[line_number] = text
    file.close()

    file = open(filename, "w", encoding = "utf-8")
    file.writelines(lines)          # <--- MASSIVE CREDITS TO: https://stackoverflow.com/questions/6457253/modifying-a-single-line-in-a-file
    file.close()



    """
    line_counter = 0
    for line in file:
        if (line_counter == line_number):
            line[line_number] = file.writelines(text)
        line_counter += 1
    """
        

    return




def number_of_lines(file):

    file = open("nexus.txt", "r", encoding = "utf-8")

    line_counter = 0

    for line in file:
        line_counter += 1
        
    return line_counter



set_warp_to("JAPI")