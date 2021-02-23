##Beschreibung Komponenten-Diagramm## 

#Übersicht# 

Die Web-Applikation "PrepPool" besteht aus drei Komponenten und dem Framework "Flask", das die Infrastruktur für das Backend bereitstellt. Das "Poolmanagement" im Frontend ist durch ein User-Interface mit dem Akteur verbunden. Frontend und Backend kommunizieren über "HTML GET/PUT"-Operationen und das Backend ist über SQL mit einer Datenbank verbunden. Das SQL-Interface bietet auch dem Systemadministrator die Möglichkeit Daten zu ändern. 

#Details# 

**Akteur**: Ist ein Nutzer von PrepPool. Lehrpersonen bilden das Zielpublikum von PrepPool.

**Poolmanagement**: Als grafische Benutzeroberfläche (UI) stellt das Frontend visuelle Elemente zur Verfügung, welcher der Interaktion mit dem Nutzer mit der Webapplikation dienen. Diese Elemente ermöglichen einerseits die Navigation über die Webseite und andererseits die Eingabe und Ausgabe von Daten. Im Spezifischen finden sich Masken für die Erstellung eines Accounts, eines Themas, einer Aufgabe und eines Aufgabenblatts sowie für das Login. Ans Backend werden die Daten per HTML GET-Operationen gesendet. Zudem werden im Frontend die bereits vom Nutzer erfassten Themen und Aufgaben per HTML POST-Operationen abgerufen und ausgegeben.

**Backend**: Das Backend ist verantwortlich für die gesamte Dienstleistung und die Bereitstellung der Daten für das Frontend. Es stellt die Administrationsoberfläche zur Erstellung neuer Inhalte für das Frontend dar und ermöglicht die Pflege der Nutzerdaten. Im Backend sind somit alle Klassen, Methoden und Interfaces gespeichert, welche zur Interaktion mit dem Frontend sowie der Datenbank dienen. Die Funktionen greifen auf die von FLASK zur Verfügung gestellten Funktionalitäten zurück. Das Backend kommuniziert über SQL mit der Datenbank.

**Flask**: Flask ist ein mikro Web-Framework für Python. Es stellt die Grundfunktionalitäten für das Backend zur Verfügung. 

**Datenbank**: Die Datenbank ist verantwortlich für die sichere, dauerhafte und effiziente Speicherung der verwalteten Daten. Dazu gehören die Nutzerdaten, wie Vorname, Nachname, Passwort, E-Mail, Schule, die von einer Lehrperson erfassten Themen und Aufgaben.

**Admin**: Der Systemadministrator ist verantwortlich für den Unterhalt der Webseite, die Autorisierung von Account-Anfragen, die Pflege der Nutzerdaten. Er kann über das Frontend kontaktiert werden und mit den Nutzern per E-Mail kommunizieren.


##Beschreibung Deployment-Diagramm##

Das "PrepPool"-Backend inkl. Flask und die Datenbank werden auf dem Webserver deployed. Nutzer führen das Frontend lokal in ihrem Webbrowser aus.
