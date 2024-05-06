%%writefile test_model.py
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

def test_model_on_noisy_data():
    np.random.seed(0)
    x = np.random.rand(100, 1)
    y3 = 2 * x + 1 + 0.5 * np.random.randn(100, 1)  # Зашумленные данные
    model = LinearRegression()
    model.fit(x, y3)
    predictions = model.predict(x)
    mse = mean_squared_error(y3, predictions)
    print(f"Mean Squared Error (MSE): {mse}")  # Вывод MSE в консоль
    assert mse < 0.5, "Model performance is not satisfactory"
