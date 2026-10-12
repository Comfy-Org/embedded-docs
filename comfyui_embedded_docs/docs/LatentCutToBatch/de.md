# LatentCutToBatch

Der Node LatentCutToBatch teilt eine latente Repräsentation entlang einer gewählten Dimension (Zeit, Breite oder Höhe) in Ausschnitte einer festgelegten Größe auf und stapelt diese Ausschnitte zu einem neuen Batch. Jeder Ausschnitt wird zu einem separaten Element im Batch, sodass verschiedene Teile einer latenten Stichprobe unabhängig verarbeitet werden können.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `samples` | Die latente Repräsentation, die aufgeteilt und gebatcht werden soll. | LATENT | Ja | - |
| `dim` | Die Dimension, entlang der die latenten Samples geschnitten werden. `"t"` bezieht sich auf die zeitliche Dimension (Frames), `"x"` auf die Breite und `"y"` auf die Höhe. | COMBO | Ja | `"t"`<br>`"x"`<br>`"y"` |
| `slice_size` | Die Größe jedes Ausschnitts, der aus der angegebenen Dimension geschnitten wird. Wenn die Größe der Dimension nicht exakt durch diesen Wert teilbar ist, wird der Rest verworfen. (Standard: 1) | INT | Ja | 1 bis 16384 (maximale Auflösung) |

Hinweis: Die Option `"t"` wird nur wirksam, wenn das Latent eine zeitliche Dimension enthält. Wenn die gewählte Dimension auf die Batch- oder Kanalposition verweist oder nicht existiert (zum Beispiel die Auswahl von `"t"` bei einem Latent ohne Frames), gibt der Node die Eingabe unverändert zurück. Wenn `slice_size` größer als die Größe der gewählten Dimension ist, wird die gesamte Dimension als ein einzelner Ausschnitt verwendet. Wenn die Dimensionsgröße nicht gleichmäßig durch `slice_size` teilbar ist, wird der übrig bleibende Teil am Ende verworfen. Die Ausgabe-Batchgröße ist die Eingabe-Batchgröße multipliziert mit der Anzahl der Ausschnitte, und die geschnittene Dimension selbst wird auf `slice_size` reduziert.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `samples` | Der resultierende latente Batch, der die geschnittenen und gestapelten Samples enthält. | LATENT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentCutToBatch/de.md)

---
**Source fingerprint (SHA-256):** `873c9bc8391971887f1ab636c086cab86f5504a9c653bc80b54120ee53980bdf`
