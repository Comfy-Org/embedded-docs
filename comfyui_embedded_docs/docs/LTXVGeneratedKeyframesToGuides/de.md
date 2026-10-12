# LTXVGeneratedKeyframesToGuides

Der Node LTXV Generated Keyframes to Guides fixiert generierte Keyframes aus einer früheren Stufe als eingefrorene Bild-Guides auf einem späteren Canvas. Er dekodiert die Keyframes als eigenständige Frames, skaliert sie bei Bedarf und schreibt sie mit einer Rauschmaske von 0, sodass sie nicht erneut entrauscht werden. Nach einem zeitlichen Upscale werden aufgezeichnete Indizes von dem Canvas, auf dem sie generiert wurden, auf diesen Canvas skaliert; verwenden Sie `override_frame_indices`, um Positionen explizit festzulegen.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `positive` | Positive Konditionierung, zu der die Keyframe-Guides hinzugefügt werden. | CONDITIONING | Ja | |
| `negative` | Negative Konditionierung, zu der die Keyframe-Guides hinzugefügt werden. | CONDITIONING | Ja | |
| `vae` | Das VAE, das zum Dekodieren der Keyframes verwendet wird, falls eine Größenänderung erforderlich ist. | VAE | Ja | |
| `latent` | Das Ziel-Video-Latent, zu dem die Guides hinzugefügt werden, z. B. das zeitlich hochskalierte. | LATENT | Ja | |
| `keyframes` | Die Keyframes-Ausgabe von LTXV Separate Generated Keyframes, die den Pixel-Frame-Index trägt, an dem jedes Keyframe generiert wurde. | LATENT | Ja | |
| `strength` | Guide-Stärke. 1.0 ist eine harte Fixierung; niedrigere Werte lockern sie. (Standard: 1.0) | FLOAT | Ja | 0.0 - 10.0 (Schritt 0.01) |
| `override_frame_indices` | Optional — an diesen Pixel-Frames fixieren statt an den aufgezeichneten (oder automatisch skalierten) Positionen. Geben Sie einen Index pro Keyframe an. Leer lassen, um aufgezeichnete Positionen wiederzuverwenden oder sie zu skalieren, wenn der Ziel-Canvas eine andere Länge hat (z. B. nach temporal x2). (Standard: "") | STRING | Nein | |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `positive` | Positive Konditionierung mit den als Bild-Guides fixierten Keyframes. | CONDITIONING |
| `negative` | Negative Konditionierung mit den als Bild-Guides fixierten Keyframes. | CONDITIONING |
| `latent` | Ziel-Video-Latent, bei dem die Keyframes als eingefrorene Guides hinzugefügt wurden. | LATENT |

## Hinweise

- Der `keyframes`-Eingang muss mit der `keyframes`-Ausgabe von LTXV Separate Generated Keyframes verbunden werden. Der Node löst einen Fehler aus, wenn das Latent keine generierten Keyframe-Positionen trägt.
- Die Eingänge `positive` und `negative` für die Konditionierung müssen von den `positive`- und `negative`-Ausgaben von LTXV Separate Generated Keyframes stammen. Der Node löst einen Fehler aus, wenn die positive Konditionierung noch generierte Keyframes trägt.
- Der `latent`-Eingang muss ein einfaches Video-Latent (5D-Tensor) sein. Guides müssen hinzugefügt werden, bevor das Video- und Audio-Latent mit Concat AV Latent zusammengeführt werden.
- Es wird nur eine Batch-Größe von 1 unterstützt. Jeder Guide wird aus einem Bild kodiert und kann daher nicht über Batch-Elemente hinweg variieren.
- Die Anzahl der Keyframes im `keyframes`-Latent muss der Anzahl der aufgezeichneten Positionen entsprechen; andernfalls wird ein Fehler ausgelöst.
- Wenn `override_frame_indices` leer gelassen wird, werden aufgezeichnete Positionen verwendet. Wenn der Ziel-Canvas eine andere Anzahl von Frames hat als der Canvas, auf dem die Keyframes generiert wurden, werden die aufgezeichneten Indizes automatisch skaliert.
- Wenn `override_frame_indices` angegeben wird, muss es einen ganzzahligen Index pro Keyframe enthalten, getrennt durch Kommas oder Leerzeichen. Indizes müssen eindeutig sein und zwischen 1 und (Anzahl der Pixel-Frames im Ziel-Latent - 1) liegen. Andernfalls wird ein Fehler ausgelöst.
- Wenn ein endgültiger Keyframe-Index größer oder gleich der Anzahl der Pixel-Frames im Ziel-Latent ist, löst der Node einen Fehler aus. Dies kann passieren, wenn das Ziel zeitlich skaliert wurde, nachdem die Keyframes generiert wurden.
- Der Parameter `strength` hat ein Minimum von 0.0 und ein Maximum von 10.0.

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVGeneratedKeyframesToGuides/de.md)

---
**Source fingerprint (SHA-256):** `b5dbf302fad5a7ffd3522d468d1a51b993145d90277592058315499f08e17e7b`
