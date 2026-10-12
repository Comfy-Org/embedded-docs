# Bildfarbe in Maske umwandeln

Der Node `ImageColorToMask` ist darauf ausgelegt, eine angegebene Farbe in einem Bild in eine Maske umzuwandeln. Er verarbeitet ein Bild und eine Zielfarbe und erzeugt eine Maske, in der die angegebene Farbe hervorgehoben wird, was Vorgänge wie farbbasierte Segmentierung oder Objektisolierung erleichtert.

## Eingaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `image` | Der Parameter `image` repräsentiert das zu verarbeitende Eingabebild. Er ist entscheidend, um die Bereiche des Bildes zu bestimmen, die der angegebenen Farbe entsprechen und in eine Maske umgewandelt werden sollen. | `IMAGE` |
| `color` | Der Parameter `color` gibt die Zielfarbe im Bild an, die in eine Maske umgewandelt werden soll. Er spielt eine entscheidende Rolle beim Identifizieren der spezifischen Farbbereiche, die in der resultierenden Maske hervorgehoben werden sollen. | `INT` |

## Ausgaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `mask` | Die Ausgabe ist eine Maske, die die Bereiche des Eingabebildes hervorhebt, die der angegebenen Farbe entsprechen. Diese Maske kann für weitere Bildverarbeitungsaufgaben verwendet werden, wie Segmentierung oder Objektisolierung. | `MASK` |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageColorToMask/de.md)
