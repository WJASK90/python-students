print("Mam na imię...")  # tutaj wpisz swoje imię
# i dodaj jeszcze jakiś ciekawy kod

print("Mam na imię Wojtek")
      
value_1 = int(input("Podaj początek zakresu liczb, sprawdzimy czy są podzielne przez 5 lub 8: "))
value_2 = int(input("Podaj koniec zakresu liczb, sprawdzimy czy są podzielne przez 5 lub 8: "))
for i in range(value_1,value_2):
    if i % 5 == 0:
        print(i)
    elif i % 8 == 0:
        print(i)
    else:
        print(end="")

print("Ciekawe, nie?")
