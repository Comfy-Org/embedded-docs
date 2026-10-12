# Preview3DAdvanced

Dieser Node zeigt eine 3D-Modellvorschau in der Benutzeroberfläche an, ohne die Datei im ComfyUI-Ausgabeverzeichnis zu speichern. Er speichert das Modell in einer temporären Datei und gibt die Modelldaten, Modellinformationen, Kamerainformationen und Vorschauabmessungen für die weitere Verarbeitung in nachgelagerten Nodes weiter.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model_3d` | 3D-Modell-Datei von einem vorgelagerten 3D-Node. | FILE3D | Ja | GLB, GLTF, FBX, OBJ, STL, USDZ oder jedes unterstützte 3D-Format |
| `model_3d_info` | Platzierung jedes Modells in der Szene: Position, Rotation und Skalierung (Y-up-Weltkoordinaten). Optional. Erweiterte Option. | LOAD3DMODELINFO | Nein | - |
| `viewport_state` | Der aktuelle Viewport-Zustand mit Kamera- und Modellinformationen. | LOAD3D | Ja | - |
| `camera_info` | Viewport-Kamerainformationen: Position, Blickziel (Look-at-Ziel), Zoom und Typ. Optional. Erweiterte Option. | LOAD3DCAMERA | Nein | - |
| `width` | Renderbreite des Viewports in Pixeln. Standard: 1024. | INT | Ja | 1 bis 4096 |
| `height` | Renderhöhe des Viewports in Pixeln. Standard: 1024. | INT | Ja | 1 bis 4096 |

Hinweis: Wenn `camera_info` oder `model_3d_info` nicht verbunden sind, werden ihre Werte aus `viewport_state` übernommen, sofern verfügbar. Wenn `viewport_state` keine Kamerainformationen enthält, ist `camera_info` None. Wenn `viewport_state` keine Modellinformationen enthält, ist `model_3d_info` standardmäßig eine leere Liste. Wenn `viewport_state` kein Dictionary ist, wird es als leer behandelt.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `model_3d` | 3D-Modell-Datei (glb/obj/stl/usw.) von einem vorgelagerten 3D-Node, unverändert weitergegeben. | FILE3D |
| `model_3d_info` | Platzierung jedes Modells in der Szene: Position, Rotation und Skalierung (Y-up-Weltkoordinaten). Verwendet den Eingabewert oder fällt auf den in `viewport_state` gespeicherten Wert zurück. | LOAD3DMODELINFO |
| `camera_info` | Viewport-Kamerainformationen: Position, Blickziel (Look-at-Ziel), Zoom und Typ. Verwendet den Eingabewert oder fällt auf den in `viewport_state` gespeicherten Wert zurück. | LOAD3DCAMERA |
| `width` | Renderbreite des Viewports in Pixeln. | INT |
| `height` | Renderhöhe des Viewports in Pixeln. | INT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Preview3DAdvanced/de.md)

---
**Source fingerprint (SHA-256):** `f2d3d35ed35fe68edebcde8fd8421d26850b04e3ae5b7147f1020c8ed904c480`
