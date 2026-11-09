# WeVisOne-VL Detect

WeVisOne-VL Detect findet Objekte in einem Bild anhand eines Text-Prompts und gibt je nach gewählter Aufgabe Boxen, Alpha-Mattes, Punkte oder die Antwort des Modells selbst zurück. Es deckt Open-Vocabulary-Erkennung und -Segmentierung, Referring Expressions, Pointing, Zählen und OCR-Grounding ab und führt pro Bild im Batch einen Prompt aus.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `clip` | Der WeVisOne-VL-Textencoder, der den Checkpoint lädt. | CLIP | Ja | - |
| `image` | Das zu durchsuchende Bild oder der Bildstapel. | IMAGE | Ja | - |
| `task` | Was der Node zurückgeben soll. Segmentation gibt Boxen plus Alpha-Mattes zurück; detection, referring, ocr und ocr_grounding geben Boxen zurück; point und count_point geben Punkte zurück; count_box zählt und liefert Boxen; visual_prompt findet Objekte, die den Referenzboxen in `bboxes` ähneln; freeform sendet die Abfrage unverändert und gibt nur Text zurück (Standard: "segmentation"). | COMBO | Ja | `"segmentation"`<br>`"detection"`<br>`"referring"`<br>`"point"`<br>`"count_box"`<br>`"count_point"`<br>`"ocr"`<br>`"ocr_grounding"`<br>`"visual_prompt"`<br>`"freeform"` |
| `query` | Was in einfacher Sprache gefunden werden soll (zum Beispiel "die rote Tasse"). `detection` und `point` lesen eine Bezeichnung pro Zeile, `count_box` und `count_point` zählen das benannte Motiv, `ocr_grounding` sucht nach genau diesem Text, `visual_prompt` verwendet stattdessen `bboxes`, und `freeform` sendet ihn als vollständigen Prompt. `ocr` ignoriert ihn. | STRING | Ja | - |
| `bboxes` | Referenzboxen, die `visual_prompt` als Beispiele für das zu findende Objekt verwendet. | BOUNDING_BOX | Nein | - |
| `individual_masks` | Gibt eine Matte pro erkanntem Feld aus der Ausgabe `bboxes` Frame für Frame zurück, statt einer kombinierten Matte pro Frame (Standard: false). | BOOLEAN | Nein | true<br>false |
| `max_length` | Maximale Anzahl an Tokens, die das Modell für seine Antwort generieren darf (Standard: 4096). | INT | Ja | 1 bis 32768 |

**Hinweis:** Mattes werden nur gefüllt, wenn das Modell mit Objektreferenzen antwortet, was die Aufgabe segmentation verlangt. Andere Aufgaben geben Boxen, Punkte oder Text mit einer leeren Matte zurück.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `masks` | Alpha-Mattes der gefundenen Objekte, standardmäßig eine pro Frame oder eine pro Box mit `individual_masks`. | MASK |
| `bboxes` | In jedem Bild gefundene Boxen, gespeichert als `x`, `y`, `width`, `height` und `label`. | BOUNDING_BOX |
| `points` | Punkte als JSON in Pixeln, geformt als `[{"x", "y", "label", "frame"}]`, gefüllt durch die Aufgaben `point` und `count_point`. | STRING |
| `text` | Die Rohtantwort des Modells, eine Zeile pro Bild. | STRING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WeVisOneDetect/de.md)

---
**Source fingerprint (SHA-256):** `0cef1dfcab790e145ace51401a84cdc10282835330cda5a3770f5b20a32d475e`
