# Kling 4.0 Edit Video

Bearbeitet ein vorhandenes Video mit einem Text-Prompt unter Verwendung des Kling-4.0-Modells, optional geleitet durch Referenzvideos und Referenzbilder. Das Ergebnis behält die Länge des Eingabevideos bei. Verwenden Sie es, um zu ändern, was in einem Clip passiert, ihn neu zu gestalten oder Elemente auszutauschen, während das ursprüngliche Timing erhalten bleibt.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model` | Modellauswahl. Nur `"kling-4.0"` ist verfügbar; bei Auswahl werden die unten aufgeführten Eingaben eingeblendet. | DYNAMIC_COMBO | Ja | `"kling-4.0"` |

### kling-4.0 Eingaben

Diese Eingaben erscheinen, wenn `model` auf `"kling-4.0"` gesetzt ist.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `video_1` | Das zu bearbeitende Video, 3 bis 30 Sekunden lang. Die Ausgabe behält die Länge des Videos bei. | VIDEO | Ja | 3 bis 30 seconds |
| `reference_videos` | Erweiterbare Slots für Referenzvideos, bis zu 4. Verweisen Sie im Prompt mit `@Video2` usw. darauf. Jedes Video sowie alle Videos zusammen müssen 3 bis 30 Sekunden lang sein. | AUTOGROW | Nein | 0 bis 4 Videos |
| `reference_images` | Erweiterbare Slots für Referenzbilder, bis zu 10. Verweisen Sie im Prompt mit `@Image1`, `@Image2` usw. darauf. | AUTOGROW | Nein | 0 bis 10 Bilder |
| `prompt` | Beschreibung dessen, was geändert und was beibehalten werden soll. Verweisen Sie auf das zu bearbeitende Video als `@Video1`, auf die Referenzvideos als `@Video2` usw. und auf die Bilder als `@Image1` usw. | STRING | Ja | 1 bis 26000 Zeichen |
| `resolution` | Auflösung des Ausgabevideos. Standard: `"720p"`. | COMBO | Ja | `"720p"`<br>`"1080p"` |
| `aspect_ratio` | Seitenverhältnis des Ausgabevideos. `"adaptive"` behält das Seitenverhältnis des Eingabevideos bei. Standard: `"adaptive"`. | COMBO | Ja | `"adaptive"`<br>`"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"21:9"` |
| `seed` | Der Seed steuert, ob der Node erneut ausgeführt werden soll; die Ergebnisse sind unabhängig vom Seed nicht deterministisch. Standard: 42. | INT | Ja | 0 bis 2147483647 |

**Einschränkungen und Verhalten:**

* Das Eingabevideo und jedes Referenzvideo müssen 3 bis 30 Sekunden lang sein, mindestens 700x700 und höchstens 4553x4553 Pixel groß sein, insgesamt nicht mehr als 8.294.400 Pixel umfassen und ein Seitenverhältnis zwischen 2:5 und 5:2 sowie eine Bildrate von mindestens 24 fps aufweisen. Alle Videos zusammen dürfen 30 Sekunden nicht überschreiten.
* Jedes Referenzbild muss mindestens 300x300 Pixel groß sein und ein Seitenverhältnis zwischen 2:5 und 5:2 aufweisen; es können höchstens 10 Bilder verbunden werden.
* Ein Prompt, der `@VideoN` oder `@ImageN` erwähnt, löst einen Fehler aus, wenn weniger als N Eingaben dieser Art verbunden sind.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `video` | Das bearbeitete Video, das nach Abschluss der Aufgabe vom Anbieter heruntergeladen wird. Es hat dieselbe Länge wie das Eingabevideo. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Kling4EditVideoNode/de.md)

---
**Source fingerprint (SHA-256):** `00e8de2529df9be6bc1fae5f2c2beda01f151143448e91b79f9cfb27436064ff`
