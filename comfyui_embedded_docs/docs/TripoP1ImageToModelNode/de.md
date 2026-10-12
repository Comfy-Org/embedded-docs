# TripoP1ImageToModelNode

Tripo P1: Image to Model wandelt ein einzelnes 2D-Bild mithilfe der Tripo P1 API in ein 3D-Modell um. Es ist für die Erzeugung niedrigpolygonaler, spielbereiter Meshes optimiert und ermöglicht die Wahl zwischen einem reinen Geometrie-Mesh oder einem texturierten Modell mit PBR-Maps. Das fertige Modell wird als GLB-Datei zurückgegeben.

## Eingaben

### Gemeinsame Eingaben

Diese Parameter sind immer verfügbar.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `output_mode` | Wählt den Ergebnistyp. "Geometry only" gibt ein untexturiertes Mesh zurück; "Textured" fügt Farb-/PBR-Maps hinzu und blendet zusätzliche Textureinstellungen ein. | DYNAMIC_COMBO | Ja | `"Geometry only"`<br>`"Textured"` |
| `image` | Das 2D-Quellbild, das zur Erzeugung des 3D-Modells verwendet wird. Ein einzelnes Bild ist erforderlich; der Node löst einen Fehler aus, wenn keines bereitgestellt wird. | IMAGE | Ja | - |
| `enable_image_autofix` | Das Eingabebild vorverarbeiten, um eine bessere Generierungsqualität zu erzielen. (Standard: False) | BOOLEAN | Nein | True<br>False |
| `face_limit` | Zielanzahl der Flächen, 48-20000. -1 lässt Tripo adaptiv auswählen. (Standard: -1) | INT | Nein | -1 bis 20000 |
| `model_seed` | Seed, der für die Geometriegenerierung verwendet wird, damit Ergebnisse reproduziert werden können. (Standard: 42) | INT | Nein | 0 bis 2147483647 |
| `auto_size` | Skaliert die Ausgabe auf ungefähre reale Meter. (Standard: False) | BOOLEAN | Nein | True<br>False |
| `export_uv` | UV-Abwicklung während der Generierung. Für schnellere reine Geometrie-Durchläufe ausschalten. (Standard: True) | BOOLEAN | Nein | True<br>False |
| `compress_geometry` | Wendet meshopt-Geometriekompression an (EXT_meshopt_compression). Kleinere Dateien, aber die 3D-Vorschau von ComfyUI kann sie nicht anzeigen; vor der Bearbeitung dekomprimieren. (Standard: False) | BOOLEAN | Nein | True<br>False |

### Eingaben für reine Geometrie

Keine zusätzlichen Parameter. Die Ausgabe ist ein untexturiertes Mesh.

### Texturierte Eingaben

Diese Parameter erscheinen, wenn `output_mode` auf "Textured" gesetzt ist.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `pbr` | PBR-Maps einschließen. Wenn aktiviert, wird auch die Basistextur zwingend aktiviert. (Standard: True) | BOOLEAN | Ja | True<br>False |
| `texture_quality` | detailed = HD-Texturen, extreme = 8K-Ultra-Texturen. (Standard: "standard") | COMBO | Ja | `"standard"`<br>`"detailed"`<br>`"extreme"` |
| `texture_alignment` | Priorisiert visuelle Treue zum Quellbild oder Ausrichtung an der Mesh-Geometrie. (Standard: "original_image") | COMBO | Ja | `"original_image"`<br>`"geometry"` |
| `orientation` | Dreht die Ausgabe so, dass sie zum Quellbild passt. Gilt nur bei Texturierung. (Standard: "default") | COMBO | Ja | `"default"`<br>`"align_image"` |
| `texture_seed` | Seed, der für die Texturgenerierung verwendet wird, damit texturierte Ergebnisse reproduziert werden können. (Standard: 42) | INT | Ja | 0 bis 2147483647 |

Hinweis: Wenn `output_mode` auf "Geometry only" gesetzt ist, ist die Texturierung für die Anfrage deaktiviert. Im Modus "Textured" wird immer eine Farbtextur angefordert; das Deaktivieren von `pbr` entfernt die PBR-Maps, behält aber die Basisfarbtextur bei, während das Aktivieren von `pbr` zusätzlich die Basistextur erzwingt. `texture_alignment` und `orientation` sind nur im Modus "Textured" verfügbar.

## Ausgaben

| Ausgabenamen | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `model_file` | Ein String, der den Dateinamen des generierten Modells enthält (`<task_id>.glb`). Nur aus Gründen der Rückwärtskompatibilität beibehalten. | STRING |
| `model task_id` | Die eindeutige Aufgaben-ID, die von der Tripo API für den abgeschlossenen Generierungsjob zurückgegeben wird. | MODEL_TASK_ID |
| `GLB` | Das generierte 3D-Modell im GLB-Format. | FILE3DGLB |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoP1ImageToModelNode/de.md)

---
**Source fingerprint (SHA-256):** `1369da2ef732556896bce3415e7b99023f310544b8077ea4c6b1730bec59ee99`
