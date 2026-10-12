# SaveAnimatedPng

Der SaveAnimatedPNG-Node dient zum Erstellen und Speichern animierter PNG-Bilder aus einer Sequenz von Frames. Er übernimmt das Zusammenfügen einzelner Bild-Frames zu einer zusammenhängenden Animation und ermöglicht die Anpassung von Frame-Dauer, Schleifen und die Einbeziehung von Metadaten.

## Eingaben

| Feld | Beschreibung | Datentyp |
| --- | --- | --- |
| `images` | Eine Liste von Bildern, die verarbeitet und als animiertes PNG gespeichert werden sollen. Jedes Bild in der Liste stellt einen Frame der Animation dar. | `IMAGE` |
| `filename_prefix` | Gibt den Basisnamen für die Ausgabedatei an, der als Präfix für die generierten animierten PNG-Dateien verwendet wird. | `STRING` |
| `fps` | Die Bildrate (Frames pro Sekunde) für die Animation, die steuert, wie schnell die Frames angezeigt werden. | `FLOAT` |
| `compress_level` | Die auf die animierten PNG-Dateien angewendete Komprimierungsstufe, die Dateigröße und Bildklarheit beeinflusst. | `INT` |

## Ausgaben

| Feld | Beschreibung | Datentyp |
| --- | --- | --- |
| `ui` | Stellt eine UI-Komponente bereit, die die generierten animierten PNG-Bilder anzeigt und angibt, ob die Animation aus einem Einzelbild oder mehreren Frames besteht. | N/A |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveAnimatedPng/de.md)
