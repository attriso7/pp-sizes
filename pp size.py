# i was just bored and wanted to practice the if-else-elif statement i just learned
# so i made this fun line of code for this
# do get offended if you must as this are my views!!
try:
    siz = float(input("What's your pp size!!\nshh it will be a secret \n\n>> "))
    sizee = f'{siz} inches'
    size = sizee
except:
    print("Please put a numeric value.. Bitch!!\n have some fuckin sence")
    quit()

if siz < 1:
    print("You kidding me right?\n Right!!")
elif siz < 2:
    print(f' {sizee},!! You a fuckin child or what mate?')
elif siz < 3:
    print(f" {sizee},!! That didn't quite grew.. did it?")
elif siz < 4:
    print(f" {sizee},!! You are barely there young man")
elif siz < 5:
    print(f"{sizee},!! erected or without erection?")
elif siz < 6:
    print(f"{sizee},!! Ahh she starts to feel it..")
elif siz < 7:
    print(f"{sizee},!! uhh average")
elif siz < 8:
    print(f"{sizee},!! that's the golden number ma man")
elif siz < 9:
    print(f"{sizee},!! IT's started hurting.. Ahh..")
elif siz < 10:
    print(f"{sizee},!! You monster")

else : print("That's out of my scale")

quit()
