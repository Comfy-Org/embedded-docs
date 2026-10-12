# Kling 3.0 Omni Video bearbeiten

Der Kling Omni Edit Video (Pro)-Node verwendet ein KI-Modell, um ein vorhandenes Video anhand einer Textbeschreibung zu bearbeiten. Sie geben ein Quellvideo und einen Prompt an, und der Node erzeugt ein neues Video derselben Länge mit den gewünschten Änderungen. Optional können Referenzbilder verwendet werden, um den Stil zu steuern, und das Original-Audio aus dem Quellvideo kann beibehalten werden.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model_name` | Das KI-Modell, das für die Videobearbeitung verwendet werden soll (Standard: `"kling-v3-omni"`). | COMBO | Ja | `"kling-v3-omni"`<br>`"kling-video-o1"` |
| `prompt` | Ein Text-Prompt, der den Videoinhalt beschreibt. Dieser kann sowohl positive als auch negative Beschreibungen enthalten. | STRING | Ja |  |
| `video` | Video zur Bearbeitung. Die Länge des Ausgabevideos bleibt gleich. | VIDEO | Ja |  |
| `keep_original_sound` | Bestimmt, ob das Original-Audio aus dem Eingabevideo in der Ausgabe beibehalten wird (Standard: True). | BOOLEAN | Ja |  |
| `reference_images` | Bis zu 4 zusätzliche Referenzbilder. | IMAGE | Nein |  |
| `resolution` | Die Auflösung für das Ausgabevideo (Standard: `"1080p"`). | COMBO | Nein | `"1080p"`<br>`"720p"` |
| `seed` | Der Seed steuert, ob der Node erneut ausgeführt werden soll; die Ergebnisse sind unabhängig vom Seed nicht deterministisch (Standard: 0). | INT | Nein | 0 bis 2147483647 |

**Einschränkungen und Beschränkungen:**

* Der `prompt` muss zwischen 1 und 2500 Zeichen lang sein.
* Das eingegebene `video` muss eine Dauer zwischen 3,0 und 10,05 Sekunden haben.
* Die Abmessungen des eingegebenen `video` müssen zwischen 720x720 und 2160x2160 Pixeln liegen.
* Es können maximal 4 `reference_images` bereitgestellt werden, wenn ein Video verwendet wird.
* Jedes `reference_image` muss mindestens 300x300 Pixel groß sein.
* Jedes `reference_image` muss ein Seitenverhältnis zwischen 1:2,5 und 2,5:1 haben.

## Ausgaben

| Name der Ausgabe | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `video` | Das vom KI-Modell generierte bearbeitete Video. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingOmniProEditVideoNode/de.md)

---
**Source fingerprint (SHA-256):** `4aa7779a30183c80f025e15ae693ba23021013c68d247753e7e9a4c3a64762da`
