# Split Image Channels

Teilt ein Bild in seine Rot-, Grün- und Blaukanäle auf und gibt den Alphakanal als Maske zurück. Jede Farbausgabe ist ein dreikanaliges Graustufenbild und lässt sich daher wie ein normales Bild in der Vorschau anzeigen und speichern. Verwenden Sie den Node, um einen einzelnen Kanal zu prüfen oder zu bearbeiten oder um die Transparenz aus einem Bild zu extrahieren.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `image` | Das zu teilende Bild. Eine einkanalige (Graustufen-)Eingabe wird erweitert, sodass alle drei Farbausgaben dieselben Daten enthalten. | IMAGE | Ja | - |

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `red` | Der rote Kanal als dreikanaliges Graustufenbild. | IMAGE |
| `green` | Der grüne Kanal als dreikanaliges Graustufenbild. | IMAGE |
| `blue` | Der blaue Kanal als dreikanaliges Graustufenbild. | IMAGE |
| `alpha` | Alpha als Maske, invertiert auf die gleiche Weise wie bei Load Image, sodass 1 vollständig transparente Pixel markiert. Ein Bild ohne Alphakanal gibt eine Maske zurück, die ausschließlich aus Nullen besteht. | MASK |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SplitImageChannels/de.md)

---
**Source fingerprint (SHA-256):** `0f300d2e86c74e856001eb82da26c871c94c1dae5ec73a4504ca258420fbcf52`
