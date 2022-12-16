# 코드 내 특정 단어 변환 필요할 때 string으로 읽어서 일괄 변환
# 변수명 align 필요할 시 사용


with open("path/to/old_function.py") as f:
    content = f.read()

word_dict = {"'col1'":"'new_col1'", "'col2'":"'new_col2"}    
    
for old_col, new_col in word_dict.items():
    new_content = content.replace(old_col, new_col)

    with open("path/to/new_function.py"%i, "w") as f:
        f.write(new_content)
