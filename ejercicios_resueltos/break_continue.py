def run():
    # for contador in range(1000):
    # if contador % 2 != 0:
    #     continue
    # print(contador)

    # for i in range(1000):
    #     print(i)
    #     if i == 578:
    #         break

    texto = input('Escribe un texto cualquiera: ')
    for letra in texto:
        if letra == 'o':
            break
        print(letra)


if __name__ == '__main__':
    run()
