# Kling 3.0 Video

Dieser Node erzeugt Videos mit dem Kling V3-Modell. Er unterstützt Text-zu-Video, wobei ein Video aus einer Textbeschreibung erstellt wird, und Bild-zu-Video, wobei ein vorhandenes Bild animiert wird. Er kann außerdem mehrsegmentige Videos mithilfe von Storyboard-Prompts erstellen und optional Audio generieren.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `multi_shot` | Erzeugt eine Reihe von Videosegmenten mit individuellen Prompts und Dauern. Wenn auf eine Storyboard-Option gesetzt, erscheinen zusätzliche Eingaben für Prompt und Dauer jedes Storyboards. | DYNAMIC_COMBO | Ja | `"disabled"`<br>`"1 storyboard"`<br>`"2 storyboards"`<br>`"3 storyboards"`<br>`"4 storyboards"`<br>`"5 storyboards"`<br>`"6 storyboards"` |
| `generate_audio` | Wenn aktiviert, erzeugt der Node Audio für das Video. Hinweis: `"kling-3.0-turbo"` erzeugt immer natives Audio, daher wird der Audio-Schalter für dieses Modell ignoriert. Standard ist True. | BOOLEAN | Ja | True<br>False |
| `model` | Modell- und Generierungseinstellungen. Bei Auswahl eines Modells werden dessen Unterparameter für Auflösung und Seitenverhältnis eingeblendet. | DYNAMIC_COMBO | Ja | `"kling-v3"`<br>`"kling-3.0-turbo"` |
| `seed` | Der Seed steuert, ob der Node erneut ausgeführt werden soll; die Ergebnisse sind unabhängig vom Seed nicht deterministisch. Standard ist 0. | INT | Ja | 0 bis 2147483647 |
| `start_frame` | Optionales Startbild. Wenn verbunden, wird zum Bild-zu-Video-Modus gewechselt. | IMAGE | Nein | - |

### kling-v3 Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model.resolution` | Die Auflösung für das erzeugte Video. Standard ist `"1080p"`. | COMBO | Ja | `"4k"`<br>`"1080p"`<br>`"720p"` |
| `model.aspect_ratio` | Das Seitenverhältnis für das erzeugte Video. Wird im Bild-zu-Video-Modus ignoriert. | COMBO | Ja | `"16:9"`<br>`"9:16"`<br>`"1:1"` |

### kling-3.0-turbo Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model.resolution` | Die Auflösung für das erzeugte Video. Standard ist `"720p"`. | COMBO | Ja | `"1080p"`<br>`"720p"` |
| `model.aspect_ratio` | Das Seitenverhältnis für das erzeugte Video. Wird im Bild-zu-Video-Modus ignoriert. | COMBO | Ja | `"16:9"`<br>`"9:16"`<br>`"1:1"` |

### Multi-Shot-Eingaben

**Wenn `multi_shot` auf `"disabled"` gesetzt ist:**

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Die Haupttextbeschreibung für das Video. Muss zwischen 1 und 2500 Zeichen lang sein. | STRING | Ja | 1 bis 2500 Zeichen |
| `negative_prompt` | Text, der beschreibt, was im Video nicht erscheinen soll. Kann leer gelassen werden. | STRING | Nein | - |
| `duration` | Die Länge des Videos in Sekunden. Standard ist 5. | INT | Ja | 3 bis 15 |

**Wenn `multi_shot` auf eine Storyboard-Option gesetzt ist (z. B. `"3 storyboards"`):**

Für jedes Storyboard-Segment N (von 1 bis zur ausgewählten Anzahl an Storyboards) erscheinen die folgenden Eingaben:

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `storyboard_N_prompt` | Prompt für Storyboard-Segment N. Max. 512 Zeichen. | STRING | Ja | 1 bis 512 Zeichen |
| `storyboard_N_duration` | Dauer für Storyboard-Segment N in Sekunden. Standard ist 4. | INT | Ja | 1 bis 15 |

**Einschränkungen und Verhalten:**

- Der Text-zu-Video-Modus wird verwendet, wenn `start_frame` nicht verbunden ist; der Bild-zu-Video-Modus wird verwendet, wenn `start_frame` verbunden ist. Im Bild-zu-Video-Modus wird `model.aspect_ratio` ignoriert, und das Eingabebild muss mindestens 300x300 Pixel groß sein und ein Seitenverhältnis zwischen 1:2.5 und 2.5:1 aufweisen.
- Im Storyboard-Modus werden der Haupt-`prompt` und `negative_prompt` nicht verwendet. Die Gesamtsumme aller Storyboard-Dauern muss zwischen 3 und 15 Sekunden liegen.
- `negative_prompt` wird nur mit `kling-v3` verwendet; es wird ignoriert, wenn `kling-3.0-turbo` ausgewählt ist.
- Für `kling-v3` wird jedes Storyboard als separates Segment an die API gesendet. Für `kling-3.0-turbo` werden die Storyboard-Prompts und -Dauern zu einem einzigen Multi-Shot-Prompt kombiniert.
- Für `kling-3.0-turbo` wird `generate_audio` ignoriert, da dieses Modell immer natives Audio erzeugt.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `video` | Die erzeugte Videodatei. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingVideoNode/de.md)

---
**Source fingerprint (SHA-256):** `2863d7a971a1978b6009e5321ed2112a9c04809281acd5f65d85ab72c4b49f08`
