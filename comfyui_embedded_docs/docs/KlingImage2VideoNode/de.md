# KlingImage2VideoNode

Der Kling Image to Video Node erzeugt ein kurzes Video, wobei ein Ausgangsbild als erstes Frame verwendet wird. Er kombiniert das Bild mit Text-Prompts und Generierungseinstellungen und gibt anschließend das resultierende Video zusammen mit seiner ID und Dauer zurück.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `start_frame` | Das Referenzbild, das zur Generierung des Videos verwendet wird. Das Bild muss mindestens 300x300 Pixel groß sein und ein Seitenverhältnis zwischen 1:2.5 und 2.5:1 haben. | IMAGE | Ja | - |
| `prompt` | Positiver Text-Prompt. Darf nicht leer sein. Maximal 500 Zeichen. | STRING | Ja | - |
| `negative_prompt` | Negativer Text-Prompt. Maximal 500 Zeichen. Leer lassen, wenn nicht verwendet. | STRING | Ja | - |
| `model_name` | Das für die Videogenerierung verwendete Modell. | COMBO | Ja | `"kling-v2-5-turbo"` |
| `cfg_scale` | Steuert, wie genau das Video dem Prompt folgt. Höhere Werte bedeuten eine stärkere Befolgung (Standard: 0.8). | FLOAT | Ja | 0.0 bis 1.0 |
| `mode` | Der Generierungsmodus. | COMBO | Ja | `"pro"` |
| `aspect_ratio` | Das Seitenverhältnis des generierten Videos (Standard: `"16:9"`). | COMBO | Ja | `"16:9"`<br>`"9:16"`<br>`"1:1"` |
| `duration` | Die Dauer des generierten Videos in Sekunden (Standard: `"5"`). | COMBO | Ja | `"5"`<br>`"10"` |

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `output` | Die generierte Videoausgabe. | VIDEO |
| `video_id` | Eindeutiger Bezeichner für das generierte Video. | STRING |
| `duration` | Dauerinformationen für das generierte Video. | STRING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingImage2VideoNode/de.md)

---
**Source fingerprint (SHA-256):** `f4a461819bc05f92d867bddcc78a66ad7beaa10707ef8cae3e7eb9e6f72c890a`
