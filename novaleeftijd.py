
def PrintLeeftijd(x):
    if x < 17:
        print('Je bent minderjarig')
    elif x > 18 and x < 45:
        print('Je bent middeljarig')
    elif x > 45 and x < 67:
        print('BOOMER!')
    elif x > 67:
        print('Geniet van je pensioen!')

y = int(input("Do je leeftijd hier: "))
PrintLeeftijd(y)
