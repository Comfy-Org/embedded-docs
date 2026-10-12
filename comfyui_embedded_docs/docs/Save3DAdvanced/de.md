# Save3DAdvanced

Speichert ein 3D-Modell in einer Datei im Ausgabeverzeichnis von ComfyUI und erzeugt eine Vorschau der gespeicherten Szene. Außerdem werden das 3D-Modell, seine Platzierung in der Szene, Kamerainformationen und Viewport-Abmessungen an nachgelagerte Nodes weitergegeben. Wenn Modellplatzierung oder Kamerainformationen nicht verbunden sind, verwendet der Node die im Viewport-Status gespeicherten Werte.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model_3d` | 3D-Modelldatei von einem vorgelagerten 3D-Node. | FILE3D | Ja | GLB<br>GLTF<br>FBX<br>OBJ<br>STL<br>USDZ<br>Any |
| `filename_prefix` | Präfix für den Dateinamen der gespeicherten Datei (Standard: "3d/ComfyUI"). | STRING | Ja | Freitext |
| `viewport_state` | Viewport-Status mit Kamera- und Modellplatzierungsinformationen, typischerweise von einem Load-3D-Node. | LOAD3D | Ja | - |
| `model_3d_info` | Platzierung jedes Modells in der Szene: Position, Rotation und Skalierung (Y-up-Weltkoordinaten). Überschreibt die in `viewport_state` gespeicherte Modellplatzierung, wenn verbunden. | LOAD3DMODELINFO | Nein | - |
| `camera_info` | Viewport-Kamerainformationen: Position, Look-at-Ziel, Zoom und Typ. Überschreibt die in `viewport_state` gespeicherten Kamerainformationen, wenn verbunden. | LOAD3DCAMERA | Nein | - |
| `width` | Renderbreite des Viewports in Pixeln (Standard: 1024). | INT | Ja | 1 bis 4096 |
| `height` | Renderhöhe des Viewports in Pixeln (Standard: 1024). | INT | Ja | 1 bis 4096 |

Hinweis: `model_3d_info` und `camera_info` sind optional. Wenn eine der Eingaben nicht verbunden ist, greift der Node auf die entsprechenden in `viewport_state` gespeicherten Werte zurück.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `model_3d` | Die vom Eingang durchgereichte 3D-Modelldatei. | FILE3D |
| `model_3d_info` | Platzierung jedes Modells in der Szene: Position, Rotation und Skalierung (Y-up-Weltkoordinaten). | LOAD3DMODELINFO |
| `camera_info` | Viewport-Kamerainformationen: Position, Look-at-Ziel, Zoom und Typ. | LOAD3DCAMERA |
| `width` | Der vom Eingang durchgereichte Wert für die Renderbreite. | INT |
| `height` | Der vom Eingang durchgereichte Wert für die Renderhöhe. | INT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Save3DAdvanced/de.md)

---
**Source fingerprint (SHA-256):** `27cb15c5cf382e6e5b8164cfd456993404222c61d59edff2d51f9f1c8e47b25f`
