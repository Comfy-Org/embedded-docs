# LoadImageSetNode

Der LoadImageSetNode lädt mehrere Bilder aus dem Eingabeverzeichnis für die Batch-Verarbeitung und zu Trainingszwecken. Er unterstützt verschiedene Bildformate und kann die Bilder optional mit unterschiedlichen Methoden skalieren. Dieser Node verarbeitet alle ausgewählten Bilder als einen Batch und gibt sie als einzelnen Tensor zurück.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `images` | Wählen Sie mehrere Bilder aus dem Eingabeverzeichnis aus. Unterstützt die Formate PNG, JPG, JPEG, WEBP, BMP, GIF, JPE, APNG, TIF und TIFF. Ermöglicht die Batch-Auswahl von Bildern. | IMAGE | Ja | Mehrere Bilddateien |
| `resize_method` | Optionale Methode zur Größenänderung geladener Bilder (Standard: "None"). Wählen Sie "None", um die Originalgrößen beizubehalten, "Stretch", um eine Größenänderung zu erzwingen, "Crop", um das Seitenverhältnis durch Zuschneiden beizubehalten, oder "Pad", um das Seitenverhältnis durch Hinzufügen von Padding beizubehalten. | STRING | Nein | "None"<br>"Stretch"<br>"Crop"<br>"Pad" |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `IMAGE` | Ein Tensor, der alle geladenen Bilder als Batch für die weitere Verarbeitung enthält. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadImageSetNode/de.md)

---
**Source fingerprint (SHA-256):** `acf0255bcf170ef3ac3b86a3f3e060c3b81064ca8924918a026ec8e3b86f7ac0`
