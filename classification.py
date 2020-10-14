import pickle
from enum import Enum
from time import sleep
import pandas as pd

data = pickle.load(
    open('C:/Users/herbe/Documents/TCC/dataset.pickle', 'rb'))

count = 0
for item in data:
    print('The data', count, 'is', item)
    count += 1

result_classification = []
tweets = []

class classification(Enum):
    INTERATIVA = 0
    NORMATIVA = 1
    SUPRAPESSOAL = 2
    EXISTENCIA = 3
    EXPERIMENTACAO = 4
    REALIZACAO = 5

def get_classification(index):
    lista = [data["interativa"][index], data["normativa"][index], data["suprapessoal"][index],
             data["existencia"][index], data["experimentacao"][index], data["realizacao"][index]]
    i = lista.index(max(lista))
    # return (i, max(lista))
    return i

for i in range(len(data["X"])):
    result_classification.append(get_classification(i))
    tweets.append(data["X"][i])

df = pd.DataFrame(list(zip(result_classification, tweets)), columns=['classificacao','tweets'])

df.to_csv(r'C:/Users/herbe/Documents/TCC/tcc/dataset.csv', header=True, index=False)