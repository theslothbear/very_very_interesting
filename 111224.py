s = input()

res = s[0]
for i in range(1, len(s)-1):
	#нечетное
	j, el = 1, s[i]
	while s[i-j] == s[i+j]:
		el = s[i-j] + el + s[i+j]
		if i == j or i+j == len(s)-1:
			break
		j+=1
	if len(el) > len(res):
		res = el
	#четное
	if s[i] == s[i+1]:
		j, el = 1, s[i] + s[i+1]
		while s[i-j] == s[i+j+1]:
			el = s[i-j] + el + s[i+j+1]
			if i == j or i+j+1 == len(s)-1:
				break
			j+=1
		if len(el) > len(res):
			res = el

print(res)
