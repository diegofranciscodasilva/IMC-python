import math


def calcular_imc():
    print("\n=== CALCULADORA DE IMC ===")
    try:
        peso = float(input("Digite o seu peso em kg (Ex: 70.5): "))
        altura = float(input("Digite a sua altura em metros (Ex: 1.75): "))

        if not math.isfinite(peso) or not math.isfinite(altura):
            print("⚠️ Digite valores numéricos finitos.")
            return

        if peso <= 0 or altura <= 0:
            print("⚠️ O peso e a altura devem ser maiores que zero.")
            return

    except ValueError:
        print("⚠️ Digite apenas valores numéricos válidos (use ponto para decimais).")
        return

    # Cálculo do IMC: peso / altura ao quadrado
    try:
        imc = peso / (altura**2)
    except (OverflowError, ZeroDivisionError):
        print("⚠️ Não foi possível calcular o IMC com esses valores.")
        return

    if not math.isfinite(imc):
        print("⚠️ Não foi possível calcular o IMC com esses valores.")
        return

    print(f"\nSeu IMC calculado é: {imc:.2f}")
    print("Classificação:")

    if imc < 18.5:
        print("🟡 Abaixo do peso ideal.")
    elif 18.5 <= imc < 25.0:
        print("🟢 Peso normal (Saudável). Parabéns!")
    elif 25.0 <= imc < 30.0:
        print("🟠 Sobrepeso (Acima do peso ideal).")
    else:
        print("🔴 Obesidade. Consulte um profissional de saúde.")


if __name__ == "__main__":
    calcular_imc()