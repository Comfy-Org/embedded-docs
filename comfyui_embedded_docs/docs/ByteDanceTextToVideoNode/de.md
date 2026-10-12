# ByteDance Text zu Video

Der ByteDance Text to Video-Node generiert mithilfe von ByteDance-Modellen über eine API basierend auf einem Text-Prompt ein Video. Sie geben einen Prompt an und wählen Einstellungen wie Modell, Auflösung, Seitenverhältnis und Dauer; der Node übermittelt die Generierungsanfrage und gibt das generierte Video zurück.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `model` | Das ByteDance-Modell, das zur Generierung des Videos verwendet wird (Standard: `"seedance-1-0-pro-fast-251015"`). | COMBO | Ja | `"seedance-1-5-pro-251215"`<br>`"seedance-1-0-pro-250528"`<br>`"seedance-1-0-pro-fast-251015"` |
| `prompt` | Der Text-Prompt, der zur Generierung des Videos verwendet wird. | STRING | Ja | - |
| `resolution` | Die Auflösung des Ausgabevideos. | COMBO | Ja | `"480p"`<br>`"720p"`<br>`"1080p"` |
| `aspect_ratio` | Das Seitenverhältnis des Ausgabevideos. | COMBO | Ja | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"` |
| `duration` | Die Dauer des Ausgabevideos in Sekunden (Standard: 5). | INT | Ja | 3 bis 12 |
| `seed` | Seed für die Generierung (Standard: 0). | INT | Nein | 0 bis 2147483647 |
| `camera_fixed` | Gibt an, ob die Kamera fixiert werden soll. Die Plattform hängt eine Anweisung zum Fixieren der Kamera an Ihren Prompt an, garantiert jedoch nicht die tatsächliche Wirkung (Standard: False). | BOOLEAN | Nein | - |
| `watermark` | Gibt an, ob dem Video ein Wasserzeichen "AI generated" hinzugefügt werden soll (Standard: False). | BOOLEAN | Nein | - |
| `generate_audio` | Dieser Parameter wird für jedes Modell außer `seedance-1-5-pro-251215` ignoriert (Standard: False). | BOOLEAN | Nein | - |

**Parametereinschränkungen:**

- Der Parameter `prompt` muss nach Entfernen von Leerzeichen mindestens 1 Zeichen enthalten.
- Der Parameter `prompt` darf die folgenden Textparameter nicht enthalten: "resolution", "ratio", "duration", "seed", "camerafixed", "watermark".
- Der Node erstellt den endgültigen Prompt, indem er die ausgewählten Einstellungen für `resolution`, `aspect_ratio`, `duration`, `seed`, `camera_fixed` und `watermark` an den Prompt-Text anhängt.
- Der Parameter `duration` ist auf Werte zwischen 3 und 12 Sekunden begrenzt. Für das Modell `seedance-1-5-pro-251215` beträgt die minimal unterstützte Dauer 4 Sekunden.
- Der Parameter `seed` akzeptiert Werte von 0 bis 2.147.483.647.
- Der Parameter `generate_audio` wirkt sich nur aus, wenn `model` auf `seedance-1-5-pro-251215` gesetzt ist; für alle anderen Modelle wird er ignoriert.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|--------------|----------|
| `output` | Die generierte Videodatei | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceTextToVideoNode/de.md)

---
**Source fingerprint (SHA-256):** `83b805b63e59a76cae378b0407b409e1bfe900677ef1e01fc836fede47283eee`
