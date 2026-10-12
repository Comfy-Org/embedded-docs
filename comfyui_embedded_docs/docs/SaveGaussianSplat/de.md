# Splat speichern

Dieser Node speichert eine Gaussian-Splat-3D-Datei im Ausgabeverzeichnis. Er übernimmt den Speichervorgang der Datei und stellt Vorschaudaten für den 3D-Viewport bereit.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model_3d` | Eine Gaussian-Splat-3D-Datei. | FILE3D | Ja | SplatAny<br>PLY<br>SPLAT<br>SPZ<br>KSPLAT |
| `filename_prefix` | Das Präfix für den gespeicherten Dateinamen (Standard: "3d/ComfyUI"). | STRING | Ja | Jedes gültige Dateinamenpräfix |
| `viewport_state` | Der aktuelle Viewport-Zustand, der Kamera- und Modellinformationen enthält. | LOAD3D | Ja | - |
| `model_3d_info` | Zusätzliche 3D-Modellinformationen für den Viewport. | LOAD3DMODELINFO | Nein | - |
| `camera_info` | Kamerainformationen für die Viewport-Vorschau. | LOAD3DCAMERA | Nein | - |
| `width` | Die Breite der Vorschau (Standard: 1024). | INT | Ja | 1 bis 4096 |
| `height` | Die Höhe der Vorschau (Standard: 1024). | INT | Ja | 1 bis 4096 |

Hinweis: Wenn `camera_info` oder `model_3d_info` nicht bereitgestellt werden, verwendet der Node die entsprechenden Werte aus `viewport_state`, sofern verfügbar.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `model_3d` | Die Gaussian-Splat-3D-Datei, die im Ausgabeverzeichnis gespeichert wurde. | FILE3D |
| `model_3d_info` | 3D-Modellinformationen für den Viewport. | LOAD3DMODELINFO |
| `camera_info` | Kamerainformationen für die Viewport-Vorschau. | LOAD3DCAMERA |
| `width` | Die Breite der Vorschau. | INT |
| `height` | Die Höhe der Vorschau. | INT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveGaussianSplat/de.md)

---
**Source fingerprint (SHA-256):** `f2d6b98d2ce1fe11df8ba440b7f46a21e2308966c15daa5ca0bdca7dab1726cc`
