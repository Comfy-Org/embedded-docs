# MiniMax H3 Referenz zu Video

MiniMax H3 Reference to Video erstellt das Text-Conditioning und das leere Audio-Video-Latent, die für die MiniMax H3 Referenz-zu-Video-Generierung benötigt werden. Sie geben einen Prompt sowie optionale Referenzbilder, -videos und -audioclips an, und der Node kodiert diese Referenzen in Conditioning, das das Modell während der Generierung verwenden kann. Der Prompt verweist mit den Tags `<Picture i>`, `<Video k>` und `<Audio j>` auf die Referenzen.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `clip` | CLIP-Modell, das zum Tokenisieren des Prompts und zum Kodieren der Referenzmedien in Conditioning-Token verwendet wird. | CLIP | Ja | |
| `vae` | Video-VAE. Ohne `vae` werden Referenzbilder und -videos nur zur Konditionierung des Text-Encoders verwendet. | VAE | Nein | |
| `audio_vae` | Audio-VAE. Ohne `audio_vae` wird Referenzaudio nur zur Konditionierung des Text-Encoders verwendet. | VAE | Nein | |
| `prompt` | Text-Prompt für das Video. Referenzmedien können mit den Tags `<Picture i>`, `<Video k>` und `<Audio j>` adressiert werden (1-basiert je Typ). Unterstützt mehrzeilige und dynamische Prompts. | STRING | Ja | |
| `width` | Breite des generierten Videos in Pixeln (Standard: 1344). | INT | Ja | 32 bis 16384 (Schritt 32) |
| `height` | Höhe des generierten Videos in Pixeln (Standard: 768). | INT | Ja | 32 bis 16384 (Schritt 32) |
| `length` | Frame-Anzahl bei 24 fps (124 = ca. 5 s, trainierter Bereich ist ca. 124–362) (Standard: 124). | INT | Ja | 5 bis 3600 (Schritt 17) |
| `ref_image_size` | Größenanpassung der Referenzbilder. `match` skaliert jede Referenz (nur herunter, unter Beibehaltung des Seitenverhältnisses) auf den Pixelbereich der Generierung; `max` verwendet die kurze Kante von 2048 px der Referenz-Pipeline für beste Identitätstreue. Referenz-Token laufen durch jeden Sampling-Schritt, daher kann `max` um ein Mehrfaches langsamer sein (Standard: `match`). | COMBO | Ja | `"match"`<br>`"max"` |
| `ref_images` | Erweiterbarer Slot: Verbinden Sie bis zu 9 Referenzbilder (`ref_image_1` ... `ref_image_9`). Referenzbild (auf 2048 px an der kurzen Kante herunterskaliert, falls größer; wird nie hochskaliert). | IMAGE | Nein | 0 bis 9 |
| `ref_videos` | Erweiterbarer Slot: Verbinden Sie bis zu 3 Referenzvideos (`ref_video_1` ... `ref_video_3`). Referenzvideo-Frames bei 24 fps (2–15 s). | IMAGE | Nein | 0 bis 3 |
| `ref_video_audios` | Erweiterbarer Slot: Verbinden Sie bis zu 3 Tonspuren (`ref_video_audio_1` ... `ref_video_audio_3`). Tonspur des gleich nummerierten Referenzvideos. | AUDIO | Nein | 0 bis 3 |
| `ref_audios` | Erweiterbarer Slot: Verbinden Sie bis zu 3 eigenständige Referenz-Audioclips (`ref_audio_1` ... `ref_audio_3`). Eigenständiges Referenzaudio. | AUDIO | Nein | 0 bis 3 |

Hinweise:

- Der Prompt verweist mit 1-basierten Tags je Typ auf Referenzmedien: `<Picture i>` für Bilder, `<Video k>` für Videos und `<Audio j>` für Audio. Referenzen werden dem Modell in einer festen Reihenfolge präsentiert: Bilder, dann Videos (wobei das `<Audio j>`-Label jeder Tonspur unmittelbar vor ihrem `<Video k>` steht), dann eigenständiges Audio.
- Eine mit `ref_video_audio_N` verbundene Tonspur wird mit dem Referenzvideo verwendet, das mit `ref_video_N` verbunden ist.
- Referenzvideos müssen mindestens 5 Frames enthalten (ca. 0,2 Sekunden bei 24 fps), andernfalls löst der Node einen Fehler aus. Frames über die angeforderte `length` hinaus werden abgeschnitten, und die verbleibende Frame-Anzahl wird an einen vom Modell unterstützten Wert angepasst.
- Die angeforderte `length` wird vor der Erstellung des Latents an eine unterstützte Frame-Anzahl ausgerichtet.
- Ohne `vae` werden Referenzbilder und -videos nur zur Konditionierung des Text-Encoders verwendet (es werden keine Referenz-Latents erzeugt). Ohne `audio_vae` wird Referenzaudio nur zur Konditionierung des Text-Encoders verwendet.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|--------------|----------|
| `positive` | Conditioning, das den kodierten Prompt enthält. Wenn Referenzmedien und die relevanten VAEs bereitgestellt werden, enthält es außerdem die kodierten Inhalte der Referenzbilder, -videos und -audios, die vom MiniMax H3-Modell verwendet werden. | CONDITIONING |
| `latent` | Leeres Audio-Video-Latent mit der angeforderten `width`, `height` und `length` (Frame-Anzahl), einschließlich des ausgerichteten Video-Latents und Audio-Latents. | LATENT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MiniMaxH3ReferenceToVideo/de.md)

---
**Source fingerprint (SHA-256):** `47df0d6d13cb02aa4f69b50a7f8d0f6c1639c1fb5e0f69bf8fc57dd4cb752db8`
