# KlingCameraControlT2VNode

Der Kling Text to Video Camera Control Node wandelt Text in filmische Videos mit professionellen Kamerabewegungen um, die reale Kinematografie simulieren. Dieser Node unterstützt die Steuerung virtueller Kameraaktionen wie Zoom, Rotation, Schwenken, Neigen und Ego-Perspektive, wobei der Fokus auf Ihrem ursprünglichen Text erhalten bleibt. Dauer, Modus und Modellname sind fest vorgegeben, da die Kamerasteuerung nur im Pro-Modus mit dem kling-v1-5-Modell bei 5-Sekunden-Dauer unterstützt wird.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `prompt` | Positiver Text-Prompt | STRING | Ja | - |
| `negative_prompt` | Negativer Text-Prompt | STRING | Ja | - |
| `cfg_scale` | Steuert, wie genau die Ausgabe dem Prompt folgt (Standard: 0.75) | FLOAT | Nein | 0.0-1.0 |
| `aspect_ratio` | Das Seitenverhältnis für das generierte Video (Standard: "16:9") | COMBO | Nein | "16:9"<br>"9:16"<br>"1:1"<br>"21:9"<br>"3:4"<br>"4:3" |
| `camera_control` | Kann mit dem Kling Camera Controls Node erstellt werden. Steuert die Kamerabewegung und Bewegung während der Videogenerierung. | CAMERA_CONTROL | Nein | - |

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|--------------|--------------|----------|
| `output` | Das generierte Video mit Kamerasteuerungseffekten | VIDEO |
| `video_id` | Die eindeutige Kennung für das generierte Video | STRING |
| `duration` | Die Dauer des generierten Videos | STRING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingCameraControlT2VNode/de.md)

---
**Source fingerprint (SHA-256):** `7975d97c4f9242a9ae3c17be03696d174a2495bd53fb9fc4405f86c44167fa21`
