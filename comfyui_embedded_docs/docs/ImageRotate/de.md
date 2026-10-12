# Bild drehen

Der Knoten ImageRotate rotiert ein Eingabebild um die angegebenen Winkel. Er unterstützt vier Rotationsoptionen: keine Drehung, 90 Grad im Uhrzeigersinn, 180 Grad und 270 Grad im Uhrzeigersinn. Die Drehung wird mithilfe effizienter Tensoroperationen durchgeführt, die die Integrität der Bilddaten erhalten.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `image` | Das zu rotierende Eingabebild | IMAGE | Ja | - |
| `rotation` | Der auf das Bild anzuwendende Drehwinkel (Standard: "none") | STRING | Ja | "none"<br>"90 degrees"<br>"180 degrees"<br>"270 degrees" |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `image` | Das rotierte Ausgabebild | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageRotate/de.md)

---
**Source fingerprint (SHA-256):** `1de36d9e42e64fe80cc13dd7da96bd946f02ba78d81317f073cf54c4e5bd12f7`
