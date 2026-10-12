# KlingOmniProVideoToVideoNode

Dieser Node verwendet das Kling-KI-Modell, um basierend auf einem Eingabevideo und optionalen Referenzbildern ein neues Video zu generieren. Sie geben einen Text-Prompt an, der den gewünschten Inhalt beschreibt, und der Node transformiert das Referenzvideo entsprechend. Er kann außerdem bis zu vier zusätzliche Referenzbilder einbeziehen, um Stil und Inhalt der Ausgabe zu steuern.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model_name` | Das spezifische Kling-Modell, das für die Videogenerierung verwendet werden soll (Standard: "kling-v3-omni"). | COMBO | Ja | `"kling-v3-omni"`<br>`"kling-video-o1"` |
| `prompt` | Ein Text-Prompt, der den Videoinhalt beschreibt. Dieser kann sowohl positive als auch negative Beschreibungen enthalten. | STRING | Ja | N/A |
| `aspect_ratio` | Das gewünschte Seitenverhältnis für das generierte Video. | COMBO | Ja | `"16:9"`<br>`"9:16"`<br>`"1:1"` |
| `duration` | Die Länge des generierten Videos in Sekunden (Standard: 3). | INT | Ja | 3 bis 10 |
| `reference_video` | Video, das als Referenz verwendet werden soll. | VIDEO | Ja | N/A |
| `keep_original_sound` | Legt fest, ob das Audio aus dem Referenzvideo in der Ausgabe beibehalten wird (Standard: True). | BOOLEAN | Ja | N/A |
| `reference_images` | Bis zu 4 zusätzliche Referenzbilder. | IMAGE | Nein | N/A |
| `resolution` | Die Auflösung für das generierte Video (Standard: "1080p"). | COMBO | Nein | `"1080p"`<br>`"720p"` |
| `seed` | Der Seed steuert, ob der Node erneut ausgeführt werden soll; die Ergebnisse sind unabhängig vom Seed nicht deterministisch (Standard: 0). | INT | Nein | 0 bis 2147483647 |

**Parametereinschränkungen:**

* Der `prompt` muss zwischen 1 und 2500 Zeichen lang sein.
* Das `reference_video` muss eine Dauer zwischen 3,0 und 10,05 Sekunden haben.
* Das `reference_video` muss Abmessungen zwischen 720x720 und 2160x2160 Pixeln haben.
* Es können maximal 4 `reference_images` bereitgestellt werden. Jedes Bild muss mindestens 300x300 Pixel groß sein und ein Seitenverhältnis zwischen 1:2,5 und 2,5:1 haben.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `output` | Das neu generierte Video. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingOmniProVideoToVideoNode/de.md)

---
**Source fingerprint (SHA-256):** `3dc2e3d153ddd9e6da705b764c51b4a859d66464b893fdebb0689d2ad5e870c7`
