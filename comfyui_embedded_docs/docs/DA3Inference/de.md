# Depth Anything 3 ausführen

Dieser Node führt das Depth Anything 3-Modell auf einem Bild aus, um Tiefen- und Geometrieinformationen zu schätzen. Im Multiview-Modus werden mehrere Bilder gemeinsam als separate Ansichten derselben Szene verarbeitet, um geometrisch konsistente Tiefenkarten und Kameraposen zu erzeugen.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `da3_model` | Das für die Inferenz zu verwendende Depth Anything 3-Modell | DA3_MODEL | Ja | - |
| `image` | Eingabebild oder Eingabebilder zur Verarbeitung | IMAGE | Ja | - |
| `resolution` | Auflösung, mit der das Modell ausgeführt wird (längste Seite, Vielfaches von 14). Niedrigere Werte sind schneller und benötigen weniger VRAM. Höhere Werte erzeugen mehr Details. Die Ausgabe wird wieder auf die Originalgröße hochskaliert (Standard: 504) | INT | Ja | 140 bis 2520 (Schritt: 14) |
| `resize_method` | upper_bound_resize: Skaliert so, dass die längste Seite der Auflösung entspricht (begrenzt den Speicher, Standard). lower_bound_resize: Skaliert so, dass die kürzeste Seite der Auflösung entspricht (bewahrt mehr Details bei hohen/breiten Bildern, verbraucht mehr Speicher) | COMBO | Ja | `"upper_bound_resize"`<br>`"lower_bound_resize"` |
| `mode` | mono: Verarbeitung eines einzelnen Bildes (funktioniert mit jeder Modellvariante). multiview: Alle Bilder werden gemeinsam verarbeitet, um geometrische Konsistenz und Kameraposen zu schätzen (nur für Small- und Base-Modelle) | COMBO | Ja | `"mono"`<br>`"multiview"` |
| `ref_view_strategy` | Welche Ansicht im Multiview-Modus als geometrischer Anker fungiert. saddle_balanced: die Ansicht, die dem Durchschnitt aller anderen am nächsten kommt (beste allgemeine Wahl). saddle_sim_range: die Ansicht, die sich visuell am stärksten von den anderen unterscheidet. first / middle: feste positionsbasierte Auswahl (Standard: saddle_balanced) | COMBO | Nein (bedingt) | `"saddle_balanced"`<br>`"saddle_sim_range"`<br>`"first"`<br>`"middle"` |
| `pose_method` | Wie das Sichtfeld der Kamera geschätzt wird (nur für Small- und Base-Modelle). cam_dec: aus Bildmerkmalen gelernt. ray_pose: geometrisch aus der 3D-Strahlenausgabe des Modells abgeleitet. Beeinflusst die Perspektivkorrektheit der 3D-Ausgabe (Standard: cam_dec) | COMBO | Nein (bedingt) | `"cam_dec"`<br>`"ray_pose"` |

**Hinweise zu Parameterbeschränkungen:**
- Die Parameter `ref_view_strategy` und `pose_method` sind nur verfügbar, wenn `mode` auf `"multiview"` gesetzt ist.
- Der Multiview-Modus erfordert eine Small- oder Base-Modellvariante. Modelle mit anderen Head-Typen (wie Metric oder Mono) unterstützen weder Cross-View-Attention noch Kameraposenschätzung.
- Wenn `pose_method` auf `"cam_dec"` gesetzt ist, muss das Modell einen Kamera-Decoder besitzen. Wenn es auf `"ray_pose"` gesetzt ist, muss das Modell einen DualDPT-Head besitzen.
- Wenn die ausgewählte `pose_method` nicht mit dem geladenen Modell kompatibel ist, wird ein Fehler ausgelöst.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `da3_geometry` | Wörterbuch nicht normalisierter Tensoren. Enthält immer die Schlüssel: depth, image, mode. Optionale Schlüssel sind: sky (für Mono-/Metric-Modelle), confidence (für Small-/Base-Modelle), extrinsics und intrinsics (für den Multiview-Modus) | DA3_GEOMETRY |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DA3Inference/de.md)

---
**Source fingerprint (SHA-256):** `e91dd47e6a01719cdd6b6ce8a9bcc45933cac72c5e147ac42906d2f83ab7c250`
