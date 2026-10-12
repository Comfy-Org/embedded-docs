# Tripo: Bild zu Modell (veraltet)

Generiert synchron 3D-Modelle basierend auf einem einzelnen Bild unter Verwendung der Tripo-API. Stellen Sie ein Eingabebild bereit, und der Node erstellt daraus ein fertiges 3D-Modell, mit optionalen Steuerungen für Modellversion, Texturgenerierung, Detailgrad und Ausgabeformat. Dies ist die Legacy-Version des Bild-zu-Modell-Nodes, die für ältere Workflows beibehalten wurde.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `image` | Das Eingabebild, das zur Generierung des 3D-Modells verwendet wird. Es muss ein Bild bereitgestellt werden, andernfalls löst der Node einen Fehler aus. | IMAGE | Ja | - |
| `model_version` | Die für die Generierung zu verwendende Modellversion. | COMBO | Nein | `"v1.4"`<br>`"v3.0"`<br>`"v3.5"`<br>`"v3.6"` |
| `style` | Wird von Tripo nicht mehr unterstützt und ignoriert. Für ältere Workflows beibehalten. (Standard: `"None"`) | COMBO | Nein | `"None"`<br>`"realistic"`<br>`"cartoon"`<br>`"sculpture"`<br>`"low_poly"` |
| `texture` | Textur-Maps generieren. Wenn deaktiviert, wird reine Geometrie zurückgegeben und `pbr` ignoriert. (Standard: True) | BOOLEAN | Nein | True<br>False |
| `pbr` | PBR-Material-Maps (Basisfarbe, Metallic, Rauheit, Normal). Erfordert `texture`. (Standard: True) | BOOLEAN | Nein | True<br>False |
| `model_seed` | Zufälliger Seed für die Modellgenerierung. (Standard: 42) | INT | Nein | 0 to 2147483647 |
| `orientation` | Ausrichtungseinstellung für das generierte Modell. (Standard: `"default"`) | COMBO | Nein | `"default"`<br>`"front"`<br>`"back"`<br>`"left"`<br>`"right"`<br>`"top"`<br>`"bottom"` |
| `texture_seed` | Zufälliger Seed für die Texturgenerierung. (Standard: 42) | INT | Nein | 0 to 2147483647 |
| `texture_quality` | Qualitätsstufe für die Texturgenerierung: `detailed` = HD-Texturen, `extreme` = 8K-Ultra-Texturen. (Standard: `"standard"`) | COMBO | Nein | `"standard"`<br>`"detailed"`<br>`"extreme"` |
| `texture_alignment` | Ausrichtungsmethode für das Textur-Mapping. (Standard: `"original_image"`) | COMBO | Nein | `"original_image"`<br>`"geometry"` |
| `face_limit` | Maximale Anzahl von Flächen. -1 lässt Tripo adaptiv wählen (etwa 1,4 Mio. Flächen bei v3.x Standard, 2 Mio. bei detailed). Tripo begrenzt stillschweigend: v2.5 bei 500.000, Quad-Meshes bei 150.000. (Standard: -1) | INT | Nein | -1 to 2000000 |
| `quad` | Quad-Mesh-Ausgabe. Tripo liefert Quad-Meshes als FBX, daher erscheint das Ergebnis an der FBX-Ausgabe und die GLB-Ausgabe bleibt leer. (Standard: False) | BOOLEAN | Nein | True<br>False |
| `geometry_quality` | Qualitätsstufe für die Geometriegenerierung. (Standard: `"standard"`) | COMBO | Nein | `"standard"`<br>`"detailed"` |
| `smart_low_poly` | Low-Poly-Mesh mit sauberer Topologie im handgefertigten Stil (500–20.000 Flächen, Quad 500–10.000). Am besten für einfache Motive geeignet; komplexe können fehlschlagen. (Standard: False) | BOOLEAN | Nein | True<br>False |
| `auto_size` | Skaliert texturierte Modelle auf ihre reale Größe in Metern. Tripo speichert die Größe als Szenen-Transformation des Modells und rechnet sie fest ein, wenn das Modell konvertiert, geriggt oder retargetet wird; ohne Textur wird sie ignoriert. (Standard: True) | BOOLEAN | Nein | True<br>False |

Hinweis: Ein `image` ist erforderlich; wenn es fehlt, löst der Node einen RuntimeError aus. Wenn `texture` False ist, enthält das Modell nur reine Geometrie und `pbr` wird auf False erzwungen. Wenn `smart_low_poly` aktiviert ist, muss `face_limit` zwischen 500 und 20.000 für Dreiecks-Meshes liegen oder zwischen 500 und 10.000, wenn `quad` ebenfalls aktiviert ist; ist der Grenzwert ungültig, löst der Node einen ValueError aus. Wenn `face_limit` auf -1 (Standard) gesetzt ist, wird kein expliziter Flächengrenzwert an die API gesendet, sodass Tripo adaptiv wählen kann.

## Ausgaben

| Ausgabenamen | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `model_file` | Die generierte 3D-Modell-Datei (nur zur Abwärtskompatibilität). | STRING |
| `model task_id` | Die Task-ID zum Verfolgen des Modellgenerierungsprozesses. | MODEL_TASK_ID |
| `GLB` | Das generierte 3D-Modell im GLB-Format. Leer, wenn `quad` aktiviert ist. | FILE3DGLB |
| `FBX` | Das generierte 3D-Modell im FBX-Format. Nur befüllt, wenn `quad` aktiviert ist. | FILE3DFBX |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoImageToModelNode/de.md)

---
**Source fingerprint (SHA-256):** `3b278abfd13329ee58ebab1bfeb47d32d09f4797f3d8628a35a028c3d15a7314`
