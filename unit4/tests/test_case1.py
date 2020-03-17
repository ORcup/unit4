file_name='wordcount.txt'
line_count=0
word_count=0
character_count=0
with open(file_name,'r',encoding='utf-8') as f:
    for line in f:
        word=line.split()
        line_count+=1
        word_count+=len(word)
        character_count+=len(line)
print('行数：',line_count)
print('单词数：',word_count)
print('字母数：', character_count)

def positive():
    if line_count > 0 and word_count > 0 and character_count > 0:
        return 1
    else:
        return 0

def test_positve():
    assert positive() == 1
