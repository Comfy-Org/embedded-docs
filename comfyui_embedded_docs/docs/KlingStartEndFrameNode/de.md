# KlingStartEndFrameNode

Dieser Node erstellt eine Videosequenz, die zwischen Ihren bereitgestellten Start- und Endbildern übergeht. Er erzeugt alle dazwischenliegenden Frames, um eine sanfte Transformation vom ersten zum letzten Frame zu erzeugen. Dieser Node ruft die Bild-zu-Video-API auf, unterstützt jedoch nur die Eingabeoptionen, die mit dem `image_tail`-Anfragefeld funktionieren.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `start_frame` | Referenzbild – URL- oder Base64-kodierte Zeichenkette, darf 10 MB nicht überschreiten, Auflösung nicht unter 300*300px, Seitenverhältnis zwischen 1:2.5 ~ 2.5:1. Base64 sollte das Präfix data:image nicht enthalten. | IMAGE | Ja | - |
| `end_frame` | Referenzbild – Endframe-Steuerung. URL- oder Base64-kodierte Zeichenkette, darf 10 MB nicht überschreiten, Auflösung nicht unter 300*300px. Base64 sollte das Präfix data:image nicht enthalten. | IMAGE | Ja | - |
| `prompt` | Positiver Text-Prompt. Darf nicht leer sein und darf 500 Zeichen nicht überschreiten. | STRING | Ja | - |
| `negative_prompt` | Negativer Text-Prompt. Darf 500 Zeichen nicht überschreiten. Wenn leer gelassen, wird er aus der Anfrage weggelassen. | STRING | Ja | - |
| `cfg_scale` | Steuert die Stärke der Prompt-Führung (Standard: 0.5). | FLOAT | Ja | 0.0-1.0 |
| `aspect_ratio` | Das Seitenverhältnis für das generierte Video (Standard: "16:9"). | COMBO | Ja | "16:9"<br>"9:16"<br>"1:1" |
| `mode` | Die Konfiguration, die für die Videoerzeugung verwendet werden soll, im Format: mode / duration / model_name. (Standard: "pro mode / 5s duration / kling-v2-5-turbo") | COMBO | Ja | "pro mode / 5s duration / kling-v2-5-turbo"<br>"pro mode / 10s duration / kling-v2-5-turbo" |

**Bildbeschränkungen:**

- Sowohl `start_frame` als auch `end_frame` sind erforderlich und dürfen eine Dateigröße von 10 MB nicht überschreiten.
- Minimale Auflösung: 300×300 Pixel für beide Bilder.
- Das Seitenverhältnis von `start_frame` muss zwischen 1:2.5 und 2.5:1 liegen.
- Base64-kodierte Bilder sollten das Präfix "data:image" nicht enthalten.

**Prompt-Beschränkungen:**

- `prompt` darf nicht leer sein und darf 500 Zeichen nicht überschreiten.
- `negative_prompt` darf 500 Zeichen nicht überschreiten; wenn leer, wird er nicht mit der Anfrage gesendet.

**Hinweise zum Modus:**

- Beide Modusoptionen verwenden den Pro-Modus mit dem Modell kling-v2-5-turbo und unterscheiden sich nur in der Dauer (5 Sekunden oder 10 Sekunden).
- Preis pro Generierung, wie im Preis-Badge des Nodes angezeigt: Der 5s-Modus kostet 0,35 USD und der 10s-Modus kostet 0,70 USD.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `output` | Die generierte Videosequenz. | VIDEO |
| `video_id` | Eindeutige Kennung für das generierte Video. | STRING |
| `duration` | Dauer des generierten Videos. | STRING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingStartEndFrameNode/de.md)

---
**Source fingerprint (SHA-256):** `a27977226360a425614255f8330ce7fd8ba94b8c3020eb8fdddc01eb74f035c1`
