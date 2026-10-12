# Vidu4ImageToVideoNode

Erzeugen Sie ein Video aus einem Startbild und einem optionalen Prompt mit einem Vidu Q4-Modell. Die Ausgabe behält das Seitenverhältnis des Eingabebilds bei.

Die Auswahl eines `model` zeigt die für dieses Modell spezifischen Parameter an.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `image` | Startbild des generierten Videos. Das Seitenverhältnis muss zwischen 1:5 und 5:1 liegen. | IMAGE | Ja | N/A |
| `model` | Modell für die Videogenerierung. Die Auswahl eines Modells zeigt die für dieses Modell spezifischen Parameter an: `prompt`, `resolution`, `duration`, `audio` und `seed`. | DYNAMIC_COMBO | Ja | `"Vidu Q4 Preview"` |
| `prompt` | Ein optionaler Text-Prompt für die Videogenerierung, bis zu 5000 Zeichen (Standard: leer). | STRING | Ja | Beliebiger Text |
| `resolution` | Auflösung des Ausgabevideos (Standard: `"720p"`). | COMBO | Ja | `"540p"`<br>`"720p"`<br>`"1080p"`<br>`"2K"`<br>`"4K"` |
| `duration` | Dauer des Ausgabevideos in Sekunden (Standard: 5). | INT | Ja | 3 bis 16 |
| `audio` | Wenn aktiviert, wird Video mit Ton ausgegeben, einschließlich Dialogen und Soundeffekten (Standard: True). | BOOLEAN | Ja | `True`<br>`False` |
| `seed` | Der Seed steuert, ob der Node erneut ausgeführt werden soll; die Ergebnisse sind unabhängig vom Seed nicht deterministisch. Dieser Parameter verfügt über die Funktion „Steuerung nach Generierung“ (Standard: 42). | INT | Ja | 1 bis 2147483647 |

**Hinweis:** Das Seitenverhältnis von `image` muss zwischen 1:5 und 5:1 bleiben, und der `prompt` darf 5000 Zeichen nicht überschreiten. Das Ergebnis behält das Seitenverhältnis des Eingabebilds bei, daher folgt die Ausgabegröße der Einstellung `resolution` nur innerhalb dieses Verhältnisses.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `VIDEO` | Die generierte Videodatei. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Vidu4ImageToVideoNode/de.md)

---
**Source fingerprint (SHA-256):** `8778696edbdfb821afaa99dcba09cbebff57fd4cd2378273e82ad9fb18600b62`
