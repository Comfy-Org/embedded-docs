# WanPhantomSubjectToVideo

Der Node WanPhantomSubjectToVideo bereitet Conditioning-Daten und einen Latent für die Wan-Videogenerierung vor. Er erstellt ein leeres Latent-Video anhand der angegebenen Breite, Höhe, Länge und Batch-Größe und kodiert, wenn Referenzbilder bereitgestellt werden, diese mit dem VAE und fügt sie den Conditionings als zeitdimensionale visuelle Führung hinzu.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `positive` | Positive Conditioning-Eingabe zur Steuerung der Videogenerierung | CONDITIONING | Ja | - |
| `negative` | Negative Conditioning-Eingabe zur Vermeidung bestimmter Merkmale | CONDITIONING | Ja | - |
| `vae` | VAE-Modell, das zum Kodieren der Referenzbilder verwendet wird, wenn diese bereitgestellt werden | VAE | Ja | - |
| `width` | Breite des Ausgabevideos in Pixeln (Standard: 832) | INT | Ja | 16 bis MAX_RESOLUTION (Schritt 16) |
| `height` | Höhe des Ausgabevideos in Pixeln (Standard: 480) | INT | Ja | 16 bis MAX_RESOLUTION (Schritt 16) |
| `length` | Anzahl der Frames im generierten Video (Standard: 81) | INT | Ja | 1 bis MAX_RESOLUTION (Schritt 4) |
| `batch_size` | Anzahl der gleichzeitig zu generierenden Videos (Standard: 1) | INT | Ja | 1 bis 4096 |
| `images` | Optionale Referenzbilder, die als zeitdimensionale visuelle Führung verwendet werden | IMAGE | Nein | - |

**Hinweis:** Wenn `images` bereitgestellt werden, werden sie automatisch hochskaliert, um der angegebenen `width` und `height` zu entsprechen, und nur die ersten `length` Bilder werden für die Verarbeitung verwendet. Jedes Bild wird mit dem `vae` kodiert und entlang der Zeitdimension verkettet, und es werden nur die RGB-Kanäle jedes Bildes verwendet. Wenn `images` nicht bereitgestellt werden, werden alle drei Conditioning-Ausgaben unverändert aus den Eingabe-Conditionings zurückgegeben.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `positive` | Positive Conditioning mit zeitdimensionaler Verkettung der kodierten Referenzbilder, wenn Bilder bereitgestellt werden; andernfalls wird die Eingabe `positive` unverändert zurückgegeben | CONDITIONING |
| `negative_text` | Negative Conditioning mit zeitdimensionaler Verkettung der kodierten Referenzbilder, wenn Bilder bereitgestellt werden; andernfalls wird die Eingabe `negative` unverändert zurückgegeben | CONDITIONING |
| `negative_img_text` | Negative Conditioning mit einer genullten zeitdimensionalen Verkettung, wenn Bilder bereitgestellt werden; andernfalls wird die Eingabe `negative` unverändert zurückgegeben | CONDITIONING |
| `latent` | Mit Nullen gefüllter latenter Video-Tensor mit 16 Kanälen; seine Frame-Anzahl wird aus `length` abgeleitet und seine räumlichen Dimensionen aus `height` und `width` | LATENT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanPhantomSubjectToVideo/de.md)

---
**Source fingerprint (SHA-256):** `a1853382f6e564f66262b69dd7b06cc58e26b93386a460a98e6fcc2ff6acf12b`
