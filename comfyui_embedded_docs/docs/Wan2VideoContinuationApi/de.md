# Wan2VideoContinuationApi

Der Wan 2.7 Video Continuation-Node erzeugt ein neues Videosegment, das an das Ende eines Eingabevideoclips anknüpft. Er verwendet das Wan 2.7-Modell, um die Fortsetzung basierend auf einem Text-Prompt zu synthetisieren, und kann optional das Ende auf einen bestimmten Ziel-Frame hinführen.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `model` | Das zu verwendende Videogenerierungsmodell. Die ausgewählte Option bestimmt, welche zusätzlichen Einstellungen unten angezeigt werden. | DYNAMIC_COMBO | Ja | `"wan2.7-i2v"` |
| `first_clip` | Eingabevideo, von dem aus fortgesetzt wird. Dauer: 2s-10s. Das Seitenverhältnis der Ausgabe wird aus diesem Video abgeleitet. | VIDEO | Ja | 2s bis 10s |
| `last_frame` | Bild des letzten Frames. Die Fortsetzung wird zu diesem Frame überleiten. | IMAGE | Nein | - |
| `seed` | Seed, der für die Generierung verwendet werden soll. (Standard: 0) | INT | Ja | 0 bis 2147483647 |
| `prompt_extend` | Ob der Prompt mit KI-Unterstützung erweitert werden soll. (Standard: True) | BOOLEAN | Ja | - |
| `watermark` | Ob dem Ergebnis ein KI-generiertes Wasserzeichen hinzugefügt werden soll. (Standard: False) | BOOLEAN | Ja | - |

### wan2.7-i2v Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `prompt` | Prompt, der die Elemente und visuellen Merkmale beschreibt. Unterstützt Englisch und Chinesisch. (Standard: leerer String) | STRING | Ja | - |
| `negative_prompt` | Negativer Prompt, der beschreibt, was vermieden werden soll. (Standard: leerer String) | STRING | Ja | - |
| `resolution` | Die Ausgabeauflösung für das generierte Video. | COMBO | Ja | `"720P"`<br>`"1080P"` |
| `duration` | Gesamtdauer der Ausgabe in Sekunden. Das Modell generiert eine Fortsetzung, um die verbleibende Zeit nach dem Eingabeclip zu füllen. (Standard: 5) | INT | Ja | 2 bis 15 |

**Hinweis:** Das Eingabevideo `first_clip` muss eine Dauer zwischen 2 und 10 Sekunden haben.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|--------------|----------|
| `output` | Die generierte Videofortsetzung. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan2VideoContinuationApi/de.md)

---
**Source fingerprint (SHA-256):** `591e551676969bc1fedb5f820f6866512c132bb98ee8ef1766d1e0b389e2dc11`
