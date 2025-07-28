print(" minha lista de desejos para o futuro ")

  NOME DO ARQUIVO = "meus_desejos.txt "
desjos = [] # lista vazia para amazenar os desejos 

with open (NOME_ARQUIVO, 'r', encodgn= 'utf-8') as arquivo:
  for linha in arquivo:
     desejos.append(linha.strip())
print(f"meus desejos foram carregados do arquivo '{NOME_ARQUIVO}' !\n ")
except FileNotFoundError:
 print ("parece que é a sua primeira vez! vamos criar sua lista de desejos. \n")
except except as e:
print (f"ocorreu um erro ao recarregar os desejos: {e}")

def  salvar_desejos(lista_de_desejos):
  try:
     with open (NOME_ARQUIVO, 'w', encoding= 'utf-8') as arquivo:
           for desejo in lista_de_desejos:
              arquivo.write(salvar_desejos + "n\") 
        
        print ("\n ✅ seus desejos foram salvoc com sucesso!")
except excepttion as e:
   print (f"\n erro ao salvar os desejos: {e} ")
while true:
   print("\n---0 que você quer fazer? ---")
   print("1 - adicionar um novo desejo")
   print("2 - ver meus fesejos")
   print("3 - sair")

      opcao = input("digite sua opção (1,2 ou 3): ")
        
        if opcao == "1":
    novo_desejo = input ("qual é o seu novo desejo para o futuro?")
  if novo_desejo.strip():
    desejos.append(novo_desejo.strip())
    salvar_desejos (desejos) 
else:
   print (" desejo nao pode ser vazio! tente novamente.")

elif opcao == "2" :
 print ("\n✨ seus desejos para futuro ✨ !")
  if not desejos:
     print ("ainda nao ha desejos na sua lista. que tal adicionar um?")
elif:
  for i, deasejo in enumerante (desejos):
   print("-------------------------------")

elif opcao == "3":
  print(" ate logo! continue sonhando alto!")
   break
   
elise: 
  print (" opcao invalida, por favor, digite1, 2 ou 3.")