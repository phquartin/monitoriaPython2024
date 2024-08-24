
def Ex01():
    horas = 0
    minutos = 0
    segundos = int(input("Digite os segundos: "))
    if segundos >= 60:
        minutos = int(segundos / 60)
        segundos = segundos % 60
        if minutos >= 60:
            horas = int(minutos / 60)
            minutos = minutos % 60
    result = str(horas) + ":" + str(minutos) + ":" + str(segundos)
    return result
def Ex02():

    def X():
        num1 = int(input("Digite X: "))
        if num1 >= 1:
            return num1
        else:
            print("X tem que ser maior que 1 ou igual")
            X()
    x = X()
    def Y():
        num2 = int(input("Digite y: "))
        if num2 <= 100:
            return num2
        else:
            print("Y tem que ser menor que 100 ou igual")
            Y()
    y = Y()
    Rafael = (3 * x) * (3 * x) + y * y
    Beto = 2 * (x ** 2) + (y * 5) ** 2
    Carlos = (-100 * x) + y ** 3
    if Rafael > Beto and Rafael > Carlos:
        return "Rafael ganhou"
    elif Rafael < Beto and Beto > Carlos:
        return "Beto ganhou"
    elif Rafael < Carlos and Carlos > Beto:
        return "Carlos ganhou"
    else:
        return "Mas não tem empates..."
