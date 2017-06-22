dia_atual=int(input('Informe o dia atual: '))

mes_atual=int(input('Informe o mês atual: '))

ano_atual=int(input('Informe o ano atual: '))

dia_nascimento=int(input('Informe o dia em que nasceu: '))

mes_nascimento=int(input('Informe o mês em que nasceu: '))

ano_nascimento=int(input('Informe o ano do seu nascimento: '))

anos=ano_atual-ano_nascimento-1

if mes_atual==mes_nascimento:

  meses=0

  if dia_atual==dia_nascimento:

      anos=anos+1

      dias=0

  elif dia_atual>dia_nascimento:

      anos=anos+1

      dias=dia_atual-dia_nascimento

  elif dia_atual<dia_nascimento:

      meses=11

      dias=30-dia_nascimento+dia_atual

if mes_atual>mes_nascimento:

  anos=anos+1

  meses=mes_atual-mes_nascimento

  dias=30-dia_nascimento+dia_atual

  if dias==30:

      dias=0

      meses=meses+1

  if dias>30:

      dias=dias-30

      meses=meses+1

if mes_nascimento>mes_atual:

  meses=12-mes_nascimento+mes_atual

  dias=30-dia_atual+dia_nascimento

  if meses==12:

      dias=dia_atual

      meses=0

      anos=anos+1

  if meses>12:

      dias=30-dia_nascimento+dia_atual

      anos=anos+1

      meses=mes_atual

if dias==30:

  dias=0

  meses=meses+1

if meses==12:

  meses=0

  anos=anos+1



print("Você já viveu: %d dias " %(dias))

print("Você já viveu %d meses " %(meses))

print("Você já viveu: %d anos " %(anos))

