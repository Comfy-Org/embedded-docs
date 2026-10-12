# PreviewPointCloud

Der Node Preview Point Cloud ermöglicht es Ihnen, eine 3D-Punktwolkendatei in der ComfyUI-Oberfläche anzuzeigen, ohne sie im ComfyUI-Ausgabeverzeichnis zu speichern. Er speichert die Punktwolke an einem temporären Speicherort und zeigt sie in einem 3D-Vorschaufenster an; gleichzeitig reicht er die Modelldaten, Modellinformationen, Kamerainformationen und Vorschauabmessungen für die weitere Verarbeitung weiter.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model_3d` | Punktwolkendatei (.ply) | FILE3D | Ja | - |
| `model_3d_info` | Informationen über das 3D-Modell | LOAD3DMODELINFO | Nein | - |
| `viewport_state` | Der aktuelle Zustand des 3D-Viewports | LOAD3D | Ja | - |
| `camera_info` | Kamerainformationen für die 3D-Ansicht | LOAD3DCAMERA | Nein | - |
| `width` | Breite des Vorschaufensters (Standard: 1024) | INT | Ja | 1 bis 4096 |
| `height` | Höhe des Vorschaufensters (Standard: 1024) | INT | Ja | 1 bis 4096 |

Hinweis: `model_3d_info` und `camera_info` sind optionale erweiterte Eingaben. Wenn sie nicht verbunden sind, greift der Node auf die entsprechenden Werte zurück, die in `viewport_state` gespeichert sind. Die Punktwolkendatei wird in das temporäre Verzeichnis von ComfyUI geschrieben und nicht in das Ausgabeverzeichnis. Dies ist ein Ausgabe-(Terminal-)Node und wird daher hauptsächlich verwendet, um die Vorschau in der Oberfläche anzuzeigen.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `model_3d` | Die Punktwolken-Modelldaten | FILE3D |
| `model_3d_info` | Informationen über das 3D-Modell | LOAD3DMODELINFO |
| `camera_info` | Kamerainformationen für die 3D-Ansicht | LOAD3DCAMERA |
| `width` | Breite des Vorschaufensters | INT |
| `height` | Höhe des Vorschaufensters | INT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PreviewPointCloud/de.md)

---
**Source fingerprint (SHA-256):** `a0b13d9d5658343a6a7c25408d5e5cd9249c92264b76aa448a6553b370f4d782`
