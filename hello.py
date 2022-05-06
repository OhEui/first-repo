#과제 : 1부터 20까지 반복 하는 과정에서 3의 배수일경우 ,year를 출력하시오
#추과 과제: 5의 배수 일때 , dream 출력
#추과 과제2: 15의 배수일때 ,yeardream 출력
#나머지 모든 경우는 숫자 그대로 출력
print('hello')
for i in range (1,21):
    if  i%5==0:
        print("dream")
    elif i%3==0:
        print("year")
    elif i%3==0 and i%5==0:
        print("yeardream")
    else:
        print(i)



