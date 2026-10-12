# Tripo: Mehransichten zu Modell

Dieser Node generiert 3D-Modelle synchron mithilfe der Tripo-API, indem er bis zu vier Bilder verarbeitet, die verschiedene Ansichten eines Objekts zeigen (Vorderseite, linke Seite, Rückseite, rechte Seite). Er erfordert ein Frontbild und mindestens eine zusätzliche Ansicht (links, hinten oder rechts), um das 3D-Modell zu erstellen. Textur, PBR-Material, Geometriequalität und Ausgabeformat können im Node gesteuert werden.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|--------|
| `image` | Vorderansicht des Objekts. | IMAGE | Ja | - |
| `image_left` | Linke Ansicht des Objekts. | IMAGE | Nein | - |
| `image_back` | Rückansicht des Objekts. | IMAGE | Nein | - |
| `image_right` | Rechte Ansicht des Objekts. | IMAGE | Nein | - |
| `model_version` | Die Modellversion, die für die Generierung verwendet wird. | COMBO | Nein | Mehrere Optionen verfügbar |
| `orientation` | Ausrichtungseinstellung für das 3D-Modell (Standard: `"default"`). | COMBO | Nein | Mehrere Optionen verfügbar |
| `texture` | Texturkarten generieren. Deaktiviert liefert reine Geometrie und ignoriert pbr. (Standard: True) | BOOLEAN | Nein | - |
| `pbr` | PBR-Materialkarten (Basisfarbe, Metallic, Rauheit, Normal). Erfordert Textur. (Standard: True) | BOOLEAN | Nein | - |
| `model_seed` | Zufälliger Seed für die Modellgenerierung (Standard: 42). | INT | Nein | 0 bis 2,147,483,647 |
| `texture_seed` | Zufälliger Seed für die Texturgenerierung (Standard: 42). | INT | Nein | 0 bis 2,147,483,647 |
| `texture_quality` | Qualitätsstufe für die Texturgenerierung (Standard: `"standard"`). `"detailed"` = HD-Texturen, `"extreme"` = 8K-Ultra-Texturen. | COMBO | Nein | `"standard"`<br>`"detailed"`<br>`"extreme"` |
| `texture_alignment` | Methode zur Ausrichtung der Texturen am Modell (Standard: `"original_image"`). | COMBO | Nein | `"original_image"`<br>`"geometry"` |
| `face_limit` | Maximale Anzahl an Flächen. -1 lässt Tripo adaptiv wählen (etwa 1,4 Mio. Flächen bei v3.x-Standard, 2 Mio. bei detailed). Tripo begrenzt stillschweigend: v2.5 bei 500.000, Quad-Meshes bei 150.000. (Standard: -1) | INT | Nein | -1 bis 2,000,000 |
| `quad` | Quad-Mesh-Ausgabe. Tripo liefert Quad-Meshes als FBX, sodass das Ergebnis am FBX-Ausgang ankommt und der GLB-Ausgang leer bleibt. (Standard: False) | BOOLEAN | Nein | - |
| `geometry_quality` | Qualitätsstufe für die Geometriegenerierung (Standard: `"standard"`). | COMBO | Nein | `"standard"`<br>`"detailed"` |
| `smart_low_poly` | Low-Poly-Mesh mit sauberer Topologie im handgefertigten Stil (500–20.000 Flächen, Quad 500–10.000). Am besten für einfache Motive geeignet; komplexe können fehlschlagen. (Standard: False) | BOOLEAN | Nein | - |
| `auto_size` | Skaliert texturierte Modelle auf ihre reale Größe in Metern. Tripo speichert die Größe als Szenentransformation des Modells und integriert sie, wenn das Modell konvertiert, geriggt oder retargetet wird; ohne Textur wird sie ignoriert. (Standard: False) | BOOLEAN | Nein | - |

**Hinweis:** Das Frontbild (`image`) ist immer erforderlich, und mindestens eines von `image_left`, `image_back` oder `image_right` muss ebenfalls angegeben werden. Wenn `texture` deaktiviert wird, wird `pbr` automatisch ebenfalls deaktiviert, da `pbr` Textur erfordert. Wenn `smart_low_poly` aktiviert ist und `face_limit` nicht auf -1 belassen wird, muss `face_limit` zwischen 500 und 20.000 für Dreiecks-Meshes oder zwischen 500 und 10.000 für Quad-Meshes liegen.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|--------------|--------------|----------|
| `model_file` | Dateipfad oder Kennung für das generierte 3D-Modell (nur zur Abwärtskompatibilität). | STRING |
| `model task_id` | Aufgabenkennung zur Nachverfolgung des Modellgenerierungsprozesses. | MODEL_TASK_ID |
| `GLB` | Die generierte 3D-Modelldatei im GLB-Format. Leer, wenn `quad` aktiviert ist. | FILE3DGLB |
| `FBX` | Die generierte 3D-Modelldatei im FBX-Format. Nur befüllt, wenn `quad` aktiviert ist. | FILE3DFBX |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoMultiviewToModelNode/de.md)

---
**Source fingerprint (SHA-256):** `b66df4cad6167fa27edf1fe21b96cb47af90027b3fbe0a3c9c14101506281ed7`
