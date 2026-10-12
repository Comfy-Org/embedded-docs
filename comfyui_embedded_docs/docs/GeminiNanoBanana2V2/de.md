# GeminiNanoBanana2V2

Dieser Node generiert oder bearbeitet Bilder, indem er einen Text-Prompt über Gemini-Bildmodelle an die Vertex AI API von Google sendet. Er erstellt neue Bilder aus einer Beschreibung oder modifiziert vorhandene Bilder mithilfe optionaler Referenzbilder.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model` | Wählt das zu verwendende Gemini-Bildmodell aus. Das gewählte Modell bestimmt die verfügbaren Auflösungsoptionen und modellspezifischen Eingaben. | DYNAMIC_COMBO | Ja | `"Gemini Nano Banana 2.1"`<br>`"Nano Banana 2 (Gemini 3.1 Flash Image)"`<br>`"Nano Banana 2 Lite"` |
| `prompt` | Text-Prompt, der das zu generierende Bild oder die anzuwendenden Bearbeitungen beschreibt. Fügen Sie alle Einschränkungen, Stile oder Details hinzu, die das Modell befolgen soll. Darf nicht leer sein. (Standard: leer) | STRING | Ja | N/A |
| `seed` | Wenn der Seed auf einen bestimmten Wert festgelegt ist, bemüht sich das Modell, bei wiederholten Anfragen die gleiche Antwort zu liefern. Eine deterministische Ausgabe ist nicht garantiert. Außerdem können Änderungen am Modell oder an Parametereinstellungen wie der Temperatur zu Abweichungen in der Antwort führen, selbst wenn derselbe Seed-Wert verwendet wird. Standardmäßig wird ein zufälliger Seed-Wert verwendet. (Standard: 42) | INT | Ja | 0 bis 18446744073709551615 |
| `response_modalities` | Bestimmt das Antwortformat. IMAGE gibt nur ein Bild zurück; IMAGE+TEXT gibt ein Bild und eine Textantwort zurück. (Standard: IMAGE) Erweiterter Parameter. | COMBO | Ja | `"IMAGE"`<br>`"IMAGE+TEXT"` |
| `system_prompt` | Grundlegende Anweisungen, die das Verhalten einer KI vorgeben. Standardmäßig wird ein integrierter Prompt verwendet, der das Modell anweist, immer ein Bild zu erzeugen. Erweiterter Parameter. | STRING | Nein | N/A |
| `temperature` | Steuert die Zufälligkeit bei der Generierung. Niedrigere Werte sind fokussierter/deterministischer. (Standard: 1.0) Erweiterter Parameter. | FLOAT | Nein | 0.0 bis 2.0 (Schrittweite 0.01) |
| `top_p` | Schwellenwert für Nucleus-Sampling. Niedrigere Werte sind fokussierter, höhere vielfältiger. (Standard: 0.95) Erweiterter Parameter. | FLOAT | Nein | 0.0 bis 1.0 (Schrittweite 0.01) |

### Gemini Nano Banana 2.1 Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `aspect_ratio` | Wenn auf 'auto' gesetzt, wird das Seitenverhältnis Ihres Eingabebilds übernommen; wenn kein Bild bereitgestellt wird, wird üblicherweise ein 16:9-Format erzeugt. (Standard: auto) | COMBO | Ja | `"auto"`<br>`"1:1"`<br>`"2:3"`<br>`"3:2"`<br>`"3:4"`<br>`"4:3"`<br>`"4:5"`<br>`"5:4"`<br>`"9:16"`<br>`"16:9"`<br>`"21:9"`<br>`"1:4"`<br>`"4:1"`<br>`"8:1"`<br>`"1:8"` |
| `resolution` | Zielauflösung der Ausgabe. | COMBO | Ja | `"1K"`<br>`"2K"`<br>`"4K"` |
| `thinking_level` | Wählt die vom Modell verwendete Denkstufe aus. | COMBO | Ja | `"MINIMAL"`<br>`"MEDIUM"`<br>`"HIGH"` |

### Nano Banana 2 (Gemini 3.1 Flash Image) Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `aspect_ratio` | Wenn auf 'auto' gesetzt, wird das Seitenverhältnis Ihres Eingabebilds übernommen; wenn kein Bild bereitgestellt wird, wird üblicherweise ein 16:9-Format erzeugt. (Standard: auto) | COMBO | Ja | `"auto"`<br>`"1:1"`<br>`"2:3"`<br>`"3:2"`<br>`"3:4"`<br>`"4:3"`<br>`"4:5"`<br>`"5:4"`<br>`"9:16"`<br>`"16:9"`<br>`"21:9"`<br>`"1:4"`<br>`"4:1"`<br>`"8:1"`<br>`"1:8"` |
| `resolution` | Zielauflösung der Ausgabe. | COMBO | Ja | `"1K"`<br>`"2K"`<br>`"4K"` |
| `thinking_level` | Wählt die vom Modell verwendete Denkstufe aus. | COMBO | Ja | `"MINIMAL"`<br>`"HIGH"` |

### Nano Banana 2 Lite Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `aspect_ratio` | Wenn auf 'auto' gesetzt, wird das Seitenverhältnis Ihres Eingabebilds übernommen; wenn kein Bild bereitgestellt wird, wird üblicherweise ein 16:9-Format erzeugt. (Standard: auto) | COMBO | Ja | `"auto"`<br>`"1:1"`<br>`"2:3"`<br>`"3:2"`<br>`"3:4"`<br>`"4:3"`<br>`"4:5"`<br>`"5:4"`<br>`"9:16"`<br>`"16:9"`<br>`"21:9"`<br>`"1:4"`<br>`"4:1"`<br>`"8:1"`<br>`"1:8"` |
| `resolution` | Zielauflösung der Ausgabe. | COMBO | Ja | `"1K"` |
| `thinking_level` | Wählt die vom Modell verwendete Denkstufe aus. | COMBO | Ja | `"MINIMAL"`<br>`"HIGH"` |

### Referenzeingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `images` | Optionale(s) Referenzbild(er). Insgesamt bis zu 14 Bilder. Erweiterbarer Slot: Verbinden Sie `image_1` bis `image_14`. | IMAGE | Nein | 0 bis 14 Bilder |
| `files` | Optionale Datei(en), die als Kontext für das Modell verwendet werden. Akzeptiert Eingaben vom Node Gemini Generate Content Input Files. | GEMINI_INPUT_FILES | Nein | N/A |

**Hinweis:** Es können maximal 14 Referenzbilder an den Eingang `images` angeschlossen werden; wird dieses Limit überschritten, wird ein Fehler ausgelöst.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `IMAGE` | Das generierte oder bearbeitete Bild. | IMAGE |
| `STRING` | Eine vom Modell generierte Textbeschreibung oder Bildunterschrift. Leer, wenn kein Text zurückgegeben wird, z. B. wenn `response_modalities` auf `IMAGE` gesetzt ist. | STRING |
| `thought_image` | Erstes Bild aus dem Denkprozess des Modells. Nur bei der Modalität IMAGE+TEXT verfügbar. | IMAGE |

**Hinweis:** Die Ausgabe `STRING` ist leer, wenn `response_modalities` auf `IMAGE` gesetzt ist. Wenn das Modell in diesem Modus kein Bild generiert, löst der Node einen Fehler aus und schlägt vor, zu IMAGE+TEXT zu wechseln, um die Denkweise des Modells anzuzeigen.

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiNanoBanana2V2/de.md)

---
**Source fingerprint (SHA-256):** `238d661259e99fd0ce8cae227d873713bbad60aa5eccb32447be464317e39ddd`
