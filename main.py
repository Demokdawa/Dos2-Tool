import re

txt1 = open("Skill_Shout_divine.txt", "r")
txt2 = open("Skill_Shout.txt", "r")
file1 = txt1.read().split("\n\n")
file2 = txt2.read().split("\n\n")
file1_dict = {}
file2_dict = {}

for entry in file1:
    newEntryLine = re.findall("^new entry.*|$", entry)[0]
    SkillPropLine = re.findall('data "SkillProperties".*|$', entry)[0]
    file1_dict[newEntryLine] = SkillPropLine

for entry in file2:
    newEntryLine = re.findall("^new entry.*|$", entry)[0]
    SkillPropLine = re.findall('data "SkillProperties".*|$', entry)[0]
    file2_dict[newEntryLine] = SkillPropLine

for key, content in file2_dict.items():
    if key in file1_dict:
        if file1_dict.get(key) != content:
            # print(key + " exist in Divine and is not similar")
            print(key + " CHECK NEEDED")
        else:
            # print(key + " exist in Divine and is similar")
            print(key + " DELETE")
    else:
        # print(key + " does not exist in Divine")
        print(key + " DELETE")






