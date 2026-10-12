# Trellis2TextureStage

Dieser Node richtet den Sampling-Durchlauf der Texturphase für die Trellis2-Generierung ein. Er liest das Koordinatenlayout und das Shape-Latent pro Voxel aus dem eingehenden Shape-Latent, erstellt ein leeres Sparse-Latent mit 32 Kanälen im selben Koordinatenlayout und hängt die erforderlichen Metadaten der Texturphase an die Konditionierung an.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `positive` | Die positive Konditionierung, die für den Texturgenerierungs-Durchlauf verwendet wird. Die Metadaten der Texturphase werden an sie angehängt. | CONDITIONING | Ja | - |
| `negative` | Die negative Konditionierung, die für den Texturgenerierungs-Durchlauf verwendet wird. Die Metadaten der Texturphase werden an sie angehängt. | CONDITIONING | Ja | - |
| `shape_latent` | Das von Trellis2ShapeStage oder Trellis2UpsampleStage erzeugte Latent-Dict. Es muss `coords` (das Koordinatenlayout, Form [N, 4]) und `samples` (das Shape-Latent pro Voxel) enthalten; `coord_resolution` und `model_frame` sind optional. | LATENT | Ja | - |

Hinweise:
- `shape_latent` muss die Ausgabe von Trellis2ShapeStage oder Trellis2UpsampleStage sein; es stellt das Koordinatenlayout und das Shape-Latent pro Voxel bereit, die vom Texturdurchlauf verwendet werden.
- Das Koordinatenlayout wird validiert: Batch-IDs in der ersten Spalte von `coords` müssen nicht negativ und zusammenhängend sein, und die Gesamtzahl der Zeilen muss mit den Koordinatenanzahlen übereinstimmen.
- Das Shape-Latent wird entweder als 4D-Sparse-Tensor (der zusammen mit seinen Koordinaten abgeflacht wird) oder bereits in abgeflachter Form akzeptiert.
- Wenn `positive` ein Projektions-Feature-Paket (Pixal3D-Konditionierung) enthält und `shape_latent` `coord_resolution` einschließt, werden Projektionsmerkmale mit 1024 Texturauflösung berechnet und an die Konditionierung angehängt.
- Der Modellrahmen wird aus `shape_latent` gelesen; wenn er fehlt, wird standardmäßig `"y_up"` verwendet, falls Projektionsmerkmale vorhanden sind, andernfalls `"z_up"`.

## Ausgaben

| Ausgabenamen | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `positive` | Die positive Konditionierung mit angehängten Metadaten der Texturphase (Generierungsmodus, Koordinaten, Koordinatenanzahlen, Shape-Latent, Modellrahmen und Projektionsmerkmale, sofern zutreffend). | CONDITIONING |
| `negative` | Die negative Konditionierung mit denselben angehängten Metadaten der Texturphase. | CONDITIONING |
| `latent` | Ein neues leeres Sparse-Latent mit 32 Kanälen im selben Koordinatenlayout wie das eingehende Shape-Latent. Sein Dict enthält `samples`, `type` ("trellis2"), `coords`, `coord_counts` und `model_frame`; `coord_resolution` wird eingeschlossen, wenn verfügbar. | LATENT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Trellis2TextureStage/de.md)

---
**Source fingerprint (SHA-256):** `ae612021af7c74cd09206d905e7b800fa48367a22daf9b0335b444c854a78b1e`
