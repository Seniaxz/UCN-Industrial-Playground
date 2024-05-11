# OctoPrint & FDM Monster til Multi-Printerstyring
Dokumentation og opsætning af Multi-printerstyring ved UCN Industrial Playground udspringer fra et elevprojekt på 6.semester. 
Dette github repo indeholder ikke kune scripts og dokumentation, men er også tænkt som en trinvis vejledning til opsætning af OctoPrint og FDM Monster til styring af flere 3D-printere fra en enkelt Raspberry Pi, samt opkobling mellem Octoprint API og PostgreSQL via et python-script.

## Indholdsfortegnelse


* <b>Status</b> ⭐
* <b>Test Setup</b> 💻
  * Hardware 
  * Software
* <b>Basis opsætning</b> ⚙️
  * Installation af Raspbian/Octopi
    * Opsætning af Raspbian 
  * Installation af Octoprint
    * Indsamling af nødvendig info
    * Opsætning af Octoprint Services
    * Octoprint Services Script
* <b>Opsætning af python script & database ⚙️
    * Python script 
* <b>Extra</b> 🛠
  * Tabel til Notater (Opsætning af Octoprint Services)
  * Installationsscript til guided/automatisk opsætning af Octoprint Services
  * <s>Installationsscript til guided fuld opsætning af raspberry pi</s>


## Status ⭐
- [ ] Del 1 - Opsætning af Octoprint og FDM Monster
    - [x] Installere Raspbian og Octoprint på raspberry pi.
    - [x] Koble flere 3d printere på en enkelt raspberry pi.
    - [x] Semi Automastisk - Installationsscript til Octoprint Services og u-dev opsætning.
    - [x] Installere FDM Monster med tilhørende database (Docker).
    - [ ] Skrive og opdatere dokumentation.
- [ ] Del 2 - Opsætning af python script & database
    - [ ] Python Script som forbinder Octoprint API med PostgreSQL Database.
    - [ ] Skrive og opdatere dokumentation.
- [ ] Del 3 - Extra
    - [ ] Guided Automatisk - Installationsscript til Octoprint Services og u-dev opsætning.
    - [ ] Guided Automatisk - Installastionsscript til at Installere alt.
    - [ ] Skrive og opdatere dokumentation.


## Test Setup 💻
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



## Basis opsætning ⚙️

### Installation & Opsætning af Raspbian/Octopi
###### For at kunne opsætte Octoprint og FDM Monster, skal der først installeres et operativ system på Raspberry Pi. Dette kan gøres ved at installere Raspbian eller Octopi. Octopi er en version af Raspbian, som er optimeret til 3D-printere og Octoprint.
###### Følg vejledningen på [Raspberry Pi's hjemmeside](https://www.raspberrypi.org/software/) for at installere Raspbian eller [Octopi's hjemmeside](https://octoprint.org/download/) for at installere Octopi.


### Installation af Octoprint
###### Denne del af dokumentationen vil beskrive hvordan Octoprint installeres på Raspberry Pi. Kan droppes hvis Octopi er installeret istedet for raspbian.

#### Indsamling af nødvendig info
###### For at kunne opsætte flere 3D-printere på en enkelt Raspberry Pi, skal der indsamles information om hver enkelt printer. Dette inkluderer IP-adresse, port, brugernavn, password, USB Serial, USB Navn, USB Adresse og Octoprint API-Key.



#### Tabel til notater: 📖
###### Tabel til at notere information, ved opsætning af multi printer styring.
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


##### Eksempel: 📖
Eksempel med udgangspunkt i test-setup ved UCN Industrial Playground.
| Nr. | Printer Navn | Lokation | OctoPrint IP    | Port | Brugernavn | Password | USB Serial | USB Navn | USB Adresse |Octoprint API-Key |
|-----|--------------|----------|-----------------|------|------------|----------|------------|----------|-------------|------------------|
| 1   | M100         | 1-1      | 192.168.251.118 | 5000 | admin      | password | AM00N6SL   | Printer1 | /dev/usb0   | API_Key_1        |
| 2   | M200         | 1-2      | 192.168.251.118 | 5001 | admin      | password | AB0KDT74   | Printer2 | /dev/usb1   | API_Key_2        |
| 3   | M300         | 1-3      | 192.168.251.118 | 5002 | admin      | password | AB0KDFPC   | Printer3 | /dev/usb2   | API_Key_3        |
| 4   | M400         | 1-4      | 192.168.251.118 | 5003 | admin      | password | AR0K4OMU   | Printer4 | /dev/usb3   | API_Key_3        |

#### Opsætning af Octoprint Services

#### Octoprint Services Script




## Installationsscript
For at lette byrden med linux terminalen, er det lavet et script som udfyldes med informationen som er fundet tidligere og skrevet ind i tabellen. Auto-script som giver en guided installation og som selv samler informationen som skal benyttes til at opsætte flere 3d-printere er planlagt, dog vil scriptet være noget af det sidste som udvikles.


### ⚠️ Under Udvikling!
Dette projekt er under aktiv udvikling og kan have problemer. Vi værdsætter din forståelse og tålmodighed. Hvis du støder på problemer, bedes du først tjekke de åbne issues. Hvis dit problem ikke er angivet der, opret da venligst en ny problemstilling, hvor du beskriver fejlen eller problemet, du oplevede. Tak for din støtte!