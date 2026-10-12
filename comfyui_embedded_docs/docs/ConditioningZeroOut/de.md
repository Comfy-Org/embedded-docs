# ConditioningZeroOut

Dieser Node setzt bestimmte Elemente innerhalb der Conditioning-Datenstruktur auf null, wodurch ihr Einfluss in nachfolgenden Verarbeitungsschritten effektiv neutralisiert wird. Er ist für erweiterte Conditioning-Operationen konzipiert, bei denen eine direkte Manipulation der internen Repräsentation des Conditionings erforderlich ist.

## Eingaben

| Parameter | Beschreibung | Comfy-Datentyp |
| --- | --- | --- |
| `CONDITIONING` | Die zu ändernde Conditioning-Datenstruktur. Dieser Node setzt die 'pooled_output'-Elemente innerhalb jedes Conditioning-Eintrags auf null, sofern vorhanden. | CONDITIONING |

## Ausgaben

| Parameter | Beschreibung | Comfy-Datentyp |
| --- | --- | --- |
| `CONDITIONING` | Die geänderte Conditioning-Datenstruktur, bei der die 'pooled_output'-Elemente, sofern zutreffend, auf null gesetzt wurden. | CONDITIONING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningZeroOut/de.md)
