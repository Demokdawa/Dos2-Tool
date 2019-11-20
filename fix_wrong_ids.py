import re
txt1 = open("OdinCore_FR.xml", "r", encoding="utf8")
txt2 = open("Good_ids_OdinCore_FR.xml", "r", encoding="utf8")

file1 = txt1.read().split("\n")
file2 = txt2.read().split("\n")
ctn = 0
text = []


def get_line_id(val, line_nb):
    line = file2[line_nb]
    uid_part = re.search('<content contentuid="(.*)">', line)
    text.append('\t' + uid_part.group() + val + '</content>')


def check_lines_ids():
    global ctn
    for line in file1:
        raw_val = re.search('">(.*)</content>', line)
        if raw_val is not None:
            val = raw_val.group(1)
            line_nb = ctn
            get_line_id(val, line_nb)
            ctn = ctn + 1
        else:
            text.append(line)
            ctn = ctn + 1


if __name__ == '__main__':
    check_lines_ids()
    final = "\n".join(text)
    File_object = open(r"test_fixed.xml", "w", encoding="utf-8")
    File_object.write(final)
    File_object.close()




