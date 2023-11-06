# var: str = "Hola"
# print(f'{var:_>10}')
# print(f'{var:_<10}')
# print(f'{var:_^10}')

names: list[str] = ["Alex", "John", "Matthew", "Arthur", "James", "Richard", "Michael", "David"]
names_ord: list[str] = sorted(names, key=len)
for name in names_ord:
    print(f'{name:-^12} ({len(name)})')

# op1 = "1. Comer"
# op2 = "2. Dormir"
# op3 = "3. Jugar"
# print(f"|{op1:<20}|")
# print(f"|{op2:^20}|")
# print(f"|{op3:>20}|")
