# Управление устройствами

### Протоколы обнаружения устройств: определение, принцип работы, характеристики.

CPD - протокол, используемый для обнаружения и сбора информации о подключенных устройствах Cisco в одной сети. Он
помогает создать карту сети, определяя соседние устройства, их типы и подключения.

![CDP.png](png/lesson7/CDP.png)
![Head_CDP.png](png/lesson7/Head_CDP.png)
![Data_CDP.png](png/lesson7/Data_CDP.png)
![Packet_WireShark_CDP.png](png/lesson7/Packet_WireShark_CDP.png)

**show cdp** - покажет общую настройку протокола
![show_cdp.png](png/lesson7/show_cdp.png)

![show_cdp_neighbors.png](png/lesson7/show_cdp_neighbors.png)

Команда show cdp neighbors отображает полезную
информацию о каждом соседнем устройстве CDP, в том числе следующие данные:

* Идентификатор устройства — имя хоста соседнего устройства (S1).
* Локальный интерфейс
* Время ожидания - сколько считаем времени устройства является подключенным
* Список возможностей — сведения о том, является ли устройство маршрутизатором или
  коммутатором (S обозначает коммутатор; I обозначает IGMP и в данном курсе не
  рассматривается).
* Платформа — аппаратная платформа устройства (WS-C3560 обозначает коммутатор Cisco
  3560).
* Идентификатор порта — имя локального или удаленного порта (Gig 0/0/1 и Fas 0/0/5
  соответственно).

![show_cdp_neighbors_detail.png](png/lesson7/show_cdp_neighbors_detail.png)

CDP на устройствах Cisco запущен по умолчанию

Существует еще 1 протокол выполняет ту же функции в сети

![LLDP.png](png/lesson7/LLDP.png)

Протокол обнаружения уровня канала (LLDP) делает то же самое, что и CDP, но он не специфичен для
устройств Cisco.

LLDP - не зависящий от производителя протокол обнаружения соседей, подобный CDP. LLDP работает с
сетевыми устройствами, такими как маршрутизаторы, коммутаторы и точки доступа к беспроводной сети
LAN. Этот протокол объявляет себя и свои возможности другим устройствам и получает данные от
физически подключенных устройств уровня 2.

![LLTP_Settings.png](png/lesson7/LLTP_Settings.png)
Отличие от CDP нужно на передачу и получение сообщений нужно настраивать отдельные команды

**lldp transmit**

**lldp receive**

### Службы времени: способы настройки системных часов, протокол NTP, его характеристика и принцип работы.

![System_Clock.png](png/lesson7/System_Clock.png)

Минусы:

1. Точность
2. Настройка на каждом устройстве
3. Если устройства выключили и включили, таймер пойдет с момента последнего
   выключения

**NTP** - сетевой протокол настройки времени. Служба устроена иерархически.

![NTP.png](png/lesson7/NTP.png)

![NTP_Settings.png](png/lesson7/NTP_Settings.png)

![example_1.png](png/lesson7/example_1.png)

![check_NTP.png](png/lesson7/check_NTP.png)

![show_ntp_associations.png](png/lesson7/show_ntp_associations.png)

* address - ip адрес устройства с которым мы синхронизируем часы (является сервером для нас)
* ref clock - показывает устройство которое выступает NTP сервером для сервера с которого мы получаем время
* st - на каком стратуме находится сервер от которого мы получаем время

### Системный журнал: протокол Syslog, характеристика и принцип работы, формат сообщений Syslog, уровни важности.

![Syslog.png](png/lesson7/Syslog.png)

![Syslog_Level_Importance_Message.png](png/lesson7/Syslog_Level_Importance_Message.png)

* level 0 - ситуация критическая и система не работает
* level 1 - 
* level 2 -
* level 3 -
* level 4 - критическое сообщение которое требует немедленных действий. Например стал не доступен интерфейс

![Syslog_Format.png](png/lesson7/Syslog_Format.png)

**service timestamps log datetime** - включение метки времени (Как в примере)

![Syslog_logging.png](png/lesson7/Syslog_logging.png)

![show_logging.png](png/lesson7/show_logging.png)

![Send_Message_to_Server_Syslog.png](png/lesson7/Send_Message_to_Server_Syslog.png)
