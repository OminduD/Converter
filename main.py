a=0
b=0
x=0
y=1
while y==1:
 print('******************###########################$$$$$ _Converter_ $$$$$###########################******************')
 print('''
Temperature = 1
Length      = 2
Weight      = 3
''')
 a = int(input('Input Your Converter Type:= '))
 while a >= 4:
    print('Invalid Number')
    a = int(input('Input Your Converter Type Again:= '))
 if a==1:
    print('''################################################_Temperature_################################################
Celsius to Kelvin   = 1
Kelvin to Celsius   = 2
Celsius to Fahr.    = 3
Fahr. to Celsius    = 4
Fahr. to Kelvin     = 5
Kelvin to Fahr.     = 6''')
    b = int(input('Input Your Converter Type:= '))
    while b >= 7:
        print('Invalid Number')
        b = int(input('Input Your Converter Type Again:= '))
    if b==1:
        x = int(input('Input Your Temperature:= '))
        x+=273
        print('Your Temperature:=', x, 'K')
    elif b==2:
        x = int(input('Input Your Temperature:= '))
        x-= 273
        print('Your Temperature:=', x, '`C')
    elif b==3:
        x = int(input('Input Your Temperature:= '))
        x=1.8*x+32
        print('Your Temperature:=', x, '`F')
    elif b==4:
        x = int(input('Input Your Temperature:= '))
        x=0.556*x-17.777
        print('Your Temperature:=', x, '`C')
    elif b==5:
        x = int(input('Input Your Temperature:= '))
        x=1.*x-459.4
        print('Your Temperature:=', x, 'K')
    elif b==6:
        x = int(input('Input Your Temperature:= '))
        x=0.556*x+255.23
        print('Your Temperature:=', x, '`F')
    print('''
Main Menu   = 1
Exit        = 2
''')
    y=int(input('Enter Your Number:= '))
 elif a==2:
    print('''################################################_Length_################################################
Miles to Kilometre  = 1
Kilometre to Miles  = 2
Yard to Metre       = 3
Metre to Yard       = 4
Foot to Metre       = 5
Metre to Foot       = 6
Inch to Centimetre  = 7
Centimetre to Inch  = 8
''')
    b = int(input('Input Your Converter Type:= '))
    while b >= 9:
        print('Invalid Number')
        b = int(input('Input Your Converter Type Again:= '))
    if b==1:
        x = int(input('Input Your Length:= '))
        while x<0:
            print('Please Input Correct Number')
            x = int(input('Input Your Length Again:= '))
        x=1.6*x
        print('Your Length:=', x, 'km')
    elif b==2:
        x = int(input('Input Your Length:= '))
        while x<0:
            print('Please Input Correct Number')
            x = int(input('Input Your Length Again:= '))
        x=x/1.6
        print('Your Length:=', x, 'miles')
    elif b==3:
        x = int(input('Input Your Length:= '))
        while x<0:
            print('Please Input Correct Number')
            x = int(input('Input Your Length Again:= '))
        x=x*1.094
        print('Your Length:=', x, 'm')
    elif b==4:
        x = int(input('Input Your Length:= '))
        while x<0:
            print('Please Input Correct Number')
            x = int(input('Input Your Length Again:= '))
        x=x/1.094
        print('Your Length:=', x, 'yard')
    elif b==5:
        x = int(input('Input Your Length:= '))
        while x<0:
            print('Please Input Correct Number')
            x = int(input('Input Your Length Again:= '))
        x=x*3.281
        print('Your Length:=', x, 'm')
    elif b==6:
        x = int(input('Input Your Length:= '))
        while x<0:
            print('Please Input Correct Number')
            x = int(input('Input Your Length Again:= '))
        x=x/3.281
        print('Your Length:=', x, 'foot')
    elif b==7:
        x = int(input('Input Your Length:= '))
        while x<0:
            print('Please Input Correct Number')
            x = int(input('Input Your Length Again:= '))
        x=x*2.54
        print('Your Length:=', x, 'cm')
    elif b==8:
        x = int(input('Input Your Length:= '))
        while x<0:
            print('Please Input Correct Number')
            x = int(input('Input Your Length Again:= '))
        x=x/2.54
        print('Your Length:=', x, 'inch')
    print('''
Main Menu   = 1
Exit        = 2
''')
    y = int(input('Enter Your Number:= '))

 elif a==3:
    print('''################################################_Weight_################################################
Pound to Kilogram   = 1
Kilogram to Pound   = 2
Carat to Gram       = 3
Gram to Carat       = 4
Ounce to Gram       = 5
Gram to Ounce       = 6
Troy to Gram        = 7
Gram to Troy        = 8
Stone to Kilogram   = 9
Kilogram to Stone   = 10
''')
    b = int(input('Input Your Converter Type:= '))
    while b >= 11:
        print('Invalid Number')
        b = int(input('Input Your Converter Type Again:= '))
    if b==1:
        x = int(input('Input Your Weight:= '))
        while x<0:
            print('Please Input Correct Number')
            x = int(input('Input Your Weight Again:= '))
        x=x/2.205
        print('Your Weight:=', x, 'kg')
    elif b==2:
        x = int(input('Input Your Weight:= '))
        while x<0:
            print('Please Input Correct Number')
            x = int(input('Input Your Weight Again:= '))
        x=x*2.205
        print('Your Weight:=', x, 'pound')
    elif b==3:
        x = int(input('Input Your Weight:= '))
        while x<0:
            print('Please Input Correct Number')
            x = int(input('Input Your Weight Again:= '))
        x=x/5
        print('Your Weight:=', x, 'g')
    elif b==4:
        x = int(input('Input Your Weight:= '))
        while x<0:
            print('Please Input Correct Number')
            x = int(input('Input Your Weight Again:= '))
        x=x*5
        print('Your Weight:=', x, 'carat')
    elif b==5:
        x = int(input('Input Your Weight:= '))
        while x<0:
            print('Please Input Correct Number')
            x = int(input('Input Your Weight Again:= '))
        x=x*28.35
        print('Your Weight:=', x, 'g')
    elif b==6:
        x = int(input('Input Your Weight:= '))
        while x<0:
            print('Please Input Correct Number')
            x = int(input('Input Your Weight Again:= '))
        x=x/28.35
        print('Your Weight:=', x, 'ounce')
    elif b==7:
        x = int(input('Input Your Weight:= '))
        while x<0:
            print('Please Input Correct Number')
            x = int(input('Input Your Weight Again:= '))
        x=x*31.103
        print('Your Weight:=', x, 'g')
    elif b==8:
        x = int(input('Input Your Weight:= '))
        while x<0:
            print('Please Input Correct Number')
            x = int(input('Input Your Weight Again:= '))
        x=x/31.103
        print('Your Weight:=', x, 'troy')
    elif b==9:
        x = int(input('Input Your Weight:= '))
        while x<0:
            print('Please Input Correct Number')
            x = int(input('Input Your Weight Again:= '))
        x=x*6.35
        print('Your Weight:=', x, 'kg')
    elif b==10:
        x = int(input('Input Your Weight:= '))
        while x<0:
            print('Please Input Correct Number')
            x = int(input('Input Your Weight Again:= '))
        x = x/6.35
        print('Your Weight:=', x, 'stone')
    print('''
Main Menu   = 1
Exit        = 2
''')
    y = int(input('Enter Your Number:= '))
