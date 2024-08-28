def bank():
    stavka = 0.1
    n = int(input("Сумма вклада?""\n"))
    years = int(input("Срок вклада?""\n"))
    x = n*(1+stavka)**years
    print("Через", years, "лет Вы получаете", round(x) , "рублей")
bank()