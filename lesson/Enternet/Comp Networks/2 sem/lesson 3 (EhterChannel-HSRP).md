# EtherChannel & HSRP

## EtherChannel

Для хорошего и эффективного создания коммутированных сетей, надо использовать трехуровневую или сдвоенную иерархическую
модель сети

Эти модели подразумевают различные варианты резервирования, в том числе резервирование каналов для увеличения надежности
такой сети, на случай если какой либо канал будет сломан или выключен.

### Агрегация трафика

![traffic_aggregation.jpg](img/lesson3/traffic_aggregation.jpg)

Из-за STP такое резервирование каналов будет блокироваться, поэтому была придумана технология EtherChannel

### EtherChannel

![EtherChannel.png](img/lesson3/EtherChannel.png)

в один EtherChannel можно объединить только каналы связи работающие на одной скорости. Нельзя объединить в 1 канал Fa и
Ge порты.

Есть 3 варианта настройки EtherChannel:

1. Статическая настройка
2. Протоколы согласования:
    * PaGP
    * LACP

В EtherChannel можно объединить до 8 портов, настройка дуплека должна быть настроена одинакова на обоих портах.

Max EtherChannel до 6

### PAgP

![pagp.png](img/lesson3/pagp.png)

Режим **on** - используется для статической настройки.

**Desirable** - отвечает за активное согласование каналов. Будет активно рассылать сообщение на установку EtherChannel.
Если на другом конце коммутатора/порта тоже будет Desirable, то он примет этот EtherChannel

**Auto** - ничего не отправляет, только принимает сообщения. Ждет сообщения от другого коммутатора

### LACP

![LACP.png](img/lesson3/LACP.png)

### Настройка PAgP

![setting_PAgP.png](img/lesson3/setting_PAgP.png)

### Настройка LACP

![setting_LACP.png](img/lesson3/setting_LACP.png)

## Команды проверки

![img.png](img/lesson3/verification_commands.png)

**show interfaces port-channel**

![show_int_port_channel.png](img/lesson3/show_int_port_channel.png)

**show etherchannel summary**

![img.png](img/lesson3/show_etherchannel_summary.png)

**show etherchannel port-channel**

![show_etherchannel_port_channel.png](img/lesson3/show_etherchannel_port_channel.png)

**show int etherchannel**

![show_int_etherchannel.png](img/lesson3/show_int_etherchannel.png)

### Отладка EtherChannel

![img.png](img/lesson3/debug_EtherChannel.png)

## FHRP

Рассмотрим что бывает если мы резервируем оборудование. Мы резервируем default gateway(L3 коммутатор или маршрутизатор)

![default_gateway.png](img/lesson3/default_gateway.png)

Из-за софтовых ограничений мы не можем использовать физически резервный маршрутизатор

![img.png](img/lesson3/virtual_router.png)

Для решения этой проблемы придумали инструмент first hop redundancy protocol - протокол избыточности первого перехода

если у нас есть несколько маршрутизирующих устройств мы можем с помощью протокола FHRP чтобы они работали как один
маршрутизатор, чтобы они подстраховывали друг друга в случае поломок.

Как работает протокол:
У нас настраивается специальный виртуальный IP-address и MAC-адрес которые будут работать с клиентами. Т.е с клиентами
мы задаем в качестве default gateway придуманный нами виртуальный адрес из нужной подсети.

Соответственно когда ПК попытается RP запрос отправить, то ему будет возвращаться виртуальный мак адрес.

Если активный перестает отправлять запросы, то включается резервный и забирает на себя эту ответственность.

![img.png](img/lesson3/error_routing.png)

### FHRP 

![img.png](img/lesson3/FHRP.png)

HSRP работает когда есть 1 активный (active) и 1 резервный (standby). 


### HSRP 

Работает также как FHRP

![img.png](img/lesson3/HSRP.png)


### HSRP v1 vs v2

![img.png](img/lesson3/HSRP_v1_v2.png)

### Состояния HSRP

![img.png](img/lesson3/state_HSRP.png)


### Настройка HSRP

![img.png](img/lesson3/settings_HSRP.png)