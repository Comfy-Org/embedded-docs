# Wan Text zu Video

Der Node „Wan Text to Video“ generiert Videoinhalte anhand von Textbeschreibungen. Er verwendet KI-Modelle, um Videos aus Prompts zu erstellen, und unterstützt verschiedene Videogrößen, Dauern und optionale Audioeingaben. Der Node kann bei Bedarf automatisch Audio generieren und bietet Optionen zur Prompt-Verbesserung und zum Hinzufügen von Wasserzeichen.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model` | Zu verwendendes Modell (Standard: "wan2.6-t2v") | COMBO | Ja | "wan2.5-t2v-preview"<br>"wan2.6-t2v" |
| `prompt` | Prompt, der die Elemente und visuellen Merkmale beschreibt. Unterstützt Englisch und Chinesisch (Standard: "") | STRING | Ja | - |
| `negative_prompt` | Negativer Prompt, der beschreibt, was vermieden werden soll (Standard: "") | STRING | Nein | - |
| `size` | Videoauflösung und Seitenverhältnis (Standard: "720p: 1:1 (960x960)") | COMBO | Nein | "480p: 1:1 (624x624)"<br>"480p: 16:9 (832x480)"<br>"480p: 9:16 (480x832)"<br>"720p: 1:1 (960x960)"<br>"720p: 16:9 (1280x720)"<br>"720p: 9:16 (720x1280)"<br>"720p: 4:3 (1088x832)"<br>"720p: 3:4 (832x1088)"<br>"1080p: 1:1 (1440x1440)"<br>"1080p: 16:9 (1920x1080)"<br>"1080p: 9:16 (1080x1920)"<br>"1080p: 4:3 (1632x1248)"<br>"1080p: 3:4 (1248x1632)" |
| `duration` | Dauer des Videos in Sekunden. Eine Dauer von 15 Sekunden ist nur für das Wan 2.6-Modell verfügbar (Standard: 5) | INT | Nein | 5-15 (in Schritten von 5) |
| `audio` | Audio muss eine klare, laute Stimme enthalten, ohne störende Geräusche oder Hintergrundmusik | AUDIO | Nein | - |
| `seed` | Für die Generierung zu verwendender Seed (Standard: 0) | INT | Nein | 0-2147483647 |
| `generate_audio` | Wenn keine Audioeingabe bereitgestellt wird, Audio automatisch generieren (Standard: False) | BOOLEAN | Nein | - |
| `prompt_extend` | Ob der Prompt mit KI-Unterstützung verbessert werden soll (Standard: True) | BOOLEAN | Nein | - |
| `watermark` | Ob dem Ergebnis ein KI-generiertes Wasserzeichen hinzugefügt werden soll (Standard: False) | BOOLEAN | Nein | - |
| `shot_type` | Gibt den Aufnahmetyp für das generierte Video an, d. h., ob das Video eine einzelne durchgehende Aufnahme oder mehrere Aufnahmen mit Schnitten ist. Dieser Parameter wird nur wirksam, wenn prompt_extend True ist (Standard: "single") | COMBO | Nein | "single"<br>"multi" |

**Hinweis:** Das Wan 2.6-Modell unterstützt keine 480p-Auflösungen. Eine Dauer von 15 Sekunden wird nur vom Wan 2.6-Modell unterstützt. Wenn eine Audioeingabe bereitgestellt wird, muss sie zwischen 3,0 und 29,0 Sekunden lang sein und eine klare Stimme ohne Hintergrundgeräusche oder Musik enthalten.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `output` | Das generierte Video basierend auf den Eingabeparametern | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanTextToVideoApi/de.md)

---
**Source fingerprint (SHA-256):** `105ff4b575dc6cd319448b0f4c0e9cfab360df025480190ae6bccc324d351525`
