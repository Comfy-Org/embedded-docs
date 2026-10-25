# ModelMergeMOSSImage

Der Node ModelMergeMOSSImage führt zwei MOSS-Bildmodelle zusammen, indem deren übereinstimmende Gewichte Block für Block gemischt werden, sodass ein Teil des Ergebnisses von einem Basismodell und der Rest von einem Fine-Tuning- oder einem zweiten Modell stammen kann. Jede Hauptkomponente der Architektur hat ihr eigenes Verhältnis: der Video-Embedder, der Text-Embedder, das Zeit-Embedding, die gemeinsame Blockmodulation, alle 42 Transformer-Schichten und die Ausgabeköpfe.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model1` | Das erste Modell, das zusammengeführt werden soll. Alles, wozu das zweite Modell nicht beiträgt, wird von diesem Modell beibehalten | MODEL | Ja | - |
| `model2` | Das zweite Modell, das zusammengeführt werden soll. Seine Gewichte werden gemäß den unten angegebenen Verhältnissen eingemischt | MODEL | Ja | - |
| `video_embedder.` | Mischverhältnis für den Video-Embedder-Block (Standard: 1.0) | FLOAT | Ja | 0.0 bis 1.0 (Schritt: 0.01) |
| `text_embedder.proj.` | Mischverhältnis für die Projektionsschicht des Text-Embedders (Standard: 1.0) | FLOAT | Ja | 0.0 bis 1.0 (Schritt: 0.01) |
| `text_embedder.blocks.0.` und `text_embedder.blocks.1.` | Mischverhältnis für jeden der beiden Text-Embedder-Blöcke (Standard: 1.0) | FLOAT | Ja | 0.0 bis 1.0 (Schritt: 0.01) |
| `time_embedding.` | Mischverhältnis für den Zeit-Embedding-Block (Standard: 1.0) | FLOAT | Ja | 0.0 bis 1.0 (Schritt: 0.01) |
| `shared_block_modulation.` | Mischverhältnis für die gemeinsame Modulationsschicht, die von den Transformer-Blöcken verwendet wird (Standard: 1.0) | FLOAT | Ja | 0.0 bis 1.0 (Schritt: 0.01) |
| `layers.0.` bis `layers.41.` | Mischverhältnis für jede der 42 Transformer-Schichten (Standard: 1.0) | FLOAT | Ja | 0.0 bis 1.0 (Schritt: 0.01) |
| `final_norm_video.` | Mischverhältnis für die abschließende Normalisierung des Videostreams (Standard: 1.0) | FLOAT | Ja | 0.0 bis 1.0 (Schritt: 0.01) |
| `final_linear_video.` | Mischverhältnis für die abschließende lineare Schicht des Videostreams (Standard: 1.0) | FLOAT | Ja | 0.0 bis 1.0 (Schritt: 0.01) |
| `video_head_modulation.` | Mischverhältnis für die Modulationsschicht des Video-Ausgabekopfs (Standard: 1.0) | FLOAT | Ja | 0.0 bis 1.0 (Schritt: 0.01) |

Ein Verhältnis von 0.0 behält diese Komponente so bei, wie sie in `model1` ist; ein Verhältnis von 1.0 übernimmt sie vollständig aus `model2`, und Werte dazwischen erzeugen eine gewichtete Mischung. Beide Eingaben müssen MOSS-Bildmodelle mit derselben Architektur sein; Gewichte, die keinem der oben genannten Präfixe entsprechen, fallen auf das Verhältnis von `video_embedder.` zurück.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `MODEL` | Das zusammengeführte Modell, das beide Eingaben gemäß den angegebenen Verhältnissen kombiniert | MODEL |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeMOSSImage/de.md)

---
**Source fingerprint (SHA-256):** `3b7d9c806a8d53ad00044bf30f5e63431fea7ee565414acb70a56e3059164288`
