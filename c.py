import sys
def soma_algarismos(a, b):
    a = int(a)
    b = int(b)
    if not (0 <= a <= 9 and 0 <= b <= 9):
        raise ValueError("Os valores devem ser algarismos de 0 a 9.")
    return a + b

def main():
    if len(sys.argv) >= 3:
        x, y = sys.argv[1], sys.argv[2]
    else:
        entrada = input("Digite dois algarismos de 0 a 9 separados por espaço: ").strip().split()
        if len(entrada) < 2:
            print("Forneça dois algarismos.")
            return
        x, y = entrada[0], entrada[1]

    try:
        resultado = soma_algarismos(x, y)
    except ValueError as e:
        print("Erro:", e)
        return

    print("Soma:", resultado)

if __name__ == "__main__":
    main()