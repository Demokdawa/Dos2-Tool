import re

txt1 = open("english_WIP_FRENCH_8.11.19.xml", "r", encoding="utf8")
txt2 = open("english.xml", "r", encoding="utf8")
txt3 = open("french.xml", "r", encoding="utf8")
file1 = txt1.read().split("\n")
file2 = txt2.read()
ctn = 1

for line in file1:
    # print(ctn)
    val = re.search('">(.*)</content>', line)
    ctn = ctn + 1
    if val is not None:
        val_grp = val.group(1)
        match = re.search(str(val_grp), file2)
        if match is not None:
            print(val_grp + ' || ' + str(match))
        else:
            print(match)