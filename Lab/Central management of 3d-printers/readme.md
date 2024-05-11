# OctoPrint & FDM Monster til Multi-Printerstyring
Dokumentation for opsætning af Multi-Printerstyring ved UCN Industrial Playground.


## Indholdsfortegnelse
* Requirements
* Hardware 
* Software
* Fremgangsmetode
* Tabel til Notater


## Requirements
### Hardware
| Antal | Navn            |
|-------|-----------------|
| 1 stk | Raspberry Pi 4B |
| 4 stk | USB Kabler      |
| 4 stk | 3D Printer      |
| 1 stk | microSD         |


### Software
| Navn        | Beskrivelse                          | Link                             |
|-------------|--------------------------------------|----------------------------------|
| Raspbian    | Operativ System til raspberry pi     | https://github.com/raspberrypi   |
| Octoprint   | Solo - Firmware/Controller/Dashboard | https://github.com/OctoPrint     |
| FDM Monster | Multi - Controller/Dashboard         | https://github.com/fdm-monster   |
| PostgreSQL  | SQL Database                         | https://github.com/postgres      |


## Tabel til notater:
Tabel til at notere information ved opsætning af Multi Printer Styring.

| Nr. | Printer Navn | Lokation | OctoPrint IP  | Port | Brugernavn | Password | USB Serial | USB Navn | USB Adresse |Octoprint API-Key |
|-----|--------------|----------|---------------|------|------------|----------|------------|----------|-------------|------------------|
| 1   |              |          |               |      |            |          |            |          |             |                  |
| 2   |              |          |               |      |            |          |            |          |             |                  |
| 3   |              |          |               |      |            |          |            |          |             |                  |
| 4   |              |          |               |      |            |          |            |          |             |                  |
| 5   |              |          |               |      |            |          |            |          |             |                  |
| 6   |              |          |               |      |            |          |            |          |             |                  |
| 7   |              |          |               |      |            |          |            |          |             |                  |
| 8   |              |          |               |      |            |          |            |          |             |                  |
| 9   |              |          |               |      |            |          |            |          |             |                  |
| 10  |              |          |               |      |            |          |            |          |             |                  |


## Eksempel:
Eksempel med udgangspunkt i test-setup ved UCN Industrial Playground.

| Nr. | Printer Navn | Lokation | OctoPrint IP    | Port | Brugernavn | Password | USB Serial | USB Navn | USB Adresse |Octoprint API-Key |
|-----|--------------|----------|-----------------|------|------------|----------|------------|----------|-------------|------------------|
| 1   | M100         | 1-1      | 192.168.251.118 | 5000 | admin      | password | AM00N6SL   | Printer1 | /dev/usb0   | API_Key_1        |
| 2   | M200         | 1-2      | 192.168.251.118 | 5001 | admin      | password | AB0KDT74   | Printer2 | /dev/usb1   | API_Key_2        |
| 3   | M300         | 1-3      | 192.168.251.118 | 5002 | admin      | password | AB0KDFPC   | Printer3 | /dev/usb2   | API_Key_3        |
| 4   | M400         | 1-4      | 192.168.251.118 | 5003 | admin      | password | AR0K4OMU   | Printer4 | /dev/usb3   | API_Key_3        |


## Installationsscript
For at lette byrden med linux terminalen, er det lavet et script som udfyldes med informationen som er fundet tidligere og skrevet ind i tabellen. Auto-script som giver en guided installation og som selv samler alt informationen som skal intastes er under udvikling.

