cpf = str(input('\033[33mInforme seu CPF: \033[m'))
cont = 0
add = 0
nx = 10
end = 10
validation = list()
final_cpf = list()

if len(cpf) == 11:
    final_cpf.append(int(cpf[9]))
    final_cpf.append(int(cpf[10]))
    while True:
        if nx == 12:
            break
        num = int(cpf[cont]) 
        mult = num * nx 
        add += mult
        cont += 1
        nx -= 1
        if cont == end - 1 and end < 12:
            valid = 11 - (add % 11)
            end += 1
            nx = end
            cont = add = 0
            mult = 1
            if valid > 9:
                valid = 0
            validation.append(valid)

if final_cpf == validation and len(cpf) == 11:
    print('\033[32mVálido!\033[m')
else:
    print('\033[31mInválido!\033[m')
print('\033[36mPrograma finalizado!\033[m')  