# Lab 4 Data processing in Databases

## Opis wybranej technologii
Do rozwiązania zadania użyłem python3 z jedną zewnętrzną biblioteką - time - do operacji na datach.

W moim rozwiązaniu użyłem słowników jako bazy danych. Tak jak widać w kodzie wydzieliłem na samej górze słowniki użyte do implementacji bazy danych.
1. Song table - indeks to songId a pola to:
    * songIdTitle = {} - idSong: Title,
    * songIdArtist = {} - songId: Artist,
2. User table - indeks to userId a pola to:
    * userSongId = {} - userId: songId's - wszystkie piosenki które odsłuchał dany user z ich licznością,
3. Date table - przechowuję tylko miesiące dla szybkości rozwiązania:
    * monthCount = {} - month: count
4. Imitacja tabeli faktów Listen - Odsłuchnia, jako powiązania między pozostałymi tabelami zaimplementowanymi w funkcjach zad1 - zad5