num_primo = int(input("Digite um número inteiro: "))
if num_primo <= 0:
    print("Número inválido")
else:
    if num_primo > 1:
        for i in range(2, num_primo):
            if num_primo % i == 0:
                print("Não primo")
                break
        else:
            print("Primo")
    else:
        print("Não primo")