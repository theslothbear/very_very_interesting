'''
В текстовом файле k7-0.txt находится цепочка из символов латинского алфавита A, B, C. Найдите длину самой длинной подцепочки, состоящей из символов C.
'''
s = open('24-1.txt', 'r').readline()
count, max_count = 0, 0
for i in range(len(s)):
	if s[i] == 'C':
		count+=1
		max_count = max(count, max_count)
	else:
		max_count = max(count, max_count)
		count = 0
print(max_count)

'''
В текстовом файле k7a-1.txt находится цепочка из символов латинского алфавита A, B, C, D, E. Найдите длину самой длинной подцепочки, состоящей из символов A, B или C (в произвольном порядке).
'''
s = open('k7a-1.txt', 'r').readline()
count, max_count = 0, 0
for i in range(len(s)):
	if s[i] in ['A', 'B', 'C']:
		count+=1
		max_count = max(count, max_count)
	else:
		max_count = max(count, max_count)
		count = 0
print(max_count)

'''
В текстовом файле k7b-2.txt находится цепочка из символов латинского алфавита A, B, C, D, E, F. Найдите максимальную длину цепочки вида DBACDBACDBAC.... (состоящей из фрагментов DBAC, последний фрагмент может быть неполным).
'''
s = open('k7b-2.txt', 'r').readline()
s2 = 'DBAC' * (len(s)//4 + 1)
count, max_count = 0, 0
for i in range(len(s)):
	if s[i] == s2[count]:
		count+=1
		max_count = max(count, max_count)
	else:
		max_count = max(count, max_count)
		count = 0
print(max_count)

'''
В текстовом файле k7c-2.txt находится цепочка из символов латинского алфавита A, B, C, D, E, F. Найдите количество цепочек длины 3, удовлетворяющих следующим условиям: 
•	1-й символ – один из A, C, E; 
•	2-й символ – один из A, D, F, который не совпадает с первым; 
•	3-й символ – один из A, B, F, который не совпадает со вторым.

'''
s = open('k7c-2.txt', 'r').readline()
count = 0
for i in range(len(s)-2):
	c = s[i:i+3]
	if c[0] in ['A', 'C', 'E'] and c[1] in ['A', 'D', 'F'] and c[1] != c[0] and c[2] in ['A', 'B', 'F'] and c[2] != c[1]:
		count+=1
print(count)

'''
В текстовом файле k7c-6.txt находится цепочка из символов латинского алфавита A, B, C, D, E, F. Найдите количество цепочек длины 3, в которых символы не совпадают.

'''
s = open('k7c-2.txt', 'r').readline()
count = 0
for i in range(len(s)-2):
	c = s[i:i+3]
	if c[0] != c[1] != c[2]:
		count+=1
print(count)
