# HeyGen Decision (Choice)

Wählen Sie eine Ihrer eigenen Optionen für den Text, die Bilder, das Audio oder das Video aus, die Sie verbinden, und erhalten Sie die gewählte Option, ihre Position und eine Konfidenz zurück. Verbinden Sie `choice` mit einem Branch-Node, dessen Eingaben dieselben Optionsnamen tragen, oder leiten Sie anhand von `option_index` weiter.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `model` | Modell, das verwendet werden soll. `heygen-decision-1-turbo` ist schneller und kostet weniger als `heygen-decision-1` (Standard: `"heygen-decision-1"`). | COMBO | Ja | `"heygen-decision-1"`<br>`"heygen-decision-1-turbo"` |
| `question` | Die Frage, die die Optionen beantworten, bis zu 5000 Zeichen (Standard: "What style is the image?"). | STRING | Ja | 1 bis 5000 Zeichen |
| `options` | Eine Option pro Zeile, genau wie eingegeben verwendet, jeweils bis zu 128 Zeichen. Fügen Sie eine Option wie `other` für Eingaben hinzu, die zu keiner der Optionen passen (Standard: `photo`, `illustration`, `3d render`, `anime`, `sketch`, `other`). | STRING | Ja | 2 bis 255 Optionen |
| `images` | Bilder, die klassifiziert werden sollen, insgesamt bis zu 4, wobei jeder Frame eines Batches gezählt wird. Sie werden über die Sockets hinweg in der Reihenfolge von `image_1` bis `image_4` nummeriert. | IMAGE | Nein | Bis zu 4 Bilder |
| `audio_1` | Audio, das klassifiziert werden soll, bis zu 30 Minuten. | AUDIO | Nein | Bis zu 30 Minuten |
| `video_1` | Video, das klassifiziert werden soll, bis zu 60 Sekunden. | VIDEO | Nein | Bis zu 60 Sekunden |
| `text` | Text, auf den sich die Frage bezieht, z. B. ein Prompt oder eine LLM-Antwort, bis zu 20000 Zeichen. | STRING | Nein | Bis zu 20000 Zeichen |

Geben Sie 2 bis 255 Optionen an, keine davon doppelt und keine, die sich nur in der Groß-/Kleinschreibung unterscheiden, andernfalls löst der Node einen Fehler aus. Verbinden Sie mindestens eine Eingabe zum Klassifizieren und bezeichnen Sie sie innerhalb der Frage mit ihrem Socket-Namen, zum Beispiel: „Welche Jahreszeit ist in image_1 zu sehen?“.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|--------------|--------------|----------|
| `choice` | Die gewählte Option, genau wie in `options` geschrieben. | STRING |
| `option_index` | Position der gewählten Option in `options`, beginnend bei 0. | INT |
| `confidence` | Konfidenz für die Auswahl, zwischen 0 und 1. | FLOAT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenDecisionChoice/de.md)

---
**Source fingerprint (SHA-256):** `dd21b3b8021b8917e7ee4d120471974634ae6771ff17b0f49e9460f82a2fbe78`
