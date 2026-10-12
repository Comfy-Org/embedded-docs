# LoadLoraTextEncoder

Wenden Sie einen Stapel von LoRAs in einem einzigen Node auf einen CLIP-Textencoder an. Jede Zeile von `loras` enthält eine LoRA-Datei, ihre Stärke und einen Ein-/Aus-Schalter, und die Zeilen werden von oben nach unten angewendet, sodass jede Zeile das Ergebnis der darüberliegenden Zeile patcht. LoRA-Dateien, die den Textencoder verändern, werden üblicherweise auch auf das Modell angewendet, daher wird dieser Node normalerweise mit Load LoRA (Model) kombiniert, wobei dieselben Zeilen verwendet werden.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `clip` | Der CLIP-Textencoder, auf den die LoRAs angewendet werden. | CLIP | Ja | - |
| `loras` | Erweiterbare Gruppe von LoRAs, die in Zeilenreihenfolge auf den Textencoder angewendet werden (`loras.0`, `loras.1` usw.). Fügen Sie eine Zeile pro LoRA hinzu; jede Zeile enthält eine Datei, eine Stärke und einen Ein-/Aus-Schalter. | DYNAMIC_GROUP | Ja | 1 bis 20 Zeilen |

### Felder der `loras`-Zeilen

Jede Zeile wiederholt die folgenden Felder, und jedes Feld ist in einer übermittelten Zeile erforderlich.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `lora_name` | Der Name der anzuwendenden LoRA-Datei. | COMBO | Ja | Mehrere Optionen verfügbar |
| `strength` | Wie stark diese LoRA auf den Textencoder angewendet wird. `0` deaktiviert sie, und ein negativer Wert kehrt den Effekt um. (Standard: 1.0) | FLOAT | Ja | -100 bis 100 (Schrittweite 0.01) |
| `enabled` | Ausschalten, um diese LoRA zu überspringen, ohne ihre Datei oder Stärke zu ändern. (Standard: true) | BOOLEAN | Ja | false / true |

### Parametereinschränkungen

- **Zeilenanzahl:** Mindestens eine Zeile muss übermittelt werden, und höchstens 20 Zeilen werden akzeptiert, sodass der höchste Zeilenindex 19 ist.
- **Übersprungene Zeilen:** Eine Zeile wird übersprungen, wenn ihre Datei leer ist, wenn `enabled` ausgeschaltet ist oder wenn `strength` `0` ist. Eine negative Stärke wird weitergereicht und nicht übersprungen.
- **Zeilenreihenfolge:** Zeilen werden in der Reihenfolge ihres Auftretens angewendet, und jede Zeile beginnt mit dem Textencoder, der von der vorherigen Zeile zurückgegeben wurde.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `CLIP` | Der CLIP-Textencoder, nachdem die nicht übersprungenen LoRA-Zeilen angewendet wurden. | CLIP |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadLoraTextEncoder/de.md)

---
**Source fingerprint (SHA-256):** `0b290d2caddc3937e962e65c70a5c99cbd4cdb40ab6f86bba8f0c270e5cebf00`
