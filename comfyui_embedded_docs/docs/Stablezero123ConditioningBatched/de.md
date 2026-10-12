# Stablezero123ConditioningBatched

Dieser Node ist darauf ausgelegt, Konditionierungsinformationen in Stapelverarbeitung speziell für das StableZero123-Modell zu verarbeiten. Der Schwerpunkt liegt auf der effizienten gleichzeitigen Verarbeitung mehrerer Sätze von Konditionierungsdaten, wodurch der Workflow für Szenarien optimiert wird, in denen Batch-Verarbeitung entscheidend ist.

## Eingaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `clip_vision` | Die CLIP-Vision-Einbettungen, die den visuellen Kontext für den Konditionierungsprozess bereitstellen. | `CLIP_VISION` |
| `init_image` | Das Ausgangsbild, auf das konditioniert werden soll, und dient als Ausgangspunkt für den Generierungsprozess. | `IMAGE` |
| `vae` | Der variationale Autoencoder, der zum Kodieren und Dekodieren von Bildern im Konditionierungsprozess verwendet wird. | `VAE` |
| `width` | Die Breite des Ausgabebilds. | `INT` |
| `height` | Die Höhe des Ausgabebilds. | `INT` |
| `batch_size` | Die Anzahl der Konditionierungssätze, die in einem einzelnen Batch verarbeitet werden sollen. | `INT` |
| `elevation` | Der Elevationswinkel für die 3D-Modell-Konditionierung, der die Perspektive des generierten Bilds beeinflusst. | `FLOAT` |
| `azimuth` | Der Azimutwinkel für die 3D-Modell-Konditionierung, der die Ausrichtung des generierten Bilds beeinflusst. | `FLOAT` |
| `elevation_batch_increment` | Die inkrementelle Änderung des Elevationswinkels über den Batch hinweg, wodurch unterschiedliche Perspektiven ermöglicht werden. | `FLOAT` |
| `azimuth_batch_increment` | Die inkrementelle Änderung des Azimutwinkels über den Batch hinweg, wodurch unterschiedliche Ausrichtungen ermöglicht werden. | `FLOAT` |

## Ausgaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `positive` | Die positive Konditionierungsausgabe, die darauf ausgerichtet ist, bestimmte Merkmale oder Aspekte im generierten Inhalt zu fördern. | `CONDITIONING` |
| `negative` | Die negative Konditionierungsausgabe, die darauf ausgerichtet ist, bestimmte Merkmale oder Aspekte im generierten Inhalt herabzusetzen. | `CONDITIONING` |
| `latent` | Die latente Repräsentation, die aus dem Konditionierungsprozess abgeleitet wird und für weitere Verarbeitungs- oder Generierungsschritte bereitsteht. | `LATENT` |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Stablezero123ConditioningBatched/de.md)
