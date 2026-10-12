# Veo3VideoGenerationNode

Erzeugt Videos aus Text-Prompts mithilfe der Veo-3-API von Google. Dieser Node unterstützt mehrere Veo-3-Modelle, einschließlich Fast- und Lite-Varianten, und ermöglicht die Angabe von Videoauflösung, Dauer und Audioerzeugung.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Textbeschreibung des Videos (Standard: "") | STRING | Ja | - |
| `aspect_ratio` | Seitenverhältnis des Ausgabevideos (Standard: "16:9") | COMBO | Ja | "16:9"<br>"9:16" |
| `resolution` | Auflösung des Ausgabevideos. 4K ist für das Modell veo-3.1-lite nicht verfügbar. (Standard: "720p") | COMBO | Nein | "720p"<br>"1080p"<br>"4k" |
| `negative_prompt` | Negativer Text-Prompt zur Steuerung, was im Video vermieden werden soll (Standard: "") | STRING | Nein | - |
| `duration_seconds` | Dauer des Ausgabevideos in Sekunden (Standard: 8) | INT | Nein | 4 - 8 (step 2) |
| `enhance_prompt` | Dieser Parameter ist veraltet und wird ignoriert. (Standard: True) | BOOLEAN | Nein | - |
| `person_generation` | Ob die Erzeugung von Personen im Video erlaubt werden soll (Standard: "ALLOW") | COMBO | Nein | "ALLOW"<br>"BLOCK" |
| `seed` | Seed für die Videoerzeugung (0 für zufällig) (Standard: 0) | INT | Nein | 0 - 4294967295 |
| `image` | Optionales Referenzbild zur Steuerung der Videoerzeugung | IMAGE | Nein | - |
| `model` | Zu verwendendes Veo-3-Modell für die Videoerzeugung (Standard: "veo-3.1-generate") | COMBO | Nein | "veo-3.1-generate"<br>"veo-3.1-fast-generate"<br>"veo-3.1-lite" |
| `generate_audio` | Audio für das Video erzeugen. Wird von allen Veo-3-Modellen unterstützt. (Standard: False) | BOOLEAN | Nein | - |

**Hinweis:** Der Parameter `enhance_prompt` ist veraltet und sein Wert wird ignoriert. Der Node verbessert den Prompt immer intern. Wenn Sie die Auflösung "4k" mit dem Modell veo-3.1-lite auswählen, löst der Node einen Fehler aus.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `output` | Die erzeugte Videodatei | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Veo3VideoGenerationNode/de.md)

---
**Source fingerprint (SHA-256):** `5320736448ad854e2f93e08ccaa870e977e06497666cb305f314bc76ff917740`
