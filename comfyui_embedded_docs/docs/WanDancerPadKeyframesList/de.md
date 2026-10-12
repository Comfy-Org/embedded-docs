# WanDancerPadKeyframesList

## Überblick

Dieser Node nimmt eine Bildsequenz und eine optionale Audiospur entgegen und teilt sie in eine angegebene Anzahl aufgefüllter Segmente auf. Er ist darauf ausgelegt, Keyframe-Sequenzen für die Videogenerierung vorzubereiten, wobei jedes Segment auf eine einheitliche Länge aufgefüllt wird und eine entsprechende Maske erstellt wird, um anzugeben, welche Frames gültig sind.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `images` | Die Eingabebildsequenz, die in Segmente aufgeteilt werden soll. | IMAGE | Ja | N/A |
| `segment_length` | Länge jedes Segments in Frames (Standard: 149). | INT | Ja | 1 bis 10000 |
| `num_segments` | Wie viele aufgefüllte Segmente als Listen ausgegeben werden sollen (Standard: 1). | INT | Ja | 1 bis 100 |
| `audio` | Audio, das für jedes ausgegebene Segment zugeschnitten werden soll. | AUDIO | Nein | N/A |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `keyframes_sequence` | Eine Liste aufgefüllter Keyframe-Sequenzen, eine für jedes Segment. | IMAGE |
| `keyframes_mask` | Eine Liste von Masken, die die gültigen Frames für jedes Segment angeben. | MASK |
| `audio_segment` | Eine Liste von Audiosegmenten, eines für jedes Videosegment. | AUDIO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanDancerPadKeyframesList/de.md)

---
**Source fingerprint (SHA-256):** `f9918166a75f688f1de6a09008780bc629bbdfb3b8d547de9ba8661ef07fc97e`
