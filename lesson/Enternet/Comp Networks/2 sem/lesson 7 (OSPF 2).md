# Дополнительные настройки OSPF

## Multiarea OSPF

### Single Area OSPF

![img.png](img/lesson7/single_OSPF.png)

### Multiarea OSPF

![multiarea.png](img/lesson7/multiarea.png)

### Иерархия в OSPF

![ierarhia_OSPF.png](img/lesson7/ierarhia_OSPF.png)

![recomindation_OSPF.png](img/lesson7/recomindation_OSPF.png)

### Внутренний маршрутизатор

![Iternal_route.png](img/lesson7/Iternal_route.png)

### Магистральные маршрутизаторы

![backbone.png](img/lesson7/backbone.png)

### Граничные маршрутизаторы (ABR)

![ARB.png](img/lesson7/ABR.png)

### Граничный маршрутизатор автономной системы (ASBR)

![ASBR.png](img/lesson7/ASBR.png)

### Типы LSA

![type_LSA.png](img/lesson7/type_LSA.png)

* LSA 1 каждый маршрутизатор сообщает информацию о сетях внутри одной области
* LSA 2 внутри области, генерируется только DR, нужно для сообщения топологии при соединении через Ethernet
* LSA 3 генерируется ABR для информирования других областей, а также получения от них DBD
* LSA 4 генерируется ABR, служат маршрутом для ASBR, говорим как добраться до него (через какие граничные идти) для
  всего домена маршрутизации
* LSA 5 генерируется ASBR для всего домена маршрутизации, сообщает о внешней сети, если настроена redistribute ...

### Type 1 LSA

![LSA_1.png](img/lesson7/LSA_1.png)

### Type 2 LSA

Записи о состоянии каналов сети. Создаются только роутером DR
![LSA_2.png](img/lesson7/LSA_2.png)

### Type 3 LSA

![LSA_3.png](img/lesson7/LSA_3.png)

### Type 4 LSA

![LSA_4.png](img/lesson7/LSA_4.png)

### Type 5 LSA

![LSA_5.png](img/lesson7/LSA_5.png)

### Таблица маршрутизации

![table_route.png](img/lesson7/table_route.png)
-------------------------------------------------------

## Настройка Multiarea OSPF

-------------------------------------------------------------------------------------

## Сети с множественным доступом в OSPF

### Типы ОСПФ сетей

![type_OSPF_network.png](img/lesson7/type_OSPF_network.png)

![point_to_point.png](img/lesson7/point_to_point.png)

### Выделенный маршрутизатор

![DR.png](img/lesson7/DR.png)

В сетях с множественным доступом OSPF все маршрутизаторы устанавливаются отношения смежности только с выделенным
маршрутизатором (Ну и с BDR т.к он запасной и нужен для подмены DR)

### Роли DR BDR

![DR_BDR.png](img/lesson7/DR_BDR.png)

LSA сообщения отправляются только DR маршрутизатором

DROTHER отправляют свои LSA пакеты только DR и BDR маршрутизаторам

![DR_BDR_Neighbor.png](img/lesson7/DR_BDR_Neighbor.png)

Для GigabitEthernet подключения состояние обязательно должно быть FULL - искл TO WAIT

### Выбор DR/BDR

![Choose_DR_BDR.png](img/lesson7/Choose_DR_BDR.png)

### Изменение приоритета

![priority.png](img/lesson7/priority.png)

255 - гарантирует что маршрутизатор станет DR

--------------------------------------------------------------------------------------

## Дополнительные настройки OSPF

### Распространение маршрута по умолчанию

Распространение маршрута по умолчанию: пусть в нашей сети пограничный маршрутизатор - R1 имеет выход в интернет и путь
до интернета задается статическим маршрутом. Чтобы этот маршрутизатор R1 распространял статику через OSPF необходимо
воспользоваться простой командой default-information originate.

![route_gateway.png](img/lesson7/route_gateway.png)

### Изменение Таймеров

![timer.png](img/lesson7/timer.png)