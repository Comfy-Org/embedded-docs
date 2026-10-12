# KlingCameraControlI2VNode

Der Kling Image to Video Camera Control Node verwandelt Standbilder in filmische Videos mit professionellen Kamerabewegungen. Dieser spezialisierte Image-to-Video-Node ermöglicht die Steuerung virtueller Kameraktionen wie Zoom, Rotation, Schwenk, Neigung und First-Person-Ansicht, während der Fokus auf Ihrem Originalbild erhalten bleibt. Die Kamerasteuerung wird derzeit nur im Pro-Modus mit dem Modell kling-v1-5 bei einer Dauer von 5 Sekunden unterstützt.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `start_frame` | Referenzbild – URL oder Base64-kodierte Zeichenkette, darf 10 MB nicht überschreiten, Auflösung nicht unter 300x300px, Seitenverhältnis zwischen 1:2.5 und 2.5:1. Base64 darf nicht das Präfix data:image enthalten. | IMAGE | Ja | - |
| `prompt` | Positiver Text-Prompt, der den gewünschten Videoinhalt beschreibt. Maximale Länge: 500 Zeichen. | STRING | Ja | - |
| `negative_prompt` | Negativer Text-Prompt, der beschreibt, was im generierten Video vermieden werden soll. Maximale Länge: 500 Zeichen. | STRING | Ja | - |
| `cfg_scale` | Steuert die Stärke der Textführung. Höhere Werte führen dazu, dass die Ausgabe dem Prompt genauer folgt (Standard: 0.75) | FLOAT | Nein | 0.0 bis 1.0 |
| `aspect_ratio` | Das Seitenverhältnis des generierten Videos (Standard: "16:9") | COMBO | Nein | `"16:9"`<br>`"9:16"`<br>`"1:1"` |
| `camera_control` | Kann mit dem Kling Camera Controls Node erstellt werden. Steuert die Kamerabewegung und die Bewegung während der Videogenerierung. | CAMERA_CONTROL | Ja | - |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `output` | Die generierte Videoausgabe | VIDEO |
| `video_id` | Eindeutige Kennung für das generierte Video | STRING |
| `duration` | Dauer des generierten Videos | STRING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingCameraControlI2VNode/de.md)

---
**Source fingerprint (SHA-256):** `65b1e4a46c2de1558c8f27ebe031f1736e84d532908170c91fb70121c350347e`
