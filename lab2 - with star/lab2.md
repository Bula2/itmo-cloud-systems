## Лабораторная работа 2

## Цель работы:
Поднять kubernetes кластер локально, в нём развернуть свой сервис, используя 2-3 ресурса kubernetes

## Задачи:
* Написать YAML файлы для быстрого разворачивания узлов;
* Поднять кластер в minikube c двумя ресурсами.

## Ход работы

Для начала установим minikube с помощью exe файла с официального сайта

![png7](./img/7.PNG)

Запустим minikube командой
  ```
  minikube start
  ```

![png5](./img/5.PNG)

Далее напишем ![deployment.yaml](./deployment.yaml): 

  ```
  apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-deployment
spec:
  replicas: 2
  selector:
    matchLabels:
      app: my-app
  template:
    metadata:
      labels:
        app: my-app
    spec:
      containers:
        - name: my-app
          image: my-app:1.0
          ports:
            - containerPort: 80
  ```

В нем указано replicas: 2, что означает, что в кластере будет создано два данных объекта.

Далее создадим ![service.yaml](./service.yaml). В роли сервиса будет выступать NodePort: 

  ```
apiVersion: v1
kind: Service
metadata:
  name: my-service
spec:
  type: NodePort
  selector:
    app: my-app
  ports:
    - port: 80
      targetPort: 80

  ```


Далее соберем и развернем наши ресурсы в minikube: 

![png4](./img/4.PNG)
![png3](./img/3.PNG)


Как видно на картинке выше, minikube вывел нам IP и порт по которому мы можем получить доступ к сервису.

Помимо этого, в браузере автоматически открылась вкладка с нашим сервисом:

![png1](./img/1.PNG)

## Вывод
В ходе выполнения данной лабораторной работы были подняты 2 сервиса в кластере minikube.
Развернуты они были с помощью описанных yaml файлов.

