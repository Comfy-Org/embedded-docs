# Kling 3.0 Omni Erstes-letztes-Frame zu Video

Dieser Node verwendet das neueste Kling AI-Modell, um ein Video aus einem Startbild, einem optionalen Endbild oder Referenzbildern zu generieren. Er kann ein einzelnes Video oder ein mehrteiliges Storyboard mit individuellen Prompts und Dauern für jedes Segment erstellen. Der Node verarbeitet diese Eingaben, um ein Video mit einer angegebenen Länge und Auflösung zu erzeugen, optional mit Audiogenerierung.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model_name` | Das spezifische Kling AI-Modell, das für die Videogenerierung verwendet werden soll. | COMBO | Ja | `"kling-v3-omni"`<br>`"kling-video-o1"` |
| `prompt` | Ein Text-Prompt, der den Videoinhalt beschreibt. Er kann sowohl positive als auch negative Beschreibungen enthalten. Wird ignoriert, wenn Storyboards aktiviert sind. | STRING | Ja | - |
| `duration` | Die gewünschte Länge des generierten Videos in Sekunden (Standard: 5). | INT | Ja | 3 bis 15 |
| `first_frame` | Das Startbild für die Videosequenz. | IMAGE | Ja | - |
| `end_frame` | Ein optionales Endbild für das Video. Es kann nicht gleichzeitig mit `reference_images` verwendet werden. Funktioniert nicht mit Storyboards. | IMAGE | Nein | - |
| `reference_images` | Bis zu 6 zusätzliche Referenzbilder. | IMAGE | Nein | - |
| `resolution` | Die Ausgabeauflösung für das generierte Video (Standard: "1080p"). | COMBO | Nein | `"4k"`<br>`"1080p"`<br>`"720p"` |
| `storyboards` | Erzeugt eine Reihe von Videosegmenten mit individuellen Prompts und Dauern. Wird nur für `kling-v3-omni` unterstützt. | DYNAMIC_COMBO | Nein | `"disabled"`<br>`"1 storyboard"`<br>`"2 storyboards"`<br>`"3 storyboards"`<br>`"4 storyboards"`<br>`"5 storyboards"`<br>`"6 storyboards"` |
| `generate_audio` | Erzeugt Audio für das Video (Standard: False). Wird nur für `kling-v3-omni` unterstützt. | BOOLEAN | Nein | True / False |
| `seed` | Der Seed steuert, ob der Node erneut ausgeführt werden soll; die Ergebnisse sind unabhängig vom Seed nicht deterministisch (Standard: 0). | INT | Nein | 0 bis 2147483647 |

### Storyboard-Eingaben

Wenn `storyboards` auf einen anderen Wert als `"disabled"` gesetzt ist, werden für jedes ausgewählte Segment die folgenden Eingaben hinzugefügt (N reicht von 1 bis zur ausgewählten Anzahl an Storyboards):

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `storyboard_N_prompt` | Prompt für Storyboard-Segment N. Maximal 512 Zeichen. (Standard: "") | STRING | Ja | - |
| `storyboard_N_duration` | Dauer für Storyboard-Segment N in Sekunden (Standard: 4). | INT | Ja | 1 bis 15 |

**Wichtige Einschränkungen:**

* Die Eingabe `end_frame` kann nicht gleichzeitig mit der Eingabe `reference_images` verwendet werden.
* Die Eingabe `end_frame` kann nicht gleichzeitig mit Storyboards verwendet werden.
* Das Modell `kling-video-o1` unterstützt keine Dauern über 10 Sekunden, keine Audiogenerierung, keine 4k-Auflösung und keine Storyboards.
* Wenn Sie mit dem Modell `kling-video-o1` weder ein `end_frame` noch `reference_images` angeben, kann die `duration` nur auf 5 oder 10 Sekunden festgelegt werden.
* Alle Eingabebilder (`first_frame`, `end_frame` und etwaige `reference_images`) müssen eine Mindestabmessung von 300 Pixeln sowohl in der Breite als auch in der Höhe haben.
* Das Seitenverhältnis aller Eingabebilder muss zwischen 1:2.5 und 2.5:1 liegen.
* Über die Eingabe `reference_images` können maximal 6 Bilder bereitgestellt werden.
* Der Text für `prompt` muss zwischen 1 und 2500 Zeichen lang sein (0 Zeichen sind erlaubt, wenn Storyboards aktiviert sind).
* Der Prompt kann die Eingabebilder über die Platzhalter `@image`, `@image1`, `@image2` usw. referenzieren; diese werden automatisch in das API-kompatible Bildreferenzformat umgewandelt.
* Wenn Storyboards aktiviert sind, muss die Gesamtdauer aller Storyboard-Segmente dem globalen Wert `duration` entsprechen.
* Jeder Storyboard-Prompt muss zwischen 1 und 512 Zeichen lang sein.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `output` | Die generierte Videodatei. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingOmniProFirstLastFrameNode/de.md)

---
**Source fingerprint (SHA-256):** `2b26914ba29c3d877a981e41acb44d15dfacc604d86d7cc232ebfa7fda0ae3b8`
