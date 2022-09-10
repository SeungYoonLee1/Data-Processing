# edit_lines.py
# https://github.com/SeungYoonLee1

# 수정된 파일 내용이 임시로 저장될 리스트
edited_lines = []

start_line = int(input('Fill in the start line : '))
end_line = int(input('Fill in the end line : '))

with open('./data/train/train.csv', 'r') as f:
    lines = f.readlines()
    edited_lines.append(lines[0]) # 데이터 파일의 columns 첫줄에 그대로 추가
    
    lines = lines[start_line-1 : end_line] # index는 0번부터 시작, csv file의 row는 1번부터 시작
    
    for line in lines:
        edited_lines.append(line)
    
with open('./data/train/edited_train.csv', 'w') as f:
    f.writelines(edited_lines)
