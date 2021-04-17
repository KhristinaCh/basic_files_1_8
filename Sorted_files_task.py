import os

os.chdir(r'D:\Python\basic_files_1_8\sorted files')
path = r'D:\Python\basic_files_1_8\sorted files'

txt_files = []
txt_files_str = []


for root, dirs, files in os.walk(path):
    for file in files:
        if os.path.splitext(os.path.join(path, file))[1] == '.txt':
            txt_files.append(file)
        with open(file, 'r', encoding='utf-8') as f:
            count = 0
            for line in f:
                count += 1
            txt_files_str.append([file, count])


txt_files_str.sort(key=lambda i: i[1])

os.chdir(r'D:\Python\basic_files_1_8')


with open('final.txt', 'w', encoding='utf-8') as f:
    for file in txt_files_str:
        filepath = os.path.join(path, file[0])
        with open(filepath, 'r', encoding='utf-8')as ff:
            f.write(f'{file[0]}\n')
            f.write(f'{str(file[1])}\n')
            f.write(f'{ff.read()}\n')


os.startfile(r'D:\Python\basic_files_1_8\final.txt')
