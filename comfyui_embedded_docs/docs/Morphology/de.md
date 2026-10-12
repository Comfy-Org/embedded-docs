# Morphologie anwenden

Der Morphology-Knoten wendet verschiedene morphologische Operationen auf Bilder an. Dabei handelt es sich um mathematische Operationen, die verwendet werden, um Formen in Bildern zu verarbeiten und zu analysieren. Er kann Operationen wie Erosion, Dilatation, Öffnen, Schließen und weitere ausführen, wobei eine anpassbare Kernel-Größe die Stärke des Effekts steuert.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `image` | Das zu verarbeitende Eingabebild | IMAGE | Ja | - |
| `operation` | Die anzuwendende morphologische Operation (Standard: "erode") | STRING | Ja | `"erode"`<br>`"dilate"`<br>`"open"`<br>`"close"`<br>`"gradient"`<br>`"bottom_hat"`<br>`"top_hat"` |
| `kernel_size` | Die Größe des Kernels des Strukturierungselements (Standard: 3). Muss eine ungerade Zahl sein. | INT | Ja | 3-999 |

## Ausgaben

| Ausgabenamen | Beschreibung | Datentyp |
| --- | --- | --- |
| `image` | Das verarbeitete Bild nach Anwendung der morphologischen Operation | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Morphology/de.md)

---
**Source fingerprint (SHA-256):** `ea596f8d30975f153fccbc5651eec0fbbf308ef1c616313d996c200cddf748e3`
