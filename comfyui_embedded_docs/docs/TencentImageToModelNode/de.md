# Hunyuan3D: Bild(er) zu Modell

Dieser Node verwendet die Hunyuan3D Pro API von Tencent, um aus einem oder mehreren Eingabebildern ein 3D-Modell zu generieren. Er verarbeitet die Bilder, sendet sie an die API und gibt die generierten 3D-Modell-Dateien in den Formaten GLB und OBJ sowie optionale Texturkarten zurück.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model` | Die Version des zu verwendenden Hunyuan3D-Modells. Die LowPoly-Option ist für das Modell `3.1` nicht verfügbar. | COMBO | Ja | `"3.0"`<br>`"3.1"` |
| `image` | Das primäre Eingabebild, das zur Generierung des 3D-Modells verwendet wird. Muss mindestens 128x128 Pixel groß sein. | IMAGE | Ja | - |
| `image_left` | Ein optionales Bild der linken Seite des Objekts für die Multi-View-Generierung. Muss mindestens 128x128 Pixel groß sein. | IMAGE | Nein | - |
| `image_right` | Ein optionales Bild der rechten Seite des Objekts für die Multi-View-Generierung. Muss mindestens 128x128 Pixel groß sein. | IMAGE | Nein | - |
| `image_back` | Ein optionales Bild der Rückseite des Objekts für die Multi-View-Generierung. Muss mindestens 128x128 Pixel groß sein. | IMAGE | Nein | - |
| `face_count` | Die Zielanzahl der Flächen für das generierte 3D-Modell (Standard: 500000). | INT | Ja | 3000 - 1500000 |
| `generate_type` | Der Typ des zu generierenden 3D-Modells. Die Auswahl einer Option blendet zusätzliche zugehörige Parameter ein. | DYNAMICCOMBO | Ja | `"Normal"`<br>`"LowPoly"`<br>`"Geometry"` |
| `generate_type.pbr` | Aktiviert die Generierung von Materialien mit Physically Based Rendering (PBR). Dieser Parameter ist nur sichtbar, wenn `generate_type` auf "Normal" oder "LowPoly" gesetzt ist (Standard: False). | BOOLEAN | Nein | - |
| `generate_type.polygon_type` | Der Typ des Polygons, das für das Mesh verwendet werden soll. Dieser Parameter ist nur sichtbar, wenn `generate_type` auf "LowPoly" gesetzt ist. | COMBO | Nein | `"triangle"`<br>`"quadrilateral"` |
| `seed` | Ein Seed-Wert für den Generierungsprozess. Der Seed steuert, ob der Node erneut ausgeführt werden soll; die Ergebnisse sind unabhängig vom Seed nicht deterministisch (Standard: 0). | INT | Ja | 0 - 2147483647 |

**Hinweis:** Alle Eingabebilder müssen eine Mindestbreite und -höhe von 128 Pixeln haben. Bilder werden automatisch herunterskaliert, wenn sie auf ihrer längsten Seite 4900 Pixel überschreiten.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `model_file` | Eine veraltete Ausgabe für Abwärtskompatibilität. | STRING |
| `GLB` | Das generierte 3D-Modell im GLB-Dateiformat (Binary GL Transmission Format). | FILE3DGLB |
| `OBJ` | Das generierte 3D-Modell im OBJ-Dateiformat (Wavefront). | FILE3DOBJ |
| `texture_image` | Das Texturbild für das generierte 3D-Modell. | IMAGE |
| `optional_metallic` | Die Metallic-Map für PBR-Materialien. Gibt ein schwarzes Bild zurück, wenn nicht verfügbar. | IMAGE |
| `optional_normal` | Die Normal-Map für PBR-Materialien. Gibt ein schwarzes Bild zurück, wenn nicht verfügbar. | IMAGE |
| `optional_roughness` | Die Roughness-Map für PBR-Materialien. Gibt ein schwarzes Bild zurück, wenn nicht verfügbar. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TencentImageToModelNode/de.md)

---
**Source fingerprint (SHA-256):** `fe422cfa714dbff7cd5dabb286d93d59afe9a01daf711ca09ebcf47ef100a52e`
