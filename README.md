# Source code
 - booking 
    1. core django aplikacie so settings.py, url.py pre URL routing, views.py pre renderovanie template a django wsgi.py protokol
 - web:
    1. static/web - zlozka so statickymi subormi - css, js, fonts a images
    2. templates - hmtl subory ktore renderuju views funkcie
    3. tiez obsahuje url.py a views.py, naviac obsahuje models.py pre modely aplikacie a tests.py pre testovaci kod aplikacie
 - manage.py - manazer na spustanie django build in funkcionality.
 
# Requirements
- nainstalovany python 3.4 
- nainstalovat kniznicu PyMySQL (pip install pymysql)
- stiahnut a nainstalovat http://dev.mysql.com/downloads/installer/
- vytvorena databaza alebo import existujucej
- nainstalovane django 1.10 (pip install django)

spustenie prikazu vo windows cmd: 
- C:\Python34\python.py C:\Users\YOUR_NAME\Documents\GitHub\Prihlasovanie-na-sportove-aktivity\manage.py runserver

dalej v prehliadaci: 
- login URL: http://127.0.0.1:8000/
- domov URL: http://127.0.0.1:8000/domov


