# Bounding Boxes zeichnen

Der Node DrawBBoxes visualisiert Ergebnisse der Objekterkennung, indem er Bounding-Boxen, Beschriftungen und Konfidenzwerte auf ein Bild zeichnet. Wenn kein Eingabebild bereitgestellt wird, erstellt er eine leere Zeichenfläche, die groß genug ist, um alle gezeichneten Boxen aufzunehmen. Er unterstützt Stapelverarbeitung, sodass Sie verschiedene Erkennungssätze für mehrere Bilder zeichnen oder dieselben Erkennungen über einen Stapel hinweg wiederholen können.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `image` | Das/die Eingabebild(er), auf das/die die Bounding-Boxen gezeichnet werden. Wenn nicht angegeben, wird eine leere Zeichenfläche erzeugt. | IMAGE | Nein | - |
| `bboxes` | Eine Liste von Wörterbüchern für Bounding-Boxen. Jedes Wörterbuch sollte Schlüssel für `x`, `y`, `width`, `height` und optional `label` und `score` enthalten. | BOUNDINGBOX | Ja | - |

**Eingabebeschränkungen:**
*   Die Eingabe `bboxes` ist erforderlich und muss bereitgestellt werden.
*   Der Node verarbeitet automatisch verschiedene Eingabeformate für `bboxes`. Ein einzelnes Wörterbuch wird auf alle Bilder im Stapel angewendet. Eine flache Liste von Wörterbüchern wird als derselbe Satz von Erkennungen für jedes Bild behandelt. Eine Liste von Listen ermöglicht es Ihnen, unterschiedliche Erkennungen für jedes Bild im Stapel anzugeben.
*   Wenn kein `image` bereitgestellt wird, erstellt der Node ein leeres Bild mit Abmessungen, die groß genug sind, um alle bereitgestellten Bounding-Boxen aufzunehmen, mit einer Standardmindestgröße von 640x640.
*   Das Feld `label` wird mit den Klassen des COCO-Datensatzes abgeglichen, eine COCO-Klasse erhält also immer dieselbe Farbe. Eine Beschriftung, die keine COCO-Klasse ist, wird trotzdem gezeichnet und bekommt die Palettenfarbe entsprechend ihrer Position unter den Beschriftungen dieses Bildes; eine Box ohne `score` wird nur mit ihrer Beschriftung gezeichnet.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `out_image` | Das/die Ausgabebild(er) mit den darübergelegten gezeichneten Bounding-Boxen, Beschriftungen und Konfidenzwerten. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DrawBBoxes/de.md)

---
**Source fingerprint (SHA-256):** `3a25677852fe1f0c137a011628ba0197034c3724281941f88a27e1ae1abfe48e`
