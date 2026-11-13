# Split Image Channels

Zerlegt ein Bild in seine Rot-, Grün- und Blaukanäle und gibt den Alphakanal als Maske zurück. Jede Farbausgabe ist ein dreikanaliges Graustufenbild, sodass sie wie ein normales Bild in der Vorschau angezeigt und gespeichert werden kann. Verwenden Sie die Node, um einen einzelnen Kanal zu prüfen oder zu bearbeiten oder um die Transparenz aus einem Bild zu extrahieren, das einen Alphakanal enthält: Mit Load Image geladene Bilder haben keinen, da das Alpha dieser Bilder als separater `MASK`-Ausgang bereitgestellt wird.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `image` | Das zu zerlegende Bild. Eine einkanalige (Graustufen-)Eingabe wird erweitert, sodass alle drei Farbausgaben dieselben Daten enthalten. | IMAGE | Ja | - |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `red` | Der Rotkanal als dreikanaliges Graustufenbild. | IMAGE |
| `green` | Der Grünkanal als dreikanaliges Graustufenbild. | IMAGE |
| `blue` | Der Blaukanal als dreikanaliges Graustufenbild. | IMAGE |
| `alpha` | Alpha als Maske, invertiert auf dieselbe Weise wie bei Load Image, sodass 1 vollständig transparente Pixel markiert. Ein Bild ohne Alphakanal gibt eine Maske zurück, die ausschließlich aus Nullen besteht. | MASK |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SplitImageChannels/de.md)

---
**Source fingerprint (SHA-256):** `0f300d2e86c74e856001eb82da26c871c94c1dae5ec73a4504ca258420fbcf52`
