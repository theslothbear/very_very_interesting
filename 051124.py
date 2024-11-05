'''
В текстовом файле k7-0.txt находится цепочка из символов латинского алфавита A, B, C. Найдите длину самой длинной подцепочки, состоящей из символов C.
'''
s = open('24-1.txt', 'r').readline()
count, max_count = 0, 0
for i in range(len(s)):
	if s[i] == 'C':
		count+=1
	else:
		max_count = max(count, max_count)
		count = 0
print(max_count)
