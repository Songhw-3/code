import calcTotalPrice as cal

if __name__ == '__main__':
    flag = True
    goodPrices = []
    goodNames = []
    while flag:
        purchase = int(input('상품을 구매 하시겠습니까? 1.구매, 2.종료 '))

        if purchase == 1:
            name = str(input('구매한 상품의 이름을 입력하세요. ' ))
            goodNames.append(name)
            price = int(input('구매한 상품의 금액을 입력하세요. ' ))
            goodPrices.append(price)
            
        elif purchase == 2:
            result = cal.calcTotalPrice(goodPrices)
            flag = False

    for i in range(len(goodPrices)):
        print(f'{goodNames[i]}: {goodPrices[i]}원')

    print('할인율 : ', result[0], '%')
    print('총합계 ; ', result[1], '원')


    

