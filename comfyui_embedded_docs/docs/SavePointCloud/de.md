# Punktwolke speichern

Der Node „Save Point Cloud“ speichert eine 3D-Punktwolkendatei im Ausgabeverzeichnis und stellt optional Vorschaudaten für den 3D-Viewer bereit. Er übernimmt Dateibenennung und Speicherung und reicht gleichzeitig Kamera- und Modellinformationen für Anzeigezwecke weiter.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model_3d` | Punktwolkendatei (.ply) | FILE3D_POINT_CLOUD_ANY oder FILE3D_PLY | Ja | - |
| `filename_prefix` | Präfix für den gespeicherten Dateinamen (Standard: "3d/ComfyUI") | STRING | Ja | - |
| `viewport_state` | Aktueller Viewport-Status mit Kamera- und Modellinformationen | LOAD3D | Ja | - |
| `model_3d_info` | Zusätzliche Modellinformationen für den 3D-Viewer | LOAD3D_MODEL_INFO | Nein | - |
| `camera_info` | Kamera-Informationen für den 3D-Viewer | LOAD3D_CAMERA | Nein | - |
| `width` | Breite der Vorschaudarstellung in Pixeln (Standard: 1024) | INT | Ja | 1 bis 4096 |
| `height` | Höhe der Vorschaudarstellung in Pixeln (Standard: 1024) | INT | Ja | 1 bis 4096 |

Die gespeicherte Datei wird unter Verwendung des `filename_prefix` mit einem angehängten fünfstelligen Zähler in das Ausgabeverzeichnis geschrieben (zum Beispiel `3d/ComfyUI_00001.ply`). Wenn die optionale Eingabe `camera_info` nicht verbunden ist, werden die Kamera-Informationen aus `viewport_state` übernommen; ebenso werden, wenn `model_3d_info` nicht verbunden ist, die Modellinformationen aus `viewport_state` übernommen (oder eine leere Liste, falls keine verfügbar ist).

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `model_3d` | Die gespeicherte Punktwolkendatei | FILE3D_POINT_CLOUD_ANY |
| `model_3d_info` | Modellinformationen für den 3D-Viewer | LOAD3D_MODEL_INFO |
| `camera_info` | Kamera-Informationen für den 3D-Viewer | LOAD3D_CAMERA |
| `width` | Breite der Vorschaudarstellung | INT |
| `height` | Höhe der Vorschaudarstellung | INT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SavePointCloud/de.md)

---
**Source fingerprint (SHA-256):** `ce8f005c431843a57d87a4aff2eed7a1604ebdf360f83b3aaaadc3ed364d218a`
