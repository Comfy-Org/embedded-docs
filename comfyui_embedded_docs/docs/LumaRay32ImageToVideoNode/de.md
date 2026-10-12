# LumaRay32ImageToVideoNode

Erzeugen Sie ein Video aus einem Start- und/oder Endframe mit dem Ray 3.2-Modell von Luma. Bildverankerte Generierungen haben immer eine Dauer von 5 Sekunden.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `prompt` | Text-Prompt für die Videogenerierung. | STRING | Ja | 1 bis 6000 Zeichen |
| `resolution` | Die Ausgabeauflösung des generierten Videos (Standard: "720p"). | COMBO | Ja | "360p"<br>"540p"<br>"720p"<br>"1080p" |
| `loop` | Lässt das Video nahtlos in einer Schleife laufen. Nicht verfügbar, wenn ein `end_frame` festgelegt ist. | BOOLEAN | Ja | True<br>False |
| `seed` | Seed-Wert für reproduzierbare Generierung. | INT | Ja | 0 bis 2147483647 |
| `start_frame` | Erstes Frame des generierten Videos. | IMAGE | Nein | - |
| `end_frame` | Letztes Frame des generierten Videos. | IMAGE | Nein | - |

**Hinweis:** Mindestens eines von `start_frame` oder `end_frame` muss angegeben werden. Wenn beide angegeben werden, geht das generierte Video vom Startframe zum Endframe über. Die Option `loop` kann nicht aktiviert werden, wenn ein `end_frame` festgelegt ist.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|--------------|--------------|----------|
| `video` | Die generierte Videoausgabe. | VIDEO |
| `generation_id` | Die eindeutige Kennung für die Generierungsanfrage. | STRING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaRay32ImageToVideoNode/de.md)

---
**Source fingerprint (SHA-256):** `ff479c196f10153ffa09af6acfb4e286d1934aa28a5e9b413613097a2cfb5f2a`
