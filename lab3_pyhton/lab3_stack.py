
#Сложность - O(n^2)

tags = input('Enter subsequence of tags: ')
stack = []
temp = ''

for i in tags:
	if (i != '<') and (i != '/'):
		if i != '>':
			temp += i
		else:
			if len(stack) == 0:
				stack.append(temp)
				temp = ''
			elif stack[-1] != temp:
				stack.append(temp)
				temp = ''
			else:
				stack.pop()
				temp = ''
				

if(len(stack) == 0):
	print('Синтаксическая ошибка в последовательности тегов отсутсвует!')
else:
	if(stack[0] == stack[-1]):
		stack.pop(0)
		stack.pop(-1)
	print(f'Ошибка где-то в следующих тегах: {stack}')

