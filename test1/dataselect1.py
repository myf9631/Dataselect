# lines = open('18101920.192').readlines()
# file = open('18101920192.txt', 'w', encoding='UTF-8')
# for line in lines[7:]:
#     if line == '\n':
#         continue
#     temp = line
#     if temp in lines[168:216]:
#         temp = line
#         temp = temp.strip().split('\t')
#         temp = temp[68:92]
#         # print(temp)
#         temp = ' '.join(temp)
#         print(temp)
#         # print(''.join(temp))
#         file.write(temp + '\n')
# file.close()
import math
lines = open('18100108.024').readlines()
file = open('18100108024.txt', 'w', encoding='UTF-8')
for line in lines[1:]:
    if line == '\n':
        continue
    temp = line
    if temp in lines[285:333]:
       temp = temp.strip().split('\t')
       temp = temp[188:212]
       # print(temp)
       temp =' '.join(temp)
       print(''.join(temp))
       file.write(temp+'\n')
file.close()


# lines = open('18040108000.txt', 'r', encoding='utf-8').readlines()
#     i = 0
#     for line in temp[245:269]:
#          i += 1
#          line = line.strip().split('\t')
#          content = line
#          content = content[429:453]
#          print('\t'.join(content))
#          file.write(''.join(content))
# print("保存成功")
# print(i)


# lines = open('18040108.000').readlines()
# temp = open('18040108000.txt', 'w', encoding='UTF-8')
# file = open('18', 'w')
# for line in lines[7:]:
#     if line == '\n':
#         continue
#     # line = line.strip().split('\t')
#     # print('\t'.join(line))
#     temp.write(''.join(line))
# temp.close()
# print("保存成功")
# lines = open('18040108000.txt', 'r', encoding='utf-8').readlines()
# i = 0
# for line in lines[245:269]:
#     i += 1
#     line = line.strip().split('\t')
#     content = line
#     content = content[429:453]
#     print('\t'.join(content))
#     file.write(' '.join(content)+'\n')
# file.close()
# print(i)
