# Load3DAdvanced

Der Node Load 3D (Advanced) lädt eine 3D-Modell-Datei aus dem Verzeichnis `input/3d` von ComfyUI und stellt die Modelldaten zusammen mit Modellplatzierungs- und Kamerainformationen bereit, die im Viewport-Zustand des 3D-Viewers erfasst wurden. Er unterstützt gängige 3D-Dateiformate und ermöglicht es Ihnen, die Renderbreite und -höhe des Viewports in Pixeln festzulegen. Dieser Node ist experimentell.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model_file` | Die zu ladende 3D-Modell-Datei. Wählen Sie "none", um das Laden einer Modelldatei zu überspringen. Dateien können auch über das Widget hochgeladen werden. | COMBO | Ja | `"none"`<br>Verfügbare 3D-Modell-Dateien im Verzeichnis `input/3d` |
| `viewport_state` | Der aktuelle Viewport-Zustand, der Kamera- und Modellinformationen aus dem 3D-Viewer enthält. | LOAD3D | Ja | - |
| `width` | Renderbreite des Viewports in Pixeln (Standard: 1024). | INT | Ja | Min: 1<br>Max: 4096<br>Standard: 1024<br>Schritt: 1 |
| `height` | Renderhöhe des Viewports in Pixeln (Standard: 1024). | INT | Ja | Min: 1<br>Max: 4096<br>Standard: 1024<br>Schritt: 1 |

**Hinweise zu Parametern:**
- Der Parameter `model_file` listet nur Dateien mit den folgenden Erweiterungen auf: .gltf, .glb, .obj, .fbx, .stl
- Dateien müssen im Verzeichnis `input/3d` Ihrer ComfyUI-Installation abgelegt werden; Unterordner werden ebenfalls durchsucht, und Dateipfade werden relativ zum Eingabeverzeichnis angezeigt
- Wenn `model_file` auf "none" gesetzt ist, werden keine Modelldaten geladen und die Ausgabe `model_3d` bleibt leer
- Wenn `model_file` auf eine nicht existierende Datei gesetzt ist, gibt der Node einen Validierungsfehler zurück: "Invalid 3D model file: {model_file}"
- Wenn `viewport_state` kein gültiges Viewport-Zustandsobjekt ist, wird es als leer behandelt, sodass `model_3d_info` zu einer leeren Liste wird und `camera_info` leer zurückgegeben wird

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `model_3d` | Geladene 3D-Modell-Datei (glb/obj/stl/usw.). Leer, wenn keine Modelldatei ausgewählt wurde. | FILE3DANY |
| `model_3d_info` | Platzierung jedes Modells in der Szene: Position, Rotation und Skalierung (Y-up-Weltkoordinatenraum). | LOAD3DMODELINFO |
| `camera_info` | Viewport-Kamerainformationen: Position, Look-at-Ziel, Zoom und Typ. | LOAD3DCAMERA |
| `width` | Renderbreite des Viewports in Pixeln. | INT |
| `height` | Renderhöhe des Viewports in Pixeln. | INT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Load3DAdvanced/de.md)

---
**Source fingerprint (SHA-256):** `c79c53dde0c8b3afb7df7b972df749f5040c92d48b47e355c4497d9b0cbf1c22`
