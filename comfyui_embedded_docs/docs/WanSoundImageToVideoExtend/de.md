# WanSoundImageToVideoExtend

Der WanSoundImageToVideoExtend-Node erweitert ein vorhandenes Video-Latent durch die Generierung zusätzlicher Frames, optional geleitet durch Audio, ein Referenzbild und ein Steuervideo. Er nimmt ein Start-Video-Latent entgegen und erzeugt eine längere Videosequenz, wobei die bereitgestellte Konditionierung und Audio-Hinweise den neuen Inhalt beeinflussen.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `positive` | Positive Konditionierungs-Prompts, die vorgeben, was das Video enthalten soll | CONDITIONING | Ja | - |
| `negative` | Negative Konditionierungs-Prompts, die angeben, was das Video vermeiden soll | CONDITIONING | Ja | - |
| `vae` | Variational Autoencoder, mit dem das Referenzbild und das Steuervideo in den Latent-Raum kodiert werden | VAE | Ja | - |
| `length` | Gesamtzahl der für die Videosequenz zu generierenden Frames (Standard: 77, Schritt: 4) | INT | Ja | 1 bis MAX_RESOLUTION |
| `video_latent` | Initiales Video-Latent, das als Ausgangspunkt für die Erweiterung dient. Die Ausgabebreite, -höhe, Batch-Größe und der Frame-Offset werden aus diesem Latent abgeleitet. Seine letzten 19 Frames werden als Referenzbewegungs-Konditionierung verwendet. | LATENT | Ja | - |
| `audio_encoder_output` | Optionale Audio-Embeddings, die die Videogenerierung basierend auf Klangeigenschaften beeinflussen können. Wenn angegeben, wird das Audio interpoliert und in einen Audio-Embedding-Bucket umgewandelt, der der Konditionierung hinzugefügt wird. | AUDIOENCODEROUTPUT | Nein | - |
| `ref_image` | Optionales Referenzbild, das visuelle Anleitung für die Videogenerierung bietet. Das Bild wird auf die Zielabmessungen hochskaliert und in ein Latent kodiert, das dann sowohl zur positiven als auch zur negativen Konditionierung hinzugefügt wird. Nur das erste Bild im Batch wird verwendet. | IMAGE | Nein | - |
| `control_video` | Optionales Steuervideo, das Bewegung und Struktur des generierten Videos vorgibt. Das Video wird hochskaliert, kodiert und sowohl zur positiven als auch zur negativen Konditionierung hinzugefügt. Das Steuervideo wird auf die angegebene `length` gekürzt. | IMAGE | Nein | - |

Hinweis: Das Ausgabe-Latent wird mit den Zielabmessungen als Nullen initialisiert. Das Eingabe-`video_latent` wird nicht in diese Ausgabe kopiert; seine letzten 19 Frames werden stattdessen als Referenzbewegung verwendet.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `positive` | Verarbeitete positive Konditionierung mit angewendetem Videokontext, einschließlich Audio-Embeddings, Referenz-Latents, Referenzbewegung und Steuervideo, falls angegeben | CONDITIONING |
| `negative` | Verarbeitete negative Konditionierung mit angewendetem Videokontext, einschließlich Audio-Embeddings (auf null gesetzt), Referenz-Latents, Referenzbewegung und Steuervideo, falls angegeben | CONDITIONING |
| `latent` | Video-Latent-Darstellung der erweiterten Sequenz, als Nullen initialisiert, mit Dimensionen, die aus dem Eingabe-`video_latent` und der Ziel-`length` abgeleitet werden | LATENT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanSoundImageToVideoExtend/de.md)

---
**Source fingerprint (SHA-256):** `32b58aaba566f346a0388ba804fc92e7ad426bf2e9e7039e5fdb0bf6a746e972`
