from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import joblib

def train_and_save_model():
    # Загрузка датасета
    data = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.2, random_state=42)

    # Обучение модели
    model = LogisticRegression(max_iter=200)
    model.fit(X_train, y_train)

    # Сохранение модели
    joblib.dump(model, 'iris_model.pkl')

if __name__ == "__main__":
    train_and_save_model()
