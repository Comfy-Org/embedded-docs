# Magnific-Bild-Upscale (Kreativ)

Dieser Node verwendet den Magnific AI-Dienst, um ein Bild hochzuskalieren und kreativ zu verbessern. Sie können die Verbesserung mit einem Text-Prompt steuern, einen bestimmten Stil auswählen, für den optimiert werden soll, und verschiedene Aspekte des kreativen Prozesses wie Detailgrad, Ähnlichkeit zum Original und Stilisierungsstärke kontrollieren. Der Node gibt ein hochskaliertes Bild mit dem gewählten Faktor (2x, 4x, 8x oder 16x) aus, wobei die maximale Ausgabegröße 25,3 Megapixel beträgt.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|-----------|--------------|---------|
| `image` | Das Eingabebild, das hochskaliert und verbessert werden soll. | IMAGE | Ja | - |
| `prompt` | Eine Textbeschreibung, um die kreative Verbesserung des Bildes zu steuern. Standard ist ein leerer String (in diesem Fall wird kein Prompt gesendet). | STRING | Ja | - |
| `scale_factor` | Der Faktor, um den die Dimensionen des Bildes hochskaliert werden. | COMBO | Ja | `"2x"`<br>`"4x"`<br>`"8x"`<br>`"16x"` |
| `optimized_for` | Der Stil oder Inhaltstyp, für den der Verbesserungsprozess optimiert werden soll. | COMBO | Ja | `"standard"`<br>`"soft_portraits"`<br>`"hard_portraits"`<br>`"art_n_illustration"`<br>`"videogame_assets"`<br>`"nature_n_landscapes"`<br>`"films_n_photography"`<br>`"3d_renders"`<br>`"science_fiction_n_horror"` |
| `creativity` | Steuert den Grad der kreativen Interpretation, die auf das Bild angewendet wird (Standard: 0). | INT | Ja | -10 bis 10 |
| `hdr` | Der Grad an Definition und Detail (Standard: 0). | INT | Ja | -10 bis 10 |
| `resemblance` | Der Grad der Ähnlichkeit mit dem Originalbild (Standard: 0). | INT | Ja | -10 bis 10 |
| `fractality` | Die Stärke des Prompts und die Feingliedrigkeit pro Quadratpixel (Standard: 0). | INT | Ja | -10 bis 10 |
| `engine` | Die spezifische KI-Engine, die für die Verarbeitung verwendet werden soll. Dies ist ein erweiterter Parameter. | COMBO | Ja | `"automatic"`<br>`"magnific_illusio"`<br>`"magnific_sharpy"`<br>`"magnific_sparkle"` |
| `auto_downscale` | Das Eingabebild automatisch herunterskalieren, wenn die Ausgabe die maximale Pixelgrenze überschreiten würde (Standard: False). Dies ist ein erweiterter Parameter. | BOOLEAN | Ja | - |

**Einschränkungen:**

* Die Eingabe `image` muss genau ein Bild sein.
* Das Eingabebild muss eine Mindesthöhe und -breite von 160 Pixeln haben.
* Das Seitenverhältnis des Eingabebilds muss zwischen 1:3 und 3:1 liegen.
* Die endgültige Ausgabegröße (Eingabemaße multipliziert mit dem `scale_factor`) darf 25.300.000 Pixel nicht überschreiten. Wenn diese Grenze überschritten würde:
  - Wenn `auto_downscale` aktiviert ist, reduziert der Node automatisch die Größe des Eingabebilds (die zusätzliche Herunterskalierung wird auf höchstens 2x begrenzt) oder verwendet einen niedrigeren `scale_factor`, damit die Ausgabe innerhalb der Grenze bleibt.
  - Wenn `auto_downscale` deaktiviert ist, löst der Node einen Fehler aus.

## Ausgaben

| Name der Ausgabe | Beschreibung | Datentyp |
|------------------|--------------|----------|
| `image` | Das kreativ verbesserte und hochskalierte Ausgabebild. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MagnificImageUpscalerCreativeNode/de.md)

---
**Source fingerprint (SHA-256):** `36c38e87f9f1e568c78cf794aeb0a268c6d25d639006eb2cf18ee040d3071ad4`
