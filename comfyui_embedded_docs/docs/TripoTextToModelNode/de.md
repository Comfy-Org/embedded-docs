# Tripo: Text zu Modell (veraltet)

Dieser Legacy-Node generiert fertige 3D-Modelle aus einer Textbeschreibung mithilfe der Tripo-API. Er wartet, bis die Generierung abgeschlossen ist, und gibt dann die Modelldatei zurück, optional mit Texturen und PBR-Materialien. Er ist als veraltet markiert und bleibt für ältere Workflows erhalten.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Textbeschreibung des zu generierenden 3D-Modells (mehrzeilig). Dieser Parameter ist erforderlich und darf nicht leer sein. | STRING | Ja | - |
| `negative_prompt` | Textbeschreibung dessen, was im generierten Modell vermieden werden soll (mehrzeilig). Bis zu 255 Zeichen. Wird nur an die API gesendet, wenn nicht leer. | STRING | Nein | Bis zu 255 Zeichen |
| `model_version` | Version des Tripo-Modells, die für die Generierung verwendet werden soll (Standard: v3_1_20260211). | COMBO | Nein | Mehrere Optionen verfügbar |
| `style` | Wird von Tripo nicht mehr unterstützt und ignoriert. Für ältere Workflows beibehalten (Standard: "None"). | COMBO | Nein | Mehrere Optionen verfügbar |
| `texture` | Texturkarten generieren. Wenn deaktiviert, wird reine Geometrie zurückgegeben und `pbr` ignoriert (Standard: True). | BOOLEAN | Nein | true / false |
| `pbr` | PBR-Materialkarten (Basisfarbe, Metallic, Rauheit, Normal). Erfordert `texture`; wird zwangsweise deaktiviert, wenn `texture` deaktiviert ist (Standard: True). | BOOLEAN | Nein | true / false |
| `image_seed` | Seed für die Bildgenerierungsphase (Standard: 42). | INT | Nein | 0 bis 2147483647 |
| `model_seed` | Seed für die Modellgenerierungsphase (Standard: 42). | INT | Nein | 0 bis 2147483647 |
| `texture_seed` | Seed für die Texturgenerierungsphase (Standard: 42). | INT | Nein | 0 bis 2147483647 |
| `texture_quality` | Qualität der generierten Texturen. detailed = HD-Texturen, extreme = 8K-Ultra-Texturen (Standard: standard). | COMBO | Nein | "standard"<br>"detailed"<br>"extreme" |
| `face_limit` | Maximale Face-Anzahl. -1 lässt Tripo adaptiv wählen (etwa 1,4 Mio. Flächen bei v3.x standard, 2 Mio. bei detailed). Tripo begrenzt stillschweigend: v2.5 bei 500.000, Quad-Meshes bei 150.000. (Standard: -1) | INT | Nein | -1 bis 2000000 |
| `quad` | Quad-Mesh-Ausgabe. Tripo liefert Quad-Meshes als FBX, daher wird das Ergebnis über die FBX-Ausgabe geliefert und die GLB-Ausgabe bleibt leer. (Standard: False) | BOOLEAN | Nein | true / false |
| `geometry_quality` | Qualität der generierten Geometrie (Standard: standard). | COMBO | Nein | "standard"<br>"detailed" |
| `smart_low_poly` | Low-Poly-Mesh mit sauberer, handgefertigt anmutender Topologie (500-20.000 Flächen, Quad 500-10.000). Am besten für einfache Motive geeignet; komplexe können fehlschlagen. (Standard: False) | BOOLEAN | Nein | true / false |
| `auto_size` | Skaliert texturierte Modelle auf ihre reale Größe in Metern. Tripo speichert die Größe als Szenen-Transformation des Modells und backt sie ein, wenn das Modell konvertiert, geriggt oder retargetet wird; ohne Textur wird sie ignoriert. (Standard: True) | BOOLEAN | Nein | true / false |

**Hinweise:**
- Dieser Node ist veraltet und als Legacy-Node markiert. Er wird aus Gründen der Abwärtskompatibilität mit älteren Workflows beibehalten.
- Der Parameter `prompt` ist obligatorisch: Ein leerer Prompt führt dazu, dass der Node einen Fehler auslöst.
- `pbr` erfordert `texture`. Wenn `texture` deaktiviert ist, erzwingt der Node, dass `pbr` deaktiviert wird, und ignoriert dessen Wert. `auto_size` hat ebenfalls keine Wirkung ohne `texture`.
- Wenn `smart_low_poly` aktiviert ist und `face_limit` auf einen anderen Wert als -1 gesetzt ist, muss das Face-Limit für die Dreiecksausgabe zwischen 500 und 20.000 liegen, oder zwischen 500 und 10.000, wenn `quad` aktiviert ist; andernfalls löst der Node einen Fehler aus.
- Wenn `quad` aktiviert ist, wird das generierte Quad-Mesh als FBX geliefert, sodass die FBX-Ausgabe befüllt wird und die GLB-Ausgabe leer bleibt.
- Der Parameter `style` wird akzeptiert, aber ignoriert.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `model_file` | Der Dateiname des generierten 3D-Modells im Format `<task_id>.<format>`, nur aus Gründen der Abwärtskompatibilität beibehalten. | STRING |
| `model task_id` | Die eindeutige Aufgabenkennung für den Modellgenerierungsprozess. | MODEL_TASK_ID |
| `GLB` | Das generierte 3D-Modell im GLB-Format. Leer, wenn `quad` aktiviert ist. | FILE3DGLB |
| `FBX` | Das generierte 3D-Modell im FBX-Format. Nur befüllt, wenn `quad` aktiviert ist. | FILE3DFBX |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoTextToModelNode/de.md)

---
**Source fingerprint (SHA-256):** `c26c8437ea66d08f7f39865fedeaaf4cf8583ca64b368f3b767ea18918dd6c08`
