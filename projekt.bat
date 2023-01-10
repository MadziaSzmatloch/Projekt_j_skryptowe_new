@echo off
:begin
chcp 65001 > nul
echo ────────────────────────────────────────────────────
echo 1.          INFORMACJE O PROJEKCIE
echo ────────────────────────────────────────────────────
echo 2.              URUCHOM PROGRAM
echo ────────────────────────────────────────────────────
echo 3.               STWÓRZ BACKUP 
echo ────────────────────────────────────────────────────
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
echo ──────────────────────────────────────────────────────────
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
echo ──────────────────────────────────────────────────────
python raport.py
echo ──────────────────────────────────────────────────────
echo                   Raport wygenerowany                    
echo ──────────────────────────────────────────────────────
pause
cls
goto begin

:option3
cls
echo ──────────────────────────────────────────────────────
echo             Tworzę kopię zapasową raportu                        
echo ──────────────────────────────────────────────────────
echo ...
echo ──────────────────────────────────────────────────────
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
