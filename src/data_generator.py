import pandas as pd
import random
import numpy as np
str = ['pig','dog','apple','abandon','greek','latin','tiger','lion','fog','generates', 'numbers', 'in', 'the', 'inclusive', 'range' ,'from']
str = np.array(str)
sentence = []
label = []


num_row = 100


for i in range(num_row):
    k = random.sample(range(len(str)),5)
    p = random.randint(0,5)
    k=str[k]
    if i %2==0:
        k=np.insert(k,p,'man')
    else:
        k=np.insert(k,p,'woman')

    sentence.append((' '.join(k),('female' if i%2 else 'male')+('0' if i%4 == 0 else '2'),i%4))
    label.append(i%2)

df = pd.DataFrame.from_records(sentence, columns=['sent','lab','sth'])

df.to_excel('output.xlsx')