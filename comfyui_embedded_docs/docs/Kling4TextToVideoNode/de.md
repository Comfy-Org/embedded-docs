# Kling 4.0 Text zu Video

Erzeugt ein Video aus einer Textbeschreibung mit dem Kling 4.0-Modell, inklusive Audio. Dieser Node sendet die Eingabeaufforderung und die Generierungseinstellungen an die Kling-API, wartet auf den Abschluss der Aufgabe und gibt das fertige Video zurück. Verwenden Sie ihn, wenn ein Clip allein aus einer Beschreibung ohne Referenzmedien erstellt werden soll.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `Modell` | Modellauswahl. `"kling-4.0"` unterstützt bis zu 1080p und 30 Sekunden; `"kling-4.0-flash"` ist auf 720p und 20 Sekunden beschränkt. Wenn Sie ein Modell auswählen, werden dessen Eingaben unten eingeblendet. | DYNAMIC_COMBO | Ja | `"kling-4.0"`<br>`"kling-4.0-flash"` |

### kling-4.0 Eingaben

Diese Eingaben erscheinen, wenn `model` auf `"kling-4.0"` gesetzt ist.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Textbeschreibung des zu generierenden Videos. Muss zwischen 1 und 26000 Zeichen lang sein. | STRING | Ja | 1 bis 26000 Zeichen |
| `resolution` | Auflösung des Ausgabevideos. Standard: `"720p"`. | COMBO | Ja | `"720p"`<br>`"1080p"` |
| `aspect_ratio` | Seitenverhältnis des Ausgabevideos. Standard: `"16:9"`. | COMBO | Ja | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"21:9"` |
| `duration` | Länge des generierten Videos in Sekunden. Standard: 5. | INT | Ja | 3 bis 30 |
| `seed` | Der Seed steuert, ob der Node erneut ausgeführt werden soll; die Ergebnisse sind unabhängig vom Seed nicht deterministisch. Standard: 42. | INT | Ja | 0 bis 2147483647 |

### kling-4.0-flash Eingaben

Diese Eingaben erscheinen, wenn `model` auf `"kling-4.0-flash"` gesetzt ist.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Textbeschreibung des zu generierenden Videos. Muss zwischen 1 und 26000 Zeichen lang sein. | STRING | Ja | 1 bis 26000 Zeichen |
| `resolution` | Auflösung des Ausgabevideos. Flash rendert ausschließlich 720p. Standard: `"720p"`. | COMBO | Ja | `"720p"` |
| `aspect_ratio` | Seitenverhältnis des Ausgabevideos. Standard: `"16:9"`. | COMBO | Ja | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"21:9"` |
| `duration` | Länge des generierten Videos in Sekunden. Standard: 5. | INT | Ja | 3 bis 20 |
| `seed` | Der Seed steuert, ob der Node erneut ausgeführt werden soll; die Ergebnisse sind unabhängig vom Seed nicht deterministisch. Standard: 42. | INT | Ja | 0 bis 2147483647 |

## Ausgaben

| Ausgabenamen | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `video` | Das generierte Video, das nach Abschluss der Aufgabe vom Anbieter heruntergeladen wird. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Kling4TextToVideoNode/de.md)

---
**Source fingerprint (SHA-256):** `3e37f976f48488c3accb4efb0d876d12c316796023eb9c28b9209cb2188249e2`
