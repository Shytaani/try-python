name = input('What is your name?\n')
print('Hi, %s.' % name) # フォーマット演算子 https://qiita.com/takahiro_itazuri/items/e585b46d096036bc837f
print('Hi, {0}.'.format(name)) # format関数
print(f'Hi, {name}.') # フォーマット文字列(3.6以上) https://note.nkmk.me/python-f-strings/