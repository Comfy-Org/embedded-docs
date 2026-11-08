# Kling 4.0 Referenz zu Video

Erzeugt ein Video aus Referenzbildern und Referenzvideos mit dem Kling 4.0-Modell, einschließlich Audio. Die Referenzen steuern Motiv, Stil und Bewegung, und ein optionales erstes und letztes Bild legen den Anfang und das Ende des Clips fest. Verwenden Sie diese Funktion, um eine Figur oder eine Szene über eine Aufnahme hinweg konsistent zu halten, während Sie die Aktion im Prompt beschreiben.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `Modell` | Modellauswahl. `"kling-4.0"` unterstützt bis zu 1080p, 30-Sekunden-Clips und ein letztes Bild; `"kling-4.0-flash"` ist auf 720p und 20 Sekunden beschränkt und hat keine `last_frame`-Eingabe. Die Auswahl eines Modells blendet die zugehörigen Eingaben unten ein. | DYNAMIC_COMBO | Ja | `"kling-4.0"`<br>`"kling-4.0-flash"` |

### kling-4.0 Eingaben

Diese Eingaben werden angezeigt, wenn `model` auf `"kling-4.0"` gesetzt ist.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `reference_images` | Erweiterbare Slots für Referenzbilder, bis zu 10. Verweisen Sie im Prompt darauf als `@Image1`, `@Image2` usw., in Verbindungsreihenfolge. | AUTOGROW | Nein | 0 bis 10 Bilder |
| `reference_videos` | Erweiterbare Slots für Referenzvideos, bis zu 5. Verweisen Sie im Prompt darauf als `@Video1`, `@Video2` usw. Jedes Video und alle Videos zusammen müssen 3 bis 30 Sekunden lang sein. | AUTOGROW | Nein | 0 bis 5 Videos |
| `first_frame` | Optionales Bild, mit dem das Video beginnt. Zählt zusammen mit den Referenzbildern zum Limit von 10 Bildern. | IMAGE | Nein | - |
| `last_frame` | Optionales Bild, mit dem das Video endet. Zählt zusammen mit den Referenzbildern zum Limit von 10 Bildern. | IMAGE | Nein | - |
| `prompt` | Beschreibung des zu generierenden Videos. Verweisen Sie auf die Eingaben als `@Image1`, `@Image2` usw. und `@Video1`, `@Video2` usw. | STRING | Ja | 1 bis 26000 Zeichen |
| `resolution` | Auflösung des Ausgabevideos. Standard: `"720p"`. | COMBO | Ja | `"720p"`<br>`"1080p"` |
| `aspect_ratio` | Seitenverhältnis des Ausgabevideos. `"adaptive"` folgt dem Prompt, dann dem ersten Bild oder den Referenzvideos und fällt andernfalls auf 16:9 zurück. Standard: `"adaptive"`. | COMBO | Ja | `"adaptive"`<br>`"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"21:9"` |
| `duration` | Länge des generierten Videos in Sekunden. Standard: 5. | INT | Ja | 3 bis 30 |
| `seed` | Der Seed steuert, ob der Node erneut ausgeführt werden soll; die Ergebnisse sind unabhängig vom Seed nicht deterministisch. Standard: 42. | INT | Ja | 0 bis 2147483647 |

### kling-4.0-flash Eingaben

Diese Eingaben werden angezeigt, wenn `model` auf `"kling-4.0-flash"` gesetzt ist.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `reference_images` | Erweiterbare Slots für Referenzbilder, bis zu 10. Verweisen Sie im Prompt darauf als `@Image1`, `@Image2` usw., in Verbindungsreihenfolge. | AUTOGROW | Nein | 0 bis 10 Bilder |
| `reference_videos` | Erweiterbare Slots für Referenzvideos, bis zu 5. Verweisen Sie im Prompt darauf als `@Video1`, `@Video2` usw. Jedes Video und alle Videos zusammen müssen 3 bis 20 Sekunden lang sein. | AUTOGROW | Nein | 0 bis 5 Videos |
| `first_frame` | Optionales Bild, mit dem das Video beginnt. Zählt zusammen mit den Referenzbildern zum Limit von 10 Bildern. | IMAGE | Nein | - |
| `prompt` | Beschreibung des zu generierenden Videos. Verweisen Sie auf die Eingaben als `@Image1`, `@Image2` usw. und `@Video1`, `@Video2` usw. | STRING | Ja | 1 bis 26000 Zeichen |
| `resolution` | Auflösung des Ausgabevideos. Flash rendert nur 720p. Standard: `"720p"`. | COMBO | Ja | `"720p"` |
| `aspect_ratio` | Seitenverhältnis des Ausgabevideos. `"adaptive"` folgt dem Prompt, dann dem ersten Bild oder den Referenzvideos und fällt andernfalls auf 16:9 zurück. Standard: `"adaptive"`. | COMBO | Ja | `"adaptive"`<br>`"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"21:9"` |
| `duration` | Länge des generierten Videos in Sekunden. Standard: 5. | INT | Ja | 3 bis 20 |
| `seed` | Der Seed steuert, ob der Node erneut ausgeführt werden soll; die Ergebnisse sind unabhängig vom Seed nicht deterministisch. Standard: 42. | INT | Ja | 0 bis 2147483647 |

**Einschränkungen und Verhalten:**

* Bilder sind insgesamt auf 10 begrenzt, wobei Referenzbilder, erstes Bild und letztes Bild gezählt werden.
* Jedes Bild muss mindestens 300x300 Pixel groß sein, mit einem Seitenverhältnis zwischen 2:5 und 5:2.
* Jedes Referenzvideo muss 3 bis 30 Sekunden lang sein (3 bis 20 bei `kling-4.0-flash`), mindestens 700x700 und höchstens 4553x4553 Pixel groß sein, insgesamt nicht mehr als 8.294.400 Pixel umfassen, ein Seitenverhältnis zwischen 2:5 und 5:2 sowie eine Bildrate von mindestens 24 fps aufweisen. Alle Referenzvideos zusammen dürfen dieselbe Grenze nicht überschreiten.
* Ein Prompt, der `@ImageN` oder `@VideoN` erwähnt, löst einen Fehler aus, wenn weniger als N Eingaben dieser Art verbunden sind.
* Wenn ein erstes oder ein letztes Bild verbunden ist, fügt der Node eine Anweisung hinzu, dass das Video genau auf diesem Bild beginnt oder endet.

## Ausgaben

| Ausgabenamen | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `video` | Das generierte Video, das nach Abschluss der Aufgabe vom Anbieter heruntergeladen wird. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Kling4ReferenceToVideoNode/de.md)

---
**Source fingerprint (SHA-256):** `78a85e66ab05f784102829fc86917b363fabad6bb5443c36b83e250e59ed07b7`
