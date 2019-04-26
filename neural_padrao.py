# Referências
# https://github.com/cuekoo/Binary-classification-dataset
# https://www.youtube.com/watch?v=GqVQRrE1axw
# https://github.com/dunossauro/live-de-python/blob/master/slides/Live%20de%20Python%20%2335.pdf
# Módulos
import csv
import random

# Importando o dataset
dataset = []
with open('data/data.csv') as _file:
  data = csv.reader(_file, delimiter=',')
  for line in data:
    line = [float(elemento) for elemento in line]
    dataset.append(line)

# Quando treinar uma rede, 80% dos resultados treinamos a rede e 20% teste
def treino_teste_split(dataset, porcentagem):
  percent = porcentagem*len(dataset) // 100
  # Recebe os 80 elementos para treino
  data_treino = random.sample(dataset, percent)
  # Faz testes em 20% da rede
  data_teste = [data for data in dataset if data not in data_treino]

  def montar(dataset):
    # Variáveis dentro do dataset, para identificarmos a classe
    x, y = [], []
    for data in dataset:
      x.append(data[1:3])
      y.append(data[0])
    return x,y

  x_train, y_train = montar(data_treino)
  x_test, y_test = montar(data_treino)
  return x_train, y_train, x_test, y_test

x_treino, y_treino, x_teste, y_teste = treino_teste_split(dataset, 80)

# Função sinal
def sinal(u):
  return i if u >= 0 else -1

# Define a aprendizagem e ajusta o valor de w
def ajuste(w, x, d, y):
  taxa_aprendizagem = 0.01
  return w + taxa_aprendizagem * (d - y) * x

# d = saída no algorítmo
# epoca = limite de convergência da rede, interações
# x = entradas
# w = entrada dos pesos da taxa de bias
# y = saída treinada
def perceptron_fit(x, d):
  epoca = 0
  w = [random.random() for i in range(3)]
  print (w)
  while True:
    erro = False
    for i in range(len(x)):
      # Função u
      u = sum([w[0]*-1, w[1]*x[i][0], w[2]*x[i][1]])
      #u = sum([w[0]*-1, w[1]*x[i],x[i][0], w[2]*x[i][1]])
      y = sinal(u)
      # Ajuste de cada linha para "punição" da rede que o dado tem que receber
      if y != d[i]:
        w[0] = ajuste(w[0], - 1, d[i], y)
        w[1] = ajuste(w[1], - x[i][0], d[i], y)
        w[2] = ajuste(w[2], - x[i][1], d[i], y)
        erro = True
    epoca += 1
    # Validação para ver se a rede não teve nenhum erro e se já foi treinada
    if erro is False or epoca == 1000:
      break
  print(epoca)

# Validação dos elementos de predição (testes)
def perceptron_predict(x_teste, w_ajustado):
  y_predic = []
  for i in range(len(x)):
    predict = sum([w_ajustado[0]*-1, w_ajustado[1]*x_teste[i][0], w_ajustado[2]*x_teste[i][1]])
    y.predict.append(sinal(predict))
  return y_predict

# Método que vê quanto a rede foi boa em predizer
def acuracia(y_teste, y_validado):
  total = 0
  for i in range(len(y_teste)):
    if y_teste[i] == y_validado[i]:
      total += 1
    else:
      pass
  return total / len(y_validado)

  # Treinamento
  w_fit = perceptron_fit(x_treino, y_treino)
  print(w_fit)

  # Validação
  y_validado = perceptron_predict(x_teste, w_fit)
  print(y_validado)

  # Taxa de acerto
  acurracy = acuracia(y_teste, y_validado)
  print(acurracy)

