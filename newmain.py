import re

txt1 = open("english_WIP_FRENCH_8.11.19.xml", "r", encoding="utf8")
txt2 = open("english.xml", "r", encoding="utf8")
txt3 = open("french.xml", "r", encoding="utf8")
file1 = txt1.read().split("\n")
file2 = txt2.read()
file3 = txt3.read()


def retrieve_trad(uid):
    match = re.search(uid, file3)
    if match is not None:
        pass
        # print('Searching for ' + uid + ' SUCESS')
    else:
        pass
        # print('Searching for ' + uid + ' FAILED')


# Check presence of string in file2, an pass uid if match
def check_for_existing(str_base):
    pat = re.escape('">' + str_base + '</content>')
    match = re.search(pat, file2)
    if match is not None:
        match3 = re.search(f'<content contentuid="(.*){pat}', file2, re.MULTILINE)
        if match3 is not None:
            uid = match3.group(1)
            retrieve_trad(uid)


# Parse line by line in file 1
def check_lines():
    for line in file1:
        raw_val = re.search('">(.*)</content>', line)
        if raw_val is not None:
            val = raw_val.group(1)
            if val == '':
                pass
            if val is not None:
                check_for_existing(val)


if __name__ == '__main__':
    check_lines()
