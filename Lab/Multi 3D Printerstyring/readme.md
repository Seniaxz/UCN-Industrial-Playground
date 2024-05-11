# OctoPrint & FDM Monster til Multi-Printerstyring
###### Dokumentation og opsætning af Multi-printerstyring ved UCN Industrial Playground udspringer fra et elevprojekt på 6.semester. Dette github repo indeholder ikke kune scripts og dokumentation, men er også tænkt som en trinvis vejledning til opsætning af OctoPrint og FDM Monster til styring af flere 3D-printere fra en enkelt Raspberry Pi, samt opkobling mellem Octoprint API og PostgreSQL via et python-script.

## Indholdsfortegnelse


* <b>Status</b> ⭐
* <b>Test Setup</b> 💻
  * Hardware 
  * Software
* <b>Basis opsætning</b> ⚙️
  * Installation & Opsætning af Octopi
    * Indsamling af nødvendig info
    * Opsætning af Octoprint Services
    * Octoprint Services Script
* <b>Opsætning af python script & database</b> ⚙️
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
    - [ ] Skrive, Opdatere & Uddybe Dokumentation/Guide.
- [ ] Del 2 - Opsætning af python script & database
    - [ ] Python Script som forbinder Octoprint API med PostgreSQL Database.
    - [ ] Skrive, Opdatere & Uddybe Dokumentation/Guide.
- [ ] Del 3 - Extra
    - [ ] Guided Automatisk - Installationsscript til Octoprint Services og u-dev opsætning.
    - [ ] Guided Automatisk - Installastionsscript til at installere alt.
    - [ ] Skrive, Opdatere & Uddybe Dokumentation/Guide.


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

### Installation & Opsætning af Octopi
###### For at kunne opsætte Octoprint og FDM Monster, skal der først installeres et operativ system på Raspberry Pi. Dette kan gøres ved at installere Raspbian, eller i dette tilfælde Octopi. Octopi er en version af Raspbian, som er optimeret til 3D-printere og Octoprint. _(det anbefales at bruge Octopi, da det er nemmere at opsætte og er optimeret til 3D-printere)_.
###### Følg vejledningen på [Octopi's hjemmeside](https://octoprint.org/download/) for at installere Octopi.

#### Indsamling af nødvendig info
###### For at kunne opsætte flere 3D-printere på en enkelt Raspberry Pi, skal der indsamles information om hver enkelt printer. Dette inkluderer IP-adresse, port, brugernavn, password, USB Serial, USB Navn, USB Adresse og Octoprint API-Key.

#### Tabel og Notater
###### Start med at udfylde felterne i tabellen nedenfor med informationen om hver enkelt printer, særligt forberedelse af "Printer Navn, Lokation, Brugernavn og Password. Hvis ip adressen til raspberry pi er ukendt, kan den findes ved at logge ind og tjekke forbundende enheder på netværksrouteren. Porten til Octoprint er standard 5000 og efterfølgende porte vælges løbende som 5001, 5002, 5003 dvs. at printer nr.1 = "5000" nr.2 = "5001" nr.3 = "5002" osv.

###### USB Serial, USB Navn og USB Adresse kan findes ved at tilslutte hver enkelte printer en, efter en til Raspberry Pi og køre kommandoen `lsusb` i terminalen. Hvorefter at du kan se hvilken USB port printeren er tilsluttet til. USB Serial kan findes ved at køre kommandoen `dmesg | grep tty` i terminalen. USB Navn og USB Adresse kan findes ved at køre kommandoen `ls -l /dev/serial/by-id/` i terminalen.

###### Octoprint API-Key kan findes/genereres ved at logge ind på Octoprint og gå til "Settings" -> "API" -> "API Key". Kopier API Key og indsæt i tabellen. API-key kan genereres senere da det ikke skal bruges før installationen af FDM Monster og så er API-Key nødvendig for at kunne forbinde Octoprint API med PostgreSQL Databasen.

##### Tabel til notater.
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


#### Eksempel:
###### Et eksempel med udgangspunkt i test-setup ved UCN Industrial Playground.
| Nr. | Printer Navn | Lokation | OctoPrint IP    | Port | Brugernavn | Password | USB Serial | USB Navn | USB Adresse |Octoprint API-Key |
|-----|--------------|----------|-----------------|------|------------|----------|------------|----------|-------------|------------------|
| 1   | M100         | 1-1      | 192.168.251.118 | 5000 | admin      | password | AM00N6SL   | Printer1 | /dev/usb0   | API_Key_1        |
| 2   | M200         | 1-2      | 192.168.251.118 | 5001 | admin      | password | AB0KDT74   | Printer2 | /dev/usb1   | API_Key_2        |
| 3   | M300         | 1-3      | 192.168.251.118 | 5002 | admin      | password | AB0KDFPC   | Printer3 | /dev/usb2   | API_Key_3        |
| 4   | M400         | 1-4      | 192.168.251.118 | 5003 | admin      | password | AR0K4OMU   | Printer4 | /dev/usb3   | API_Key_3        |

