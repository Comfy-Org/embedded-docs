# Tripo P2: Text zu Modell

Erzeugt aus einem Text-Prompt ein Low-Poly-3D-Modell mit sauberer Topologie unter Verwendung des P2-Modells von Tripo. Das Ergebnis wird als Dreiecksnetz (GLB) zurückgegeben oder, wenn `model.quad` aktiviert ist, als quad-dominantes Netz (FBX).

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model` | Zu verwendendes Modell der Tripo P-Serie. Wenn Sie ein Modell auswählen, werden unten dessen eigene Eingaben angezeigt. | DYNAMIC_COMBO | Ja | `"P2"` |

### P2 Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model.prompt` | Textbeschreibung des zu erzeugenden 3D-Modells. Darf nicht leer sein, bis zu 1024 Zeichen (Standard: leer). | STRING | Ja | Bis zu 1024 Zeichen |
| `model.negative_prompt` | Textbeschreibung dessen, was im erzeugten Modell vermieden werden soll (Standard: leer). | STRING | Nein | Bis zu 255 Zeichen |
| `model.quad` | Gibt statt eines Dreiecksnetzes auf der GLB-Ausgabe ein quad-dominantes Netz auf der FBX-Ausgabe zurück (Standard: False). | BOOLEAN | Ja | True/False |
| `model.face_limit` | Zielanzahl der Flächen. `-1` lässt Tripo wählen. Wenn `model.quad` aktiviert ist, liegt das Limit bei 48 bis 25.000, andernfalls bei 48 bis 50.000 (Standard: -1). | INT | Ja | -1 oder 48 bis 50000 |
| `model.texture` | Auflösung der Basisfarbtextur: standard ist 2K, detailed 4K und extreme 8K. `"none"` gibt ein untexturiertes Netz zurück (Standard: `"standard"`). | COMBO | Ja | `"standard"`<br>`"detailed"`<br>`"extreme"`<br>`"none"` |
| `model.pbr` | Fügt der Basisfarbe Metallic-, Rauheits- und Normal-Maps hinzu. Wird ignoriert, wenn `model.texture` auf `"none"` gesetzt ist (Standard: True). | BOOLEAN | Ja | True/False |
| `model.model_seed` | Seed für die Geometrie (Standard: 42). | INT | Ja | 0 bis 2147483647 |
| `model.image_seed` | Seed für das Bild, das Tripo vor der Modellierung aus dem Prompt erzeugt (Standard: 42). Erweiterte Einstellung. | INT | Ja | 0 bis 2147483647 |
| `model.texture_seed` | Seed für die Texturen (Standard: 42). Erweiterte Einstellung. | INT | Ja | 0 bis 2147483647 |
| `model.auto_size` | Skaliert das Modell über seine Szenentransformation auf seine reale Größe in Metern. Wird ignoriert, wenn `model.texture` auf `"none"` gesetzt ist (Standard: False). Erweiterte Einstellung. | BOOLEAN | Ja | True/False |
| `model.export_uv` | Führt ein UV-Unwrap des Netzes durch, wenn es untexturiert ist. Texturierte Netze werden immer entfaltet (Standard: True). Erweiterte Einstellung. | BOOLEAN | Ja | True/False |
| `model.compress_geometry` | Wendet meshopt-Geometriekompression an: deutlich kleinere Dateien, aber die 3D-Vorschau von ComfyUI kann sie nicht anzeigen. Wird bei Quad-Netzen ignoriert (Standard: False). Erweiterte Einstellung. | BOOLEAN | Ja | True/False |

**Hinweise:**

- `model.prompt` ist erforderlich; `model.negative_prompt` ist optional und auf 255 Zeichen begrenzt.
- `model.face_limit` ist ein Zielwert und keine harte Obergrenze, daher kann das Ergebnis mehr Flächen enthalten als angefordert. `-1` überlässt die Wahl Tripo.
- `model.quad` entscheidet, welche Ausgabe das Netz enthält. Wenn es aktiviert ist, kommt das Modell auf der FBX-Ausgabe an und die GLB-Ausgabe bleibt leer; wenn es deaktiviert ist, kommt das Modell auf GLB an und FBX bleibt leer. Der Node löst einen Fehler aus, wenn die leere Ausgabe diejenige ist, die Sie verbunden haben.
- `model.texture`, `model.pbr`, `model.texture_seed` und `model.auto_size` gelten nur für texturierte Modelle: Bei `"none"` sendet der Node keine Textur-Einstellungen und gibt reine Geometrie zurück.
- `model.compress_geometry` hat keine Auswirkung auf Quad-Netze.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `model task_id` | Die eindeutige Task-ID für die Modellgenerierungsanfrage. | MODEL_TASK_ID |
| `GLB` | Das erzeugte 3D-Modell im GLB-Format. Leer, wenn `model.quad` aktiviert ist. | FILE3DGLB |
| `FBX` | Das erzeugte 3D-Modell im FBX-Format. Nur befüllt, wenn `model.quad` aktiviert ist. | FILE3DFBX |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoPSeriesTextToModelNode/de.md)

---
**Source fingerprint (SHA-256):** `e55596c1a237cf6b92e3bdead4359f380c6cba60992dcc61b5ee4e6b1bdd843b`
