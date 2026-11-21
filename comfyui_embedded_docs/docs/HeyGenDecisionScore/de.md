# HeyGen Decision (Score)

Bewerten Sie den Text, die Bilder, das Audio oder das Video, das Sie verbinden, von 1 bis 10 und erhalten Sie die Punktzahl sowie einen booleschen Wert, der bei einem von Ihnen festgelegten Schwellenwert umschaltet. Verwenden Sie ihn zum Filtern oder Sortieren von Ausgaben und verbinden Sie `result` mit einem If/Else Switch-Node, um auf die Punktzahl zu reagieren.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model` | Zu verwendendes Modell. `heygen-decision-1-turbo` ist schneller und kostet weniger als `heygen-decision-1` (Standard: `"heygen-decision-1"`). | COMBO | Ja | `"heygen-decision-1"`<br>`"heygen-decision-1-turbo"` |
| `question` | Was bewertet werden soll, wobei angegeben wird, was 1 und 10 bedeuten (Standard: „Rate the technical quality of the image from 1 (worst) to 10 (best).“). | STRING | Ja | 1 bis 5000 Zeichen |
| `threshold` | `result` ist wahr, wenn die Punktzahl mindestens diesem Wert entspricht. Saubere, scharfe Bilder erzielen etwa 7, stark beschädigte etwa 3 bis 5 (Standard: 6.0). | FLOAT | Ja | 1.0 bis 10.0 (Schritt 0.1) |
| `images` | Zu bewertende Bilder, insgesamt bis zu 4, wobei jeder Frame eines Batches gezählt wird. Sie werden über die Sockets hinweg der Reihe nach von `image_1` bis `image_4` nummeriert. | IMAGE | Nein | Bis zu 4 Bilder |
| `audio_1` | Zu bewertendes Audio, bis zu 30 Minuten. | AUDIO | Nein | Bis zu 30 Minuten |
| `video_1` | Zu bewertendes Video, bis zu 60 Sekunden. | VIDEO | Nein | Bis zu 60 Sekunden |
| `text` | Text, auf den sich die Frage bezieht, etwa ein Prompt oder eine LLM-Antwort, bis zu 20000 Zeichen. | STRING | Nein | Bis zu 20000 Zeichen |

Verbinden Sie mindestens eine Eingabe zum Bewerten und benennen Sie sie in der Frage über den Socket, zum Beispiel „Wie scharf ist image_1?“.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `result` | Wahr, wenn die Punktzahl mindestens `threshold` entspricht, andernfalls falsch. | BOOLEAN |
| `score` | Die Bewertung von 1 bis 10. | FLOAT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenDecisionScore/de.md)

---
**Source fingerprint (SHA-256):** `47f7aeab15292a2156b8da23c9911f4155c5b05c9ea9c0c502c30221aa522b58`
