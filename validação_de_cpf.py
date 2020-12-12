cpf = str(input('\033[33mInforme seu CPF: \033[m'))
cont = add = 0 #cont = variável utilizada para indicar um índice dentro de "cpf" / add = variável que faz a soma das múltiplas "mult" para ser utilizada na fórmula
nx = end = 10 #nx = número a ser multiplicado pelos algorismos em "cpf" que diminui a cada volta no laço / end = variável que indica o final para zerar os valores e realizar a fórmula
validation = list()
final_cpf = list()

if len(cpf) == 11:
    final_cpf = [cpf[9], cpf[10]]
    while True:
        if nx == 12:
            break
        num = int(cpf[cont]) 
        mult = num * nx 
        add += mult
        cont += 1
        nx -= 1 
        if cont == end - 1 and end < 12:
            valid = 11 - (add % 11) #Fórmula para validação dos últimos dígitos do CPF
            end += 1
            nx = end
            cont = add = mult = 0
            if valid > 9:
                valid = 0
            validation.append(str(valid))

if final_cpf == validation and len(cpf) == 11:
    print('\033[32mVálido!\033[m')
else:
    print('\033[31mInválido!\033[m')
print('\033[36mPrograma finalizado!\033[m') 
