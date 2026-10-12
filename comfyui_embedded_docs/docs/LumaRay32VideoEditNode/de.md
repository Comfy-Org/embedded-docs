# LumaRay32VideoEditNode

## Übersicht

Dieser Node rendert ein vorhandenes Video mit einem neuen Prompt unter Verwendung von Luma Ray 3.2 neu, sodass Sie Elemente umstylen, neu beleuchten, hinzufügen oder entfernen können, während die ursprüngliche Bewegung erhalten bleibt. Das Quellvideo kann bis zu 18 Sekunden lang sein, und das bearbeitete Video behält die ursprüngliche Länge der Quelle bei.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `video` | Quellvideo zum Bearbeiten. Bis zu 18 Sekunden. | VIDEO | Ja | - |
| `prompt` | Beschreibt die gewünschte Bearbeitung. | STRING | Ja | - |
| `resolution` | Die Ausgabeauflösung für das bearbeitete Video. (Standard: "720p") | COMBO | Ja | `"360p"`<br>`"540p"`<br>`"720p"`<br>`"1080p"` |
| `strength` | Wie stark die Quelle bewahrt werden soll, anstatt sie neu zu interpretieren. "auto" lässt Ray 3.2 wählen; adhere_* bewahrt am meisten, flex_* ist ausgewogen, reimagine_* ändert am meisten. (Standard: "auto") | COMBO | Ja | `"auto"`<br>`"adhere_1"`<br>`"adhere_2"`<br>`"adhere_3"`<br>`"flex_1"`<br>`"flex_2"`<br>`"flex_3"`<br>`"reimagine_1"`<br>`"reimagine_2"`<br>`"reimagine_3"` |
| `seed` | Seed für Reproduzierbarkeit. | INT | Ja | - |

**Hinweis:** Der `prompt` muss zwischen 1 und 6000 Zeichen lang sein. Das Quellvideo darf eine Dauer von 18 Sekunden nicht überschreiten.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|--------------|----------|
| `VIDEO` | Die bearbeitete Videoausgabe. | VIDEO |
| `generation_id` | Die eindeutige Kennung für die Generierungsanfrage. | STRING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaRay32VideoEditNode/de.md)

---
**Source fingerprint (SHA-256):** `936d9d7da3fdee9b0b468781fd470751db01f772f3c5c20582da7fb1ff85e6e6`
