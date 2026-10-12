# FeatherMask

Der Node `FeatherMask` wendet einen Feathering-Effekt auf die Ränder einer gegebenen Maske an und sorgt für einen weichen Übergang der Maskenränder, indem deren Deckkraft basierend auf angegebenen Abständen zu jedem Rand angepasst wird. Dadurch entsteht ein weicherer, stärker vermischter Randeffekt.

## Eingaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `mask` | Die Maske, auf die der Feathering-Effekt angewendet wird. Sie bestimmt den Bereich des Bildes, der vom Feathering-Effekt beeinflusst wird. | MASK |
| `left` | Gibt den Abstand vom linken Rand an, innerhalb dessen der Feathering-Effekt angewendet wird. | INT |
| `top` | Gibt den Abstand vom oberen Rand an, innerhalb dessen der Feathering-Effekt angewendet wird. | INT |
| `right` | Gibt den Abstand vom rechten Rand an, innerhalb dessen der Feathering-Effekt angewendet wird. | INT |
| `bottom` | Gibt den Abstand vom unteren Rand an, innerhalb dessen der Feathering-Effekt angewendet wird. | INT |

## Ausgaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `mask` | Die Ausgabe ist eine modifizierte Version der Eingabemaske, bei der ein Feathering-Effekt auf ihre Ränder angewendet wurde. | MASK |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FeatherMask/de.md)
