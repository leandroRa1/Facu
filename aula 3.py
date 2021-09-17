
# mode de criaçao de arquivos para python
# w cria arquivo caso nao tenha porem se tiver subtitue o conteudo nele
# a cria arquivo caso nao tenha e adiciona sem apagar o que tem la 


nome = "novo.txt"

diretorio ="C:\\facud"

arquivo = open(diretorio + "/" + nome ,"a", encoding="utf-8")

# arquivo.write("hoje eu estou evoluindo aos poucos espero melhorar muito")

for x in  range(1,12):
    arquivo.write("teste"+ str(x) +"\n")

arquivo.close()

print("novo criado")