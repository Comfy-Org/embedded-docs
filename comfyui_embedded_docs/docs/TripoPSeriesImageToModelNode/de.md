# Tripo P2: Bild zu Modell

Erzeugt aus einem einzelnen Bild mithilfe des P2-Modells von Tripo ein Low-Poly-3D-Modell mit sauberer Topologie. Das Ergebnis wird als Dreiecksnetz (GLB) oder, wenn `model.quad` aktiviert ist, als quad-dominantes Netz (FBX) zurückgegeben.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model` | Zu verwendendes Tripo-Modell der P-Serie. Bei Auswahl eines Modells werden dessen eigene Eingaben unten eingeblendet. | DYNAMIC_COMBO | Ja | `"P2"` |

### P2 Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model.image` | Das Bild, aus dem das Modell generiert wird. | IMAGE | Ja | - |
| `model.quad` | Gibt ein quad-dominantes Netz an der FBX-Ausgabe statt eines Dreiecksnetzes an der GLB-Ausgabe zurück (Standard: False). | BOOLEAN | Ja | True/False |
| `model.face_limit` | Zielanzahl der Flächen. `-1` lässt Tripo wählen. Bei aktiviertem `model.quad` liegt das Limit bei 48 bis 25.000, andernfalls bei 48 bis 50.000 (Standard: -1). | INT | Ja | -1 oder 48 bis 50000 |
| `model.texture` | Auflösung der Basisfarbtextur: standard ist 2K, detailed 4K und extreme 8K. `"none"` gibt ein untexturiertes Netz zurück (Standard: `"standard"`). | COMBO | Ja | `"standard"`<br>`"detailed"`<br>`"extreme"`<br>`"none"` |
| `model.pbr` | Fügt der Basisfarbe Metallic-, Rauheits- und Normal-Maps hinzu. Wird ignoriert, wenn `model.texture` auf `"none"` gesetzt ist (Standard: True). | BOOLEAN | Ja | True/False |
| `model.model_seed` | Seed für die Geometrie (Standard: 42). | INT | Ja | 0 bis 2147483647 |
| `model.texture_alignment` | Passt die Farben an das Eingabebild an oder richtet die Texturen an der generierten Geometrie aus. Wird ignoriert, wenn `model.texture` auf `"none"` gesetzt ist (Standard: `"original_image"`). Erweiterte Einstellung. | COMBO | Ja | `"original_image"`<br>`"geometry"` |
| `model.orientation` | `"align_image"` dreht das Modell auf den Blickwinkel des Eingabebilds. Wird ignoriert, wenn `model.texture` auf `"none"` gesetzt ist (Standard: `"default"`). Erweiterte Einstellung. | COMBO | Ja | `"default"`<br>`"align_image"` |
| `model.enable_image_autofix` | Lässt Tripo ein niedrig aufgelöstes oder qualitativ schlechtes Bild vor der Modellierung verbessern (Standard: False). Erweiterte Einstellung. | BOOLEAN | Ja | True/False |
| `model.texture_seed` | Seed für die Texturen (Standard: 42). Erweiterte Einstellung. | INT | Ja | 0 bis 2147483647 |
| `model.auto_size` | Skaliert das Modell über seine Szenentransformation auf seine reale Größe in Metern. Wird ignoriert, wenn `model.texture` auf `"none"` gesetzt ist (Standard: False). Erweiterte Einstellung. | BOOLEAN | Ja | True/False |
| `model.export_uv` | Führt ein UV-Unwrap des Netzes durch, wenn es untexturiert ist. Texturierte Netze werden immer entfaltet (Standard: True). Erweiterte Einstellung. | BOOLEAN | Ja | True/False |
| `model.compress_geometry` | Wendet Meshopt-Geometriekompression an: deutlich kleinere Dateien, aber die 3D-Vorschau von ComfyUI kann sie nicht anzeigen. Wird bei Quad-Netzen ignoriert (Standard: False). Erweiterte Einstellung. | BOOLEAN | Ja | True/False |

**Hinweise:**

- `model.image` ist erforderlich, und es wird nur das erste Bild des Stapels verwendet.
- `model.face_limit` ist ein Zielwert und keine harte Obergrenze, daher kann das Ergebnis mehr Flächen enthalten als angefordert. `-1` überlässt die Wahl Tripo.
- `model.quad` entscheidet, welche Ausgabe das Netz enthält. Ist es aktiviert, kommt das Modell an der FBX-Ausgabe an und die GLB-Ausgabe bleibt leer; ist es deaktiviert, kommt das Modell an GLB an und FBX bleibt leer. Der Node löst einen Fehler aus, wenn die leere Ausgabe die von Ihnen verbundene ist.
- `model.texture`, `model.pbr`, `model.texture_seed`, `model.auto_size`, `model.texture_alignment` und `model.orientation` gelten nur für texturierte Modelle: Bei `"none"` sendet der Node keine Textur-Einstellungen und gibt reine Geometrie zurück.
- `model.compress_geometry` hat keine Auswirkung auf Quad-Netze.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `model task_id` | Die eindeutige Task-ID für die Modellgenerierungsanfrage. | MODEL_TASK_ID |
| `GLB` | Das generierte 3D-Modell im GLB-Format. Leer, wenn `model.quad` aktiviert ist. | FILE3DGLB |
| `FBX` | Das generierte 3D-Modell im FBX-Format. Wird nur befüllt, wenn `model.quad` aktiviert ist. | FILE3DFBX |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoPSeriesImageToModelNode/de.md)

---
**Source fingerprint (SHA-256):** `9bfad31ee00546d0603ce3273502cfc93c79e3b125941fed255866aa83f770a5`
