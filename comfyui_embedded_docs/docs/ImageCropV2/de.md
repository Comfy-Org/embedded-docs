# ImageCropV2

Der Node Crop Image extrahiert einen rechteckigen Bereich aus einem Eingabebild. Sie definieren den beizubehaltenden Bereich, indem Sie die Koordinaten der oberen linken Ecke sowie Breite und Höhe angeben. Der Node gibt anschließend den zugeschnittenen Teil des Originalbilds zurück.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `image` | Das Eingabebild, das zugeschnitten werden soll. | IMAGE | Ja | N/A |
| `crop_region` | Definiert den rechteckigen Bereich, der aus dem Bild extrahiert werden soll. Er wird durch `x` (horizontaler Start), `y` (vertikaler Start), `width` und `height` festgelegt. Wenn der definierte Bereich über die Bildränder hinausragt, wird er automatisch angepasst, damit er innerhalb der Bildabmessungen liegt. | BOUNDINGBOX | Ja | N/A |

**Hinweis zu Bereichseinschränkungen:** Der Zuschneidebereich wird automatisch so beschränkt, dass er innerhalb der Grenzen des Eingabebilds bleibt. Wenn die angegebene Koordinate `x` oder `y` größer als die Breite oder Höhe des Bilds ist, wird sie auf die maximal gültige Position gesetzt. Die resultierende Zuschnittbreite und -höhe werden angepasst, sodass der Bereich die Bildränder nicht überschreitet.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `image` | Der zugeschnittene Ausschnitt des ursprünglichen Eingabebilds. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageCropV2/de.md)

---
**Source fingerprint (SHA-256):** `c09c68a46c4b0418903a627b98dd848264d53b58bd3ffe99e40ef125b15b3aae`
