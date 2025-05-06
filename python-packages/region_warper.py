def set_warp_to(colour_string):
    # if number_of_lines("nexus.txt") < 2:

    change_specified_line_in_a_txt_file("nexus.txt", 0, colour_string)

    # print("yay :3")

    return




def change_specified_line_in_a_txt_file(filename, line_number, text):
    file = open(filename, "r", encoding = "utf-8")
    lines = file.readlines()
    lines[line_number] = text + "\n"
    file.close()

    file = open(filename, "w", encoding = "utf-8")
    file.writelines(lines)          # <--- MASSIVE CREDITS TO: https://stackoverflow.com/questions/6457253/modifying-a-single-line-in-a-file
    file.close()


# set_warp_to("testt")