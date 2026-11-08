# OpenAI GPT Image 2.6 GIF

## Überblick

OpenAI GPT Image 2.6 GIF erzeugt aus einem Prompt mit den GPT Image-Modellen von OpenAI eine animierte GIF-Datei und gibt sie als Frame-Batch zusammen mit der Bildrate zurück, sodass sie direkt in einen Video- oder Animationsbild-Speicherknoten übergeben werden kann. Zwei Modelle stehen zur Verfügung: `gpt-image-2.6-flare` und `gpt-image-2.6-sunburst`.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Range |
| --- | --- | --- | --- | --- |
| `model` | Das GPT Image-Modell, das für die Animation verwendet werden soll. | DYNAMIC_COMBO | Ja | `"gpt-image-2.6-flare"`<br>`"gpt-image-2.6-sunburst"` |

### gpt-image-2.6-flare und gpt-image-2.6-sunburst Eingaben

Beide Modelle verwenden dieselben Parameter.

| Parameter | Beschreibung | Datentyp | Erforderlich | Range |
| --- | --- | --- | --- | --- |
| `model.prompt` | Was animiert werden soll. (Standard: `""`) | STRING | Ja | N/A |
| `model.size` | Größe jedes Frames. Größere Größen lassen nur niedrigere Frame-Anzahlen zu. (Standard: `"512x512"`) | COMBO | Ja | `"384x384"`<br>`"512x512"`<br>`"640x640"`<br>`"720x720"`<br>`"768x768"`<br>`"960x960"`<br>`"512x288"`<br>`"288x512"`<br>`"1024x576"`<br>`"576x1024"`<br>`"1280x720"`<br>`"720x1280"` |
| `model.frame_count` | Anzahl der Frames. Frames werden in Stufen abgerechnet: 2 bis 8, 9, 10 bis 12, 13 bis 16. (Standard: `9`) | INT | Ja | 2 bis 16 |
| `model.frame_duration_ms` | Wie lange jeder Frame angezeigt wird, in Millisekunden. (Standard: `200`) | INT | Ja | 20 bis 2000 (Schritt: 10) |
| `model.background` | Frame-Hintergrund. Transparenz wird von Save WEBM mit vp9, Save Animated WEBP und Save Animated PNG beibehalten. (Standard: `"opaque"`) | COMBO | Ja | `"opaque"`<br>`"transparent"` |
| `model.quality` | Bildqualität. Höhere Stufen kosten mehr und dauern länger. (Standard: `"low"`) | COMBO | Ja | `"low"`<br>`"medium"`<br>`"high"`<br>`"xhigh"`<br>`"max"` |
| `model.complexity` | Wie stark das Modell die Animation vor dem Rendern plant. (Standard: `"high"`) | COMBO | Ja | `"low"`<br>`"medium"`<br>`"high"` |
| `model.seed` | Steuert, ob der Knoten erneut ausgeführt wird; die Ergebnisse sind unabhängig vom Seed nicht deterministisch. (Standard: `42`) | INT | Ja | 0 bis 2147483647 |

**Parametereinschränkungen und -beschränkungen:**

- Die Bildrate wird aus `model.frame_duration_ms` berechnet: 200 ms ergeben 5 fps.
- Eine große `model.size` in Kombination mit einer hohen `model.frame_count` ist nicht verfügbar und zeigt „Size too large for this frame count“ auf dem Preisabzeichen an.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `frames` | Die Animation als Batch von Frames, bereit für einen Video- oder Animationsbild-Speicherknoten. | IMAGE |
| `fps` | Frames pro Sekunde, aus der Frame-Dauer der zurückgegebenen GIF-Datei ausgelesen. | FLOAT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIGPTImageGIFNode/de.md)

---
**Source fingerprint (SHA-256):** `e47ebaef90f8b2618ef3c2659778f75ac9763013dcc515ba5650764ce49da951`
