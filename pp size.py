# I was just bored and wanted to practice the if-else-elif statement I just learned
# so I made this fun line of code for this
# do get offended if you must as this are my views!!

def ppsize():
    if siz < 1:
        return "You kidding me right?\n Right!!"
    elif siz < 2:
        return f' {sizee},!! You a fuckin child or what mate?'
    elif siz < 3:
        return f" {sizee},!! That didn't quite grew.. did it?"
    elif siz < 4:
        return f" {sizee},!! You are barely there young man"
    elif siz < 5:
        return f"{sizee},!! erected or without erection?"
    elif siz < 6:
        return f"{sizee},!! Ahh she starts to feel it.."
    elif siz < 7:
        return f"{sizee},!! uhh average"
    elif siz < 8:
        return f"{sizee},!! that's the golden number ma man"
    elif siz < 9:
        return f"{sizee},!! IT's started hurting.. Ahh.."
    elif siz < 10:
        return f"{sizee},!! You monster"

    else:
        return "That's out of my scale"


try:
    siz = float(input("What's your pp size!!\nshh it will be a secret \n\n>> "))
    sizee = f'{siz} inches'
    size = sizee
except:
    print("Please put a numeric value.. Bitch!!\n have some fuckin sence")
    quit()

print(ppsize())

quit()