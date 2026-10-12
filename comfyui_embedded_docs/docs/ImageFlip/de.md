# Bild spiegeln

Der ImageFlip-Node spiegelt Bilder entlang verschiedener Achsen. Er kann Bilder vertikal entlang der x-Achse oder horizontal entlang der y-Achse spiegeln. Der Node verwendet torch.flip-Operationen, um die Spiegelung basierend auf der ausgewählten Methode durchzuführen.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `image` | Das Eingabebild, das gespiegelt werden soll | IMAGE | Ja | - |
| `flip_method` | Die anzuwendende Spiegelungsrichtung (Standard: "x-axis: vertically") | STRING | Ja | "x-axis: vertically"<br>"y-axis: horizontally" |

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `image` | Das gespiegelte Ausgabebild | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageFlip/de.md)

---
**Source fingerprint (SHA-256):** `481cd167d57746f242fcc4b5f2e3bb0bff0184b5870626d5f24a34422464ddd6`
