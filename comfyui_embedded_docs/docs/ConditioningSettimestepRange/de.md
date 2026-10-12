# ConditioningSettimestepRange

Dieser Node dient dazu, den zeitlichen Aspekt der Konditionierung anzupassen, indem er einen bestimmten Bereich von Zeitschritten festlegt. Er ermöglicht die präzise Kontrolle über Start- und Endpunkt des Konditionierungsprozesses und erlaubt so eine gezieltere und effizientere Generierung.

## Eingaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `CONDITIONING` | Der Eingang für die Konditionierung stellt den aktuellen Zustand des Generierungsprozesses dar, den dieser Node ändert, indem er einen bestimmten Bereich von Zeitschritten festlegt. | CONDITIONING |
| `start` | Der Parameter `start` gibt den Beginn des Zeitschrittbereichs als Prozentsatz des gesamten Generierungsprozesses an und ermöglicht eine fein abgestimmte Kontrolle darüber, wann die Konditionierungseffekte beginnen. | `FLOAT` |
| `end` | Der Parameter `end` definiert den Endpunkt des Zeitschrittbereichs als Prozentsatz und ermöglicht eine präzise Kontrolle über die Dauer und den Abschluss der Konditionierungseffekte. | `FLOAT` |

## Ausgaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `CONDITIONING` | Die Ausgabe ist die modifizierte Konditionierung mit dem angegebenen Zeitschrittbereich, bereit für die weitere Verarbeitung oder Generierung. | CONDITIONING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningSettimestepRange/de.md)
