# MLOps
Educational MLOps project

# Lab 1

### Создание виртуального окружения
python3 -m venv myenv

### Активация виртуального окружения на MacOS/Linux
source myenv/bin/activate

### Активация виртуального окружения на Windows
myenv\Scripts\activate

### Установка зависимостей
pip install -r requirements.txt

### Запуск пайплайна
./pipeline.sh

# Результаты:

Model score for test_noisy.csv: 0.0006964917996773456
Model score for test_normal.csv: 0.0022260347055085283
Model score for test_anomaly.csv: 0.002585070833325931

Скрипты успешно выполнились, и модель линейной регрессии была протестирована на тестовых данных. Результаты показывают значения коэффициента детерминации ( R^2 ) для каждого из тестовых наборов данных. Этот коэффициент измеряет, насколько хорошо будущие выборки, вероятно, будут предсказаны моделью. Значение ( R^2 ) близкое к 1 указывает на то, что модель хорошо объясняет вариабельность данных вокруг среднего.

# Анализ результатов
test_noisy.csv: ( R^2 = 0.000696 ) - очень низкое значение, что указывает на то, что модель практически не объясняет вариабельность данных. Это может быть связано с шумом в данных.
test_normal.csv: ( R^2 = 0.002226 ) - также очень низкое значение, что может указывать на недостаточность модели для объяснения данных или на неадекватность данных для моделирования линейной регрессией.
test_anomaly.csv: ( R^2 = 0.002585 ) - аналогично низкое значение, что может быть связано с аномалиями в данных.
## Возможные шаги для улучшения
### Пересмотреть модель: 
Линейная регрессия может быть не лучшим выбором для этих данных. Возможно, стоит рассмотреть другие модели, такие как полиномиальная регрессия, деревья решений или ансамблевые методы, которые могут лучше справляться с нелинейностями или шумом в данных.
### Улучшение предобработки данных: 
Можно попробовать другие методы масштабирования или трансформации данных, такие как логарифмическое преобразование или использование робастных масштабировщиков, которые менее чувствительны к выбросам.
### Инженерия признаков: 
Добавление новых признаков или преобразование существующих может помочь улучшить производительность модели. Это может включать в себя создание полиномиальных признаков, взаимодействий между признаками или использование методов для уменьшения размерности, таких как PCA.
### Анализ данных: 
Важно тщательно изучить данные на предмет аномалий, выбросов или необычных паттернов, которые могут негативно влиять на модель.
### Кросс-валидация: 
Использование кросс-валидации может помочь лучше оценить производительность модели на различных подмножествах данных и уменьшить переобучение.

# Lab 2

### Сборка образа Docker
docker build -t my-jenkins-image .

### Запуск контейнера Docker
docker run -p 8080:8080 -p 50000:50000 --name my-jenkins-container my-jenkins-image
