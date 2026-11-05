# ByteDance Erstes/letztes Frame zu Video

Dieser Node erzeugt ein Video mithilfe eines Text-Prompts sowie Bildern für das erste und letzte Frame. Dabei verwendet er Ihre Beschreibung und die beiden Keyframes, um eine vollständige Videosequenz zu erstellen, die zwischen ihnen übergeht. Der Node bietet verschiedene Optionen zur Steuerung der Auflösung, des Seitenverhältnisses, der Dauer und weiterer Generierungsparameter des Videos.

**Hinweis:** Dieser Node ist im Quellcode als veraltet markiert.

**Hinweis:** BytePlus stellt das Modell Seedance 1.5 Pro am 11. November 2026 ein, daher bietet dieser Node es nicht mehr an und mit ihm gespeicherte Workflows funktionieren nicht mehr. `seedance-1-0-pro-250528` ist das einzige verbleibende Modell in diesem Node. Für Video mit Audio und längere Clips verwende den [Seedance 2.5 Partner-Node](https://docs.comfy.org/de/tutorials/partner-nodes/bytedance/seedance-2-5).

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model` | Das für die Videogenerierung verwendete Modell (Standard: `"seedance-1-0-pro-250528"`). | COMBO | Ja | `"seedance-1-0-pro-250528"` |
| `prompt` | Der Text-Prompt, der zur Generierung des Videos verwendet wird. Darf nicht leer sein und darf keine reservierten Parameter-Schlüsselwörter enthalten (`resolution`, `ratio`, `duration`, `seed`, `camerafixed`, `watermark`). | STRING | Ja | - |
| `first_frame` | Das erste für das Video zu verwendende Frame. Es muss zwischen 300x300 und 6000x6000 Pixeln liegen und ein Seitenverhältnis zwischen 0,4 und 2,5 haben. | IMAGE | Ja | - |
| `last_frame` | Das letzte für das Video zu verwendende Frame. Es muss zwischen 300x300 und 6000x6000 Pixeln liegen und ein Seitenverhältnis zwischen 0,4 und 2,5 haben. | IMAGE | Ja | - |
| `resolution` | Die Auflösung des Ausgabevideos. | COMBO | Ja | `"480p"`<br>`"720p"`<br>`"1080p"` |
| `aspect_ratio` | Das Seitenverhältnis des Ausgabevideos. | COMBO | Ja | `"adaptive"`<br>`"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"` |
| `duration` | Die Dauer des Ausgabevideos in Sekunden. (Standard: 5) | INT | Ja | 3 - 12 |
| `seed` | Seed, der für die Generierung verwendet wird. (Standard: 0) | INT | Nein | 0 - 2147483647 |
| `camera_fixed` | Gibt an, ob die Kamera fixiert werden soll. Die Plattform hängt eine Anweisung zum Fixieren der Kamera an Ihren Prompt an, garantiert jedoch nicht die tatsächliche Wirkung. (Standard: False) | BOOLEAN | Nein | - |
| `watermark` | Ob dem Video ein Wasserzeichen "AI generated" hinzugefügt werden soll. (Standard: False) | BOOLEAN | Nein | - |
| `generate_audio` | Fügt eine KI-generierte Audiospur hinzu. Die übrigen Modelle ignorieren diese Eingabe (Standard: False) | BOOLEAN | Nein | - |

**Hinweis:** Sowohl `first_frame` als auch `last_frame` müssen zwischen 300x300 und 6000x6000 Pixeln liegen und ein Seitenverhältnis zwischen 0,4 und 2,5 haben. Der `prompt` wird geprüft und abgelehnt, wenn er reservierte Parameter-Schlüsselwörter enthält.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `output` | Die generierte Videodatei. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceFirstLastFrameNode/de.md)

---
**Source fingerprint (SHA-256):** `76f077c215942f164a024b85594e921b5fdb2d667a99ad4de2fe0f1195a15bb8`
