# ImageBlur

Der Node `ImageBlur` wendet einen Gaußschen Weichzeichner auf ein Bild an, wodurch Kanten weicher werden und Details sowie Rauschen reduziert werden. Er bietet über Parameter Kontrolle über Intensität und Ausbreitung der Weichzeichnung.

## Eingaben

| Feld | Beschreibung | Datentyp |
| --- | --- | --- |
| `image` | Das Eingabebild, das weichgezeichnet werden soll. Dies ist das primäre Ziel für den Weichzeichnungseffekt. | `IMAGE` |
| `blur_radius` | Bestimmt den Radius des Weichzeichnungseffekts. Ein größerer Radius führt zu einer stärkeren Weichzeichnung. | `INT` |
| `sigma` | Steuert die Ausbreitung der Weichzeichnung. Ein höherer Sigma-Wert bedeutet, dass die Weichzeichnung einen größeren Bereich um jeden Pixel herum beeinflusst. | `FLOAT` |

## Ausgaben

| Feld | Beschreibung | Datentyp |
| --- | --- | --- |
| `image` | Die Ausgabe ist die weichgezeichnete Version des Eingabebildes, wobei der Grad der Weichzeichnung durch die Eingabeparameter bestimmt wird. | `IMAGE` |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageBlur/de.md)
