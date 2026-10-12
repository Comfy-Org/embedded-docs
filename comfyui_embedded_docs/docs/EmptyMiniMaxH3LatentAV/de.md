# EmptyMiniMaxH3LatentAV

Dieser Node erstellt ein leeres Latent, das sowohl Video- als auch Audioinformationen für das MiniMax H3-Modell kombiniert. Sie legen Breite, Höhe und Länge des Inhalts fest, und der Node erzeugt ein leeres Latent, das das Modell als Ausgangspunkt für die Generierung verwenden kann. Die Dauer (Länge) wird automatisch angepasst, damit sie in das vom Modell geforderte Frame-Raster von 17k+5 Frames bei 24 fps passt.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `width` | Die Breite des Latents in Pixeln. Die Werte müssen Vielfache von 32 sein. Standard: 1344. | INT | Ja | 32 - MAX_RESOLUTION (step 32) |
| `height` | Die Höhe des Latents in Pixeln. Die Werte müssen Vielfache von 32 sein. Standard: 768. | INT | Ja | 32 - MAX_RESOLUTION (step 32) |
| `length` | Frame-Anzahl bei 24 fps, aufgerundet auf das 17k+5-Raster des Modells (124 = ca. 5 s; trainierter Bereich ist ca. 124–362, längere Werte sind ungetestet). Standard: 124. | INT | Ja | 5 - 3600 (step 17) |

Hinweis: Der Wert `length` wird auf die nächste Frame-Anzahl aufgerundet, die in das 17k+5-Raster des Modells passt (17 x k + 5 Frames, z. B. 5, 22, 39, 56, 73, 90, 107, 124 usw.). Die Werte `width` und `height` müssen Vielfache von 32 sein. Die maximale Auflösung ist der systemdefinierte Wert in ComfyUI.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|--------------|----------|
| `latent` | Das erzeugte leere gemeinsame Video+Audio-Latent für MiniMax H3, dimensioniert entsprechend den Eingabewerten für Breite, Höhe und Länge. | LATENT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyMiniMaxH3LatentAV/de.md)

---
**Source fingerprint (SHA-256):** `ee24f4ac630858d87b9b98bb402689a5790e0ed882ec47dffe7b497216e37a5c`
