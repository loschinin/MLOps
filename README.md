### Создание виртуального окружения
python3 -m venv myenv

### Активация виртуального окружения на MacOS/Linux
source myenv/bin/activate

### Установка DVC 3.50.1
pip install dvc
pip install --upgrade pip

### Инициализация Git и DVC:
git init
dvc init

### Настройка удаленного хранилища (Google Drive):
dvc remote add -d myremote gdrive://19x6V3UPdJ8bN5H8EvagGMvdR02e-zYSf

### Установка зависимостей
pip install -r requirements.txt

pip install 'dvc[gdrive]'


## Start project
python3 app.py

dvc add titanic_v1.csv
git add titanic_v1.csv.dvc .gitignore
git commit -m "Add initial Titanic dataset"
