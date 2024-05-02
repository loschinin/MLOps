# Lab 3

### Создание виртуального окружения
python3 -m venv myenv

### Активация виртуального окружения на MacOS/Linux
source myenv/bin/activate

### Активация виртуального окружения на Windows
myenv\Scripts\activate

### Установка зависимостей
pip install -r requirements.txt

### Сборка образа Docker
docker build -t iris-model-app .

### Запуск контейнера Docker
docker run -p 5000:5000 iris-model-app

