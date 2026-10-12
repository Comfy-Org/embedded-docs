# MinimaxHailuoVideoNode

Erzeugt Videos aus Text-Prompts mithilfe des MiniMax Hailuo-02-Modells. Optional können Sie ein Startbild angeben, das als erstes Einzelbild verwendet wird; dadurch entsteht ein Video, das von diesem Bild aus fortgesetzt wird.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `prompt_text` | Text-Prompt zur Steuerung der Videoerzeugung (Standard: leer). | STRING | Ja | - |
| `seed` | Der Zufallsseed, der zum Erzeugen des Rauschens verwendet wird (Standard: 0). | INT | Nein | 0 to 18446744073709551615 |
| `first_frame_image` | Optionales Bild, das als erstes Einzelbild zur Erzeugung eines Videos verwendet wird. | IMAGE | Nein | - |
| `prompt_optimizer` | Optimiert den Prompt, um bei Bedarf die Generierungsqualität zu verbessern (Standard: True). | BOOLEAN | Nein | True<br>False |
| `duration` | Die Länge des Ausgabevideos in Sekunden (Standard: 6). | COMBO | Nein | 6<br>10 |
| `resolution` | Die Abmessungen der Videoanzeige. 1080p entspricht 1920x1080, 768p entspricht 1366x768 (Standard: "768P"). | COMBO | Nein | "768P"<br>"1080P" |

**Hinweis:** Wenn `resolution` auf "1080P" gesetzt ist, ist `duration` auf 6 Sekunden begrenzt. Wenn `first_frame_image` nicht angegeben wird, darf `prompt_text` nicht leer sein.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `output` | Die erzeugte Videodatei. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuoVideoNode/de.md)

---
**Source fingerprint (SHA-256):** `f371aae15cfbe7353236bc679c8a6d558703c5037e49ab7ddb9bdf5c50ef0995`
