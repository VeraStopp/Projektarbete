# Projektarbete: Analys av E-handelsdata

Detta repository innehåller en snabbanalys av e-handelsdata. Målet är att identifiera nyckeltal och försäljningstrender för att ge rekommendationer till ledningen.

Den fullständiga, körbara rapporten finns i filen `report.ipynb`.

---

## 2. Hur man kör rapporten

För att köra denna analys lokalt, följ dessa steg:

1.  **Klona projektet:**
    ```bash
    git clone [https://github.com/VeraStopp/Projektarbete.git](https://github.com/VeraStopp/Projektarbete.git)
    cd Projektarbete
    ```

2.  **Skapa och aktivera en virtuell miljö (venv):**
    ```bash
    # Skapa miljön
    python -m venv venv
    
    # Aktivera miljön (Bash/Git Bash)
    source venv/Scripts/activate
    ```

3.  **Installera alla nödvändiga paket:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Kör rapporten:**
    Öppna mappen i VS Code och kör alla celler i `report.ipynb` från topp till botten.

---

## 3. Team & Ansvar

* **Vera:** Ansvarig för Intäkt per stad och sammanfattning av rapporten.
* **Carina:** Ansvarig för Intäkt per kategori.
* **Azar:** Ansvarig för Total intäkt och totalt antal enheter.
* **Ali:** Ansvarig för beräkning av AOV (Average Order Value) och alla visualiseringsfunktioner.
* **Gemensamt:** Hela teamet arbetade tillsammans på att implementera `EcommerceAnalyzer`-klassen.

---

## 4. Miljö

* **Python:** 3.13.7
* **Huvudbibliotek:** pandas
matplotlib
contourpy==1.3.3 
cycler==0.12.1
fonttools==4.60.1 
kiwisolver==1.4.9
matplotlib==3.10.7
numpy==2.3.4
packaging==25.0
pillow==12.0.0
pyparsing==3.2.5
python-dateutil==2.9.0.post0
six==1.17.0