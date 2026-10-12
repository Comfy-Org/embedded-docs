# Hunyuan Video 1.5 Latent-Upscale mit Modell

Der Node „Hunyuan Video 15 Latent Upscale With Model“ erhöht die Auflösung einer latenten Bilddarstellung. Zuerst werden die latenten Samples mit einer ausgewählten Interpolationsmethode auf eine angegebene Größe hochskaliert, anschließend wird das hochskalierte Ergebnis mit einem spezialisierten Hunyuan Video 1.5-Upscale-Modell verfeinert, um die Qualität zu verbessern.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model` | Das Hunyuan Video 1.5-Latent-Upscale-Modell, das verwendet wird, um die hochskalierten Samples zu verfeinern. | LATENT_UPSCALE_MODEL | Ja | N/A |
| `samples` | Die latente Bilddarstellung, die hochskaliert werden soll. | LATENT | Ja | N/A |
| `upscale_method` | Der Interpolationsalgorithmus, der für den anfänglichen Upscaling-Schritt verwendet wird (Standard: `"bilinear"`). | COMBO | Ja | `"nearest-exact"`<br>`"bilinear"`<br>`"area"`<br>`"bicubic"`<br>`"bislerp"` |
| `width` | Die Zielbreite für das hochskalierte Latent in Pixeln. Ein Wert von 0 berechnet die Breite automatisch basierend auf der Zielhöhe und dem ursprünglichen Seitenverhältnis. Die endgültige Ausgabebreite ist ein Vielfaches von 16 (Standard: 1280). | INT | Ja | 0 bis 16384 (Schrittweite: 8) |
| `height` | Die Zielhöhe für das hochskalierte Latent in Pixeln. Ein Wert von 0 berechnet die Höhe automatisch basierend auf der Zielbreite und dem ursprünglichen Seitenverhältnis. Die endgültige Ausgabehöhe ist ein Vielfaches von 16 (Standard: 720). | INT | Ja | 0 bis 16384 (Schrittweite: 8) |
| `crop` | Bestimmt, wie das hochskalierte Latent zugeschnitten wird, damit es in die Zielabmessungen passt. | COMBO | Ja | `"disabled"`<br>`"center"` |

**Hinweis zu Abmessungen:** Wenn sowohl `width` als auch `height` auf 0 gesetzt sind, gibt der Node die Eingabe `samples` unverändert zurück. Wenn nur eine Dimension auf 0 gesetzt ist, wird die andere Dimension berechnet, um das ursprüngliche Seitenverhältnis beizubehalten. Beide Werte werden auf ein Minimum von 64 begrenzt, und das an den Interpolationsschritt übergebene Upscale-Ziel ist `width // 16` mal `height // 16`, sodass die angeforderten Abmessungen effektiv auf Vielfache von 16 abgerundet werden.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `LATENT` | Die hochskalierte und vom Modell verfeinerte latente Bilddarstellung, zurückgegeben als Float-Tensor auf der CPU. | LATENT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanVideo15LatentUpscaleWithModel/de.md)

---
**Source fingerprint (SHA-256):** `71af49eefb010aadd30f8699b751ad901b1ee385d6cbeedd3a83995a1a623516`
