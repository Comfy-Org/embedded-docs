# Stablezero123Conditioning

Dieser Node ist darauf ausgelegt, Daten für die Verwendung in StableZero123-Modellen zu verarbeiten und zu konditionieren. Der Fokus liegt darauf, die Eingabe in einem spezifischen Format vorzubereiten, das mit diesen Modellen kompatibel und für sie optimiert ist.

## Eingaben

| Parameter | Beschreibung | Comfy dtype |
| --- | --- | --- |
| `clip_vision` | Verarbeitet visuelle Daten, um sie an die Anforderungen des Modells anzupassen und das Verständnis des Modells für den visuellen Kontext zu verbessern. | `CLIP_VISION` |
| `init_image` | Dient als initiale Bildeingabe für das Modell und legt die Basis für weitere bildbasierte Operationen fest. | `IMAGE` |
| `vae` | Integriert Ausgaben des variationalen Autoencoders und erleichtert dem Modell die Fähigkeit, Bilder zu erzeugen oder zu verändern. | `VAE` |
| `width` | Gibt die Breite des Ausgabebilds an und ermöglicht eine dynamische Größenanpassung entsprechend den Modellanforderungen. | `INT` |
| `height` | Bestimmt die Höhe des Ausgabebilds und ermöglicht die Anpassung der Ausgabedimensionen. | `INT` |
| `batch_size` | Steuert die Anzahl der Bilder, die in einem einzelnen Batch verarbeitet werden, und optimiert die Recheneffizienz. | `INT` |
| `elevation` | Passt den Elevationswinkel für das Rendering des 3D-Modells an und verbessert das räumliche Verständnis des Modells. | `FLOAT` |
| `azimuth` | Ändert den Azimutwinkel für die Visualisierung des 3D-Modells und verbessert die Wahrnehmung der Ausrichtung durch das Modell. | `FLOAT` |

## Ausgaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `positive` | Erzeugt positive Konditionierungsvektoren und unterstützt die positive Merkmalsverstärkung des Modells. | `CONDITIONING` |
| `negative` | Erzeugt negative Konditionierungsvektoren und hilft dem Modell, bestimmte Merkmale zu vermeiden. | `CONDITIONING` |
| `latent` | Erzeugt latente Repräsentationen und ermöglicht dem Modell tiefere Einblicke in die Daten. | `LATENT` |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Stablezero123Conditioning/de.md)
