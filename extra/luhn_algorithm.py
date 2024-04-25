"""
The Luhn Algorithm is widely used for error-checking in various applications,
such as verifying credit card numbers.

Muito utilizado para verificar/validar uma variedade de números, como cartões
Para utilizar:
  troque o valor de card_number em main(), assim retornará se é válido ou não

projeto realizado no site freecodecamp.com

este algoritmo funciona da seguinte forma:
inverte o número, pegando os com índice ímpares e os soma.
assim como com os números com índice pares.
se a soma destes dois dividido por 10 não tiver resto
retorna True
"""


def verify_card_number(card_number):
    sum_of_odd_digits = 0
    card_number_reversed = card_number[::-1]
    odd_digits = card_number_reversed[::2]

    # sum of odd index of the number reversed
    for digit in odd_digits:
        sum_of_odd_digits += int(digit)

    sum_of_even_digits = 0
    even_digits = card_number_reversed[1::2]
    # sum of even index of the number reversed
    for digit in even_digits:
        number = int(digit) * 2
        # first_digit plus second_digit
        if number >= 10:
            number = (number // 10) + (number % 10)
        sum_of_even_digits += number
    total = sum_of_odd_digits + sum_of_even_digits
    return total % 10 == 0


def main():
    card_number = '4111-1111-4555-1142'
    card_translation = str.maketrans({'-': '', ' ': ''})
    translated_card_number = card_number.translate(card_translation)

    if verify_card_number(translated_card_number):
        print('VALID!')
    else:
        print('INVALID!')


main()
