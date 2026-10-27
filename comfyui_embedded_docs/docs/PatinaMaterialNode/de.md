# Patina Material

Erzeugt ein vollständiges, nahtlos kachelbares PBR-Material aus einer Textbeschreibung: eine Basistextur plus bis zu fünf Material-Maps, mit optionalem SeedVR-Upscaling der Maps. Ein Eingabebild kann das Ergebnis als Image-to-Image-Durchlauf steuern, und ein Eingabebild mit Maske macht daraus einen Inpaint-Durchlauf. Damit lassen sich spielfertige oder 3D-fertige Oberflächen erzeugen, ohne ein echtes Material zu scannen.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Beschreibung des zu generierenden Materials oder der Textur. | STRING | Ja | Mehrzeiliger Text |
| `image_size` | Größe der Ausgabetextur. `"custom"` blendet die Eingaben `width` und `height` ein. Standard: `"1:1 (1024x1024)"`. | DYNAMIC_COMBO | Ja | `"1:1 (1024x1024)"`<br>`"1:1 (512x512)"`<br>`"4:3 (1024x768)"`<br>`"3:4 (768x1024)"`<br>`"16:9 (1024x576)"`<br>`"9:16 (576x1024)"`<br>`"custom"` |
| `basecolor` | Erzeugt die Basecolor-(Albedo-)Map. Standard: True. | BOOLEAN | Ja | true<br>false |
| `normal` | Erzeugt die Normal-Map. Standard: True. | BOOLEAN | Ja | true<br>false |
| `roughness` | Erzeugt die Roughness-Map. Standard: False. | BOOLEAN | Ja | true<br>false |
| `metalness` | Erzeugt die Metalness-Map. Standard: False. | BOOLEAN | Ja | true<br>false |
| `height` | Erzeugt die Height-(Displacement-)Map. Standard: False. | BOOLEAN | Ja | true<br>false |
| `upscale_factor` | Nahtloses SeedVR-Upscaling der PBR-Maps. Die Basistextur wird nicht hochskaliert, und 4x macht aus einer 2048-Pixel-Map eine 8K-Map. Standard: 0 (aus). | INT | Ja | 0 bis 4 (Schritt 2) |
| `seed` | Seed für reproduzierbare Generierung. Standard: 42. | INT | Ja | 0 bis 2147483646 |
| `tiling_mode` | Kachelungsrichtung: omnidirektional, horizontal oder vertikal. Erweiterte Einstellung. Standard: `"both"`. | COMBO | Ja | `"both"`<br>`"horizontal"`<br>`"vertical"` |
| `num_inference_steps` | Denoising-Schritte für die Texturerzeugung. Erweiterte Einstellung. Standard: 8. | INT | Ja | 1 bis 8 |
| `tile_size` | Kachelgröße im Latent Space, wobei 64 für 512 Pixel und 128 für 1024 Pixel steht. Erweiterte Einstellung. Standard: 128. | INT | Ja | 32 bis 256 (Schritt 2) |
| `tile_stride` | Kachel-Schrittweite im Latent Space. Erweiterte Einstellung. Standard: 64. | INT | Ja | 16 bis 128 (Schritt 2) |
| `image` | Optionales Quellbild. Allein verwendet führt es einen Image-to-Image-Durchlauf aus; zusammen mit einer Maske führt es einen Inpaint-Durchlauf aus. | IMAGE | Nein | - |
| `mask` | Optionale Inpaint-Maske, erfordert ein Eingabebild. Weiße Bereiche werden neu generiert, schwarze Bereiche bleiben erhalten. | MASK | Nein | - |
| `strength` | Wie stark das Eingabebild verändert wird. Wird nur verwendet, wenn ein Bild verbunden ist. Erweiterte Einstellung. Standard: 0.6. | FLOAT | Ja | 0.01 bis 1.0 (Schritt 0.01) |
| `prompt_expansion` | Erweitert den Prompt mit einem Sprachmodell für reichere Texturdetails. Standardmäßig deaktiviert, da die Erweiterung den Prompt als Fotografie neu formuliert und dazu neigt, die Metalness-Map auszuwaschen. Erweiterte Einstellung. | BOOLEAN | Ja | true<br>false |
| `safety_checker` | Führt die Inhalts-Sicherheitsprüfung des Anbieters für die Anfrage aus. Erweiterte Einstellung. Standard: False. | BOOLEAN | Ja | true<br>false |

### Benutzerdefinierte Bildgrößen-Eingaben

Diese Eingaben erscheinen, wenn `image_size` auf `"custom"` gesetzt ist.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `image_size.width` | Texturbreite in Pixeln. Standard: 1024. | INT | Ja | 512 bis 2048 (Schritt 16) |
| `image_size.height` | Texturhöhe in Pixeln. Standard: 1024. | INT | Ja | 512 bis 2048 (Schritt 16) |

**Einschränkungen und Verhalten:**

* Mindestens eine Material-Map muss aktiviert sein, andernfalls schlägt der Lauf fehl.
* Eine Maske erfordert ein Eingabebild; eine Maske allein löst einen Fehler aus.
* Ein 8K-Ergebnis entsteht durch 4x-Upscaling der Maps eines 2048-Pixel-Renderings, nicht durch eine einzelne 8K-Generierung.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `texture` | Die Basistextur des Materials, ohne dass eine Map angewendet wurde. | IMAGE |
| `basecolor` | Die Basecolor-(Albedo-)Map oder ein 1x1-Platzhalter, wenn diese Map deaktiviert ist. | IMAGE |
| `normal` | Die Normal-Map oder ein 1x1-Platzhalter, wenn diese Map deaktiviert ist. | IMAGE |
| `roughness` | Die Roughness-Map oder ein 1x1-Platzhalter, wenn diese Map deaktiviert ist. | IMAGE |
| `metalness` | Die Metalness-Map oder ein 1x1-Platzhalter, wenn diese Map deaktiviert ist. | IMAGE |
| `height` | Die Height-(Displacement-)Map oder ein 1x1-Platzhalter, wenn diese Map deaktiviert ist. | IMAGE |
| `expanded_prompt` | Der Prompt, den der Anbieter tatsächlich verwendet hat; er unterscheidet sich nur dann von der Eingabe, wenn `prompt_expansion` aktiviert ist. | STRING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PatinaMaterialNode/de.md)

---
**Source fingerprint (SHA-256):** `4e8305fa56a29dce72c54de12ae05207e8de39a1fea1f4753906c26e8af60383`
