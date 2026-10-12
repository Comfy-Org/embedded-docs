# LoadLoraModel

Wendet einen Stapel von LoRAs in einem einzigen Node auf ein Diffusionsmodell an. Jede Zeile von `loras` enthält eine LoRA-Datei, ihre Stärke und einen Ein-/Aus-Schalter, und die Zeilen werden von oben nach unten angewendet, sodass jede Zeile das Ergebnis der darüber liegenden Zeile patcht. Verwenden Sie diesen Node anstelle des Verkettens mehrerer einzelner LoRA-Loader, wenn ein Workflow eine lange Liste von LoRAs auf dasselbe Modell anwendet.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model` | Das Diffusionsmodell, auf das die LoRAs angewendet werden. | MODEL | Ja | - |
| `loras` | Erweiterbare Gruppe von LoRAs, die in Zeilenreihenfolge auf das Modell angewendet werden (`loras.0`, `loras.1` und so weiter). Fügen Sie eine Zeile pro LoRA hinzu; jede Zeile enthält eine Datei, eine Stärke und einen Ein-/Aus-Schalter. | DYNAMIC_GROUP | Ja | 1 bis 20 Zeilen |

### `loras` Zeilenfelder

Jede Zeile wiederholt die folgenden Felder, und jedes Feld ist innerhalb einer übermittelten Zeile erforderlich.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `lora_name` | Der Name der anzuwendenden LoRA-Datei. | COMBO | Ja | Mehrere Optionen verfügbar |
| `strength` | Wie stark diese LoRA angewendet wird. `0` deaktiviert sie, und ein negativer Wert kehrt den Effekt um. (Standard: 1.0) | FLOAT | Ja | -100 bis 100 (Schrittweite 0.01) |
| `enabled` | Deaktivieren, um diese LoRA zu überspringen, ohne ihre Datei oder Stärke zu ändern. (Standard: true) | BOOLEAN | Ja | false / true |

### Parameterbeschränkungen

- **Zeilenanzahl:** Mindestens eine Zeile muss übermittelt werden, und höchstens 20 Zeilen werden akzeptiert, sodass der höchste Zeilenindex 19 ist.
- **Übersprungene Zeilen:** Eine Zeile wird übersprungen, wenn ihre Datei leer ist, wenn `enabled` deaktiviert ist oder wenn `strength` `0` ist. Eine negative Stärke wird durchgereicht und nicht übersprungen.
- **Zeilenreihenfolge:** Die Zeilen werden in der Reihenfolge ihres Erscheinens angewendet, und jede Zeile beginnt mit dem Modell, das von der vorherigen Zeile zurückgegeben wurde.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `MODEL` | Das Diffusionsmodell, nachdem die nicht übersprungenen LoRA-Zeilen angewendet wurden. | MODEL |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadLoraModel/de.md)

---
**Source fingerprint (SHA-256):** `a656bba0248d2f6d4eb65e15e3a19f2e76edecd4b34710921a02f3ba5c598e1d`
