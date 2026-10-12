# TripoConversionNode

Dieser Node konvertiert ein vorhandenes Tripo-3D-Modell in ein anderes 3D-Dateiformat. Er nimmt die Task-ID eines Modells, das zuvor durch eine Tripo-Operation erstellt oder verarbeitet wurde (z. B. Modellgenerierung, Rigging, Retargeting oder Segmentierung), übermittelt eine Konvertierungsaufgabe an die Tripo-API, wartet, bis diese Aufgabe abgeschlossen ist, und gibt anschließend die konvertierte Modelldatei zurück.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `original_model_task_id` | Task-ID des zu konvertierenden Tripo-Modells. Sie muss aus einer früheren Tripo-Aufgabe zur Modellgenerierung, zum Rigging, Retargeting oder zur Segmentierung stammen. Wenn die ID fehlt oder leer ist, löst der Node einen Fehler aus. | STRING | Ja | MODEL_TASK_ID<br>RIG_TASK_ID<br>RETARGET_TASK_ID<br>SEGMENT_TASK_ID |
| `format` | Zieldateiformat für das konvertierte 3D-Modell. | COMBO | Ja | GLTF<br>USDZ<br>FBX<br>OBJ<br>STL<br>3MF |
| `quad` | Wandelt Dreiecke in Vierecke um, wenn aktiviert (Standard: False). | BOOLEAN | Nein | True oder False |
| `face_limit` | Maximale Anzahl von Flächen im konvertierten Modell. Auf -1 setzen für kein Limit (Standard: -1). | INT | Nein | -1 bis 2000000 |
| `texture_size` | Auflösung der Ausgabetexturen in Pixeln (Standard: 4096). | INT | Nein | 128 bis 8192 |
| `texture_format` | Dateiformat für exportierte Texturen (Standard: JPEG). | COMBO | Nein | BMP<br>DPX<br>HDR<br>JPEG<br>OPEN_EXR<br>PNG<br>TARGA<br>TIFF<br>WEBP |
| `force_symmetry` | Erzwingt ein symmetrisches Modell, wenn aktiviert (Standard: False). | BOOLEAN | Nein | True oder False |
| `flatten_bottom` | Flacht die Unterseite des Modells ab, wenn aktiviert (Standard: False). | BOOLEAN | Nein | True oder False |
| `flatten_bottom_threshold` | Abflachungstiefe, die mit `flatten_bottom` verwendet wird (Standard: 0.01). Dieser Wert wird nur angewendet, wenn `flatten_bottom` aktiviert ist. | FLOAT | Nein | 0.01 bis 1.0 |
| `pivot_to_center_bottom` | Verschiebt den Pivot-Punkt zur Mitte der Unterseite des Modells, wenn aktiviert (Standard: False). | BOOLEAN | Nein | True oder False |
| `scale_factor` | Skalierungsfaktor, der auf das konvertierte Modell angewendet wird (Standard: 1.0). | FLOAT | Nein | 0.01 und höher |
| `with_animation` | Behält das Skelett und die Animation von geriggten oder retargeteten Modellen bei (Standard: True). | BOOLEAN | Nein | True oder False |
| `pack_uv` | Packt die UV-Koordinaten neu, wenn aktiviert (Standard: False). | BOOLEAN | Nein | True oder False |
| `bake` | Backt erweiterte Materialien in die Basistexturen ein, um breitere Kompatibilität zu erreichen (Standard: True). | BOOLEAN | Nein | True oder False |
| `part_names` | Kommagetrennte Liste von Modellteilnamen, die an die Konvertierung gesendet werden. Leere Einträge werden ignoriert und doppelte Namen entfernt. Leer lassen, um diese Option auszulassen (Standard: leer). | STRING | Nein | Kommagetrennte Liste von Teilnamen |
| `fbx_preset` | FBX-Kompatibilitätsvoreinstellung. bake_scale backt die Skalierungstransformation in die Geometrie ein (Standard: blender). | COMBO | Nein | blender<br>mixamo<br>3dsmax<br>bake_scale |
| `export_vertex_colors` | Exportiert Vertex-Farben, wenn aktiviert (Standard: False). | BOOLEAN | Nein | True oder False |
| `export_orientation` | Vorwärtsachse des exportierten Modells. default behält Tripos +x bei (Standard: default). | COMBO | Nein | default<br>+x<br>-x<br>+y<br>-y |
| `animate_in_place` | Animiert das Modell an Ort und Stelle, wenn aktiviert (Standard: False). | BOOLEAN | Nein | True oder False |

**Hinweis:** Außer `original_model_task_id` und `format` sind alle Eingaben optionale erweiterte Einstellungen. Die meisten Einstellungen, die auf ihren Standardwerten belassen werden, werden aus der Konvertierungsanfrage weggelassen, damit die Tripo-API ihr Standardverhalten verwenden kann. Die Optionen `with_animation` und `bake` werden immer gesendet. `flatten_bottom_threshold` wird nur angewendet, wenn `flatten_bottom` aktiviert ist.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `model_3d` | Konvertiertes Modell im angeforderten Format. OBJ wird von Tripo als ZIP-Archiv geliefert (Mesh, Material und Texturen). | FILE_3D |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoConversionNode/de.md)

---
**Source fingerprint (SHA-256):** `b6be09bf6b1c5ccd6de5ae56ed28bfe1f0b81c1ca8ff61623e3094917c98d68a`
