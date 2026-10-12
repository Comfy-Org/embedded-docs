# Bild mit Alpha aufteilen

Der SplitImageWithAlpha-Node dient dazu, die Farb- und Alpha-Komponenten eines Bildes zu trennen. Er verarbeitet einen Eingabebild-Tensor, extrahiert die RGB-Kanäle als Farbkomponente und den Alpha-Kanal als Transparenzkomponente, wodurch Vorgänge erleichtert werden, die die Bearbeitung dieser unterschiedlichen Bildaspekte erfordern.

## Eingaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `image` | Der Parameter `image` repräsentiert den Eingabebild-Tensor, aus dem die RGB- und Alpha-Kanäle getrennt werden sollen. Er ist für den Vorgang entscheidend, da er die Quelldaten für die Aufteilung liefert. | `IMAGE` |

## Ausgaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `image` | Die Ausgabe `image` repräsentiert die getrennten RGB-Kanäle des Eingabebilds und liefert die Farbkomponente ohne die Transparenzinformationen. | `IMAGE` |
| `mask` | Die Ausgabe `mask` repräsentiert den getrennten Alpha-Kanal des Eingabebilds und liefert die Transparenzinformationen. | `MASK` |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SplitImageWithAlpha/de.md)
