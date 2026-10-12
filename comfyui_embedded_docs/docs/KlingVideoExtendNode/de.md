# KlingVideoExtendNode

Der Kling Video Extend Node ermöglicht die Erweiterung von Videos, die von anderen Kling-Nodes erstellt wurden. Er nimmt ein vorhandenes Video anhand seiner Video-ID und generiert zusätzlichen Inhalt basierend auf Ihren Text-Prompts. Der Node funktioniert, indem er Ihre Erweiterungsanfrage an die Kling API sendet und das erweiterte Video zusammen mit seiner neuen ID und Dauer zurückgibt.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Positiver Text-Prompt zur Steuerung der Videoerweiterung | STRING | Nein | - |
| `negative_prompt` | Negativer Text-Prompt für Elemente, die im erweiterten Video vermieden werden sollen | STRING | Nein | - |
| `cfg_scale` | Steuert die Stärke der Prompt-Führung (Standard: 0.5) | FLOAT | Nein | 0.0 - 1.0 |
| `video_id` | Die ID des zu erweiternden Videos. Unterstützt Videos, die durch Text-zu-Video-, Bild-zu-Video- und vorherige Videoerweiterungsvorgänge generiert wurden. Die Gesamtdauer nach der Erweiterung darf 3 Minuten nicht überschreiten. | STRING | Ja | - |

**Hinweis:** Die `video_id` muss auf ein Video verweisen, das von anderen Kling-Nodes erstellt wurde, und die Gesamtdauer nach der Erweiterung darf 3 Minuten nicht überschreiten. Der positive Prompt darf nicht leer sein, und beide Prompts müssen unter 2500 Zeichen liegen.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `output` | Das von der Kling API generierte erweiterte Video | VIDEO |
| `video_id` | Der eindeutige Bezeichner für das erweiterte Video | STRING |
| `duration` | Die Dauer des erweiterten Videos | STRING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingVideoExtendNode/de.md)

---
**Source fingerprint (SHA-256):** `56674dee721a1784138852f5fd1cce137acf0b5e09bd9ee17353dde6fb251b5e`
