# SV3D_Conditioning

SV3D_Conditioning bereitet Konditionierungsdaten für die 3D-Videogenerierung mit dem SV3D-Modell vor. Es nimmt ein Ausgangsbild und verarbeitet es durch CLIP-Vision- und VAE-Encoder, um positive und negative Konditionierung sowie eine latente Repräsentation zu erzeugen. Der Node generiert Kamera-Elevations- und Azimutsequenzen für die Multiframe-Videogenerierung basierend auf der angegebenen Anzahl an Videoframes.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `clip_vision` | Das CLIP-Vision-Modell, das zum Kodieren des Eingabebilds verwendet wird | CLIP_VISION | Ja | - |
| `init_image` | Das Ausgangsbild, das als Startpunkt für die 3D-Videogenerierung dient | IMAGE | Ja | - |
| `vae` | Das VAE-Modell, das zum Kodieren des Bilds in den latenten Raum verwendet wird | VAE | Ja | - |
| `width` | Die Ausgabebreite für die generierten Videoframes (Standard: 576, Schrittweite 8) | INT | Ja | 16 bis MAX_RESOLUTION |
| `height` | Die Ausgabebreite für die generierten Videoframes (Standard: 576, Schrittweite 8) | INT | Ja | 16 bis MAX_RESOLUTION |
| `video_frames` | Die Anzahl der Frames, die für die Videosequenz generiert werden sollen (Standard: 21) | INT | Ja | 1 bis 4096 |
| `elevation` | Der Kamera-Elevationswinkel in Grad für die 3D-Ansicht (Standard: 0.0, Schrittweite 0.1) | FLOAT | Ja | -90.0 bis 90.0 |

Hinweis: Der Kamera-Azimut beginnt bei 0 Grad und erhöht sich pro Frame um einen konstanten Betrag, sodass die Kamera über die generierten Frames hinweg eine vollständige 360-Grad-Umlaufbahn um das Objekt abschließt. Das Inkrement pro Frame wird als 360 geteilt durch (`video_frames` - 1) berechnet, wobei ein minimaler Divisor von 2 verwendet wird, wenn nur ein Frame angefordert wird. Der Wert `elevation` bleibt für jeden Frame konstant.

Das `init_image` wird vor der VAE-Kodierung auf die angegebene `width` und `height` skaliert, und der zurückgegebene Latent-Tensor verwendet Dimensionen von `video_frames` x 4 x (`height` // 8) x (`width` // 8).

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `positive` | Die positiven Konditionierungsdaten, die Bild-Embeddings und Kameraparameter für die Generierung enthalten | CONDITIONING |
| `negative` | Die negativen Konditionierungsdaten mit auf null gesetzten Embeddings und Latents für die kontrastive Generierung | CONDITIONING |
| `latent` | Ein leerer latenter Tensor mit Dimensionen, die den angegebenen Videoframes und der Auflösung entsprechen | LATENT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SV3D_Conditioning/de.md)

---
**Source fingerprint (SHA-256):** `e28173cfa560290e66b032687088cf0b981256ca5c21f6aa608e0fdaec886665`
