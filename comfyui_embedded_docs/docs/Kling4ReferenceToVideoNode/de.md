# Kling 4.0 Reference to Video

Erzeugt ein Video aus Referenzbildern und Referenzvideos mit dem Kling 4.0-Modell, einschließlich Audio. Die Referenzen bestimmen Motiv, Stil und Bewegung, und ein optionales erstes und letztes Frame legen den Anfang und das Ende des Clips fest. Verwenden Sie den Node, um eine Figur oder eine Szene innerhalb einer Aufnahme konsistent zu halten, während Sie die Aktion im Prompt beschreiben.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model` | Modellauswahl. Nur `"kling-4.0"` ist verfügbar; die Auswahl blendet die unten aufgeführten Eingaben ein. | DYNAMIC_COMBO | Ja | `"kling-4.0"` |

### kling-4.0 Eingaben

Diese Eingaben erscheinen, wenn `model` auf `"kling-4.0"` gesetzt ist.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `reference_images` | Erweiterbare Slots für Referenzbilder, bis zu 10. Verweisen Sie im Prompt in Verbindungsreihenfolge als `@Image1`, `@Image2` usw. auf sie. | AUTOGROW | Nein | 0 bis 10 Bilder |
| `reference_videos` | Erweiterbare Slots für Referenzvideos, bis zu 5. Verweisen Sie im Prompt als `@Video1`, `@Video2` usw. auf sie. Jedes Video und alle Videos zusammen müssen 3 bis 30 Sekunden lang sein. | AUTOGROW | Nein | 0 bis 5 Videos |
| `first_frame` | Optionales Frame, mit dem das Video beginnt. Zählt zusammen mit den Referenzbildern zum Limit von 10 Bildern. | IMAGE | Nein | - |
| `last_frame` | Optionales Frame, mit dem das Video endet. Zählt zusammen mit den Referenzbildern zum Limit von 10 Bildern. | IMAGE | Nein | - |
| `prompt` | Beschreibung des zu erzeugenden Videos. Verweisen Sie auf die Eingaben als `@Image1`, `@Image2` usw. sowie `@Video1`, `@Video2` usw. | STRING | Ja | 1 bis 26000 Zeichen |
| `resolution` | Auflösung des Ausgabevideos. Standard: `"720p"`. | COMBO | Ja | `"720p"`<br>`"1080p"` |
| `aspect_ratio` | Seitenverhältnis des Ausgabevideos. `"adaptive"` folgt dem Prompt, dann dem ersten Frame oder den Referenzvideos und greift andernfalls auf 16:9 zurück. Standard: `"adaptive"`. | COMBO | Ja | `"adaptive"`<br>`"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"21:9"` |
| `duration` | Länge des erzeugten Videos in Sekunden. Standard: 5. | INT | Ja | 3 bis 30 |
| `seed` | Der Seed steuert, ob der Node erneut ausgeführt werden soll; die Ergebnisse sind unabhängig vom Seed nicht deterministisch. Standard: 42. | INT | Ja | 0 bis 2147483647 |

**Einschränkungen und Verhalten:**

* Bilder sind insgesamt auf 10 begrenzt, wobei die Referenzbilder, das erste Frame und das letzte Frame mitgezählt werden.
* Jedes Bild muss mindestens 300x300 Pixel groß sein und ein Seitenverhältnis zwischen 2:5 und 5:2 aufweisen.
* Jedes Referenzvideo muss 3 bis 30 Sekunden lang sein, mindestens 700x700 und höchstens 4553x4553 Pixel groß sein, insgesamt nicht mehr als 8.294.400 Pixel umfassen, ein Seitenverhältnis zwischen 2:5 und 5:2 und eine Bildrate von mindestens 24 fps haben. Alle Referenzvideos zusammen dürfen 30 Sekunden nicht überschreiten.
* Ein Prompt, der `@ImageN` oder `@VideoN` erwähnt, löst einen Fehler aus, wenn weniger als N Eingaben dieser Art verbunden sind.
* Wenn ein erstes oder letztes Frame verbunden ist, fügt der Node eine Anweisung hinzu, dass das Video genau auf diesem Frame beginnt oder endet.

## Ausgaben

| Ausgabenamen | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `video` | Das erzeugte Video, das nach Abschluss der Aufgabe vom Anbieter heruntergeladen wird. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Kling4ReferenceToVideoNode/de.md)

---
**Source fingerprint (SHA-256):** `bda2298ed6ed06db04a8f342ec6ad0d5a0494e09bfadee72fce4420ebe4eaf6a`
