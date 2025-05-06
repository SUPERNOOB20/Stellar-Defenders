# import os
# print("YOUR DIRECTORY RN:", os.getcwd())
# os.chdir("./python-packages")

# print("YOUR DIRECTORY RN, ONCE AGAIN:", os.getcwd())

def set_warp_to(colour_string):

    file = open("nexus.txt", "r+", encoding = "utf-8")

    if number_of_lines(file) < 2:
        file.write(colour_string)
        print("yay :3")

    file.close()


    return




def number_of_lines(file):

    line_counter = 0

    for line in file:
        line_counter += 1
        
    return line_counter



# set_warp_to("yellow heh")