# LotusConditioning

Der Node LotusConditioning stellt feste, vorab berechnete Conditioning-Embeddings für das Lotus-Modell bereit. Da Lotus einen eingefrorenen Encoder mit Null-Conditioning verwendet, fügt der Node die resultierenden Prompt-Embeddings direkt ein, anstatt Inferenz auszuführen oder große Tensor-Dateien zu laden, sodass sich seine Ausgabe nie ändert. Das zurückgegebene Conditioning kann direkt in eine Generierungspipeline eingesetzt werden, die Lotus-kompatibles Conditioning erwartet.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| *Keine Eingaben* | Dieser Node akzeptiert keine Eingabeparameter. | - | - | - |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `conditioning` | Die vorab berechneten Conditioning-Embeddings für das Lotus-Modell. Zurückgegeben als Conditioning-Liste, die die festen Prompt-Embeddings zusammen mit einem leeren Dictionary enthält. | CONDITIONING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LotusConditioning/de.md)

---
**Source fingerprint (SHA-256):** `1fcb6530850341253c8acb47b2f26ee79d93f51eca84bef03a1fa5de33d6bc8d`
