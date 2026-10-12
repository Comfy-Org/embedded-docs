# Tripo: Retopologie

Tripo: Retopology nimmt ein hochauflösendes 3D-Modell, das von einem früheren Tripo-Node generiert wurde, und erstellt daraus eine niedrig aufgelöste Version mit sauberer Topologie. Es übermittelt das Modell an den Tripo-Retopology-Dienst, wartet auf den Abschluss der Aufgabe, lädt anschließend das fertige Modell herunter und stellt dessen Task-ID für die Verwendung durch andere Tripo-Nodes bereit.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model_task_id` | Task-ID des hochauflösenden Quellmodells. Akzeptiert eine Modell-Task-ID von einem Tripo-Generierungs-Node oder eine Segment-Task-ID von Tripo: Segment Model. | STRING | Ja | Tripo task ID |
| `face_limit` | Zielanzahl der Flächen: 500–20.000 Dreiecke oder 500–10.000 Quads. -1 überlässt die Wahl Tripo. (Standard: -1) | INT | Ja | -1 (automatisch)<br>500 bis 20.000 (Dreiecke)<br>500 bis 10.000 (Quads) |
| `quad` | Ausgabe als Quad-Mesh. Tripo liefert Quad-Meshes als FBX, daher erscheint das Ergebnis am FBX-Ausgang und der GLB-Ausgang bleibt leer. (Standard: False) | BOOLEAN | Ja | True<br>False (Standard) |
| `bake` | Backt die Quelltexturen auf das niedrig aufgelöste Mesh. (Standard: True) | BOOLEAN | Nein | True (Standard)<br>False |
| `part_names` | Kommagetrennte Part-Namen von Tripo: Segment Model. Leer verarbeitet das gesamte Modell. (Standard: "") | STRING | Nein | Modell-Part-Namen oder leer |

Hinweis: Wenn `face_limit` auf -1 gesetzt ist, entscheidet Tripo die Flächenanzahl automatisch. Wenn `quad` aktiviert ist, beträgt das maximale Flächenlimit 10.000 Quads statt 20.000 Dreiecke, und das Ergebnis wird als FBX bereitgestellt (der GLB-Ausgang bleibt leer). Wenn `part_names` leer ist, wird das gesamte Modell verarbeitet. Wenn `face_limit` einen anderen Wert als -1 hat und außerhalb des zulässigen Bereichs liegt, gibt der Node einen Fehler aus.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `model_file` | Abwärtskompatible Ausgabe, die die fertige Modelldatei identifiziert. Neuere Workflows sollten stattdessen die GLB- oder FBX-Ausgaben verwenden. | STRING |
| `model task_id` | Task-ID des fertigen Retopology-Ergebnisses. Kann an andere Tripo-Nodes übergeben werden, um auf dieses Modell zu verweisen. | STRING |
| `GLB` | Das retopologisierte niedrig aufgelöste Modell im GLB-Format. Leer, wenn `quad` aktiviert ist. | GLB FILE |
| `FBX` | Das retopologisierte niedrig aufgelöste Modell im FBX-Format. Nur befüllt, wenn `quad` aktiviert ist. | FBX FILE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoRetopologyNode/de.md)

---
**Source fingerprint (SHA-256):** `b0e967eb4987a70242b6cfce93f09e0caffb7f4bdd3e4f1439e68f33f9138bb5`
