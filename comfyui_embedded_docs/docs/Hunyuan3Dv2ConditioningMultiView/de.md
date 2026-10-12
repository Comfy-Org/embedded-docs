# Hunyuan3Dv2ConditioningMultiView

Der Hunyuan3Dv2ConditioningMultiView-Node kombiniert CLIP-Vision-Ausgaben von bis zu vier Ansichten (vorne, links, hinten und rechts) zu einer einzigen Multiview-Konditionierung. Bei jeder bereitgestellten Ansicht wird eine Positionskodierung zu ihrer CLIP-Vision-Einbettung hinzugefügt, und die resultierenden Einbettungen werden konkateniert. Der Node gibt eine positive Konditionierung auf Basis der kombinierten Einbettungen sowie eine negative Konditionierung aus, die mit Nullen derselben Form gefüllt ist.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `front` | CLIP-Vision-Ausgabe für die vordere Ansicht. Optionaler Ansichtseingang. | CLIP_VISION_OUTPUT | Nein | - |
| `left` | CLIP-Vision-Ausgabe für die linke Ansicht. Optionaler Ansichtseingang. | CLIP_VISION_OUTPUT | Nein | - |
| `back` | CLIP-Vision-Ausgabe für die hintere Ansicht. Optionaler Ansichtseingang. | CLIP_VISION_OUTPUT | Nein | - |
| `right` | CLIP-Vision-Ausgabe für die rechte Ansicht. Optionaler Ansichtseingang. | CLIP_VISION_OUTPUT | Nein | - |

**Hinweis:** Mindestens ein Ansichtseingang muss bereitgestellt werden, damit der Node funktioniert. Der Node verarbeitet nur Ansichten, die gültige CLIP-Vision-Ausgabedaten enthalten, und überspringt Ansichten, die nicht verbunden sind. Jede Ansicht erhält eine feste Positionskodierung basierend auf ihrem Slot (vorne, links, hinten, rechts), und die verarbeiteten Einbettungen aller bereitgestellten Ansichten werden entlang der Sequenzdimension zusammengefügt.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `positive` | Positive Konditionierung, die die kombinierten Multiview-Einbettungen mit Positionskodierung enthält. | CONDITIONING |
| `negative` | Negative Konditionierung mit Nullwerten, die der Form der positiven Konditionierung entspricht. | CONDITIONING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Hunyuan3Dv2ConditioningMultiView/de.md)

---
**Source fingerprint (SHA-256):** `1492b51661d0bb8f2c142c1b1e8ef104beed1b9dae532a970e2928e27ad71d69`
