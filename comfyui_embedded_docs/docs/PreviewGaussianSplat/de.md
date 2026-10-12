# PreviewGaussianSplat

Der Knoten PreviewGaussianSplat zeigt eine 3D-Gaussian-Splat-Datei in einem Vorschaufenster an, ohne sie im ComfyUI-Ausgabeverzeichnis zu speichern. Er akzeptiert eine 3D-Modelldatei in verschiedenen Gaussian-Splat-Formaten, speichert eine temporäre Kopie für die Vorschau und reicht die Modelldaten für die weitere Verarbeitung im Workflow durch. Dieser Knoten ist als experimentell gekennzeichnet und fungiert als Ausgabeknoten.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model_3d` | Eine Gaussian-Splat-3D-Datei. | FILE3D | Ja | splat<br>ply<br>spz<br>ksplat |
| `model_3d_info` | Optionale Metadateninformationen zum 3D-Modell. Wenn nicht verbunden, verwendet der Knoten die Modellinformationen aus `viewport_state`. | LOAD3DMODELINFO | Nein | - |
| `viewport_state` | Der aktuelle Zustand des 3D-Viewports, einschließlich Kamera- und Modellinformationen. | LOAD3D | Ja | - |
| `camera_info` | Optionale Kamerainformationen für die Vorschau. Wenn nicht verbunden, verwendet der Knoten die Kamerainformationen aus `viewport_state`. | LOAD3DCAMERA | Nein | - |
| `width` | Die Breite des Vorschau-Renderings in Pixeln (Standard: 1024). | INT | Ja | 1 bis 4096 |
| `height` | Die Höhe des Vorschau-Renderings in Pixeln (Standard: 1024). | INT | Ja | 1 bis 4096 |

Hinweis: Wenn `camera_info` oder `model_3d_info` nicht angegeben werden, greift der Knoten auf die im `viewport_state` gespeicherten Kamera- und Modellinformationen zurück. Wenn `viewport_state` kein gültiges Viewport-State-Objekt ist, wird es als leer behandelt.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `model_3d` | Die eingegebene 3D-Gaussian-Splat-Datei, unverändert durchgereicht. | FILE3D |
| `model_3d_info` | Metadateninformationen zum 3D-Modell, entweder aus der Eingabe oder aus dem Viewport-Zustand abgeleitet. | LOAD3DMODELINFO |
| `camera_info` | Kamerainformationen für die Vorschau, entweder aus der Eingabe oder aus dem Viewport-Zustand abgeleitet. | LOAD3DCAMERA |
| `width` | Die Breite des Vorschau-Renderings. | INT |
| `height` | Die Höhe des Vorschau-Renderings. | INT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PreviewGaussianSplat/de.md)

---
**Source fingerprint (SHA-256):** `4fc86c692724ce406f9bba9aa9ebe22a92e72a25d11abf8f55d1b99044bb1acd`
