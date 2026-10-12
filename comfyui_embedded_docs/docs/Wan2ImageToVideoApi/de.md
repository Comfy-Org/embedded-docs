# Wan2ImageToVideoApi

Der Wan 2.7 Image to Video-Node erzeugt ein Video ausgehend von einem Bild des ersten Frames. Optional können Sie ein Bild des letzten Frames bereitstellen, um einen Übergang zwischen beiden zu erzeugen, oder eine Audiodatei angeben, um die Bewegung und das Timing des Videos zu steuern. Der Node verwendet ein KI-Modell, um die Szene basierend auf Ihrer Textbeschreibung zu animieren.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model` | Das KI-Modell, das für die Videogenerierung verwendet werden soll. | DYNAMIC_COMBO | Ja | `"wan2.7-i2v"` |
| `first_frame` | Bild des ersten Frames. Das Seitenverhältnis der Ausgabe wird von diesem Bild abgeleitet. | IMAGE | Ja | - |
| `last_frame` | Bild des letzten Frames. Das Modell generiert ein Video, das vom ersten zum letzten Frame übergeht. | IMAGE | Nein | - |
| `audio` | Audio zur Steuerung der Videogenerierung (z. B. Lip-Sync, beat-synchrone Bewegung). Dauer: 2s-30s. Wenn nicht bereitgestellt, generiert das Modell automatisch passende Hintergrundmusik oder Soundeffekte. | AUDIO | Nein | - |
| `seed` | Seed für die Generierung (Standard: 0). | INT | Ja | 0 to 2147483647 |
| `prompt_extend` | Gibt an, ob der Prompt mit KI-Unterstützung erweitert werden soll (Standard: True). Dies ist eine erweiterte Einstellung. | BOOLEAN | Ja | True<br>False |
| `watermark` | Gibt an, ob dem Ergebnis ein KI-generiertes Wasserzeichen hinzugefügt werden soll (Standard: False). Dies ist eine erweiterte Einstellung. | BOOLEAN | Ja | True<br>False |

### wan2.7-i2v Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `prompt` | Prompt, der die Elemente und visuellen Merkmale beschreibt. Unterstützt Englisch und Chinesisch. (Standard: leer) | STRING | Ja | - |
| `negative_prompt` | Negativer Prompt, der beschreibt, was vermieden werden soll. (Standard: leer) | STRING | Ja | - |
| `resolution` | Die Auflösung des Ausgabevideos. | COMBO | Ja | `"720P"`<br>`"1080P"` |
| `duration` | Die Länge des generierten Videos in Sekunden (Standard: 5). | INT | Ja | 2 to 15 |

**Hinweis:** Die Eingabe `audio` hat eine Dauerbeschränkung. Wenn sie bereitgestellt wird, muss die Audiodatei zwischen 2 und 30 Sekunden lang sein.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `output` | Die generierte Videodatei. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan2ImageToVideoApi/de.md)

---
**Source fingerprint (SHA-256):** `81b0dc9500ff00e1428422d3d9c8df8f790c1d9dec547dcba0d1aa239f8a8beb`
