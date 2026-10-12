# Leeres Bild

## Funktionsbeschreibung

Der EmptyImage-Node dient zum Erstellen leerer Bilder mit angegebenen Abmessungen und Farben. Er kann einfarbige Hintergrundbilder generieren, die häufig als Ausgangspunkte oder Hintergrundbilder für Bildverarbeitungs-Workflows verwendet werden.

## Funktionsweise

So wie ein Maler vor dem Beginn des Malens eine leere Leinwand vorbereitet, stellt Ihnen der EmptyImage-Node eine „digitale Leinwand“ bereit. Sie können die Leinwandgröße (Breite und Höhe) festlegen, die Grundfarbe der Leinwand auswählen und sogar mehrere Leinwände mit denselben Spezifikationen auf einmal vorbereiten. Dieser Node ist wie ein intelligentes Künstlerbedarfsgeschäft, das standardisierte Leinwände erstellen kann, die Ihre Größen- und Farbanforderungen perfekt erfüllen.

## Eingaben

| Parametername | Beschreibung | Datentyp |
| --- | --- | --- |
| `width` | Legt die Breite des erzeugten Bildes fest (in Pixeln) und bestimmt die horizontalen Abmessungen der Leinwand | INT |
| `height` | Legt die Höhe des erzeugten Bildes fest (in Pixeln) und bestimmt die vertikalen Abmessungen der Leinwand | INT |
| `batch_size` | Die Anzahl der auf einmal zu erzeugenden Bilder, verwendet für die Batch-Erstellung von Bildern mit denselben Spezifikationen | INT |
| `color` | Die Hintergrundfarbe des Bildes. Sie können hexadezimale Farbeinstellungen eingeben, die automatisch in Dezimal umgewandelt werden | INT |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `image` | Der erzeugte leere Bildtensor im Format [batch_size, height, width, 3], der drei RGB-Farbkanäle enthält | IMAGE |

## Gängige Farbreferenzwerte

Da die aktuelle Farbeingabe für diesen Node nicht benutzerfreundlich ist und alle Farbwerte in Dezimal umgewandelt werden, finden Sie hier einige gängige Farbwerte, die direkt für den schnellen Einsatz verwendet werden können.

| Farbname | Hexadezimalwert |
|------------|-------------------|
| Schwarz      | 0x000000         |
| Weiß         | 0xFFFFFF         |
| Rot          | 0xFF0000         |
| Grün         | 0x00FF00         |
| Blau         | 0x0000FF         |
| Gelb         | 0xFFFF00         |
| Cyan         | 0x00FFFF         |
| Magenta      | 0xFF00FF         |
| Orange       | 0xFF8000         |
| Violett      | 0x8000FF         |
| Rosa         | 0xFF80C0         |
| Braun        | 0x8B4513         |
| Dunkelgrau   | 0x404040         |
| Hellgrau     | 0xC0C0C0         |
| Marineblau   | 0x000080         |
| Dunkelgrün   | 0x008000         |
| Dunkelrot    | 0x800000         |
| Gold         | 0xFFD700         |
| Silber       | 0xC0C0C0         |
| Beige        | 0xF5F5DC         |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyImage/de.md)
