# Stworzyć funkcję, która będzie sprawdzała czy przekazana liczba w
# parametrze jest parzysta i zwróci tą informację jako typ logiczny bool
# ( True / False ). Należy uruchomić funkcję, wynik wykonania zapisać do
# zmiennej, a następnie wykorzystując warunek logiczny wyświetlić prawidłowy
# tekst "Liczba parzysta" / "Liczba nieparzysta"

def is_even( a: int ) -> bool:
    if a%2 == 0:
        return True
    
x = 10
if is_Even(x):
    print('is Even')
else:
    print('is Odd')


