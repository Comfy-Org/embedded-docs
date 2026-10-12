# Preview3DAnimation

Der Node Preview3DAnimation dient hauptsächlich zur Vorschau von 3D-Modellausgaben. Dieser Node nimmt zwei Eingaben entgegen: eine ist die `camera_info` vom Load3D-Node, und die andere ist der Pfad zur 3D-Modelldatei. Der Modelldateipfad muss sich im Ordner `ComfyUI/output` befinden.

**Unterstützte Formate**
Derzeit unterstützt dieser Node mehrere 3D-Dateiformate, darunter `.gltf`, `.glb`, `.obj`, `.fbx` und `.stl`.

**3D-Node-Einstellungen**
Einige zugehörige Einstellungen für 3D-Nodes können im Einstellungsmenü von ComfyUI konfiguriert werden. Bitte beachten Sie die folgende Dokumentation für die entsprechenden Einstellungen:
[Einstellungsmenü](https://docs.comfy.org/interface/settings/3d)

## Eingaben

| Parametername | Beschreibung | Typ |
| --- | --- | --- |
| camera_info | Kamerainformationen | LOAD3D_CAMERA |
| model_file | Pfad zur Modelldatei unter `ComfyUI/output/` | STRING |

## Beschreibung des Canvas-Bereichs

Derzeit verwenden die 3D-bezogenen Nodes im ComfyUI-Frontend dieselbe Canvas-Komponente, sodass ihre grundlegenden Bedienvorgänge abgesehen von einigen funktionalen Unterschieden größtenteils konsistent sind.

> Der folgende Inhalt und die Oberfläche basieren hauptsächlich auf dem Load3D-Node. Bitte beziehen Sie sich für spezifische Funktionen auf die tatsächliche Node-Oberfläche.

Der Canvas-Bereich umfasst verschiedene Ansichtsoperationen, wie zum Beispiel:

- Einstellungen für die Vorschauansicht (Raster, Hintergrundfarbe, Vorschauansicht)
- Kamerasteuerung: FOV, Kameratyp
- Globale Beleuchtungsintensität: Beleuchtung anpassen
- Modellexport: Unterstützt die Formate `GLB`, `OBJ`, `STL`
- usw.

![Benutzeroberfläche des Load-3D-Nodes](../Preview3D/asset/preview3d_canvas.jpg)

1. Enthält mehrere Menüs und versteckte Menüs des Load-3D-Nodes
2. Achse für 3D-Ansichtsoperationen

### 1. Ansichtsoperationen

<video controls width="640" height="360">
  <source src="https://raw.githubusercontent.com/Comfy-Org/embedded-docs/refs/heads/main/comfyui_embedded_docs/docs/Load3D/asset/view_operations.mp4" type="video/mp4">
  Ihr Browser unterstützt die Videowiedergabe nicht.
</video>

Ansichtssteuerungsoperationen:

- Linksklick + Ziehen: Ansicht drehen
- Rechtsklick + Ziehen: Ansicht verschieben
- Mausrad scrollen oder Mittelklick + Ziehen: Vergrößern/Verkleinern
- Koordinatenachse: Ansichten wechseln

### 2. Funktionen des linken Menüs

![Menü](https://raw.githubusercontent.com/Comfy-Org/embedded-docs/refs/heads/main/comfyui_embedded_docs/docs/Load3d/asset/menu.webp)

Im Vorschaubereich sind einige Ansichtsoperationsmenüs im Menü ausgeblendet. Klicken Sie auf die Menüschaltfläche, um verschiedene Menüs zu erweitern.

- 1. Szene: Enthält Raster des Vorschaufensters, Hintergrundfarbe, Vorschauminiatur-Einstellungen
- 2. Modell: Modell-Rendering-Modus, Texturmaterial, Einstellungen für die Aufwärtsrichtung
- 3. Kamera: Zwischen orthografischer und perspektivischer Ansicht wechseln, Perspektivwinkel festlegen
- 4. Licht: Globale Beleuchtungsintensität der Szene
- 5. Export: Modell in andere Formate exportieren (GLB, OBJ, STL)

#### Szene

![Szenenmenü](https://raw.githubusercontent.com/Comfy-Org/embedded-docs/refs/heads/main/comfyui_embedded_docs/docs/Load3d/asset/menu_scene.webp)

Das Szenenmenü bietet einige grundlegende Funktionen zur Szeneneinstellung:

1. Raster ein-/ausblenden
2. Hintergrundfarbe festlegen
3. Klicken, um ein Hintergrundbild hochzuladen
4. Vorschauminiatur ausblenden

#### Modell

![Menü_Szene](https://raw.githubusercontent.com/Comfy-Org/embedded-docs/refs/heads/main/comfyui_embedded_docs/docs/Load3d/asset/menu_model.webp)

Das Modellmenü bietet einige modellbezogene Funktionen:

1. **Aufwärtsrichtung**: Bestimmen, welche Achse die Aufwärtsrichtung für das Modell ist
2. **Materialmodus**: Modell-Rendering-Modi umschalten – Original, Normal, Wireframe, Lineart

#### Kamera

![Menü_Modellmenü_Kamera](https://raw.githubusercontent.com/Comfy-Org/embedded-docs/refs/heads/main/comfyui_embedded_docs/docs/Load3d/asset/menu_camera.webp)

Dieses Menü bietet das Umschalten zwischen orthografischer und perspektivischer Ansicht sowie Einstellungen für die Größe des Perspektivwinkels:

1. **Kamera**: Schnell zwischen orthografischer und perspektivischer Ansicht wechseln
2. **FOV**: FOV-Winkel anpassen

#### Licht

![Menü_Modellmenü_Kamera](https://raw.githubusercontent.com/Comfy-Org/embedded-docs/refs/heads/main/comfyui_embedded_docs/docs/Load3d/asset/menu_light.webp)

Über dieses Menü können Sie die globale Beleuchtungsintensität der Szene schnell anpassen.

#### Export

![Menü_Export](https://raw.githubusercontent.com/Comfy-Org/embedded-docs/refs/heads/main/comfyui_embedded_docs/docs/Load3d/asset/menu_export.webp)

Dieses Menü bietet die Möglichkeit, Modellformate schnell zu konvertieren und zu exportieren.

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Preview3DAnimation/de.md)
