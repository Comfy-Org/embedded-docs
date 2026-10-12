# WanDancerPadKeyframes

## Überblick

Dieser Node bereitet eine Sequenz von Keyframes für einen bestimmten Abschnitt eines längeren Videogenerierungsprozesses vor. Er empfängt einen Stapel Eingabebilder und eine Audiospur, berechnet anhand der Audiodauer, wie viele Frames das vollständige Video insgesamt haben sollte, und verteilt dann die Eingabebilder als Keyframes über den ausgewählten Abschnitt, während der Rest mit leeren Frames aufgefüllt wird. Außerdem extrahiert er den entsprechenden Teil des Audios für diesen Abschnitt.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `images` | Die Eingabebilder, die als Keyframes verteilt werden sollen. | IMAGE | Ja | Stapel von Bildern |
| `segment_length` | Länge dieses Segments in Frames (Standard: 149). | INT | Ja | 1 bis 10000 |
| `segment_index` | Welches Segment dies ist (0 für das erste, 1 für das zweite usw., Standard: 0). | INT | Ja | 0 bis 100 |
| `audio` | Audio, aus dem die Gesamtzahl der Ausgabeframes berechnet und das Audio für das Segment extrahiert wird. | AUDIO | Ja | Audiodaten |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `keyframes_sequence` | Aufgefüllte Keyframe-Sequenz für das angegebene Segment. | IMAGE |
| `keyframes_mask` | Maske, die gültige Frames angibt (1 für Keyframe-Positionen, 0 für aufgefüllte Positionen). | MASK |
| `audio_segment` | Audiosegment für dieses Videosegment. | AUDIO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanDancerPadKeyframes/de.md)

---
**Source fingerprint (SHA-256):** `93393e39cb1968b6e8720dfad213c16c534857bcfafcc577be64e0733ab3a760`
