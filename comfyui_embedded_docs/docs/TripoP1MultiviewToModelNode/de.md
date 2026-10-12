# TripoP1MultiviewToModelNode

Dieser Node generiert ein 3D-Modell aus zwei bis vier Referenzbildern eines Objekts oder Charakters. Stellen Sie die Vorderansicht sowie eine beliebige Kombination aus linker, hinterer und rechter Ansicht bereit, und der Node gibt das rekonstruierte Subjekt als GLB-Mesh zurück.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `image` | Vorderansicht (0°). Erforderlich. | IMAGE | Ja | - |
| `image_left` | Linke Ansicht (90°), d. h. die linke Seite des Subjekts. | IMAGE | Nein | - |
| `image_back` | Hinteransicht (180°). | IMAGE | Nein | - |
| `image_right` | Rechte Ansicht (270°), d. h. die rechte Seite des Subjekts. | IMAGE | Nein | - |
| `output_mode` | Wählen Sie den Typ des zu generierenden Modells. "Geometry only" gibt ein untexturiertes Mesh zurück. "Textured" fügt Farb-/PBR-Maps hinzu. | DYNAMIC_COMBO | Ja | "Geometry only"<br>"Textured" |
| `face_limit` | Zielanzahl der Flächen, 48-20000. -1 lässt Tripo adaptiv wählen. (Standard: -1) | INT | Nein | -1 bis 20000 |
| `model_seed` | Seed für reproduzierbare Modellgenerierung. (Standard: 42) | INT | Nein | 0 bis 2147483647 |
| `auto_size` | Skaliert die Ausgabe auf ungefähre reale Größe in Metern. (Standard: False) | BOOLEAN | Nein | True<br>False |
| `export_uv` | UV-Entfaltung während der Generierung. Für schnellere Nur-Geometrie-Durchläufe deaktivieren. (Standard: True) | BOOLEAN | Nein | True<br>False |
| `compress_geometry` | Wendet meshopt-Geometriekompression an (EXT_meshopt_compression). Kleinere Dateien, aber die 3D-Vorschau von ComfyUI kann sie nicht anzeigen; vor der Bearbeitung dekomprimieren. (Standard: False) | BOOLEAN | Nein | True<br>False |

### Nur Geometrie Eingaben

Für diesen Modus werden keine zusätzlichen Eingaben angezeigt. Das generierte Modell wird ohne Textur zurückgegeben.

### Texturierte Eingaben

Diese Eingaben erscheinen, wenn `output_mode` auf `"Textured"` gesetzt ist.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `pbr` | PBR-Maps einbeziehen. Wenn aktiviert, wird die Basistextur ebenfalls erzwungen. (Standard: True) | BOOLEAN | Ja | True<br>False |
| `texture_quality` | Texturqualitätsstufe. `detailed` = HD-Texturen, `extreme` = 8K-Ultra-Texturen. (Standard: "standard") | COMBO | Ja | "standard"<br>"detailed"<br>"extreme" |
| `texture_alignment` | Priorisiert visuelle Treue zum Quellbild oder Ausrichtung an der Mesh-Geometrie. (Standard: "original_image") | COMBO | Ja | "original_image"<br>"geometry" |
| `orientation` | Dreht die Ausgabe, um sie an das Quellbild anzupassen. Gilt nur bei texturierter Ausgabe. (Standard: "default") | COMBO | Ja | "default"<br>"align_image" |
| `texture_seed` | Seed für die Texturgenerierung. (Standard: 42) | INT | Ja | 0 bis 2147483647 |

**Hinweis:** Sie müssen mindestens 2 Bilder bereitstellen: die Vorderansicht (`image`) plus mindestens eine der anderen Ansichten (`image_left`, `image_back` oder `image_right`). Wenn weniger als 2 Bilder bereitgestellt werden, löst der Node einen Fehler aus.

## Ausgaben

| Ausgabenamen | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `model_file` | Der Dateiname des generierten GLB-Modells (nur zur Abwärtskompatibilität). | STRING |
| `model task_id` | Die eindeutige Task-ID für diese Modellgenerierungsanfrage. | MODEL_TASK_ID |
| `GLB` | Das generierte 3D-Modell im GLB-Format. | FILE3DGLB |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoP1MultiviewToModelNode/de.md)

---
**Source fingerprint (SHA-256):** `1153f74ac76603829142959844e701f3c8f16be080e3de849951cffdda322d12`
