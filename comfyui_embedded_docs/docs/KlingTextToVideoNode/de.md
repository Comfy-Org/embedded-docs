# Kling Text zu Video

Der Node „Kling Text to Video“ generiert Videos aus Textbeschreibungen mithilfe der Kling-Videogenerierungs-API. Er sendet den Prompt und die Einstellungen (Seitenverhältnis, Generierungsmodus und CFG-Skalierung) an die API, wartet, bis die Generierungsaufgabe abgeschlossen ist, und gibt dann das resultierende Video zusammen mit seiner ID und Dauer zurück.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Positiver Text-Prompt | STRING | Ja | Maximal 2500 Zeichen |
| `negative_prompt` | Negativer Text-Prompt | STRING | Nein | Maximal 2500 Zeichen |
| `cfg_scale` | Konfigurationsskalierungswert, der steuert, wie eng das Video dem Prompt folgt (Standard: 1.0) | FLOAT | Nein | 0.0 bis 1.0 |
| `aspect_ratio` | Einstellung des Seitenverhältnisses des Videos (Standard: "16:9") | COMBO | Nein | "16:9"<br>"9:16"<br>"1:1" |
| `mode` | Die für die Videogenerierung zu verwendende Konfiguration im Format: mode / duration / model_name (Standard: "pro mode / 5s duration / kling-v2-5-turbo") | COMBO | Nein | "pro mode / 5s duration / kling-v2-5-turbo"<br>"pro mode / 10s duration / kling-v2-5-turbo" |

Hinweis: Der Parameter `prompt` ist erforderlich und darf nicht leer sein. Sowohl `prompt` als auch `negative_prompt` sind auf maximal 2500 Zeichen begrenzt. Die 10-Sekunden-Option von `mode` kostet mehr als die 5-Sekunden-Option.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `output` | Die generierte Videoausgabe | VIDEO |
| `video_id` | Eindeutiger Bezeichner für das generierte Video | STRING |
| `duration` | Dauerinformationen für das generierte Video | STRING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingTextToVideoNode/de.md)

---
**Source fingerprint (SHA-256):** `6a63b0b8bc45dc5a6300cdfe7a373399eeead36de6727f7aae2c026ba0deaea8`
