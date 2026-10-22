# ClipVisionEncode

Der Node `CLIP Vision Encode` ist ein Bildkodierungs-Node in ComfyUI, der Eingabebilder mithilfe des CLIP-Vision-Modells in visuelle Merkmalsvektoren umwandelt. Dieser Node ist eine wichtige Brücke zwischen Bild- und Textverständnis und wird in zahlreichen KI-Bildgenerierungs- und -verarbeitungs-Workflows eingesetzt.

**Funktionsweise des Nodes**

- **Bildmerkmalsextraktion**: Wandelt Eingabebilder in hochdimensionale Merkmalsvektoren um
- **Multimodale Verknüpfung**: Bietet eine Grundlage für die gemeinsame Verarbeitung von Bildern und Text
- **Bedingte Generierung**: Stellt visuelle Bedingungen für bildbasierte bedingte Generierung bereit

## Eingaben

| Parametername | Beschreibung | Datentyp |
| --- | --- | --- |
| `clip_vision` | CLIP-Vision-Modell, wird normalerweise über den Node CLIPVisionLoader geladen | CLIP_VISION |
| `image` | Das zu kodierende Eingabebild | IMAGE |
| `crop` | Methode zum Zuschneiden des Bildes, Optionen: center (zentrierter Zuschnitt), none (kein Zuschnitt) | Dropdown |

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| CLIP_VISION_OUTPUT | Kodierte visuelle Merkmale | CLIP_VISION_OUTPUT |

Dieses Ausgabeobjekt enthält:

- `last_hidden_state`: Der letzte verborgene Zustand
- `image_embeds`: Bild-Embedding-Vektor
- `penultimate_hidden_states`: Der vorletzte verborgene Zustand
- `mm_projected`: Ergebnis der multimodalen Projektion (falls verfügbar)

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPVisionEncode/de.md)
