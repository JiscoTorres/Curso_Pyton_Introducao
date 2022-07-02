
# Usa-se o "#" para escrever avisos, mensagens e comentários na própria programação. 


#--------------------------------------------------------#


# IMPRIMIR MENSAGENS - Com o comando print.

print('Hello World') # Quando se coloca textos dentro dos apóstrofos, o mesmo texto será impresso na tela(Console).



#--------------------------------------------------------#



#CALCULOS - Com o comando print.

print(3+3+3) # Com esse tipo de comando,sem os apóstrofos, a soma dos números será impressa na tela. ~Resultado = 9~

print(5*2) # Multiplicação de números, utiliza-se um asterisco. ~Resultado = 10~

print(4**2) #Exponeciação, ou seja, quatro elevado a dois; para isso, utiliza-se dois asteriscos. ~Resultado = 16~



#--------------------------------------------------------#  


a = 2  # Declarar a variável "a" igual ao número 2. 
b = 3  # Declarar a variável "b" igual ao número 3. 

soma = a + b # Declarar a variável "soma" igual a soma de "a"+"b".

print(soma) # Imprimir o resultado da soma, no caso "a"+"b".   ~Resultado = 5~ 

print('O valor da soma é:', soma) # Pode-se colocar uma mensagem que indique o valor de algo, dentro dos apostrofos e em seguida, depois da vírgula, o nome da variável. 

print('A soma é igual a:', soma, ' A variável a é igual a:', a, ' A variável b é igual a:', b) # Também é possível colocar mais de um valor, como mostrado nesse exemplo. Além da soma, foram adicionados os valores de A e B. 




#--------------------------------------------------------#




c = 5
d = 3

soma = c + d
print(soma==8) # Este "==" nada mais é do que uma pergunta para o programa se o resultado da soma é igual a 8, nesse caso o resultado é igual ao número indicado(8), logo a resposta impressa será "True". 

print(soma==2) # Pelo fato do valor da soma NÃO ser igual a 2, a resposta impressa será "False".




#--------------------------------------------------------#




# Caso a Soma resulte em 8, o comando que aparecerá será 'O resultado é igual a 8', mas, caso não resulte em 8, o camando impresso será 'O resultado NÃO é igual a 8'.

e = 5
f = 3

soma = e + f

if soma == 8:
  print('O resultado é igual a 8') # O espaço que tem do print para a borda é chamado de IDENTAÇÃO, nesse tipo de comando logo após o If o print nescessita de uma identação. Por isso o prints que vem depois dos ifs tem esse espaço da borda.  
else:
  print('O resultado NÃO é igual a 8') 
  
# Pelo fato da vriável "soma" resultar em 8, a resposta será 'O resultado é igual a 8'. 





if soma == 23:
  print('O resultado é igual a 23')
else:
  print('O resultado NÃO é igual a 23, e sim igual a 8')

# A variável soma resulta em 8 e não em 23, por isso a resposta printada será 'O resultado NÃO é igual a 23, e sim igual a 8'. 



#--------------------------------------------------------#




# FOR é um loop, para fazer várias operações ao mesmo tempo.

for a in range(5):
  print(a)

# os valores de Phyton começam do 0, por isso o valor final printado do exemplo é 4 (Zero foi o primeiro número da contagem e Quatro foi o quinto número da contagem). Para fazer com que o último valor impresso seja 5 é nescessário colocar no range() o número 6.






#Usar esse comando como frases

for b in range(10):
  print('Harry Potter é bom!')

# Assim, o comando imprimirá a frase "Harry Potter é bom!" 10 vezes no console. 





#------------------------FIM-----------------------------#
