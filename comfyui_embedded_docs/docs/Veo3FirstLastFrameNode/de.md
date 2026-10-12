# Google Veo 3 Erstes und letztes Frame zu Video

Der Veo3FirstLastFrameNode verwendet das Veo 3-Modell von Google, um anhand eines Text-Prompts ein Video zu generieren, wobei ein bereitgestelltes erstes und letztes Frame den Anfang und das Ende der Videosequenz definieren.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Textbeschreibung des Videos (Standard: leerer String). | STRING | Ja | N/A |
| `negative_prompt` | Negativer Text-Prompt, um anzugeben, was im Video vermieden werden soll (Standard: leerer String). | STRING | Nein | N/A |
| `resolution` | Die Auflösung des Ausgabevideos. | COMBO | Ja | `"720p"`<br>`"1080p"`<br>`"4k"` |
| `aspect_ratio` | Seitenverhältnis des Ausgabevideos (Standard: "16:9"). | COMBO | Nein | `"16:9"`<br>`"9:16"` |
| `duration` | Dauer des Ausgabevideos in Sekunden (Standard: 8, Schrittweite: 2). | INT | Nein | 4 bis 8 |
| `seed` | Seed für die Videogenerierung (Standard: 0). | INT | Nein | 0 bis 4294967295 |
| `first_frame` | Das Startframe für das Video. | IMAGE | Ja | N/A |
| `last_frame` | Das Endframe für das Video. | IMAGE | Ja | N/A |
| `model` | Das spezifische Veo-Modell, das für die Generierung verwendet werden soll (Standard: "veo-3.1-generate"). | COMBO | Nein | `"veo-3.1-generate"`<br>`"veo-3.1-fast-generate"`<br>`"veo-3.1-lite"` |
| `generate_audio` | Audio für das Video generieren (Standard: True). | BOOLEAN | Nein | N/A |

**Hinweis:** Das Modell `veo-3.1-lite` unterstützt keine 4K-Auflösung. Wenn Sie `veo-3.1-lite` und die Auflösung `4k` auswählen, tritt ein Fehler auf.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `output` | Die generierte Videodatei. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Veo3FirstLastFrameNode/de.md)

---
**Source fingerprint (SHA-256):** `2fe55d2a1d018e58fd290c901c596708898acda835d2358adf36ed80103aeb6e`
