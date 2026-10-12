# TripoPSeriesMultiviewToModelNode

Erzeugt ein Low-Poly-3D-Modell mit sauberer Topologie aus mehreren Ansichten desselben Motivs unter Verwendung von Tripos P2-Modell. Die Vorderansicht ist erforderlich, und ein bis drei der Ansichten links, hinten und rechts können hinzugefügt werden, um das Ergebnis zu verbessern. Das Modell wird als Dreiecksnetz (GLB) zurückgegeben oder, wenn `model.quad` aktiviert ist, als quad-dominantes Netz (FBX).

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model` | Zu verwendendes Modell der Tripo P-Serie. Wenn Sie ein Modell auswählen, werden die zugehörigen Eingaben unten eingeblendet. | DYNAMIC_COMBO | Ja | `"P2"` |

### P2 Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model.image` | Vorderansicht (0°) des Motivs. | IMAGE | Ja | - |
| `model.image_left` | Linke Ansicht (90°), die eigene linke Seite des Motivs. | IMAGE | Nein | - |
| `model.image_back` | Rückansicht (180°). | IMAGE | Nein | - |
| `model.image_right` | Rechte Ansicht (270°), die eigene rechte Seite des Motivs. | IMAGE | Nein | - |
| `model.quad` | Gibt an der FBX-Ausgabe ein quad-dominantes Netz statt eines Dreiecksnetzes an der GLB-Ausgabe zurück (Standard: False). | BOOLEAN | Ja | True/False |
| `model.face_limit` | Zielanzahl der Flächen. `-1` lässt Tripo wählen. Wenn `model.quad` aktiviert ist, liegt das Limit bei 48 bis 25.000, andernfalls bei 48 bis 50.000 (Standard: -1). | INT | Ja | -1, or 48 to 50000 |
| `model.texture` | Auflösung der Basisfarbtextur: standard ist 2K, detailed 4K und extreme 8K. `"none"` gibt ein untexturiertes Netz zurück (Standard: `"standard"`). | COMBO | Ja | `"standard"`<br>`"detailed"`<br>`"extreme"`<br>`"none"` |
| `model.pbr` | Fügt der Basisfarbe Metall-, Rauheits- und Normal-Maps hinzu. Wird ignoriert, wenn `model.texture` `"none"` ist (Standard: True). | BOOLEAN | Ja | True/False |
| `model.model_seed` | Seed für die Geometrie (Standard: 42). | INT | Ja | 0 to 2147483647 |
| `model.texture_alignment` | Gleicht die Farben der Eingabebilder ab oder passt die Texturen an die generierte Geometrie an. Wird ignoriert, wenn `model.texture` `"none"` ist (Standard: `"original_image"`). Erweiterte Einstellung. | COMBO | Ja | `"original_image"`<br>`"geometry"` |
| `model.orientation` | `"align_image"` dreht das Modell auf den Blickwinkel der Eingabebilder. Wird ignoriert, wenn `model.texture` `"none"` ist (Standard: `"default"`). Erweiterte Einstellung. | COMBO | Ja | `"default"`<br>`"align_image"` |
| `model.texture_seed` | Seed für die Texturen (Standard: 42). Erweiterte Einstellung. | INT | Ja | 0 to 2147483647 |
| `model.auto_size` | Skaliert das Modell über seine Szenentransformation auf seine reale Größe in Metern. Wird ignoriert, wenn `model.texture` `"none"` ist (Standard: False). Erweiterte Einstellung. | BOOLEAN | Ja | True/False |
| `model.export_uv` | Führt UV-Unwrapping für das Netz durch, wenn es untexturiert ist. Texturierte Netze werden immer entpackt (Standard: True). Erweiterte Einstellung. | BOOLEAN | Ja | True/False |
| `model.compress_geometry` | Wendet meshopt-Geometriekompression an: viel kleinere Dateien, aber die 3D-Vorschau von ComfyUI kann sie nicht anzeigen. Wird bei Quad-Netzen ignoriert (Standard: False). Erweiterte Einstellung. | BOOLEAN | Ja | True/False |

**Hinweise:**

- `model.image` ist erforderlich, und mindestens eine der Eingaben `model.image_left`, `model.image_back` oder `model.image_right` muss ebenfalls verbunden werden; der Node wirft einen Fehler aus, wenn die Vorderansicht das einzige Bild ist.
- Nur das erste Bild jedes Batches wird verwendet.
- `model.face_limit` ist ein Zielwert und keine feste Obergrenze, daher kann das Ergebnis mehr Flächen enthalten als angefordert. `-1` überlässt die Wahl Tripo.
- `model.quad` entscheidet, welche Ausgabe das Netz enthält. Wenn es aktiviert ist, wird das Modell an der FBX-Ausgabe ausgegeben und die GLB-Ausgabe bleibt leer; wenn es deaktiviert ist, wird das Modell an GLB ausgegeben und FBX bleibt leer. Der Node wirft einen Fehler aus, wenn die leere Ausgabe die von Ihnen verbundene ist.
- `model.texture`, `model.pbr`, `model.texture_seed`, `model.auto_size`, `model.texture_alignment` und `model.orientation` gelten nur für texturierte Modelle: Bei `"none"` sendet der Node keine Textureinstellungen und gibt reine Geometrie zurück.
- `model.compress_geometry` hat keine Auswirkung auf Quad-Netze.

## Ausgaben

| Name der Ausgabe | Beschreibung | Datentyp |
| --- | --- | --- |
| `model task_id` | Die eindeutige Task-ID für die Modellgenerierungsanfrage. | MODEL_TASK_ID |
| `GLB` | Das generierte 3D-Modell im GLB-Format. Leer, wenn `model.quad` aktiviert ist. | FILE3DGLB |
| `FBX` | Das generierte 3D-Modell im FBX-Format. Nur belegt, wenn `model.quad` aktiviert ist. | FILE3DFBX |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoPSeriesMultiviewToModelNode/de.md)

---
**Source fingerprint (SHA-256):** `cea0a65ca001bc8298af9fbe2a83f592abf497987e634b0126482f3d2a18571c`
