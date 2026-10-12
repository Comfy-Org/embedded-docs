# VideoLinearCfgGuidance

Der VideoLinearCFGGuidance-Node wendet eine lineare Conditioning-Guidance-Skala auf ein Videomodell an und passt den Einfluss der konditionierten und unkonditionierten Komponenten über einen angegebenen Bereich an. Dadurch wird eine dynamische Steuerung des Generierungsprozesses ermöglicht, sodass die Ausgabe des Modells basierend auf dem gewünschten Grad der Konditionierung fein abgestimmt werden kann.

## Eingaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `model` | Der Parameter `model` repräsentiert das Videomodell, auf das die lineare CFG-Guidance angewendet wird. Er ist entscheidend für die Definition des Basismodells, das mit der Guidance-Skala modifiziert wird. | MODEL |
| `min_cfg` | Der Parameter `min_cfg` gibt die minimale Conditioning-Guidance-Skala an, die angewendet wird, und dient als Ausgangspunkt für die lineare Skalenanpassung. Er spielt eine Schlüsselrolle bei der Bestimmung der unteren Grenze der Guidance-Skala und beeinflusst die Ausgabe des Modells. | `FLOAT` |

## Ausgaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `model` | Die Ausgabe ist eine modifizierte Version des Eingabemodells, auf die die lineare CFG-Guidance-Skala angewendet wurde. Dieses angepasste Modell ist in der Lage, Ausgaben mit unterschiedlichem Grad der Konditionierung basierend auf der angegebenen Guidance-Skala zu generieren. | MODEL |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VideoLinearCfgGuidance/de.md)
