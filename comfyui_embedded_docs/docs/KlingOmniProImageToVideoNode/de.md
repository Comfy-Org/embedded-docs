# KlingOmniProImageToVideoNode

Dieser Node verwendet das Kling-KI-Modell, um anhand eines Text-Prompts und bis zu sieben Referenzbildern ein Video zu generieren. Er ermöglicht die Steuerung von Seitenverhältnis, Dauer und Auflösung des Videos sowie optional die Verwendung von Storyboards oder die Generierung von Audio. Der Node sendet die Anfrage an eine externe API und gibt das generierte Video zurück.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `model_name` | Das spezifische Kling-Modell, das für die Videogenerierung verwendet werden soll (Standard: `"kling-v3-omni"`). | COMBO | Ja | `"kling-v3-omni"`<br>`"kling-video-o1"` |
| `prompt` | Ein Text-Prompt, der den Videoinhalt beschreibt. Er kann sowohl positive als auch negative Beschreibungen enthalten. Wird ignoriert, wenn Storyboards aktiviert sind. Platzhalter wie `@image` oder `@video` (optional nummeriert) werden automatisch in das API-kompatible Format konvertiert. Muss zwischen 1 und 2500 Zeichen lang sein (kann leer sein, wenn Storyboards aktiviert sind). | STRING | Ja | 1 bis 2500 Zeichen (0 bis 2500, wenn Storyboards aktiviert sind) |
| `aspect_ratio` | Das gewünschte Seitenverhältnis für das generierte Video. | COMBO | Ja | `"16:9"`<br>`"9:16"`<br>`"1:1"` |
| `duration` | Die Länge des Videos in Sekunden, angepasst mit einem Schieberegler (Standard: 5). | INT | Ja | 3 bis 15 |
| `reference_images` | Bis zu 7 Referenzbilder. Jedes Bild muss mindestens 300x300 Pixel groß sein und ein Seitenverhältnis zwischen 1:2.5 und 2.5:1 haben. | IMAGE | Ja | 1 bis 7 Bilder |
| `resolution` | Die Ausgabeauflösung des Videos (Standard: `"1080p"`). | COMBO | Nein | `"4k"`<br>`"1080p"`<br>`"720p"` |
| `storyboards` | Eine Reihe von Videosegmenten mit individuellen Prompts und Dauern generieren. Wird nur für `kling-v3-omni` unterstützt. Wenn aktiviert, wird der globale `prompt` ignoriert, und die Gesamtdauer aller Storyboard-Segmente muss der globalen `duration` entsprechen (Standard: `"disabled"`). | DYNAMIC_COMBO | Nein | `"disabled"`<br>`"1 storyboard"`<br>`"2 storyboards"`<br>`"3 storyboards"`<br>`"4 storyboards"`<br>`"5 storyboards"`<br>`"6 storyboards"` |
| `generate_audio` | Audio für das Video generieren. Wird nur für `kling-v3-omni` unterstützt (Standard: false). | BOOLEAN | Nein | `true`<br>`false` |
| `seed` | Der Seed steuert, ob der Node erneut ausgeführt werden soll; die Ergebnisse sind unabhängig vom Seed nicht deterministisch (Standard: 0). | INT | Nein | 0 bis 2147483647 |

### Storyboard-Eingaben

Wenn `storyboards` aktiviert ist, erscheinen die folgenden Eingaben für jedes ausgewählte Storyboard-Segment. N reicht von 1 bis zur ausgewählten Anzahl an Storyboards.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `storyboard_N_prompt` | Prompt für Storyboard-Segment N. Max. 512 Zeichen. | STRING | Ja | 1 bis 512 Zeichen |
| `storyboard_N_duration` | Dauer für Storyboard-Segment N in Sekunden (Standard: 4). | INT | Ja | 1 bis 15 |

**Hinweis:** Die Eingabe `reference_images` akzeptiert maximal 7 Bilder. Wenn mehr bereitgestellt werden, löst der Node einen Fehler aus. Jedes Bild wird auf Mindestabmessungen (300x300 Pixel) und Seitenverhältnis (zwischen 1:2.5 und 2.5:1) validiert.

**Modellspezifische Einschränkungen:**
- `kling-video-o1` unterstützt keine Dauern größer als 10 Sekunden.
- `kling-video-o1` unterstützt keine Audiogenerierung.
- `kling-video-o1` unterstützt keine 4k-Auflösung.
- `kling-video-o1` unterstützt keine Storyboards.

**Storyboard-Einschränkung:** Die Gesamtdauer aller Storyboard-Segmente muss dem globalen Wert `duration` entsprechen. Wenn die Summe nicht übereinstimmt, löst der Node einen Fehler aus.

## Ausgaben

| Ausgabenamen | Beschreibung | Datentyp |
|--------------|--------------|----------|
| `output` | Die generierte Videodatei. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingOmniProImageToVideoNode/de.md)

---
**Source fingerprint (SHA-256):** `ccf7881065d2a365cdaa0e164b8b1d46c67985067866ab0fe91d492a62015f07`
