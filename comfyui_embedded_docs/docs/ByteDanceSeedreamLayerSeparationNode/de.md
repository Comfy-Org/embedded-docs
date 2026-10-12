# ByteDance Seedream 5.0 Pro Ebenentrennung (Legacy)

ByteDance Seedream 5.0 Pro Layer Separation zerlegt ein Bild in eine Hintergrundplatte plus bis zu 16 neu positionierbare transparente Ebenen, jede mit Stapelreihenfolge, Bounding-Box, Name und Beschreibung. Es gibt den Hintergrund, Bilder pro Ebene mit Masken, Platzierungsboxen und einen sofort bearbeitbaren Ebenenstapel zurück.

**Hinweis:** Dieser Node ist im Quellcode als veraltet markiert.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `image` | Das zu trennende Bild. Genau ein Bild, mindestens 512x512 Pixel, Seitenverhältnis zwischen 1:16 und 16:1. Eingaben, die größer als etwa 4 MP sind, werden vor dem Hochladen herunterskaliert. | IMAGE | Ja | Einzelbild |
| `prompt` | Wie das Bild getrennt werden soll. Leer lassen, um automatisch alle Hauptelemente zu erkennen und zu trennen. Beschreiben Sie Elemente in natürlicher Sprache, um die Trennung zu steuern, oder zielen Sie mit `<bbox>left top right bottom</bbox>`-Tags auf exakte Bereiche ab (0-1000 Promille-Koordinaten). Standard: leerer String. | STRING | Ja | Mehrzeiliger Text |
| `size` | Auflösungsstufe der Ausgabe. "auto" folgt der Größe des Eingabebilds (auf den Bereich 1K-2K begrenzt). Standard: "auto". | COMBO | Ja | "auto"<br>"1K"<br>"1.5K"<br>"2K" |
| `seed` | Seed für die Generierung. Standard: 0. | INT | Ja | 0 bis 2147483647 |
| `prompt_optimization` | Prompt-Optimierungsmodus: "standard" liefert höhere Qualität, "fast" eine kürzere Generierungszeit. Standard: "standard". | COMBO | Nein | "standard"<br>"fast" |
| `watermark` | Ob den Bildern ein "AI generated"-Wasserzeichen hinzugefügt werden soll. Standard: false. | BOOLEAN | Nein | false<br>true |
| `crop_layers` | Geometrie der Batch-Ausgaben von `layers`/`masks` (`layer_stack` ist nicht betroffen und immer eng zugeschnitten). Volle Leinwand: jede Ebene auf einer Leinwand in Basisgröße an ihrer Bounding-Box-Position – direkt mit ImageCompositeMasked neu zusammensetzen. Minimale Größe: jede Ebene auf ihre Bounding-Box zugeschnitten (für das Batching auf die größte Ebene aufgefüllt) – deutlich kleinere Tensoren; Platzierung mit Layers From Bounding Boxes unter Verwendung der `bboxes`-Ausgabe wiederherstellen. Standard: false (volle Leinwand). | BOOLEAN | Nein | false (volle Leinwand)<br>true (minimale Größe) |

Hinweis: Die Eingabe `image` muss ein einzelnes Bild sein; Batches werden nicht unterstützt. Das Bild muss mindestens 512x512 Pixel groß sein und ein Seitenverhältnis zwischen 1:16 und 16:1 aufweisen.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `base_image` | Das Basisbild (Hintergrundplatte), auf das die Ebenen gestapelt werden. | IMAGE |
| `base_mask` | Transparenz des Basisbilds (1 = transparent, LoadImage-Konvention); derzeit immer vollständig undurchsichtig. | MASK |
| `layers` | Transparente Ebenen, von unten nach oben geordnet. Modus "volle Leinwand": auf einer schwarzen Leinwand in Basisgröße an ihrer Bounding-Box-Position platziert. Modus "minimale Größe": auf ihre Bounding-Box zugeschnitten, oben links verankert, auf die größte Ebene aufgefüllt. | IMAGE |
| `masks` | Transparenz je Ebene, indexgleich mit dem `layers`-Batch (1 = transparent, LoadImage-Konvention). Für Compositing im ImageCompositeMasked-Stil zuerst InvertMask hinzufügen. | MASK |
| `bboxes` | Eine Platzierungsbox pro Ebene, indexgleich mit dem `layers`-Batch (beide zusammen mit `masks` in Layers From Bounding Boxes einspeisen, um die Platzierung je Ebene wiederherzustellen): `{x, y, width, height, metadata: {name, desc, z_index, native_size, content_rect, flags}}`. `content_rect = [left, top, width, height]` ist der Inhaltsbereich der Ebene innerhalb ihres eigenen Rahmens; er landet auf der Leinwand an der Boxposition plus diesem Offset. | BOUNDING_BOX |
| `layer_stack` | Sofort bearbeitbares Ebenendokument für Create Layered Image: die Grundplatte plus jedes Element als eigene benannte, eng zugeschnittene Ebene an seiner tatsächlichen Position und in seiner Stapelreihenfolge. Direkt verbinden oder mit Add Layer erweitern. | LAYERS |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceSeedreamLayerSeparationNode/de.md)

---
**Source fingerprint (SHA-256):** `7c0d8ca76ee4b8d6a34fec2edbb753982a05160540ae1d1867efb79c9f9c5498`
