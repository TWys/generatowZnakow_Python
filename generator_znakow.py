import random

print('Generator znaków')


def generate(qty, params):
    string = []
    while len(string) < qty:
        if 1 in params:
            string.append(chr(random.randint(97, 122)))
            if len(string) == qty:
                break
        if 2 in params:
            string.append(chr(random.randint(65, 90)))
            if len(string) == qty:
                break
        if 5 in params:
            string.append(' ')
            if len(string) == qty:
                break
        if 3 in params:
            string.append(str(random.randint(0, 9)))
            if len(string) == qty:
                break
        if 4 in params:
            string.append(chr(random.randint(33, 47)))
            if len(string) == qty:
                break
    random.shuffle(string)
    string = ''.join(string)
    print('\nTwój wygenerowny ciąg znaków:\n{}'.format(string))


qty = input('\nWpisz ile znaków chcesz wygenerować: ')
while not qty.isdigit():
        qty = input('Proszę podać prawidłową wartość (liczbę): ')
qty = int(qty)


print('\nWybierz jakie znaki chcesz wygenerowac?\n'
      '[1] małe litery\n'
      '[2] wielkie litery\n'
      '[3] cyfry\n'
      '[4] znaki specjalne\n'
      '[5] spacje\n')

params = input("wybrane opcje (wpisz po spacji):\n")
params = [int(n) for n in params.split(' ')]
if len(params) > qty:
    qty = len(params)
generate(qty, params)
