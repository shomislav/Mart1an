import datetime

danasnjiDan = datetime.date.today()

print(danasnjiDan.strftime("%d %B %Y"))

sledecaOpozicija = danasnjiDan + datetime.timedelta(days=780)

#sledeca opozicija se zapravo ne racuna od danasnjeg datuma,
#ali ovo je samo proba kako radi timedelta

print(sledecaOpozicija.strftime("%d %B %Y"))


def sledecaOpozicija():
    # Add 780 days delta.
    return datetime.date.today() + datetime.timedelta(days=780)

print(datetime.date.today())
print(sledecaOpozicija())


nextOpposition = datetime.datetime.strptime("22/05/2016", "%d/%m/%Y").date() #zadata vrednost sledece opozicije
currentDate = datetime.date.today() #danasnji datum
difference = nextOpposition - currentDate #razlika koja kao rezultat ispisuje broj dana do sledece opozicije
print("Shomi se vraca sa Marsa za",difference.days, "dana.")