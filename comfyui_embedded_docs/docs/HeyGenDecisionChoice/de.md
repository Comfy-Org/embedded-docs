# HeyGen Decision (Choice)

Wählen Sie eine Ihrer eigenen Optionen für den Text, die Bilder, das Audio oder das Video aus, das Sie verbinden, und erhalten Sie die gewählte Option, ihre Position und eine Konfidenz zurück. Verbinden Sie `choice` mit einem Branch-Node, dessen Eingaben dieselben Optionsnamen tragen, oder leiten Sie anhand von `option_index` weiter. Ein Branch-Node akzeptiert höchstens 32 Eingaben, daher sollten Sie größere Optionssätze mit `option_index` weiterleiten.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model` | Zu verwendendes Modell. `heygen-decision-1-turbo` ist schneller und kostengünstiger als `heygen-decision-1` (Standard: `"heygen-decision-1"`). | COMBO | Ja | `"heygen-decision-1"`<br>`"heygen-decision-1-turbo"` |
| `question` | Die Frage, die die Optionen beantworten, bis zu 5000 Zeichen (Standard: "What style is the image?"). | STRING | Ja | 1 bis 5000 Zeichen |
| `options` | Eine Option pro Zeile, genau wie eingegeben verwendet, jeweils bis zu 128 Zeichen. Fügen Sie eine Option wie `other` für Eingaben hinzu, die zu keiner der Optionen passen (Standard: `photo`, `illustration`, `3d render`, `anime`, `sketch`, `other`). | STRING | Ja | 2 bis 255 Optionen |
| `images` | Zu klassifizierende Bilder, insgesamt bis zu 4, wobei jedes Frame eines Batches gezählt wird. Sie werden über die Sockets hinweg in der Reihenfolge von `image_1` bis `image_4` nummeriert. | IMAGE | Nein | Bis zu 4 Bilder |
| `audio_1` | Zu klassifizierendes Audio, bis zu 30 Minuten. | AUDIO | Nein | Bis zu 30 Minuten |
| `video_1` | Zu klassifizierendes Video, bis zu 60 Sekunden. | VIDEO | Nein | Bis zu 60 Sekunden |
| `text` | Text, auf den sich die Frage bezieht, z. B. ein Prompt oder eine LLM-Antwort, bis zu 20000 Zeichen. | STRING | Nein | Bis zu 20000 Zeichen |

Geben Sie 2 bis 255 Optionen an, keine davon doppelt und keine, die sich nur in der Groß-/Kleinschreibung unterscheiden, da der Node sonst einen Fehler auslöst. Verbinden Sie mindestens eine zu klassifizierende Eingabe und benennen Sie sie innerhalb der Frage über den Socket, zum Beispiel „Welche Jahreszeit ist auf image_1 zu sehen?“.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `choice` | Die gewählte Option, genau wie sie in `options` geschrieben wurde. | STRING |
| `option_index` | Position der gewählten Option in `options`, beginnend bei 0. | INT |
| `confidence` | Konfidenz der Wahl, zwischen 0 und 1. | FLOAT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenDecisionChoice/de.md)

---
**Source fingerprint (SHA-256):** `dd21b3b8021b8917e7ee4d120471974634ae6771ff17b0f49e9460f82a2fbe78`
