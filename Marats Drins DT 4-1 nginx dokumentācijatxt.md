
# Nginx dokumentācija
Autors - Marats Driņs DT4-1
## Saturs

 - Sistēmas prasības
 -  Instalācijas Soļi

    <sup> 1. Atjauniniet Sistēmas Pakotnes
    2. Instalējiet Nginx
    3. Startējiet/pārbaudījiet/ieslēdziet  Nginx Servisu
    4. Pārbaudiet nginx darbību
    5. Konfigurācija

 - Komandas nozīmes

## Sistēmas Prasības
Minimālas prasības lai instalētu Nginx servisu:
RAM - 512 MB
CPU - Vienkodola procesors
Diska brīva vieta - 50 MB
Administratora (root) tiesības
 

## Instalācijas Soļi

### 1. Atjauniniet Sistēmas Pakotnes
Pirms instalācijas atjauniniet pakotņu sarakstu un esošās pakotnes:
```bash
sudo apt update && sudo apt upgrade -y
```


### 2. Instalējiet Nginx

```bash 
 sudo apt install nginx -y
 ```
 
### 3. Startējiet/pārbaudijiet/ieslēdziet  Nginx Servisu
Startēt :
```bash 
sudo systemctl start nginx
```
Parbaudīt statusu:

```bash 
sudo systemctl status nginx
```
Ieslēgt:
```bash 
sudo systemctl enable nginx
```
### 4. Pārbaudiet nginx darbību
Aiziesim uz http://localhost vietni internet pārlūkprogrammā. Jums ir jābūt redzamai nginx sveiciena web-lapai. "Welcome to nginx!"

### 5. Konfigurācija
Konfigurācijas fails atrodās */etc/nginx* direktorijā.

## Komandas nozīmes
sudo - lietot administratora (root tiesības) 
apt - advanced package tools programma (pakotņu atjaunošanas programma) 
&& - modifikators, kas ļauj ievadīt divus komandus viena rindā 
-y - modifikators, kas automatiski atbild Yes (jā) uz visiem terminala jautājumiem
update - atjaunināt pakotņu sarakstu
upgrade - atjaunināt pakotnes
systemctl - pārvalda Linux sistēmas pakalpojumus (servisus)





