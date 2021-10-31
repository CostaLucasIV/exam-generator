import requests
import random
import json


def generate_random_exam(cpf):
    exam = {"isInfected": random.choice([True, False]),
            "cpf": cpf}
    return json.dumps(exam)

# Credits to lucascnr Gist: https://gist.github.com/lucascnr/24c70409908a31ad253f97f9dd4c6b7c


def generate_cpf():
    cpf = [random.randint(0, 9) for x in range(9)]

    for _ in range(2):
        val = sum([(len(cpf) + 1 - i) * v for i, v in enumerate(cpf)]) % 11

        cpf.append(11 - val if val > 1 else 0)

    return '%s%s%s.%s%s%s.%s%s%s-%s%s' % tuple(cpf)


counter = int(input('Please, enter how many exams will be generated: '))
generated_exams = open(".\logs\exams.txt", "w+")

for x in range(counter):
    cpf = generate_cpf()
    exam = generate_random_exam(cpf)

    generated_exams.write(exam + "\n")

    response = requests.post("http://localhost:3000/send",
                             data=exam, headers={"Content-Type": "application/json"})

    if(response.status_code == 200):
        print(f'{cpf} sended succesfully')

generated_exams.close()
