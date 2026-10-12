# SaveAnimatedWebp

Dieser Node ist dafür konzipiert, eine Bildsequenz als animierte WEBP-Datei zu speichern. Er übernimmt die Zusammenführung einzelner Frames zu einer zusammenhängenden Animation, wendet angegebene Metadaten an und optimiert die Ausgabe basierend auf Qualitäts- und Kompressionseinstellungen.

## Eingaben

| Feld | Beschreibung | Datentyp |
| --- | --- | --- |
| `images` | Eine Liste von Bildern, die als Frames in der animierten WEBP-Datei gespeichert werden. Dieser Parameter ist wesentlich, um den visuellen Inhalt der Animation festzulegen. | `IMAGE` |
| `filename_prefix` | Gibt den Basisnamen für die Ausgabedatei an, an den ein Zähler und die Erweiterung '.webp' angehängt werden. Dieser Parameter ist entscheidend für die Identifizierung und Organisation der gespeicherten Dateien. | `STRING` |
| `fps` | Die Bildrate pro Sekunde für die Animation, die die Wiedergabegeschwindigkeit beeinflusst. | `FLOAT` |
| `lossless` | Ein boolescher Wert, der angibt, ob verlustfreie Kompression verwendet werden soll; dies beeinflusst die Dateigröße und die Qualität der Animation. | `BOOLEAN` |
| `quality` | Ein Wert zwischen 0 und 100, der die Kompressionsqualität festlegt; höhere Werte führen zu besserer Bildqualität, aber größeren Dateien. | `INT` |
| `method` | Gibt die zu verwendende Kompressionsmethode an, die sich auf die Kodierungsgeschwindigkeit und die Dateigröße auswirken kann. | COMBO[STRING] |

## Ausgaben

| Feld | Beschreibung | Datentyp |
| --- | --- | --- |
| `ui` | Stellt eine UI-Komponente bereit, die die gespeicherten animierten WEBP-Bilder zusammen mit ihren Metadaten anzeigt und angibt, ob die Animation aktiviert ist. | N/A |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveAnimatedWebp/de.md)
