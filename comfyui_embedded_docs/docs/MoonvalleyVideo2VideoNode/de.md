# MoonvalleyVideo2VideoNode

Der Node „Moonvalley Marey Video to Video“ wandelt ein Eingabevideo basierend auf einer Textbeschreibung in ein neues Video um. Er verwendet die Moonvalley-API, um Videos zu generieren, die zu Ihrem Prompt passen, während Bewegungs- oder Pose-Merkmale aus dem Originalvideo beibehalten werden. Sie können den Stil und Inhalt des Ausgabevideos über Text-Prompts und verschiedene Generierungsparameter steuern.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `prompt` | Beschreibt das zu generierende Video (mehrzeilige Eingabe) | STRING | Ja | - |
| `negative_prompt` | Negativer Prompt-Text (Standard: umfangreiche Liste negativer Deskriptoren) | STRING | Nein | - |
| `seed` | Zufälliger Seed-Wert (Standard: 9) | INT | Ja | 0 to 4294967295 |
| `video` | Das Referenzvideo, das zur Generierung des Ausgabevideos verwendet wird. Muss mindestens 5 Sekunden lang sein. Videos, die länger als 5 s sind, werden automatisch gekürzt. Nur das MP4-Format wird unterstützt. | VIDEO | Ja | - |
| `control_type` | Auswahl des Steuerungstyps (Standard: "Motion Transfer") | COMBO | Nein | "Motion Transfer"<br>"Pose Transfer" |
| `motion_intensity` | Wird nur verwendet, wenn `control_type` auf "Motion Transfer" gesetzt ist (Standard: 100) | INT | Nein | 0 to 100 |
| `steps` | Anzahl der Inferenzschritte (Standard: 33) | INT | Ja | 1 to 100 |

**Hinweis:** Der Parameter `motion_intensity` wird nur angewendet, wenn `control_type` auf "Motion Transfer" gesetzt ist. Bei Verwendung von "Pose Transfer" wird dieser Parameter ignoriert.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `output` | Die generierte Videoausgabe | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoonvalleyVideo2VideoNode/de.md)

---
**Source fingerprint (SHA-256):** `8202a4be469afa16d77b9e0287c290b9c3f390347fc60f23878f50fd95a758e0`
