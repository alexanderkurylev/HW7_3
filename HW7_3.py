import os
direct = [[os.path.join(os.getcwd(), '1.txt')], [os.path.join(os.getcwd(), '2.txt')], [os.path.join(os.getcwd(), '3.txt')]]
#file_path1 = os.path.join(os.getcwd(), '1.txt')
#file_path2 = os.path.join(os.getcwd(), '2.txt')
#file_path3 = os.path.join(os.getcwd(), '3.txt')
file_path4 = os.path.join(os.getcwd(), '4.txt')
counter = []
with open(direct[0][0], 'rt', encoding='UTF-8') as file1:
    counter1 = 0
    for line in file1:
        counter1 += 1
counter += [counter1]
with open(direct[1][0], 'rt', encoding='UTF-8') as file2:
    counter2 = 0
    for line in file2:
        counter2 += 1
counter += [counter2]
with open(direct[2][0], 'rt', encoding='UTF-8') as file3:
    counter3 = 0
    for line in file3:
        counter3 += 1
counter += [counter3]
print(counter)
counter4 = []
for id, i in enumerate(counter):
    counter4 += [[i, id+1]]
sc = sorted(counter4)
print(sc)
print(len(counter4))
for num in sc:
    print(num[1])
    with open(direct[num[1]-1][0], 'rt', encoding='UTF-8') as new_file1:
    #with open(os.path.join(os.getcwd(), '3.txt'), 'rt', encoding='UTF-8') as new_file1:
        with open(file_path4, 'a', encoding='UTF-8') as new_file:
            new_file.write(f'{num[1]}.txt\n')
            new_file.write(f'{num[0]}\n')
            new_file.write(f'{new_file1.read()}\n')