#### Opsætning af Octoprint Services
###### For at kunne opsætte flere 3D-printere på en enkelt Raspberry Pi, skal der opsættes en service for hver enkelt printer. Hver service kommer til at køre en instans af Octoprint, som er forbundet til en specifik 3D-printer. For at opsætte en service, skal der oprettes en fil med navnet `octoprint@.service` i mappen `/etc/systemd/system/`. Baseret på overstående eksempel skal filen indeholde koden som er i filen eksempel_octoprint_services.sh


#### Octoprint Services Script
###### For at lette byrden med at opsætte en service for hver enkelt printer, kan følgende script benyttes. Scriptet opretter 3 services, ud over den som allerede er oprettet via Octoprint installationen, disse kører alle en instans af Octoprint, men bliver forbundet til en specifik 3D-printer. Scriptet opretter også en regel i `udev` for at oprette en symbolisk link til hver enkelt printer. Scriptet kan køres ved at kopiere koden ind i en fil som navngives dit-filnavn-her.sh, og derefter indsætte de korrekte informationer på linjerne.

###### Når filen er rettet og gemt, kan scriptet køres ved at skrive `sudo bash dit-filnavn-her.sh` i terminalen. Scriptet vil nu oprette 3 extra services, som kører Octoprint instanser, og en regel i `udev` for at oprette en symbolisk link til hver enkelt printer.


```bash
#!/bin/bash
cp -R /home/pi/.octoprint /home/pi/.octoprint2
cp -R /home/pi/.octoprint /home/pi/.octoprint3
cp -R /home/pi/.octoprint /home/pi/.octoprint4
sudo chown -R pi:pi /home/pi/.octoprint2
sudo chown -R pi:pi /home/pi/.octoprint3
sudo chown -R pi:pi /home/pi/.octoprint4
cd /etc/systemd/system/
sudo sed s/127.0.0.1/0.0.0.0/ < octoprint.service | sed s/5000/5001/ | sed s/--port=\${PORT}/--port=\${PORT}\ --basedir=\\/home\\/pi\\/\.octoprint2/ > octoprint2.service
sudo sed s/127.0.0.1/0.0.0.0/ < octoprint.service | sed s/5000/5002/ | sed s/--port=\${PORT}/--port=\${PORT}\ --basedir=\\/home\\/pi\\/\.octoprint3/ > octoprint3.service
sudo sed s/127.0.0.1/0.0.0.0/ < octoprint.service | sed s/5000/5003/ | sed s/--port=\${PORT}/--port=\${PORT}\ --basedir=\\/home\\/pi\\/\.octoprint4/ > octoprint4.service
sudo systemctl enable octoprint2
sudo systemctl enable octoprint3
sudo systemctl enable octoprint4
sudo systemctl start octoprint2
sudo systemctl start octoprint3
sudo systemctl start octoprint4
echo "SUBSYSTEM==\"tty\", ATTRS{idVendor}==\"0403\", ATTRS{idProduct}==\"6001\", ATTRS{devpath}==\"\", ATTRS{serial}==\"AM00N6SL\", SYMLINK+=\"M100\"" > /etc/udev/rules.d/99-usb.rules
echo "SUBSYSTEM==\"tty\", ATTRS{idVendor}==\"0403\", ATTRS{idProduct}==\"6001\", ATTRS{devpath}==\"\", ATTRS{serial}==\"AB0KDT74\", SYMLINK+=\"M200\"" >> /etc/udev/rules.d/99-usb.rules
echo "SUBSYSTEM==\"tty\", ATTRS{idVendor}==\"0403\", ATTRS{idProduct}==\"6001\", ATTRS{devpath}==\"\", ATTRS{serial}==\"AB0KDFPC\", SYMLINK+=\"M300\"" >> /etc/udev/rules.d/99-usb.rules
echo "SUBSYSTEM==\"tty\", ATTRS{idVendor}==\"0403\", ATTRS{idProduct}==\"6001\", ATTRS{devpath}==\"\", ATTRS{serial}==\"AR0K4OMU\", SYMLINK+=\"M400\"" >> /etc/udev/rules.d/99-usb.rules
```

### <s>Opsætning af python script & database</s> ⚙️

#### <s>Python script</s>

#### <s>PostgresSQL Database</s>

### <s>Extra 🛠</s>

#### <s>Tabel til Notater (Opsætning af Octoprint Services)</s>

#### <s>Installationsscript til guided/automatisk opsætning af Octoprint Services</s>

#### <s>Installationsscript til guided fuld opsætning af raspberry pi</s>

### ⚠️ Under Udvikling!
###### Dette projekt er under aktiv udvikling og kan have problemer. Vi værdsætter din forståelse og tålmodighed. Hvis du støder på problemer, bedes du først tjekke de åbne issues. Hvis dit problem ikke er angivet der, opret da venligst en ny problemstilling, hvor du beskriver fejlen eller problemet, du oplevede. Tak for din støtte!