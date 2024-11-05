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
