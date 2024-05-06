import pandas as pd

# Загрузка датасета Титаника
data = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')
data = data[['Pclass', 'Sex', 'Age']]
data.to_csv('titanic_v1.csv', index=False)

# Заполнение пропущенных значений без использования inplace=True
data['Age'] = data['Age'].fillna(data['Age'].mean())
data.to_csv('titanic_v2.csv', index=False)

# Добавление нового признака (one-hot-encoding для 'Sex')
data = pd.get_dummies(data, columns=['Sex'])
data.to_csv('titanic_v3.csv', index=False)
