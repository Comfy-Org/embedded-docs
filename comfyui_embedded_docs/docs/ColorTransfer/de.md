# Farbe übertragen

Der Node ColorTransfer passt die Farbpalette eines Zielbilds an die Farben eines Referenzbilds an. Er verwendet verschiedene mathematische Algorithmen, um die Farbeigenschaften wie Helligkeit, Kontrast und Farbtonverteilung vom Referenzbild auf das Zielbild zu analysieren und zu übertragen. Dies ist nützlich, um visuelle Konsistenz über mehrere Bilder hinweg zu erzeugen oder ein bestimmtes Color Grading anzuwenden.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `image_target` | Bild(er), auf die die Farbtransformation angewendet werden soll. | IMAGE | Ja | - |
| `image_ref` | Referenzbild(er), deren Farben abgeglichen werden sollen. | IMAGE | Ja | - |
| `method` | Der zu verwendende Farbübertragungsalgorithmus. | COMBO | Ja | `"reinhard_lab"`<br>`"mkl_lab"`<br>`"histogram"` |
| `source_stats` | Legt fest, wie die Farbstatistiken aus dem Quellbild (Zielbild) berechnet werden. | DYNAMICCOMBO | Ja | `"per_frame"`<br>`"uniform"`<br>`"target_frame"` |
| `strength` | Die Intensität des Farbübertragungseffekts. Ein Wert von 1.0 wendet die vollständige Transformation an, während 0.0 das Originalbild zurückgibt. Standard: 1.0 | FLOAT | Ja | 0.0 bis 10.0 |

**Parameterdetails:**
*   **`source_stats` Optionen:**
    *   **`per_frame`**: Jedes Frame in einem Batch wird einzeln mit dem `image_ref` abgeglichen.
    *   **`uniform`**: Farbstatistiken werden über alle Quellframes zusammengefasst, um eine einzelne Basis zu erstellen, die dann mit dem `image_ref` abgeglichen wird.
    *   **`target_frame`**: Verwendet einen ausgewählten Frame aus dem Ziel-Batch als Basis für die Berechnung der Transformation zum `image_ref`. Diese Transformation wird dann einheitlich auf alle Frames angewendet, wodurch die relativen Farbunterschiede zwischen ihnen erhalten bleiben. Wenn diese Option ausgewählt ist, wird ein zusätzlicher Parameter `target_index` verfügbar.
*   **`target_index`** (erscheint, wenn `source_stats` auf `"target_frame"` gesetzt ist): Der Frame-Index (beginnend bei 0), der als Quellbasis für die Berechnung der Transformation verwendet wird. Standard: 0. Muss zwischen 0 und 10000 liegen.

**Einschränkungen:**
*   Wenn `strength` auf 0.0 gesetzt ist oder `image_ref` `None` ist, gibt der Node das ursprüngliche `image_target` zurück, ohne eine Verarbeitung durchzuführen.
*   Wenn `source_stats` auf `"target_frame"` gesetzt ist, muss `target_index` ein gültiger Index innerhalb des Batches von `image_target` sein. Wenn er die Anzahl der Frames überschreitet, wird der letzte Frame verwendet.
*   Beim `histogram`-Verfahren mit `source_stats` auf `"per_frame"`: Wenn die Batch-Größe von `image_ref` größer als 1 ist, wird jeder Ziel-Frame dem entsprechenden Referenz-Frame nach Index zugeordnet. Wenn der Referenz-Batch nur einen Frame enthält, wird dieser für alle Ziel-Frames verwendet.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `image` | Das resultierende Bild / die resultierenden Bilder nach Anwendung der Farbübertragung. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ColorTransfer/de.md)

---
**Source fingerprint (SHA-256):** `f844af34ac6129c7751953c48e2d12aa0d2c556937e610f649f3eb2725955711`
