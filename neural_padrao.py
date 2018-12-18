# Referências
# https://github.com/cuekoo/Binary-classification-dataset
# https://www.youtube.com/watch?v=GqVQRrE1axw
# https://github.com/dunossauro/live-de-python/blob/master/slides/Live%20de%20Python%20%2335.pdf
# Módulos
import csv
import random

# Importando o dataset
dataset = [] with open('data.csv') as _file
  data = csv.reader(_file, delimiter=',')
  for line in data
    line = [float(elemento) for elemento in line]
    dataset.append(line)

# Quando treinar uma rede, 80% dos resultados treinamos a rede e 20% teste
def treino_teste_split(dataset, porcentagem):
  percent = porcentagem*len(dataset) // 100
  # Recebe os 80 elementos para treino
  data_treino = random.sample(dataset, percent)
  # Faz testes em 20% da rede  
  data_teste = [data for data in dataset if data not_in data_treino]
  
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

x_treino, y_treino, x_teste, y_teste = teste_split(dataset, 80)

# d = saída no algorítmo
# epoca = limite de convergência da rede, interações
w = entrada dos pesos da taxa de bias
def perceptron_fit(x, d):
  epoca = 0
  w = [random.random() for i in range(3)]
  print (w)
  while True:
    erro = False
    for i in range(len(x)):
	# Parei em 28 min
      u = sum(w[0]*-1, w[1]*x[i],)
