peso = float(input("Seu peso: " ))
altura = float(input("Sua altura: " ))

imc = peso / altura ** 2

if (imc <= 18.5 ):
    situacao = "Você está abaixo do peso ideal"
elif (18.5 < imc < 24.9):
    situacao = "Parabéns — você está em seu peso normal!"    
elif (25 <= imc < 29.9):
    situacao = "Você está acima de seu peso"
elif (30 <= imc < 34.9):
    situacao = "Obesidade grau I"
elif (35 <= imc < 39.9):
    situacao = "Obesidade grau II"
elif (imc > 40):
    situacao = "Obesidade grau III"
    
print(situacao)
