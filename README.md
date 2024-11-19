# Python_Beadandó
Keresztes Tamás - FFMUOO

Az alábbi projekt során egy grafikus szókitaláló játékot készítettem.

**main.py**
- A main.py felelős a grafikus felület megjelenítéséért és annak kezeléséért a Python tkinter könyvtárának segítségével.
- Az ablakot (root) hozza létre, beállítja annak címét és alapvető méretét, valamint hozzáadja a felhasználói interakciókat támogató elemeket, mint például címkék (label), beviteli mezők (entry) és gombok (button).
- A main.py kapcsolódik a játék logikájához, amit a game.py biztosít. A fájl importálja a Game osztályt, amely a játék működését (szó kitalálása, próbálkozások száma stb.) irányítja.
- A fájl kezeli az eseményeket, mint a gombokra kattintás: a felhasználó tippjei, új játék indítása, próbálkozások száma, és a játék befejezésének ellenőrzése.
- Az egyes GUI elemekhez (gombokhoz) eseménykezelőket rendel: amikor a felhasználó a "Tippelek" gombra kattint, vagy új játékot indít, akkor a megfelelő függvények hívódnak meg a játékmenet irányítására.
- A felhasználó tippjei alapján a kt_guess függvény segítségével ellenőrzi, hogy a betű szerepel-e a szóban, és visszajelzést ad a felhasználónak a tipp helyességéről.
- Az App osztályban van egy lehetőség az új játék indítására. A felhasználó egy gomb megnyomásával új szót kap, és a próbálkozások száma is visszaáll.

**game.py**
- Az alábbi modulban található az előre megadott szavak listája, amelyből a program random választ ki egyet a random modul segítségével.
- A kt_check_guess függvény a tippelt betűk helyességét vizsgálja. Azaz azt nézi meg, hogy a felhasználó által megadott karakter szerepel-e a kiválasztott szóban. Ha igen, akkor frissíti a current_state-t (az aktuális szó rejtett, de már kitalált karaktereit tartalmazó változó), és jelez, hogy a tipp helyes volt. Ha nem szerepel a szóban, akkor azt is jelzi, és növeli a próbálkozások számát.

**kt_functions.py**
- Az alábbi modul tartalmazza a függvényemet saját monogrammal. A függvény azt ellenőrzi, hogy a felhasználó megfelelő bevitelt adott-e meg. Nem lehet szám és 1 betűnél több, különben hibával tér vissza a program.
