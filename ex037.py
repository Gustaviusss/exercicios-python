num = int(input('Digite um numero: '))
base = int(input(("para qual base você quer converter? 1:bin 2:oct 3:hex ")))
if base == 1:
    print(bin(num))
elif base == 2:
    print(oct(num))
elif base == 3:
    print(hex(num))
