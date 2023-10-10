# AssignmentsSharing
Laboratorium 2 - Modelowanie rzeczywistości projektu - w ramach zajęć "Programowanie zaawansowane"

## Opis
Program umożliwia przydzielanie zadań programistycznych do deweloperów.

W ramach narzędzia mamy możliwość dodania, edycji i usunięcia zadania jak również przydzielenia zadania określonemu deweloperowi.

Pojedyncze zadanie posiada pola: nazwa, opis oraz pracochłonność (czas w godzinach potrzebny do ukończenia zadania). 

Do każdego zadania przydzielana jest również etykieta statusu z ograniczonej puli (New, In Progress, Done).

Aplikacja oparta jest na framework Django.

## Setup
0. Sklonuj to repo
1. Zbuduj image:
   ```bash
   docker build -t assignments_sharing .
   ```
3. Uruchom container z image:
   ```bash
   docker run -p 8000:8000 -it assignments_sharing
   ```

## Instrukcja
Po poprawnym zbudowaniu projektu w formie aplikacji terminalowej możliwe jest wykonywanie poleceń w powłoce `/bin/bash`

Uruchomienie serwera Django możliwe jest przy użyciu polecenia:
```
python manage.py runserver 0.0.0.0:8000
```

## Lista komend:
Przykładowe komendy wchodzące w skład rozwiązania Django:
* https://www.educative.io/answers/what-are-django-commands

* https://docs.djangoproject.com/en/4.2/ref/django-admin/
