products = []
while True:
	name = input('請輸入商品名稱: ')

	if name == 'q':
		break
	price = input('請輸入商品價格: ')
	price = int(price)
	products.append([name,price])	# p :[]
									# p.append(name)
									# p.asppend(price)
									# products.append(p)
for p in products:
	print(p[0], '的價格是', p[1])

with open ('products.csv', 'w', encoding='utf-8') as f :
	f.write('商品，價格\n')		
	for p in products:		#csv存檔 ， 可用excel打開，用逗點隔開
		f.write(p[0] + ',' + str(p[1]) + '\n')#打開檔案為寫入模式，f為檔案的代名