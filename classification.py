import pickle
from enum import Enum
from time import sleep
import pandas as pd

data = pickle.load(
    open('/Users/herbertcordeiro/Documents/tcc/tcc-env/texts.pickle', 'rb'))

count = 0
for item in data:
    print('The data', count, 'is', item)
    count += 1

class classification(Enum):
    INTERATIVA = 0
    NORMATIVA = 1
    SUPRAPESSOAL = 2
    EXISTENCIA = 3
    EXPERIMENTACAO = 4
    REALIZACAO = 5

result = []
classification_list = []

def get_classification(index):
    lista = [data["interativa"][index], data["normativa"][index], data["suprapessoal"][index],
             data["existencia"][index], data["experimentacao"][index], data["realizacao"][index]]
    i = lista.index(max(lista))
    classification_list.append(i)
    return (classification(i), max(lista))

for i in range(len(data["X"])):
    result.append(get_classification(i))

df = pd.DataFrame(result)

df.to_csv(r'/Users/herbertcordeiro/Documents/tcc/tcc-env/result.csv', header=False)

print(classification_list)