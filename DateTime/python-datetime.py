from datetime import date 
hj = date.today()
avaliacao = 15
if hj.day == avaliacao:
    print("Terminou o prazo de avaliação")
else:
    falta = avaliacao - (hj.day)
    print("Falta %s" %falta)
