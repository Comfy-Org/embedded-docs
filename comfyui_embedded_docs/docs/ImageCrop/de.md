# ImageCrop

Der `ImageCrop`-Node ist darauf ausgelegt, Bilder auf eine angegebene Breite und Höhe zuzuschneiden, beginnend bei einer gegebenen x- und y-Koordinate. Diese Funktionalität ist wichtig, um sich auf bestimmte Bereiche eines Bildes zu konzentrieren oder die Bildgröße an bestimmte Anforderungen anzupassen.

## Eingaben

| Feld | Beschreibung | Datentyp |
| --- | --- | --- |
| `image` | Das Eingabebild, das zugeschnitten werden soll. Dieser Parameter ist entscheidend, da er das Quellbild definiert, aus dem anhand der angegebenen Abmessungen und Koordinaten ein Bereich extrahiert wird. | `IMAGE` |
| `width` | Gibt die Breite des zugeschnittenen Bildes an. Dieser Parameter bestimmt, wie breit das resultierende zugeschnittene Bild sein wird. | `INT` |
| `height` | Gibt die Höhe des zugeschnittenen Bildes an. Dieser Parameter bestimmt die Höhe des resultierenden zugeschnittenen Bildes. | `INT` |
| `x` | Die x-Koordinate der oberen linken Ecke des Zuschneidebereichs. Dieser Parameter legt den Startpunkt für die Breitendimension des Zuschnitts fest. | `INT` |
| `y` | Die y-Koordinate der oberen linken Ecke des Zuschneidebereichs. Dieser Parameter legt den Startpunkt für die Höhendimension des Zuschnitts fest. | `INT` |

## Ausgaben

| Feld | Beschreibung | Datentyp |
| --- | --- | --- |
| `image` | Das zugeschnittene Bild als Ergebnis des Zuschneidevorgangs. Diese Ausgabe ist wichtig für die weitere Verarbeitung oder Analyse des angegebenen Bildbereichs. | `IMAGE` |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageCrop/de.md)
