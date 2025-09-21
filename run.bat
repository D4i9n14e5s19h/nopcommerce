@echo off
call .venv\Scripts\activate
if not exist reports mkdir reports
python -m pytest -s -v -m "sanity" --html=reports\test_report.html --browser chrome
pause
