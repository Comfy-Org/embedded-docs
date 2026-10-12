# ModelMergeSimple

Der Node ModelMergeSimple dient dem Zusammenführen zweier Modelle, indem deren Parameter basierend auf einem angegebenen Verhältnis vermischt werden. Dieser Node ermöglicht die Erstellung hybrider Modelle, die die Stärken oder Eigenschaften beider Eingabemodelle kombinieren.

Der Parameter `ratio` bestimmt das Mischungsverhältnis zwischen den beiden Modellen. Wenn dieser Wert 1 ist, besteht das Ausgabemodell zu 100 % aus `model1`; wenn dieser Wert 0 ist, besteht das Ausgabemodell zu 100 % aus `model2`.

## Eingaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `model1` | Das erste Modell, das zusammengeführt werden soll. Es dient als Basismodell, auf das die Patches des zweiten Modells angewendet werden. | `MODEL` |
| `model2` | Das zweite Modell, dessen Patches auf das erste Modell angewendet werden, beeinflusst durch das angegebene Verhältnis. | `MODEL` |
| `ratio` | Wenn dieser Wert 1 ist, besteht das Ausgabemodell zu 100 % aus `model1`; wenn dieser Wert 0 ist, besteht das Ausgabemodell zu 100 % aus `model2`. | `FLOAT` |

## Ausgaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `model` | Das resultierende zusammengeführte Modell, das Elemente aus beiden Eingabemodellen gemäß dem angegebenen Verhältnis enthält. | MODEL |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeSimple/de.md)
