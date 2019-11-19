import re

txt1 = open("OdinbladePyromancer_Input.xml", "r", encoding="utf8")
txt2 = open("english_base.xml", "r", encoding="utf8")
txt3 = open("french_base.xml", "r", encoding="utf8")
file1 = txt1.read().split("\n")
file2 = txt2.read()
file3 = txt3.read()
text = []
ctn = 0


# Check presence of uid in file3
def retrieve_trad(uid, line):
    global ctn
    match = re.search(f'<content contentuid="{uid}">(.*)</content>', file3, re.MULTILINE)
    if match is not None:
        uid_part = re.search('<content contentuid="(.*)">', line)
        text.append('\t' + uid_part.group() + match.group(1) + '</content>')
        ctn = ctn + 1
    else:
        text.append(line)


# Check presence of string in file2, an pass uid if match
def check_for_existing(str_base, line):
    pat = re.escape('">' + str_base + '</content>')
    match = re.search(f'<content contentuid="(.*){pat}', file2, re.MULTILINE)
    if match is not None:
        uid = match.group(1)
        retrieve_trad(uid, line)
    else:
        text.append(line)


# Parse line by line in file 1
def check_lines():
    for line in file1:
        raw_val = re.search('">(.*)</content>', line)
        if raw_val is not None:
            val = raw_val.group(1)
            if val == '':
                text.append(line)
            if val is not None:
                pass
                check_for_existing(val, line)
        else:
            text.append(line)


if __name__ == '__main__':
    check_lines()
    print('Fixed ' + str(ctn) + ' entries successfully !')
    final = "\n".join(text)
    File_object = open(r"test.xml", "w", encoding="utf-8")
    File_object.write(final)
    File_object.close()

