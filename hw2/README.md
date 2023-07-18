# hw2

Весь первый блок и первое задание второго блока были сделаны до мягкого дедлайна. Остальное все сделано после мягкого.
## Блок 1:
### Разворачиваем кластер: 
1) изменил файл conf/spark-env.sh, добавив:  
    SPARK_WORKER_CORES=1  
    SPARK_WORKER_INSTANCES=2  
    SPARK_EXECUTOR_CORES=1  
2) запустил start-master.sh
3) запустил start-worker.sh <ссылка на мастер>  
   ![](https://github.com/Big-Data-2023/polozhiev/blob/hw2/Screenshot_20230406_231916.png)  

### Подключаемся к кластеру с помощью Jupyter
1) запускаем jupyter notebook
2) прописываем в нем spark = SparkSession.builder.master("ссылка на мастер").getOrCreate()  
![](https://github.com/Big-Data-2023/polozhiev/blob/hw2/work_session_jupyter.png)  

## Блок 2:
### Преобразуем данные в parquet
parquet файл занимает 700 MB vs 1200 MB csv файла  
разницы в скорости чтения parquet файла и объединенного csv файла нет (2 µs)

### Получаем результаты:
a)   
![](https://github.com/Big-Data-2023/polozhiev/blob/hw2/counts_review.png)  
b)   
![](https://github.com/Big-Data-2023/polozhiev/blob/hw2/page_num.png)  
c)   
![](https://github.com/Big-Data-2023/polozhiev/blob/hw2/year_count.png)  
d)  
в качестве меры разброса использовал стандартное отклонение    
![](https://github.com/Big-Data-2023/polozhiev/blob/hw2/rating_std.png)   
e) Посмотрим на средний рейтинг по годам. Учитывались только года, в которые выпускалось более 1000 книг. Учитывался рейтинг книг, имеющих только более 500 оценок. Выведены топ-10 лучших и топ-10 худших годов по такому среднему рейтингу.  
![](https://github.com/Big-Data-2023/polozhiev/blob/hw2/year_rating.png)
