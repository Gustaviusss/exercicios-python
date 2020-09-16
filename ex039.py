import datetime
now = datetime.datetime.now()
ano = int(input('digite o ano do seu nascimento: '))
ano_atual = now.year
idade = 18
if (ano_atual - ano) > idade:
    passado = ano_atual - ano
    print('Já passaram {} anos da hora de você se alistar'.format(passado-idade))
elif (ano_atual - ano) < idade:
    restante = (ano_atual - ano)
    print('Faltam {} anos para você se alistar'.format(idade-restante))
else:
    print('está na hora de se alistar')
