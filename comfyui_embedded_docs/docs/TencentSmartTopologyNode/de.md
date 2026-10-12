# Hunyuan3D: Intelligente Topologie

Dieser Node führt eine intelligente Retopologie an einem 3D-Modell durch und erzeugt automatisch ein neues, saubereres Mesh mit optimierter Polygonanzahl. Er stellt eine Verbindung zu einer Tencent Hunyuan 3D API her, um das Modell zu verarbeiten, und unterstützt die Dateiformate GLB und OBJ bis zu 200 MB. Der Node gibt das verarbeitete Modell als OBJ-Datei zurück.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `model_3d` | Eingabe-3D-Modell (GLB oder OBJ). Die Datei muss im GLB- oder OBJ-Format vorliegen und darf 200 MB nicht überschreiten. | FILE3D | Ja | - |
| `polygon_type` | Typ der Oberflächenzusammensetzung. | STRING | Ja | `"triangle"`<br>`"quadrilateral"` |
| `face_level` | Grad der Polygonreduzierung. | STRING | Ja | `"medium"`<br>`"high"`<br>`"low"` |
| `seed` | Der Seed steuert, ob der Node erneut ausgeführt werden soll; die Ergebnisse sind unabhängig vom Seed nicht deterministisch. (Standard: 0) | INT | Nein | 0 bis 2147483647 |

**Hinweis:** Der Parameter `seed` wird verwendet, um eine erneute Ausführung des Nodes auszulösen, aber es ist nicht garantiert, dass die endgültige Ausgabe bei demselben Seed-Wert identisch ist.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|--------------|----------|
| `OBJ` | Das verarbeitete 3D-Modell mit optimierter Topologie, zurückgegeben im OBJ-Format. | FILE3D |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TencentSmartTopologyNode/de.md)

---
**Source fingerprint (SHA-256):** `effbccb4d239ffb6b575fc547dd54cbb61aa4508502345cb5bef1d66b320926b`
