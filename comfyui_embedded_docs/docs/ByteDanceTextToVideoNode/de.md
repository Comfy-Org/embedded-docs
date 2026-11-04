# ByteDance Text zu Video

Der ByteDance Text to Video-Node generiert mithilfe von ByteDance-Modellen über eine API basierend auf einem Text-Prompt ein Video. Sie geben einen Prompt an und wählen Einstellungen wie Modell, Auflösung, Seitenverhältnis und Dauer; der Node übermittelt die Generierungsanfrage und gibt das generierte Video zurück.

**Hinweis:** Dieser Node ist im Quellcode als veraltet markiert.

**Hinweis:** BytePlus stellt das Modell Seedance 1.5 Pro am 11. November 2026 ein, daher bietet dieser Node es nicht mehr an und mit ihm gespeicherte Workflows funktionieren nicht mehr. Verwende stattdessen `seedance-1-0-pro-250528`, `seedance-1-0-pro-fast-251015` oder den [Seedance 2.5 Partner-Node](https://docs.comfy.org/de/tutorials/partner-nodes/bytedance/seedance-2-5).

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `model` | Das ByteDance-Modell, das zur Generierung des Videos verwendet wird (Standard: `"seedance-1-0-pro-fast-251015"`). | COMBO | Ja | `"seedance-1-0-pro-250528"`<br>`"seedance-1-0-pro-fast-251015"` |
| `prompt` | Der Text-Prompt, der zur Generierung des Videos verwendet wird. | STRING | Ja | - |
| `resolution` | Die Auflösung des Ausgabevideos. | COMBO | Ja | `"480p"`<br>`"720p"`<br>`"1080p"` |
| `aspect_ratio` | Das Seitenverhältnis des Ausgabevideos. | COMBO | Ja | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"` |
| `duration` | Die Dauer des Ausgabevideos in Sekunden (Standard: 5). | INT | Ja | 3 bis 12 |
| `seed` | Seed für die Generierung (Standard: 0). | INT | Nein | 0 bis 2147483647 |
| `camera_fixed` | Gibt an, ob die Kamera fixiert werden soll. Die Plattform hängt eine Anweisung zum Fixieren der Kamera an Ihren Prompt an, garantiert jedoch nicht die tatsächliche Wirkung (Standard: False). | BOOLEAN | Nein | - |
| `watermark` | Gibt an, ob dem Video ein Wasserzeichen "AI generated" hinzugefügt werden soll (Standard: False). | BOOLEAN | Nein | - |
| `generate_audio` | Fügt eine KI-generierte Audiospur hinzu. Die übrigen Modelle ignorieren diese Eingabe (Standard: False). | BOOLEAN | Nein | - |

**Parametereinschränkungen:**

- Der Parameter `prompt` muss nach Entfernen von Leerzeichen mindestens 1 Zeichen enthalten.
- Der Parameter `prompt` darf die folgenden Textparameter nicht enthalten: "resolution", "ratio", "duration", "seed", "camerafixed", "watermark".
- Der Node erstellt den endgültigen Prompt, indem er die ausgewählten Einstellungen für `resolution`, `aspect_ratio`, `duration`, `seed`, `camera_fixed` und `watermark` an den Prompt-Text anhängt.
- Der Parameter `duration` ist auf Werte zwischen 3 und 12 Sekunden begrenzt.
- Der Parameter `seed` akzeptiert Werte von 0 bis 2.147.483.647.
- Der Parameter `generate_audio` wird aus Kompatibilitätsgründen akzeptiert, die übrigen Modelle ignorieren ihn jedoch.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|--------------|----------|
| `output` | Die generierte Videodatei | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceTextToVideoNode/de.md)

---
**Source fingerprint (SHA-256):** `d26d13c99a25bb14a0b1c1f3bae2dea1b30bf35f886331f26ef72e64ca357ef5`
