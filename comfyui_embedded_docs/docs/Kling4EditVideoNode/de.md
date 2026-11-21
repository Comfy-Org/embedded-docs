# Kling 4.0 Video bearbeiten

Bearbeitet ein vorhandenes Video mit einem Text-Prompt unter Verwendung des Kling 4.0-Modells, optional unterstützt durch Referenzvideos und Referenzbilder. Das Ergebnis behält die Länge des Eingabevideos bei. Verwenden Sie es, um zu ändern, was in einem Clip passiert, ihn neu zu gestalten oder Elemente auszutauschen, während das ursprüngliche Timing erhalten bleibt.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model` | Modellauswahl. `"kling-4.0"` unterstützt Bearbeitungen bis zu 4K HDR und 30 Sekunden; `"kling-4.0-flash"` ist auf 720p und 20 Sekunden beschränkt. Die Auswahl eines Modells blendet die zugehörigen Eingaben unten ein. | DYNAMIC_COMBO | Ja | `"kling-4.0"`<br>`"kling-4.0-flash"` |

### kling-4.0 Eingaben

Diese Eingaben erscheinen, wenn `model` auf `"kling-4.0"` gesetzt ist.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `video_1` | Das zu bearbeitende Video, 3 bis 30 Sekunden lang. Die Ausgabe behält seine Länge bei. | VIDEO | Ja | 3 bis 30 Sekunden |
| `reference_videos` | Erweiterbare Slots für Referenzvideos, bis zu 4. Verweisen Sie im Prompt mit `@Video2` usw. auf sie. Jedes Video und alle Videos zusammen müssen 3 bis 30 Sekunden lang sein. | AUTOGROW | Nein | 0 bis 4 Videos |
| `reference_images` | Erweiterbare Slots für Referenzbilder, bis zu 10. Verweisen Sie im Prompt mit `@Image1`, `@Image2` usw. auf sie. | AUTOGROW | Nein | 0 bis 10 Bilder |
| `prompt` | Beschreibung, was geändert und was beibehalten werden soll. Verweisen Sie auf das zu bearbeitende Video als `@Video1`, auf die Referenzvideos als `@Video2` usw. und auf die Bilder als `@Image1` usw. | STRING | Ja | 1 bis 26000 Zeichen |
| `resolution` | Auflösung des Ausgabevideos; eine Option mit `HDR` im Namen liefert ein HDR-Video. Standard: `"720p"`. | COMBO | Ja | `"720p"`<br>`"1080p"`<br>`"4k"`<br>`"1080p HDR"`<br>`"4k HDR"` |
| `aspect_ratio` | Seitenverhältnis des Ausgabevideos. `"adaptive"` behält das Seitenverhältnis des Eingabevideos bei. Standard: `"adaptive"`. | COMBO | Ja | `"adaptive"`<br>`"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"21:9"`<br>`"4:3"`<br>`"3:4"` |
| `seed` | Der Seed steuert, ob der Node erneut ausgeführt werden soll; die Ergebnisse sind unabhängig vom Seed nicht deterministisch. Standard: 42. | INT | Ja | 0 bis 2147483647 |
| `audio` | `"native"` erzeugt neues Audio für das bearbeitete Video, `"original"` behält das Audio des Eingabevideos bei. Standard: `"native"`. | COMBO | Nein | `"native"`<br>`"original"` |

### kling-4.0-flash Eingaben

Diese Eingaben erscheinen, wenn `model` auf `"kling-4.0-flash"` gesetzt ist.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `video_1` | Das zu bearbeitende Video, 3 bis 20 Sekunden lang. Die Ausgabe behält seine Länge bei. | VIDEO | Ja | 3 bis 20 Sekunden |
| `reference_videos` | Erweiterbare Slots für Referenzvideos, bis zu 4. Verweisen Sie im Prompt mit `@Video2` usw. auf sie. Jedes Video und alle Videos zusammen müssen 3 bis 20 Sekunden lang sein. | AUTOGROW | Nein | 0 bis 4 Videos |
| `reference_images` | Erweiterbare Slots für Referenzbilder, bis zu 10. Verweisen Sie im Prompt mit `@Image1`, `@Image2` usw. auf sie. | AUTOGROW | Nein | 0 bis 10 Bilder |
| `prompt` | Beschreibung, was geändert und was beibehalten werden soll. Verweisen Sie auf das zu bearbeitende Video als `@Video1`, auf die Referenzvideos als `@Video2` usw. und auf die Bilder als `@Image1` usw. | STRING | Ja | 1 bis 26000 Zeichen |
| `resolution` | Auflösung des Ausgabevideos. Flash rendert nur 720p. Standard: `"720p"`. | COMBO | Ja | `"720p"` |
| `aspect_ratio` | Seitenverhältnis des Ausgabevideos. `"adaptive"` behält das Seitenverhältnis des Eingabevideos bei. Standard: `"adaptive"`. | COMBO | Ja | `"adaptive"`<br>`"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"21:9"`<br>`"4:3"`<br>`"3:4"` |
| `seed` | Der Seed steuert, ob der Node erneut ausgeführt werden soll; die Ergebnisse sind unabhängig vom Seed nicht deterministisch. Standard: 42. | INT | Ja | 0 bis 2147483647 |
| `audio` | `"native"` erzeugt neues Audio für das bearbeitete Video, `"original"` behält das Audio des Eingabevideos bei. Standard: `"native"`. | COMBO | Nein | `"native"`<br>`"original"` |

**Einschränkungen und Verhalten:**

* Das Eingabevideo und jedes Referenzvideo müssen 3 bis 30 Sekunden lang sein (3 bis 20 mit `kling-4.0-flash`), mindestens 700x700 und höchstens 4553x4553 Pixel groß sein, insgesamt nicht mehr als 8.294.400 Pixel umfassen, mit einem Seitenverhältnis zwischen 2:5 und 5:2 und einer Bildrate von mindestens 24 fps. Alle Videos zusammen dürfen dasselbe Limit nicht überschreiten.
* Jedes Referenzbild muss mindestens 300x300 Pixel groß sein, mit einem Seitenverhältnis zwischen 2:5 und 5:2, und es können höchstens 10 Bilder verbunden werden.
* Ein Prompt, der `@VideoN` oder `@ImageN` erwähnt, löst einen Fehler aus, wenn weniger als N Eingaben dieser Art verbunden sind.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `video` | Das bearbeitete Video, das vom Anbieter heruntergeladen wird, sobald die Aufgabe abgeschlossen ist. Es hat dieselbe Länge wie das Eingabevideo. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Kling4EditVideoNode/de.md)

---
**Source fingerprint (SHA-256):** `7b7f48c3292a0c380f5fceecca2291dc74d99d5d73e4049bd67d33822cd0696e`
