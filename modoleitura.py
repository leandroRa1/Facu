
nome = "novo.txt"

diretorio ="C:\\facud"

arquivo = open(diretorio + "/" + nome ,"r", encoding="utf-8")

ler = arquivo.read()

for x in  ler:
    print(x)

arquivo.close()

