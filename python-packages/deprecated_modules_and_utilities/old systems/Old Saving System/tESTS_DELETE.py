import os
dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)

nexus_textfile = open("nexus.txt", "r")
nexus_file = nexus_textfile.readlines()

region_progress = []
for i in range(1, 16):
    print("LINE:", nexus_file[i])
    plain_text_to_be_appended = nexus_file[i].replace("\n", "")
    region_progress.append(plain_text_to_be_appended)
print(region_progress)
# print(bool(region_progress[3]))
# print(bool(0))
# print(bool('0'))
# print(bool(int('0')))

print(bool(False))
print(bool('False'))
# print(bool(int('True')))

print(float("0.2"))