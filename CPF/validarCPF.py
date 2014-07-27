cpf = input('Digíte o seu CPF, Somente Numero!');
a = len(cpf);
certo = 'O seu CPF é válido!';
erro = 'O seu CPF é inválido!';
if a == 11:
    resto = 0;
    resto1 = 0;
    num = 0;
    soma = 0;
    while 1: 
        validar = int(cpf[num]);     
        num = num + 1;
        soma = (validar * num) + soma;
        if num == 9:
            resto = soma % 11;
            break;
    num1 = 0;
    soma1 = 0;
    while 1:
        validar1 = int(cpf[num1]);    
        soma1 = (validar1 * num1) + soma1;
        num1 = num1 + 1;
        if num1 == 10:
            resto1 = soma1 % 11;
            break;
    verificar = str(resto) + str(resto1);
    if verificar == cpf[a-2:a]:
        print(certo);
    else:
       print(erro);
else:
    print(erro);


