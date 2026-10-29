import contextlib
import io
import unittest
from unittest.mock import patch

from calculadora_imc import calcular_imc


class CalcularImcTests(unittest.TestCase):
    def executar_calculo(self, peso, altura):
        output = io.StringIO()
        with patch("builtins.input", side_effect=[peso, altura]):
            with contextlib.redirect_stdout(output):
                calcular_imc()
        return output.getvalue()

    def test_calcula_imc_e_classifica_peso_normal(self):
        output = self.executar_calculo("70.5", "1.75")

        self.assertIn("23.02", output)
        self.assertIn("Peso normal", output)

    def test_aplica_limites_das_classificacoes(self):
        cases = [
            ("18.49", "Abaixo do peso"),
            ("18.5", "Peso normal"),
            ("25", "Sobrepeso"),
            ("30", "Obesidade"),
        ]

        for peso, classification in cases:
            with self.subTest(peso=peso):
                self.assertIn(classification, self.executar_calculo(peso, "1"))

    def test_rejeita_valores_nao_finitos(self):
        for peso, altura in [("nan", "1.75"), ("70", "inf"), ("-inf", "1.75")]:
            with self.subTest(peso=peso, altura=altura):
                output = self.executar_calculo(peso, altura)
                self.assertIn("valores numéricos finitos", output)
                self.assertNotIn("Classificação:", output)

    def test_rejeita_valores_nao_numericos(self):
        output = self.executar_calculo("peso", "1.75")

        self.assertIn("valores numéricos válidos", output)
        self.assertNotIn("Classificação:", output)

    def test_rejeita_zero_e_resultados_fora_do_intervalo_calculavel(self):
        zero_height = self.executar_calculo("70", "0")
        uncalculable = self.executar_calculo("70", "1e-300")

        self.assertIn("maiores que zero", zero_height)
        self.assertIn("Não foi possível calcular", uncalculable)


if __name__ == "__main__":
    unittest.main()
