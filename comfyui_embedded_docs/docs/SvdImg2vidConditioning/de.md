# SvdImg2vidConditioning

Dieser Node ist für die Generierung von Conditioning-Daten für Videogenerierungsaufgaben konzipiert und speziell auf die Verwendung mit SVD_img2vid-Modellen zugeschnitten. Er nimmt verschiedene Eingaben entgegen, darunter Ausgangsbilder, Videoparameter und ein VAE-Modell, um Conditioning-Daten zu erzeugen, die zur Steuerung der Generierung von Videoframes verwendet werden können.

## Eingaben

| Parameter | Beschreibung | Comfy dtype |
| --- | --- | --- |
| `clip_vision` | Repräsentiert das CLIP-Vision-Modell, das zur Kodierung visueller Merkmale aus dem Ausgangsbild verwendet wird und eine entscheidende Rolle beim Verständnis des Inhalts und Kontexts des Bildes für die Videogenerierung spielt. | `CLIP_VISION` |
| `init_image` | Das Ausgangsbild, aus dem das Video generiert wird, dient als Startpunkt für den Videogenerierungsprozess. | `IMAGE` |
| `vae` | Ein Variational-Autoencoder-(VAE-)Modell, das zur Kodierung des Ausgangsbilds in einen latenten Raum verwendet wird, um die Generierung kohärenter und kontinuierlicher Videoframes zu ermöglichen. | `VAE` |
| `width` | Die gewünschte Breite der zu generierenden Videoframes, wodurch die Auflösung des Videos angepasst werden kann. | `INT` |
| `height` | Die gewünschte Höhe der Videoframes, wodurch das Seitenverhältnis und die Auflösung des Videos gesteuert werden können. | `INT` |
| `video_frames` | Gibt die Anzahl der für das Video zu generierenden Frames an und bestimmt damit die Länge des Videos. | `INT` |
| `motion_bucket_id` | Ein Bezeichner zur Kategorisierung der Art der im Video anzuwendenden Bewegung, der bei der Erstellung dynamischer und ansprechender Videos hilft. | `INT` |
| `fps` | Die Bildrate (Frames pro Sekunde, fps) für das Video, die die Flüssigkeit und Realitätsnähe des generierten Videos beeinflusst. | `INT` |
| `augmentation_level` | Ein Parameter, der die Stärke der auf das Ausgangsbild angewendeten Augmentierung steuert und die Vielfalt und Variabilität der generierten Videoframes beeinflusst. | `FLOAT` |

## Ausgaben

| Parameter | Beschreibung | Comfy dtype |
| --- | --- | --- |
| `positive` | Die positiven Conditioning-Daten, bestehend aus kodierten Merkmalen und Parametern, um den Videogenerierungsprozess in eine gewünschte Richtung zu lenken. | `CONDITIONING` |
| `negative` | Die negativen Conditioning-Daten, die einen Kontrast zu den positiven Conditioning-Daten bieten und verwendet werden können, um bestimmte Muster oder Merkmale im generierten Video zu vermeiden. | `CONDITIONING` |
| `latent` | Latente Repräsentationen, die für jedes Frame des Videos generiert werden und als grundlegende Komponente für den Videogenerierungsprozess dienen. | `LATENT` |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SvdImg2vidConditioning/de.md)
