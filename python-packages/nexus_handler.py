def change_specified_line_in_a_txt_file(filename, line_number, text):
    file = open(filename, "r", encoding = "utf-8")
    lines = file.readlines()
    lines[line_number] = text + "\n"
    file.close()

    file = open(filename, "w", encoding = "utf-8")
    file.writelines(lines)          # <--- MASSIVE CREDITS TO: https://stackoverflow.com/questions/6457253/modifying-a-single-line-in-a-file
    file.close()

    return