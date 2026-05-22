def up():
    str=input('Enter the string :- ')
    out=''
    for i in str:
        if 'A'<=i<='Z':
            out+=i
    print(out)

up()
