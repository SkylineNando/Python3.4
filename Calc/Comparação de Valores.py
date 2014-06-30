quat = int(input("Quantidade: "))
valor = int(input("Valor da nota: "))
num = 0
total = 0
while 1:
    num = num + 1
    print ("\n CALCULO %s" %num)
    n = int(input('Digite a quantidade %s:' %num))
    n2 = int(input('Digite o preço unitário %s:' %num))
    n3 = n * n2
    print ("Total %s:" %num, n3)  
    total = total + n3
    if total == valor != quat == num:
        print("VALOR CONFERE", total)
    elif total >= valor or quat == num:
        print("VALOR NÃO CONFERE")
    if total == valor or quat == num: break
