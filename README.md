# big_data_course

## hw 1

- [Развернут](https://github.com/Polozhiev/big_data_course/blob/main/hw1/screen_230607.png) локальный кластер Hadoop в конфигурации 2 DN + 2 NM
- Написан map reduce на Python для подсчета среднего значения и дисперсии [датасета](https://www.kaggle.com/dgomonov/new-york-city-airbnb-open-data) цен на жилье

## hw 2


### Разворачиваем standalone cluster Spark: master + 2 workers: 
1) изменил файл conf/spark-env.sh, добавив:  
    SPARK_WORKER_CORES=1  
    SPARK_WORKER_INSTANCES=2  
    SPARK_EXECUTOR_CORES=1  
2) запустил start-master.sh
3) запустил start-worker.sh <ссылка на мастер>  
   ![](https://github.com/Polozhiev/big_data_course/blob/main/hw2/Screenshot_20230406_231916.png)  


### Подключаемся к кластеру с помощью Jupyter
1) запускаем jupyter notebook
2) прописываем в нем spark = SparkSession.builder.master("ссылка на мастер").getOrCreate()  
![](https://github.com/Polozhiev/big_data_course/blob/main/hw2/work_session_jupyter.png)  


### Преобразуем данные в parquet
parquet файл занимает 700 MB vs 1200 MB csv файла  
разницы в скорости чтения parquet файла и объединенного csv файла нет (2 µs)

### Получаем результаты:
- Топ-10 книг с наибольшим числом ревью
![](https://github.com/Polozhiev/big_data_course/blob/main/hw2/counts_review.png)  
- Топ-10 издателей с наибольшим средним числом страниц в книгах  
![](https://github.com/Polozhiev/big_data_course/blob/main/hw2/page_num.png)  
- Десять наиболее активных по числу изданных книг лет
![](https://github.com/Polozhiev/big_data_course/blob/main/hw2/year_count.png)  
- Топ-10 книг имеющих наибольший разброс в оценках среди книг имеющих больше 500 оценок
в качестве меры разброса использовал стандартное отклонение    
![](https://github.com/Polozhiev/big_data_course/blob/main/hw2/rating_std.png)   
- Посмотрим на средний рейтинг по годам. Учитывались только года, в которые выпускалось более 1000 книг. Учитывался рейтинг книг, имеющих только более 500 оценок. Выведены топ-10 лучших и топ-10 худших годов по такому среднему рейтингу.  
![](https://github.com/Polozhiev/big_data_course/blob/main/hw2/year_rating.png)
