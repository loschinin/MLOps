%%writefile app.py
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Создание датасетов
np.random.seed(0)
x = np.random.rand(100, 1)
y1 = 2 * x + 1
y2 = 2 * x + 1 + 0.1 * np.random.randn(100, 1)
y3 = 2 * x + 1 + 0.5 * np.random.randn(100, 1)

# Обучение модели на первом датасете
model = LinearRegression()
model.fit(x, y1)
predictions = model.predict(x)

# Визуализация
plt.scatter(x, y1, color='blue')
plt.plot(x, predictions, color='red')
plt.title('Linear Regression')
plt.show()

# Оценка модели
mse = mean_squared_error(y1, predictions)
print(f'Mean Squared Error: {mse}')