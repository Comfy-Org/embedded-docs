# SaveConditioning

Dieser Node speichert ein einzelnes Conditioning als Safetensors-Datei im Ausgabeordner. Die gespeicherte Datei kann in den Ordner models/embeddings verschoben und später mit Load Conditioning geladen werden, um beispielsweise den Text-Encoder zu überspringen. Der Node reicht das Conditioning unverändert weiter, sodass es später im Workflow weiterhin verwendet werden kann.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `conditioning` | Das zu speichernde Conditioning. Es wird nur ein einzelner Conditioning-Eintrag unterstützt. | CONDITIONING | Ja | - |
| `filename_prefix` | Präfix, das zum Erstellen des Ausgabedateinamens verwendet wird. Die Datei wird mit einem angehängten numerischen Zähler im Ausgabeordner geschrieben. Standard: `conditioning/ComfyUI` | STRING | Ja | - |

**Hinweise:**

- Wenn die Eingabe `conditioning` mehr als einen Eintrag enthält (zum Beispiel nach dem Kombinieren von Conditionings), gibt der Node einen Fehler aus: "Save Conditioning supports a single conditioning entry, save it before combining."
- Conditioning-Optionen, die Tensoren, Listen/Tupel von Tensoren, boolesche Werte, Ganzzahlen, Floats oder Strings sind, werden zusammen mit dem Conditioning gespeichert. Optionen, die `None` sind, werden übersprungen. Jeder andere Optionstyp führt zu einem Fehler mit der Meldung, dass die Option nicht gespeichert werden kann.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `conditioning` | Das unveränderte Conditioning, das übergeben wurde. | CONDITIONING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveConditioning/de.md)

---
**Source fingerprint (SHA-256):** `07b7d2be5262c4782f237138d034b130322507e62ae8775b9c94634df8e7a3fa`
