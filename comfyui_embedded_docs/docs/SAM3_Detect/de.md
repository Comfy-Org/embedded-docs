# SAM3 Erkennung

## Überblick

Der Node SAM3 Detect führt Open-Vocabulary-Erkennung und Segmentierung mithilfe von Textbeschreibungen, Bounding-Boxen oder Punkt-Prompts durch. Er kann Objekte in einem Bild identifizieren und segmentieren, basierend darauf, was Sie im Text beschreiben, wo Sie Boxen zeichnen oder wo Sie Punkte setzen.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model` | Das SAM3-Modell, das für Erkennung und Segmentierung verwendet wird | MODEL | Ja | - |
| `image` | Das zu verarbeitende Eingabebild | IMAGE | Ja | - |
| `conditioning` | Text-Konditionierung aus CLIPTextEncode. Erforderlich, wenn Text-Prompts für die Erkennung verwendet werden | CONDITIONING | Nein | - |
| `bboxes` | Bounding-Boxen, innerhalb derer segmentiert werden soll. Kann eine einzelne Box (auf alle Frames angewendet), eine Liste von Boxen (auf alle Frames angewendet) oder eine Liste von Listen (Boxen pro Frame) sein. Wenn sie ohne Text-Konditionierung bereitgestellt werden, segmentiert der Node innerhalb jeder Box | BOUNDING_BOX | Nein | - |
| `positive_coords` | Positive Punkt-Prompts im JSON-Format `[{"x": int, "y": int}, ...]` mit Pixelkoordinaten. Dies sind Punkte, die in die Segmentierung einbezogen werden sollen | STRING | Nein | - |
| `negative_coords` | Negative Punkt-Prompts im JSON-Format `[{"x": int, "y": int}, ...]` mit Pixelkoordinaten. Dies sind Punkte, die aus der Segmentierung ausgeschlossen werden sollen | STRING | Nein | - |
| `threshold` | Konfidenzschwellenwert für textbasierte Erkennungen. Nur Erkennungen mit Scores über diesem Wert werden beibehalten (Standard: 0.5) | FLOAT | Nein | 0.0 to 1.0 |
| `refine_iterations` | Anzahl der SAM-Decoder-Verfeinerungsdurchläufe. Höhere Werte können die Maskenqualität verbessern. Auf 0 setzen, um rohe Detektor-Masken ohne Verfeinerung zu verwenden (Standard: 2) | INT | Nein | 0 to 5 |
| `individual_masks` | Wenn aktiviert, werden separate Masken für jedes erkannte Objekt ausgegeben, anstatt sie zu einer einzigen Maske zusammenzufassen (Standard: False) | BOOLEAN | Nein | True/False |

### Parameterbeschränkungen und Hinweise

- **Text-Prompts**: Um textbasierte Erkennung zu verwenden, müssen Sie die Eingabe `conditioning` bereitstellen. Wenn Text-Konditionierung bereitgestellt wird, führt der Node eine textgesteuerte Erkennung auf dem Bild aus.
- **Box-Prompts**: Wenn `bboxes` ohne Text-Konditionierung bereitgestellt werden, segmentiert der Node den Bereich innerhalb jeder Bounding-Box.
- **Punkt-Prompts**: Wenn `positive_coords` oder `negative_coords` bereitgestellt werden, verwendet der Node punktbasierte Segmentierung. Punkte werden automatisch auf die interne Auflösung des Modells skaliert.
- **Mehrere Prompt-Typen**: Sie können verschiedene Prompt-Typen kombinieren. Zum Beispiel können Sie sowohl Text-Konditionierung als auch Bounding-Boxen bereitstellen, um die Texterkennung auf bestimmte Bereiche zu beschränken.
- **Batch-Verarbeitung**: Der Node unterstützt gebatchte Bilder. Bei der Verarbeitung mehrerer Frames können Bounding-Boxen pro Frame im Format einer Liste von Listen bereitgestellt werden.
- **JSON-Format für Punkte**: Punktkoordinaten müssen als gültige JSON-Strings im Format `[{"x": 100, "y": 200}, {"x": 150, "y": 250}]` bereitgestellt werden.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `masks` | Segmentierungsmasken. Wenn `individual_masks` False ist (Standard), wird eine einzelne kombinierte Maske pro Frame zurückgegeben. Wenn True, werden individuelle Masken für jedes erkannte Objekt zurückgegeben | MASK |
| `bboxes` | Erkannte Bounding-Boxen mit Koordinaten und Konfidenzwerten. Jede Box enthält Werte für `x`, `y`, `width`, `height` und `score` | BOUNDING_BOX |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SAM3_Detect/de.md)

---
**Source fingerprint (SHA-256):** `3f61343c284c249476f2010831863c6094260b11d0a348003b270a126c67d399`
