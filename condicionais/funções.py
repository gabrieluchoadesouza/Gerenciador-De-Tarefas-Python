# Exemplo
def saudacao(nome):
    print(f"Olá, {nome}!")

print(f"\nChamando a função saudacao")
saudacao("alice")
saudacao("bob")

def quadrado(numero):
    resultado = numero **2
    return resultado

print(f"\nResultado:")
resultado_quadrado = quadrado(116)
print(f"resultado da função quadratica:", resultado_quadrado)

#função com multiplos parametro