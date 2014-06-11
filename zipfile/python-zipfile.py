import zipfile 
#Importando o arquivo zipfile para execução do aplicativo

f = zipfile.ZipFile('MeuArquivoZipado.zip', 'w')
#Responsavel para criar o arquivo 'ZIP'

f.write('LOCAL ONDE O ARQUIVO ESTA MAMAZENADO')
#Arquivo que será zipado 

f.close()
#Fecha a aplicação
