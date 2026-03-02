# Photo Album - Django Project

## Fontos tudnivalók 
* **Adatbázis:** Az app **SQLite**-ot használ. Ez azt jelenti, hogy OpenShiften minden egyes új Build vagy újraindítás után az adatok (felhasználók, fotó hivatkozások) elveszhetnek, mivel a fájlrendszer nem perzisztens.
* **Fotók kezelése:** Ebben a verzióban fotót feltölteni és törölni **kizárólag a Django Admin felületén** (`/admin`) keresztül lehet. A felhasználói felület (UI) jelenleg csak a képek megtekintésére és a regisztrációra szolgál.

## ✨ Funkciók
* Regisztráció és Login rendszer.
* Responsive galéria nézet
* Egyedi képnézegető oldal
