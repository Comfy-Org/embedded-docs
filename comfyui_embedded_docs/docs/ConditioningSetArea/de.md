# Konditionierung (Bereich festlegen)

Dieser Node dient dazu, die Konditionierungsinformationen zu ändern, indem bestimmte Bereiche innerhalb des Konditionierungskontexts festgelegt werden. Er ermöglicht die präzise räumliche Manipulation von Konditionierungselementen, wodurch gezielte Anpassungen und Verbesserungen basierend auf angegebenen Dimensionen und Stärke möglich sind.

## Eingaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `CONDITIONING` | Die zu ändernden Konditionierungsdaten. Sie dienen als Basis für die Anwendung räumlicher Anpassungen. | CONDITIONING |
| `width` | Gibt die Breite des festzulegenden Bereichs innerhalb des Konditionierungskontexts an und beeinflusst den horizontalen Umfang der Anpassung. | `INT` |
| `height` | Bestimmt die Höhe des festzulegenden Bereichs und wirkt sich auf die vertikale Ausdehnung der Konditionierungsänderung aus. | `INT` |
| `x` | Der horizontale Startpunkt des festzulegenden Bereichs, der die Anpassung innerhalb des Konditionierungskontexts positioniert. | `INT` |
| `y` | Der vertikale Startpunkt für die Bereichsanpassung, der ihre Position innerhalb des Konditionierungskontexts festlegt. | `INT` |
| `strength` | Definiert die Intensität der Konditionierungsänderung innerhalb des angegebenen Bereichs und ermöglicht eine fein abgestufte Steuerung der Auswirkung der Anpassung. | `FLOAT` |

## Ausgaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `CONDITIONING` | Die geänderten Konditionierungsdaten, die die angegebenen Bereichseinstellungen und Anpassungen widerspiegeln. | CONDITIONING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningSetArea/de.md)
