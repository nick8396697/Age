driving = input('請問你有沒有開過車? ')
if driving != '有' and driving != '沒有':
	print('只能輸入 有/沒有')
	raise SystemExit #程式終止

age = input('請問你的年齡是? ')
age = int(age)
if driving == '有':
	if age >= 18:
		print('開車要小心唷!')
	else:
		print('奇怪 你怎麼會開過車!!')
elif driving == '沒有':
	if age >= 18:
		print('可以考駕照囉!快去報名考試吧!')
	else:
		print('等到滿18歲就可以去考駕照囉!')
#else:
	#print('只能輸入 有/沒有') (如有 2 3 4 行，則不用這行)
