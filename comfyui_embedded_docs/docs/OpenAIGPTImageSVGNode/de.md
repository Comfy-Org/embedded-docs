# OpenAI GPT Image 2.6 SVG

## Übersicht

OpenAI GPT Image 2.6 SVG erzeugt aus einem Prompt mit den GPT-Image-Modellen von OpenAI eine editierbare SVG-Datei. Das Ergebnis ist Vektor-Markup, sodass Formen und Text in einem Vektor-Editor editierbar bleiben. Es sind zwei Modelle verfügbar: `gpt-image-2.6-flare` und `gpt-image-2.6-sunburst`.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model` | Das GPT-Image-Modell, das für die SVG verwendet wird. | DYNAMIC_COMBO | Ja | `"gpt-image-2.6-flare"`<br>`"gpt-image-2.6-sunburst"` |

### gpt-image-2.6-flare und gpt-image-2.6-sunburst Eingaben

Beide Modelle verwenden dieselben Parameter.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model.prompt` | Beschreibung der zu zeichnenden SVG. (Standard: `""`) | STRING | Ja | N/A |
| `model.size` | Größe des Referenzbildes, aus dem die SVG gezeichnet wird. (Standard: `"1024x1024"`) | COMBO | Ja | `"1024x1024"`<br>`"1024x1536"`<br>`"1536x1024"` |
| `model.background` | Hintergrund des Referenzbildes. (Standard: `"auto"`) | COMBO | Ja | `"auto"`<br>`"opaque"`<br>`"transparent"` |
| `model.quality` | Qualität des Referenzbildes, aus dem die SVG gezeichnet wird. (Standard: `"low"`) | COMBO | Ja | `"low"`<br>`"medium"`<br>`"high"`<br>`"xhigh"`<br>`"max"` |
| `model.complexity` | Wie stark das Modell das Referenzbild vor dem Rendern plant. (Standard: `"high"`) | COMBO | Ja | `"low"`<br>`"medium"`<br>`"high"` |
| `model.seed` | Steuert, ob der Node erneut ausgeführt wird; die Ergebnisse sind unabhängig vom Seed nicht deterministisch. (Standard: `42`) | INT | Ja | 0 bis 2147483647 |

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `svg` | Das erzeugte Vektorbild als SVG-Markup. | SVG |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIGPTImageSVGNode/de.md)

---
**Source fingerprint (SHA-256):** `8ac2f473b265d3b6857e6280a1c017301b124fc6d671ec83a59c677218062c90`
