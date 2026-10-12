# Tripo: Text zu Modell

Erzeugt mithilfe des Tripo-Dienstes ein 3D-Modell aus einer Textbeschreibung. Der Node sendet den Prompt und die Einstellungen an Tripo, wartet auf den Abschluss der Generierungsaufgabe und gibt die fertige 3D-Datei zusammen mit der Aufgabenkennung zurück.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Die Textbeschreibung des zu generierenden Modells. Darf nicht leer sein. | STRING | Ja | Mehrzeiliger Text |
| `negative_prompt` | Text, der beschreibt, was im generierten Modell nicht erscheinen soll. Bis zu 255 Zeichen. | STRING | Nein | Mehrzeiliger Text, max. 255 Zeichen |
| `model_version` | Die für die Generierung verwendete Tripo-Modellversion (Standard: `v3.1_20260211`). | COMBO | Nein | Liste der unterstützten Tripo-Modellversionen |
| `texture` | Texturkarten generieren. Aus liefert reine Geometrie und ignoriert `pbr` (Standard: True). | BOOLEAN | Nein | True<br>False |
| `pbr` | PBR-Materialkarten (Basisfarbe, Metallic, Roughness, Normal). Erfordert `texture` (Standard: True). | BOOLEAN | Nein | True<br>False |
| `image_seed` | Seed-Wert für die Bilderzeugung (Standard: 42). | INT | Nein | 0 bis 2147483647 |
| `model_seed` | Seed-Wert für die Modellgenerierung (Standard: 42). | INT | Nein | 0 bis 2147483647 |
| `texture_seed` | Seed-Wert für die Texturgenerierung (Standard: 42). | INT | Nein | 0 bis 2147483647 |
| `texture_quality` | Texturdetailgrad (Standard: "standard"). "detailed" = HD-Texturen, "extreme" = 8K-Ultra-Texturen. | COMBO | Nein | `"standard"`<br>`"detailed"`<br>`"extreme"` |
| `face_limit` | Maximale Flächenanzahl. -1 lässt Tripo adaptiv wählen (etwa 1,4 Mio. Flächen bei v3.x standard, 2 Mio. bei detailed). Tripo begrenzt stillschweigend: v2.5 bei 500.000, Quad-Meshes bei 150.000 (Standard: -1). | INT | Nein | -1 bis 2000000 |
| `quad` | Quad-Mesh-Ausgabe. Tripo liefert Quad-Meshes als FBX, daher kommt das Ergebnis an der FBX-Ausgabe an und die GLB-Ausgabe bleibt leer (Standard: False). | BOOLEAN | Nein | True<br>False |
| `geometry_quality` | Geometriedetailgrad (Standard: "standard"). | COMBO | Nein | `"standard"`<br>`"detailed"` |
| `smart_low_poly` | Low-Poly-Mesh mit sauberer, handgefertigt wirkender Topologie (500–20.000 Flächen, Quad 500–10.000). Am besten für einfache Motive geeignet; komplexe können fehlschlagen (Standard: False). | BOOLEAN | Nein | True<br>False |
| `auto_size` | Skaliert texturierte Modelle auf ihre reale Größe in Metern. Tripo speichert die Größe als Szenentransformation des Modells und backt sie ein, wenn das Modell konvertiert, geriggt oder retargetet wird; ohne Textur ignoriert (Standard: True). | BOOLEAN | Nein | True<br>False |

### Hinweise

- `prompt` ist erforderlich und darf nicht leer oder nur aus Leerzeichen bestehen.
- Wenn `texture` auf False gesetzt ist, wird `pbr` zwangsweise deaktiviert und `auto_size` hat keine Wirkung.
- Wenn `smart_low_poly` aktiviert ist und `face_limit` nicht -1 ist, muss `face_limit` bei Dreiecks-Meshes zwischen 500 und 20.000 liegen, oder zwischen 500 und 10.000, wenn `quad` aktiviert ist.
- Wenn `quad` aktiviert ist, gibt Tripo eine FBX-Datei zurück, sodass die `GLB`-Ausgabe leer bleibt und die `FBX`-Ausgabe befüllt wird.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `model task_id` | Kennung der Tripo-Generierungsaufgabe, die das Modell erzeugt hat. | MODEL_TASK_ID |
| `GLB` | Das generierte Modell im GLB-Format. Leer, wenn `quad` aktiviert ist. | FILE3D_GLB |
| `FBX` | Das generierte Modell im FBX-Format. Wird nur befüllt, wenn `quad` aktiviert ist. | FILE3D_FBX |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoTextToModelNodeV2/de.md)

---
**Source fingerprint (SHA-256):** `8af7044188c6dbb87d23298bf7b99fe826bdc7bd7ba0948db2066887274faa00`
