# TypeSafe Jev (Choice)

Der Node TypeSafe Jev (Choice) wählt eine Ihrer eigenen Optionen für verbundenen Text, Bilder oder beides aus. Verbinden Sie `choice` mit einem Branch-Node, dessen Eingaben die Optionsnamen tragen, oder verwenden Sie `option_index`, um auf die Position der gewählten Option umzuschalten. Dies ist ein API-Node und erfordert ein Comfy.org-Konto sowie einen API-Schlüssel.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model` | Zu verwendendes Jev-Modell. Derzeit ist nur ein Modell verfügbar: `jev-1.14.0`. | COMBO | Ja | `"jev-1.14.0"` |
| `question` | Die Frage, die die Optionen beantworten. Bei mehreren Bild-Sockets verwenden Sie deren Namen, zum Beispiel `Which season is shown in image_1?` (Standard: `What style is the image?`). | STRING | Ja | 1 bis 1000 Zeichen |
| `options` | Die Optionen zur Auswahl, eine pro Zeile. Fügen Sie eine Option wie `other` für Eingaben hinzu, die zu keiner der Optionen passen (Standard: `photo`, `illustration`, `3d render`, `anime`, `sketch` und `other`, eine pro Zeile). | STRING | Ja | 2 bis 50 Optionen, jeweils bis zu 40 Zeichen |
| `images` | Die Bilder, auf die sich die Frage bezieht. Insgesamt bis zu 32 Bilder; eine Batch-Eingabe zählt einmal pro Bild, und mehr als 4 Bilder werden in einer kleineren Größe gesendet. | AUTOGROW | Nein | 0 bis 32 Bilder |
| `text` | Der Text, auf den sich die Frage bezieht, wie etwa ein Prompt oder eine LLM-Antwort. | STRING | Nein | 0 bis 3000 Zeichen |

**Hinweise:**

- Verbinden Sie Text oder mindestens ein Bild; der Node löst einen Fehler aus, wenn beides leer ist.
- Der Node löst einen Fehler aus, wenn weniger als 2 oder mehr als 50 Optionen angegeben werden, wenn eine Option länger als 40 Zeichen ist oder wenn sich zwei Optionen nur in der Groß-/Kleinschreibung unterscheiden.
- `option_index` zählt ab 0, daher hat die erste Option in der Liste den Index 0.
- Die Abrechnung erfolgt tokenbasiert; das Preis-Badge auf dem Node zeigt den ungefähren Preis pro 1 Mio. Tokens.

## Ausgaben

| Ausgabenamen | Beschreibung | Datentyp |
| --- | --- | --- |
| `choice` | Die gewählte Option, exakt so geschrieben, wie sie in `options` erscheint. | STRING |
| `option_index` | Position der gewählten Option in der Optionsliste, beginnend bei 0. | INT |
| `confidence` | Wie sicher sich Jev ist, von 0 (kein klarer Gewinner) bis 1 (sicher). | FLOAT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TypeSafeJevChoice/de.md)

---
**Source fingerprint (SHA-256):** `b1cd36d600f5c07935c455d9e926e6c0a53f172fcc1a6f602c8d4dc70eeffabe`
