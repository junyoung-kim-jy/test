basket = 200
#현금 가격
cash = 2000
#카드 가격
card = cash + cash * 0.1
#단건 계산 시 금액
erning = 0
#총 매출액
totalerning = 0

while basket > 0:
#몇개 살지, 결제 방법은 input으로 입력받음
  count = int(input("몇개를 사시겠어요?"))
  pay = str(input("결제 방법을 선택해 주세요"))

#'카드', '현금' 외 입력 시 예외처리는 따로 하지 않음
#카드 결제 시
  if pay == "카드":
    erning = card * count
    basket = basket - count
    print("결제 금액은 %d 원 입니다." %erning)
#현금 결제 시
  else:
    erning = cash * count
    basket = basket - count
    print("결제 금액은 %d 원 입니다." %erning)

  totalerning = totalerning + erning
  print("남은 수량 : %d \n 총 수입 : %d" %(basket, totalerning))
#test