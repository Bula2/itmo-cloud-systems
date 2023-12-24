
# Лабораторная работа №4 "Мониторинг сервиса, поднятого в кубере"

## Выполнили:
Булаев Дмитрий K34211, Мелких Дмитрий K34211

## Цель работы:
Сделать мониторинг сервиса, поднятого в kubernetes

## Задачи:
* Локально установить Prometheus
* Локально установить Grafana
* Зафиксировать два графика, отображающих состояние системы

## Ход работы

Для начала проверим, установлен ли helm на нашей машине

![1](./img/1.PNG)

Увидим, что не установлен. Скачаем и установим helm.

![2](./img/2.PNG)

Далее с помощью helm добавим репозиторий и установим prometheus:

```
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm install prometheus prometheus-community/prometheus
```

Аналогично установим grafana:

```
helm repo add grafana https://grafana.github.io/helm-charts
helm install grafana grafana/grafana
```

Далее запустим prometheus:
```
kubectl expose service prometheus-server --type=NodePort --target-port=9090 --name=prometheus-server-np
```

Чтобы подключиться к веб-интерфейсу prometheus, воспользуемся параметром --url.

![3](./img/5.PNG)

Посмотрим через браузер как работает prometheus

![4](./img/3.PNG)

Далее запустим grafana:
```
kubectl expose service grafana --type=NodePort --target-port=3000 --name=grafana-dimases
```
Аналогично воспользуемся параметром --url
![5](./img/grafInst.PNG)

В веб-интерфейсе grafana увидим авторизацию:

![6](./img/loginGraf.PNG)

Получим пароль для admin с помощью команды (через powershell не получилось, поэтому использовали git cmd):

![7](./img/7.PNG)

После авторизации укажем prometheus как Datasource для grafana:

![8](./img/10.PNG)

Далее импортируем дашборд Node Exporter Full:

![9](./img/import.PNG)

В результате увидим графики состояния системы:

![10](./img/9.PNG)

## Вывод:
В ходе выполнения работы были установлены prometheus и grafana, были построены графики отражающие состояние системы. Во время выполнения работы проблем не возникло. 
