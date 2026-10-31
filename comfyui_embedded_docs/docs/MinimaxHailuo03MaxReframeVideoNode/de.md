# MiniMax H3 Max Reframe Video

Dieser Node passt ein Video an ein neues Seitenverhältnis an, indem er es auf eine neue Leinwand einpasst und die umgebenden Bereiche generiert. Timing und Ton des Quellvideos bleiben erhalten. Verwenden Sie ihn, um einen Querformat-Clip in einen vertikalen umzuwandeln oder umgekehrt, ohne das Motiv aus dem Bild zu schneiden.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model` | Modell, das für die Videogenerierung verwendet wird. | DYNAMIC_COMBO | Ja | "MiniMax H3 Max" |

### MiniMax H3 Max Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `video` | Quellvideo, das neu gerahmt werden soll, 0,5 bis 300 Sekunden lang. | VIDEO | Ja | 0.5 bis 300 Sekunden |
| `aspect_ratio` | Seitenverhältnis der Ausgabeleinwand (Standard: "9:16"). | COMBO | Ja | "16:9"<br>"9:16"<br>"1:1"<br>"4:3"<br>"3:4"<br>"21:9"<br>"9:21" |
| `resolution` | Auflösung des Ausgabevideos (Standard: "768P"). | COMBO | Ja | "480P"<br>"768P"<br>"1080P" |
| `prompt` | Optionale Vorgabe für die generierten Umgebungsbereiche. | STRING | Ja | 0 bis 50000 Zeichen |
| `seed` | Zufallsseed. Dieselbe Anfrage mit demselben Seed liefert ähnliche, aber nicht garantiert identische Ergebnisse (Standard: 42). | INT | Ja | 0 bis 4294967295 |

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `video` | Das neu gerahmte Video im ausgewählten Seitenverhältnis. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuo03MaxReframeVideoNode/de.md)

---
**Source fingerprint (SHA-256):** `83d780c2fe8c42475d4ad25ad5b318f2a4c135edef9c0ca1ff0d1fd07d90c1c6`
