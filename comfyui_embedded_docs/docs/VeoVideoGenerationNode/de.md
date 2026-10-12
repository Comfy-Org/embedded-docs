# VeoVideoGenerationNode

Erzeugt Videos aus Text-Prompts mithilfe der Google Veo API. Dieser Node kann Videos aus Textbeschreibungen und optionalen Bildeingaben erstellen, mit Kontrolle über Parameter wie Seitenverhältnis, Dauer und mehr.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Textbeschreibung des Videos (Standard: leer) | STRING | Ja | - |
| `aspect_ratio` | Seitenverhältnis des Ausgabevideos (Standard: "16:9") | COMBO | Ja | "16:9"<br>"9:16" |
| `negative_prompt` | Negativer Text-Prompt, der angibt, was im Video vermieden werden soll (Standard: leer) | STRING | Nein | - |
| `duration_seconds` | Dauer des Ausgabevideos in Sekunden (Standard: 5) | INT | Nein | 5-8 |
| `enhance_prompt` | Gibt an, ob der Prompt mit KI-Unterstützung verbessert werden soll (Standard: True). Dies ist ein erweiterter Parameter. | BOOLEAN | Nein | - |
| `person_generation` | Gibt an, ob die Generierung von Personen im Video erlaubt werden soll (Standard: "ALLOW"). Dies ist ein erweiterter Parameter. | COMBO | Nein | "ALLOW"<br>"BLOCK" |
| `seed` | Seed für die Videogenerierung (0 für zufällig) (Standard: 0). Dies ist ein erweiterter Parameter. | INT | Nein | 0-4294967295 |
| `image` | Optionales Referenzbild zur Steuerung der Videogenerierung | IMAGE | Nein | - |
| `model` | Veo-Modell zur Videogenerierung (Standard: "veo-2.0-generate-001") | COMBO | Nein | "veo-2.0-generate-001"<br>"veo-3.1-generate"<br>"veo-3.1-fast-generate"<br>"veo-3.1-lite"<br>"veo-3.0-generate-001"<br>"veo-3.0-fast-generate-001" |

**Hinweis:** Der Parameter `generate_audio` ist nur für Veo 3.0- und Veo 3.1-Modelle verfügbar und wird vom Node automatisch basierend auf dem ausgewählten Modell verwaltet. Bei Verwendung von Veo 3.0- oder Veo 3.1-Modellen wird der Parameter `enhance_prompt` auf True gesetzt.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `output` | Die generierte Videodatei | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VeoVideoGenerationNode/de.md)

---
**Source fingerprint (SHA-256):** `055569f26c7e8f074371239f12f307ca86ce2aa5fd17ca55dd951b34f71fa559`
