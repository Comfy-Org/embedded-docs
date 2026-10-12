# ThresholdMask

Der ThresholdMask-Node wandelt eine Maske in eine binäre Maske um, indem er einen Schwellenwert anwendet. Er vergleicht jedes Pixel in der Eingabemaske mit dem angegebenen Schwellenwert und erstellt eine neue Maske, in der Pixel oberhalb des Schwellenwerts 1 (weiß) werden und Pixel auf oder unterhalb des Schwellenwerts 0 (schwarz) werden.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `mask` | Die zu verarbeitende Eingabemaske | MASK | Ja | - |
| `value` | Der Schwellenwert für die Binarisierung (Standard: 0.5) | FLOAT | Ja | 0.0 - 1.0 |

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `mask` | Die resultierende binäre Maske nach der Schwellenwertanwendung | MASK |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ThresholdMask/de.md)

---
**Source fingerprint (SHA-256):** `eff4479b70c1ca87ba9ba17b771edf5d816cf13c12ac0767cd7ee79d18e326c3`
