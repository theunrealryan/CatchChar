import time
def obter_caracter(str, index):
    return str[index]

def Escreva(text):
    Ne, N1 = 0, 0
    tex = ""
    
    while tex != text:
        C1 = obter_caracter("abcçdefghijklmnopqrstuvwxyz ABCÇDEFGHIJKLMNOPQRSTUVWXYZ", Ne)
        print("\n" + tex + C1)
        time.sleep(0.02)
        
        if obter_caracter(text, N1) == C1:
            tex += C1
            Ne, N1 = 0, N1 + 1
            
        else:
            Ne += 1

    for i in range(100):
        print("\n" + tex)

def main():
    texto = input("Digite um texto: ")
    Escreva(texto)

if __name__ == "__main__":
    main()
