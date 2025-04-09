reais = int(input('Digite aqui o valor em reais: '))

dolar = reais * 0.17
euro = reais * 0.16
libras = reais * 0.13
iene = reais * 25.08
peso_argentino = reais * 182.65

print(f'''Segue abaixo o valor convertido para outras moedas:\n
      \tDólar: ${dolar:.2f}\n
      \tEuro: €{euro:.2f}\n
      \tLibras: £{libras:.2f}\n
      \tIene: ¥{iene:.2f}\n
      \tPeso Argentino: AR${peso_argentino:.2f}''')
