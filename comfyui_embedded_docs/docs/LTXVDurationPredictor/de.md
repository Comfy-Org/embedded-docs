# LTXVDurationPredictor

Dieser Node sagt die natürliche Aufnahmedauer für einen Text-Prompt mithilfe eines LTX 2.4 Duration Head voraus, der mit ModelPatchLoader geladen wurde, und richtet das Ergebnis anschließend am 8k+1-Frame-Raster des VAE aus. Die Vorhersage wird mithilfe der ausgewählten Bildrate sowie der minimalen und maximalen Dauerlimits in eine Frame-Anzahl umgerechnet.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model` | Das Modell, das verwendet wird, um die Text-Embeddings vorzuverarbeiten und den Duration Head auszuführen. | MODEL | Ja | N/A |
| `positive` | Das Conditioning, das die Text-Embeddings und Metadaten des Prompts für die Dauervorhersage bereitstellt. | CONDITIONING | Ja | N/A |
| `duration_head` | Mit ModelPatchLoader geladener LTX 2.4 Duration Head. Muss ein LTX Duration Head sein. | MODEL_PATCH | Ja | N/A |
| `frame_rate` | Bildrate in Frames pro Sekunde, die verwendet wird, um Sekunden in Frames umzurechnen (Standard: 24.0). | FLOAT | Ja | 1.0 bis 120.0 |
| `min_seconds` | Minimale Dauer in Sekunden, die bei der Umrechnung der Vorhersage in eine Frame-Anzahl verwendet wird (Standard: 1.0). | FLOAT | Ja | 0.5 bis 120.0 |
| `max_seconds` | Maximale Dauer in Sekunden, die bei der Umrechnung der Vorhersage in eine Frame-Anzahl verwendet wird (Standard: 20.0). | FLOAT | Ja | 0.5 bis 120.0 |

Hinweis: Die Eingabe `duration_head` muss ein Model Patch sein, der einen LTX Duration Head enthält. Wenn der verbundene Model Patch kein LTX Duration Head ist, löst der Node einen ValueError aus. Es wird nur der erste Conditioning-Eintrag verwendet – wenn `positive` einen Batch mit mehr als einem Prompt enthält, wertet der Node nur den ersten aus.

## Ausgaben

| Ausgabenamen | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `num_frames` | Die vorhergesagte Dauer, umgerechnet in eine Frame-Anzahl und auf das 8k+1-Frame-Raster des VAE eingerastet. | INT |
| `seconds` | Rohe (nicht begrenzte) vorhergesagte Dauer. Dies ist der Wert vor dem Einrasten auf das Frame-Raster. | FLOAT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVDurationPredictor/de.md)

---
**Source fingerprint (SHA-256):** `a4abb43128b8fe396e4c986d75028aea6bfdd9bb6fda07e24c88f8e04a61669e`
