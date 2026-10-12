# Kling 3.0 Omni Text zu Video

Dieser Node erzeugt ein Video aus einer Textbeschreibung mithilfe des neuesten Kling-KI-Modells. Er sendet Ihren Prompt an eine Remote-API und gibt das generierte Video zurück. Sie können die Länge, das Format und die Qualität des Videos steuern und optional Multi-Shot-Storyboards erstellen.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|--------------|---------|
| `model_name` | Das spezifische Kling-Modell, das für die Videogenerierung verwendet werden soll (Standard: `"kling-v3-omni"`). | COMBO | Ja | `"kling-v3-omni"`<br>`"kling-video-o1"` |
| `prompt` | Ein Text-Prompt, der den Videoinhalt beschreibt. Er kann sowohl positive als auch negative Beschreibungen enthalten. Wird ignoriert, wenn Storyboards aktiviert sind. | STRING | Ja | 0 bis 2500 Zeichen |
| `aspect_ratio` | Die Form oder Abmessungen des zu generierenden Videos. | COMBO | Ja | `"16:9"`<br>`"9:16"`<br>`"1:1"` |
| `duration` | Die Länge des Videos in Sekunden (Standard: 5). | INT | Ja | 3 bis 15 Sekunden |
| `resolution` | Die Qualität oder Pixelauflösung des Videos (Standard: `"1080p"`). Wird intern den Qualitätsstufen Standard, Pro oder 4K zugeordnet. | COMBO | Nein | `"4k"`<br>`"1080p"`<br>`"720p"` |
| `storyboards` | Erzeugt eine Reihe von Videosegmenten mit individuellen Prompts und Dauern. Wird für das o1-Modell ignoriert. | DYNAMIC_COMBO | Nein | `"disabled"`<br>`"1 storyboard"`<br>`"2 storyboards"`<br>`"3 storyboards"`<br>`"4 storyboards"`<br>`"5 storyboards"`<br>`"6 storyboards"` |
| `generate_audio` | Ob Audio für das Video generiert werden soll (Standard: False). | BOOLEAN | Nein | True / False |
| `seed` | Der Seed steuert, ob der Node erneut ausgeführt werden soll; die Ergebnisse sind unabhängig vom Seed nicht deterministisch (Standard: 0). | INT | Nein | 0 bis 2147483647 |

### Storyboard-Untereingaben

Wenn `storyboards` auf einen anderen Wert als `"disabled"` gesetzt wird, erscheinen die folgenden Eingaben für jedes Storyboard-Segment. In den unten stehenden Parameternamen ist `{i}` die Segmentnummer, von 1 bis zur ausgewählten Anzahl an Storyboards.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|--------------|---------|
| `storyboard_{i}_prompt` | Prompt für Storyboard-Segment {i}. Maximal 512 Zeichen. | STRING | Ja | 1 bis 512 Zeichen |
| `storyboard_{i}_duration` | Dauer für Storyboard-Segment {i} in Sekunden (Standard: 4). | INT | Ja | 1 bis 15 Sekunden |

### Parametereinschränkungen und Beschränkungen

- **Modellspezifische Einschränkungen:**
  - Das Modell `kling-video-o1` unterstützt nur Dauern von **5 oder 10 Sekunden**.
  - Das Modell `kling-video-o1` unterstützt **keine** Audiogenerierung.
  - Das Modell `kling-video-o1` unterstützt **keine** 4K-Auflösung.
  - Das Modell `kling-video-o1` unterstützt **keine** Storyboards.
- **Storyboard-Einschränkungen:**
  - Wenn Storyboards aktiviert sind, wird das Feld `prompt` ignoriert.
  - Jedes Storyboard erfordert einen eigenen Prompt (1 bis 512 Zeichen) und eine eigene Dauer.
  - Die Gesamtdauer aller Storyboards muss exakt dem globalen Parameter `duration` entsprechen.
- **Prompt-Anforderungen:**
  - Wenn Storyboards **deaktiviert** sind, ist das Feld `prompt` erforderlich (mindestens 1 Zeichen).
  - Wenn Storyboards **aktiviert** sind, kann das Feld `prompt` leer sein (0 Zeichen).

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `output` | Das auf Basis des angegebenen Text-Prompts und der Einstellungen generierte Video. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingOmniProTextToVideoNode/de.md)

---
**Source fingerprint (SHA-256):** `d2fbbe7c6aae283eb3fa7f73d788b809098a9a4dd6e8ada54697d43fd5bf10f2`
