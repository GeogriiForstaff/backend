# Обслуживание устройств

### Операционные и файловые системы сетевого оборудования.

![memory.png](png/lesson8/memory.png)

**show file systems** - выводит список всех доступных файловых систем на маршрутизаторе

![show_file_system.png](png/lesson8/show_file_system.png)

#### flash

**dir** - посмотреть содержимое flash памяти

![Flash_File_System.png](png/lesson8/Flash_File_System.png)

**!Важный файл - файл ISO образа**

#### nvram

**cd nvram** - переход в новую файловую систему
**pwd** - показать в какой файловой системе находишься

![NVRAM_File_System.png](png/lesson8/NVRAM_File_System.png)

**!Важный файл - startapp config**

### Загрузка коммутатора и маршрутизатора. Начальный загрузчик.

![Processing_to_Start.png](png/lesson8/Processing_to_Start.png)
![Processing_to_Start_2.png](png/lesson8/Processing_to_Start_2.png)

#### Светодиодные индикаторы коммутатора

![Indicator_Commutator.png](png/lesson8/Indicator_Commutator.png)

### Резервное копирование и восстановление конфигурации.

Самый простой способ резервного копирования - это прописать команду **show running-config** и скопировать все в
текстовый файл. Далее при необходимости просто вставить содержимое текстового файла в интерфейс командной строки.

![Backup.png](png/lesson8/Backup.png)

![Password_Recovery.png](png/lesson8/Password_Recovery.png)

**Вход в режим ROMMON**

![ROMMON.png](png/lesson8/ROMMON.png)

![confreg.png](png/lesson8/confreg.png)

![copy.png](png/lesson8/copy.png)

![config_register.png](png/lesson8/config_register.png)

**Начальный загрузчик коммутатора**
![Password_Recovery_Commutator.png](png/lesson8/Password_Recovery_Commutator.png)

### Управление образами IOS. Имена файлов образов. Резервное копирование и восстановление образов IOS.

![Services_of_Demand.png](png/lesson8/Services_of_Demand.png)

![IOS_Image.png](png/lesson8/IOS_Image.png)

#### Резервное копирование образов IOS

![Backup_IOS.png](png/lesson8/Backup_IOS.png)

#### Восстановление образов IOS

![Restore_ISO.png](png/lesson8/Restore_IOS.png)

Просто скопировать образ недостаточно, нужно назначить какой образ должен быть использован при загрузке.

**R1(config)# boot system flash0://образ**

**copy running-config startapp-config** - нужно сохранять boot

Если boot не указан, то при загрузке устройство ищет первый доступный файл образа операционной системы.

**show version** - можно посмотреть какой файл образа запущен 