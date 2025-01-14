import random, re
from faker import Faker

fake = Faker("la")
texto = ''


def date_converter(date):
    return(f'{date[3:5]}/{date[0:2]}/{date[6:10]}')

def with_date(frase):
    date = fake.date_object()
    date = f"{date.month:02}/{date.day:02}/{date.year:04}"
    return frase.replace(random.choice(frase.split()[:-1]), date)


if __name__ == "__main__":
    for i in range(random.randint(3, 20)):
        for i in range(random.randint(4, 20)):
            frase = fake.sentence()
            if random.random() < 0.25:
                frase = with_date(frase)
            texto += frase
            texto += ' '

        texto += '\n'


print(texto)

pattern = r"[0-9]?[0-9]/[0-9]?[0-9]/[0-9]+"

dates = re.findall(pattern,texto)
print(dates)
for date in dates:
    texto = texto.replace(date, date_converter(date))

print(texto)

# Expressão regular = [0-9]?[0-9]/[0-9]?[0-9]/[0-9]+