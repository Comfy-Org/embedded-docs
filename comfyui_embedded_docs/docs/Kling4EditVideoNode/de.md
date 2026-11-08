# Kling 4.0 Video bearbeiten

Bearbeitet ein vorhandenes Video mit einem Text-Prompt unter Verwendung des Kling 4.0-Modells, optional unterstützt durch Referenzvideos und Referenzbilder. Das Ergebnis behält die Länge des Eingabevideos bei. Verwenden Sie es, um zu ändern, was in einem Clip passiert, ihn neu zu gestalten oder Elemente auszutauschen, während das ursprüngliche Timing unverändert bleibt.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `Modell` | Modellauswahl. `"kling-4.0"` unterstützt 1080p-Bearbeitungen bis zu 30 Sekunden; `"kling-4.0-flash"` ist auf 720p und 20 Sekunden beschränkt. Die Auswahl eines Modells blendet dessen Eingaben unten ein. | DYNAMIC_COMBO | Ja | `"kling-4.0"`<br>`"kling-4.0-flash"` |

### kling-4.0 Eingaben

Diese Eingaben erscheinen, wenn `model` auf `"kling-4.0"` gesetzt ist.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `video_1` | Das zu bearbeitende Video, 3 bis 30 Sekunden lang. Die Ausgabe behält seine Länge bei. | VIDEO | Ja | 3 bis 30 Sekunden |
| `reference_videos` | Erweiterbare Slots für Referenzvideos, bis zu 4. Verweisen Sie im Prompt darauf als `@Video2` und so weiter. Jedes Video und alle Videos zusammen müssen 3 bis 30 Sekunden lang sein. | AUTOGROW | Nein | 0 bis 4 Videos |
| `reference_images` | Erweiterbare Slots für Referenzbilder, bis zu 10. Verweisen Sie im Prompt darauf als `@Image1`, `@Image2` und so weiter. | AUTOGROW | Nein | 0 bis 10 Bilder |
| `prompt` | Beschreibung dessen, was geändert und was beibehalten werden soll. Verweisen Sie auf das zu bearbeitende Video als `@Video1`, auf die Referenzvideos als `@Video2` und so weiter und auf die Bilder als `@Image1` und so weiter. | STRING | Ja | 1 bis 26000 Zeichen |
| `resolution` | Auflösung des Ausgabevideos. Standard: `"720p"`. | COMBO | Ja | `"720p"`<br>`"1080p"` |
| `aspect_ratio` | Seitenverhältnis des Ausgabevideos. `"adaptive"` behält das Seitenverhältnis des Eingabevideos bei. Standard: `"adaptive"`. | COMBO | Ja | `"adaptive"`<br>`"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"21:9"` |
| `seed` | Der Seed steuert, ob der Node erneut ausgeführt werden soll; die Ergebnisse sind unabhängig vom Seed nicht deterministisch. Standard: 42. | INT | Ja | 0 bis 2147483647 |
| `audio` | `"native"` erzeugt neues Audio für das bearbeitete Video, `"original"` behält das Audio des Eingabevideos bei. Standard: `"native"`. | COMBO | Nein | `"native"`<br>`"original"` |

### kling-4.0-flash Eingaben

Diese Eingaben erscheinen, wenn `model` auf `"kling-4.0-flash"` gesetzt ist.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `video_1` | Das zu bearbeitende Video, 3 bis 20 Sekunden lang. Die Ausgabe behält seine Länge bei. | VIDEO | Ja | 3 bis 20 Sekunden |
| `reference_videos` | Erweiterbare Slots für Referenzvideos, bis zu 4. Verweisen Sie im Prompt darauf als `@Video2` und so weiter. Jedes Video und alle Videos zusammen müssen 3 bis 20 Sekunden lang sein. | AUTOGROW | Nein | 0 bis 4 Videos |
| `reference_images` | Erweiterbare Slots für Referenzbilder, bis zu 10. Verweisen Sie im Prompt darauf als `@Image1`, `@Image2` und so weiter. | AUTOGROW | Nein | 0 bis 10 Bilder |
| `prompt` | Beschreibung dessen, was geändert und was beibehalten werden soll. Verweisen Sie auf das zu bearbeitende Video als `@Video1`, auf die Referenzvideos als `@Video2` und so weiter und auf die Bilder als `@Image1` und so weiter. | STRING | Ja | 1 bis 26000 Zeichen |
| `resolution` | Auflösung des Ausgabevideos. Flash rendert nur in 720p. Standard: `"720p"`. | COMBO | Ja | `"720p"` |
| `aspect_ratio` | Seitenverhältnis des Ausgabevideos. `"adaptive"` behält das Seitenverhältnis des Eingabevideos bei. Standard: `"adaptive"`. | COMBO | Ja | `"adaptive"`<br>`"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"21:9"` |
| `seed` | Der Seed steuert, ob der Node erneut ausgeführt werden soll; die Ergebnisse sind unabhängig vom Seed nicht deterministisch. Standard: 42. | INT | Ja | 0 bis 2147483647 |
| `audio` | `"native"` erzeugt neues Audio für das bearbeitete Video, `"original"` behält das Audio des Eingabevideos bei. Standard: `"native"`. | COMBO | Nein | `"native"`<br>`"original"` |

**Einschränkungen und Verhalten:**

* Das Eingabevideo und jedes Referenzvideo müssen 3 bis 30 Sekunden lang sein (3 bis 20 mit `kling-4.0-flash`), mindestens 700x700 und höchstens 4553x4553 Pixel groß sein, insgesamt nicht mehr als 8.294.400 Pixel umfassen, ein Seitenverhältnis zwischen 2:5 und 5:2 sowie eine Bildrate von mindestens 24 fps aufweisen. Alle Videos zusammen dürfen dasselbe Limit nicht überschreiten.
* Jedes Referenzbild muss mindestens 300x300 Pixel groß sein und ein Seitenverhältnis zwischen 2:5 und 5:2 aufweisen; es können höchstens 10 Bilder verbunden werden.
* Ein Prompt, der `@VideoN` oder `@ImageN` erwähnt, löst einen Fehler aus, wenn weniger als N Eingaben dieser Art verbunden sind.

## Ausgaben

| Ausgabenamen | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `video` | Das bearbeitete Video, das vom Anbieter heruntergeladen wird, sobald die Aufgabe abgeschlossen ist. Es hat dieselbe Länge wie das Eingabevideo. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Kling4EditVideoNode/de.md)

---
**Source fingerprint (SHA-256):** `c682db61e1426059dc565b12c0da749944394f77f34aaa71b97c69f984cb0931`
