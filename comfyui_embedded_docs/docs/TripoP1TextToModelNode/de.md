# Tripo P1: Text zu Modell

Tripo P1 Text-zu-3D. Dieser Node erzeugt mithilfe der Tripo P1 API ein 3D-Modell aus einer Textbeschreibung. Er ist für die Erstellung von spielfertigen Low-Poly-Meshes mit stabiler Topologie optimiert und eignet sich damit für Echtzeitanwendungen.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `output_mode` | Steuert, ob das generierte Modell nur Geometrie oder auch Farb-/PBR-Texturen enthält. `"Geometry only"` gibt ein untexturiertes Mesh zurück. `"Textured"` fügt Farb-/PBR-Maps hinzu und blendet die unten aufgeführten Texturoptionen ein. | DYNAMIC_COMBO | Ja | `"Geometry only"`<br>`"Textured"` |
| `prompt` | Die Textbeschreibung des 3D-Modells, das Sie generieren möchten. Bis zu 1024 Zeichen. Erforderlich und darf nicht leer sein. | STRING | Ja | Bis zu 1024 Zeichen |
| `negative_prompt` | Eine Textbeschreibung dessen, was Sie im generierten Modell nicht haben möchten. Bis zu 255 Zeichen. Standard: nicht gesetzt. | STRING | Nein | Bis zu 255 Zeichen |
| `image_seed` | Ein Seed-Wert zur Steuerung der Zufälligkeit. Standard: 42. | INT | Nein | 0 bis 2147483647 |
| `face_limit` | Zielanzahl der Flächen, 48-20000. -1 lässt Tripo adaptiv auswählen. Standard: -1. | INT | Nein | -1 bis 20000 |
| `model_seed` | Ein Seed-Wert zur Steuerung der Zufälligkeit. Standard: 42. | INT | Nein | 0 bis 2147483647 |
| `auto_size` | Skaliert die Ausgabe so, dass sie ungefähren realen Metern entspricht. Standard: False. | BOOLEAN | Nein | True / False |
| `export_uv` | UV-Unwrap während der Generierung. Für schnellere Nur-Geometrie-Durchläufe deaktivieren. Standard: True. | BOOLEAN | Nein | True / False |
| `compress_geometry` | Wendet meshopt-Geometriekompression an (EXT_meshopt_compression). Kleinere Dateien, aber die 3D-Vorschau von ComfyUI kann sie nicht anzeigen; vor der Bearbeitung dekomprimieren. Standard: False. | BOOLEAN | Nein | True / False |

### Nur-Geometrie-Eingaben

Wenn `output_mode` auf `"Geometry only"` gesetzt ist, sind keine zusätzlichen Eingaben verfügbar. Texturbezogene Parameter werden in diesem Modus nicht an Tripo gesendet.

### Texturierte Eingaben

Diese Eingaben werden nur angezeigt, wenn `output_mode` auf `"Textured"` gesetzt ist.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `pbr` | PBR-Maps einschließen. Wenn diese Option aktiviert ist, wird auch die Basistextur zwangsweise aktiviert. Standard: True. | BOOLEAN | Ja | True / False |
| `texture_quality` | Voreinstellung für die Texturqualität. detailed = HD-Texturen, extreme = 8K-Ultra-Texturen. Standard: "standard". | COMBO | Ja | `"standard"`<br>`"detailed"`<br>`"extreme"` |
| `texture_seed` | Ein Seed-Wert für die Texturgenerierung, der zur Steuerung der Zufälligkeit verwendet wird. Standard: 42. | INT | Ja | 0 bis 2147483647 |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|--------------|----------|
| `model_file` | Der Dateiname des generierten Modells, nur aus Gründen der Abwärtskompatibilität beibehalten. | STRING |
| `model task_id` | Die eindeutige Task-ID für die Modellgenerierungsanfrage. | MODEL_TASK_ID |
| `GLB` | Das generierte 3D-Modell im GLB-Format. | FILE3DGLB |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoP1TextToModelNode/de.md)

---
**Source fingerprint (SHA-256):** `53a5573384294612b912558436e82f3481717d2ba3d50b73f1e40c3065aff2a0`
