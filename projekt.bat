@echo off
:begin
chcp 65001 > nul
echo ────────────────────────────────────────────────────
echo                       MENU
echo ────────────────────────────────────────────────────
echo 1.          INFORMACJE O PROJEKCIE
echo 2.              URUCHOM PROGRAM
echo 3.               STWÓRZ BACKUP 
echo 4.                  ZAMKNIJ         
echo ────────────────────────────────────────────────────

set /p option=
if %option%==1 goto option1
if %option%==2 goto option2
if %option%==3 goto option3
if %option%==4 exit
goto wrong

:option1
cls
echo ──────────────────────────────────────────────────────────
echo                   INFORMACJE O PROJEKCIE                       
echo ──────────────────────────────────────────────────────────
echo            Autor projektu: Magdalena Szmatłoch             
echo        Zadanie 5 - "Bryły Obrotowe", Algorytmion 2015            
echo           Program oblicza przybliżone pole boczne 
echo             bryły obrotowej metodą trapezową  
echo ──────────────────────────────────────────────────────────
pause
cls
goto begin

:option2
cls
echo ──────────────────────────────────────────────────────
echo                 Uruchamiam skrypt python                  
python raport.py
python timesaving.py
python runwebsite.py
echo                   Raport wygenerowany                    
echo ──────────────────────────────────────────────────────
pause
cls
goto begin

:option3
cls
echo ──────────────────────────────────────────────────────
echo             Tworzę kopię zapasową raportu               
FOR /F %%i IN (time.txt) DO set time=%%i
mkdir kopie_zapasowe\%time%
xcopy raport.html kopie_zapasowe\%time%
ren kopie_zapasowe\%time%\raport.html %time%.html
xcopy Plot.png kopie_zapasowe\%time%
xcopy style.css kopie_zapasowe\%time%
echo                Kopia zapasowa wykonana                   
echo ──────────────────────────────────────────────────────
pause
cls
goto begin

:wrong
cls
echo ────────────────────────────────────────────────────────────
echo                   Podałeś błędną wartość.  
echo      Wciśnij dowolny klawisz aby wrócić do okna wyboru.                 
echo ────────────────────────────────────────────────────────────
pause
goto begin
