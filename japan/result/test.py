import json

fh = open('result_comment.txt')
comment_dict = fh.readlines()
for line in comment_dict:
    print line
    line_dict = json.loads(line)
    print line_dict
    for item in line_dict:
        print line_dict[item]
    break
    