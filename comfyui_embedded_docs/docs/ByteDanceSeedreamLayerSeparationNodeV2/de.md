# ByteDanceSeedreamLayerSeparationNodeV2

ByteDance Seedream 5.0 Layer Separation zerlegt ein Bild in eine Hintergrundplatte plus bis zu 16 repositionierbare transparente Ebenen, jede mit Stapelreihenfolge, Begrenzungsrahmen, Name und Beschreibung. Es gibt den Hintergrund, Bilder pro Ebene mit Masken, Platzierungsboxen und einen sofort editierbaren Ebenenstapel zurück. Die Auswahl `model` wählt zwischen Seedream 5.0 Pro und dem schnelleren Seedream 5.0 Flash.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model` | Das für die Trennung verwendete Seedream-Modell. "seedream 5.0 pro" (Standard) liefert die höchste Trennungqualität und bietet außerdem eine `prompt_optimization`-Steuerung; "seedream 5.0 flash" ist schneller und günstiger und besitzt keine Prompt-Optimierungs-Steuerung. | DYNAMIC_COMBO | Ja | "seedream 5.0 pro"<br>"seedream 5.0 flash" |

### Seedream 5.0 Pro und 5.0 Flash Eingaben

Diese Eingaben sind bei beiden Modellen verfügbar.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `image` | Das zu trennende Bild. Genau ein Bild, mindestens 512x512 Pixel, Seitenverhältnis zwischen 1:16 und 16:1. Eingaben, die größer als etwa 4 MP sind, werden vor dem Hochladen herunterskaliert. | IMAGE | Ja | Einzelbild |
| `prompt` | Wie das Bild getrennt werden soll. Leer lassen, um alle wesentlichen Elemente automatisch zu erkennen und zu trennen. Beschreiben Sie Elemente in natürlicher Sprache, um die Trennung zu steuern, oder zielen Sie mit `<bbox>left top right bottom</bbox>`-Tags auf exakte Bereiche (0-1000-Promille-Koordinaten). Standard: leerer String. | STRING | Ja | Mehrzeiliger Text |
| `size` | Auflösungsstufe der Ausgabe. "auto" folgt der Größe des Eingabebilds (auf den Bereich 1K-2K begrenzt). Standard: "auto". | COMBO | Ja | "auto"<br>"1K"<br>"1.5K"<br>"2K" |
| `seed` | Seed für die Generierung. Standard: 42. | INT | Ja | 0 bis 2147483647 |
| `watermark` | Ob den Bildern ein "AI generated"-Wasserzeichen hinzugefügt werden soll. Standard: false. | BOOLEAN | Ja | false<br>true |
| `crop_layers` | Geometrie der Batch-Ausgaben von layers/masks (layer_stack ist nicht betroffen und immer passgenau). Vollständige Leinwand: jede Ebene auf einer Leinwand in Basisgröße an ihrer Begrenzungsrahmenposition – direkt mit ImageCompositeMasked wieder zusammensetzen. Minimale Größe: jede Ebene auf ihren Begrenzungsrahmen zugeschnitten (für das Batching auf die größte Ebene aufgefüllt) – deutlich kleinere Tensoren; Platzierung mit Layers From Bounding Boxes unter Verwendung der bboxes-Ausgabe wiederherstellen. Standard: false (vollständige Leinwand). | BOOLEAN | Ja | false (vollständige Leinwand)<br>true (minimale Größe) |

### Nur für Seedream 5.0 Pro: Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `prompt_optimization` | Prompt-Optimierungsmodus: "standard" liefert höhere Qualität, "fast" kürzere Generierungszeit. Nur mit Seedream 5.0 Pro verfügbar. Standard: "standard". | COMBO | Ja | "standard"<br>"fast" |

**Hinweis:** Die Eingabe `image` muss ein einzelnes Bild sein; Batches werden nicht unterstützt. Das Bild muss mindestens 512x512 Pixel groß sein und ein Seitenverhältnis zwischen 1:16 und 16:1 aufweisen. Seedream 5.0 Flash besitzt keine `prompt_optimization`-Eingabe.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `base_image` | Das Basisbild (Hintergrundplatte), auf das die Ebenen gestapelt werden. | IMAGE |
| `base_mask` | Transparenz des Basisbilds (1 = transparent, LoadImage-Konvention); derzeit immer vollständig undurchsichtig. | MASK |
| `layers` | Transparente Ebenen, von unten nach oben geordnet. Modus „vollständige Leinwand“: auf einer schwarzen Leinwand in Basisgröße an ihrer Begrenzungsrahmenposition platziert. Modus „minimale Größe“: auf ihren Begrenzungsrahmen zugeschnitten, oben links verankert, auf die größte Ebene aufgefüllt. | IMAGE |
| `masks` | Transparenz pro Ebene, indexausgerichtet mit dem layers-Batch (1 = transparent, LoadImage-Konvention). Für Compositing im ImageCompositeMasked-Stil zuerst InvertMask hinzufügen. | MASK |
| `bboxes` | Eine Platzierungsbox pro Ebene, indexausgerichtet mit dem layers-Batch (beide, plus masks, in Layers From Bounding Boxes einspeisen, um die Platzierung pro Ebene wiederherzustellen): `{x, y, width, height, metadata: {name, desc, z_index, native_size, content_rect, flags}}`. `content_rect = [left, top, width, height]` ist der Inhaltsbereich der Ebene innerhalb ihres eigenen Rahmens; er landet auf der Leinwand an der Boxposition plus diesem Versatz. | BOUNDING_BOX |
| `layer_stack` | Sofort editierbares Ebenendokument für Create Layered Image: die Basisplatte plus jedes Element als eigene benannte, passgenau zugeschnittene Ebene an seiner wahren Position und Stapelreihenfolge. Direkt verbinden oder mit Add Layer erweitern. | LAYERS |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceSeedreamLayerSeparationNodeV2/de.md)

---
**Source fingerprint (SHA-256):** `b106ca63d37aea68079f0032a1f7dfeefee9f759c71bb1605bbfe66c3d9dad62`
