import random
import pandas as pd
n = 2
lst = ['robot'] * n
lst += ['human'] * n
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
one_hot_data = pd.DataFrame({'whoAmI': lst})

# data['robot'] = data['robot'].astype(int)
# data['human'] = data['human'].astype(int)
for i in range(len(data)):
    if data['whoAmI'][i] == 'human':
       data.loc[i,['human']]=1; data.loc[i,['robot']]=0
       
    else:
        data.loc[i,['robot']]=1; data.loc[i,['human']]=0  
data[['robot', 'human']] = data[['robot', 'human']].astype (int)
print('Без метода get_dummies:\n')
print(data.head(n*2))
print('\n')
print('С методом get_dummies:\n')
one_hot_data = pd.get_dummies(data, columns=['whoAmI'])
print(one_hot_data.head(n*2))
