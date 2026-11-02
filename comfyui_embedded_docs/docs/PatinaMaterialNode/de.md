# Patina Material

Erzeugt ein vollständiges, nahtlos kachelbares PBR-Material aus einer Textbeschreibung: eine Basistextur plus bis zu fünf Material-Maps, mit optionaler SeedVR-Hochskalierung der Maps. Ein Eingabebild kann das Ergebnis als Image-to-Image-Durchlauf steuern, und ein Eingabebild mit einer Maske verwandelt es in einen Inpaint-Durchlauf. Verwenden Sie es, um spielfertige oder 3D-fertige Oberflächen zu produzieren, ohne ein reales Material scannen zu müssen.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Beschreibung des zu erzeugenden Materials oder der Textur. | STRING | Ja | Mehrzeiliger Text |
| `image_size` | Größe der Ausgabetextur. `"custom"` blendet die Eingaben `width` und `height` ein. Standard: `"1:1 (1024x1024)"`. | DYNAMIC_COMBO | Ja | `"1:1 (1024x1024)"`<br>`"1:1 (512x512)"`<br>`"4:3 (1024x768)"`<br>`"3:4 (768x1024)"`<br>`"16:9 (1024x576)"`<br>`"9:16 (576x1024)"`<br>`"custom"` |
| `basecolor` | Die Basecolor-(Albedo-)Map erzeugen. Standard: True. | BOOLEAN | Ja | true<br>false |
| `normal` | Die Normal-Map erzeugen. Standard: True. | BOOLEAN | Ja | true<br>false |
| `roughness` | Die Roughness-Map erzeugen. Standard: False. | BOOLEAN | Ja | true<br>false |
| `metalness` | Die Metalness-Map erzeugen. Standard: False. | BOOLEAN | Ja | true<br>false |
| `height` | Die Height-(Displacement-)Map erzeugen. Standard: False. | BOOLEAN | Ja | true<br>false |
| `upscale_factor` | Nahtlose SeedVR-Hochskalierung der PBR-Maps. Die Basistextur wird nicht hochskaliert, und 4x macht aus einer 2048-Pixel-Map eine 8K-Map. Standard: 0 (aus). | INT | Ja | 0 bis 4 (Schritt 2) |
| `seed` | Seed für reproduzierbare Generierung. Standard: 42. | INT | Ja | 0 bis 2147483646 |
| `tiling_mode` | Kachelrichtung: omnidirektional, horizontal oder vertikal. Erweiterte Einstellung. Standard: `"both"`. | COMBO | Ja | `"both"`<br>`"horizontal"`<br>`"vertical"` |
| `num_inference_steps` | Denoising-Schritte für die Texturerzeugung. Erweiterte Einstellung. Standard: 8. | INT | Ja | 1 bis 8 |
| `tile_size` | Kachelgröße im Latentraum, wobei 64 für 512 Pixel und 128 für 1024 Pixel steht. Erweiterte Einstellung. Standard: 128. | INT | Ja | 32 bis 256 (Schritt 2) |
| `tile_stride` | Kachelschrittweite im Latentraum. Erweiterte Einstellung. Standard: 64. | INT | Ja | 16 bis 128 (Schritt 2) |
| `image` | Optionales Quellbild. Allein ausgeführt startet es einen Image-to-Image-Durchlauf; zusammen mit einer Maske startet es einen Inpaint-Durchlauf. | IMAGE | Nein | - |
| `mask` | Optionale Inpaint-Maske, erfordert ein Eingabebild. Weiße Bereiche werden neu erzeugt und schwarze Bereiche bleiben erhalten. | MASK | Nein | - |
| `strength` | Wie stark das Eingabebild verändert wird. Wird nur verwendet, wenn ein Bild verbunden ist. Erweiterte Einstellung. Standard: 0.6. | FLOAT | Ja | 0.01 bis 1.0 (Schritt 0.01) |
| `prompt_expansion` | Den Prompt mit einem Sprachmodell erweitern, um reichhaltigere Texturdetails zu erhalten. Standardmäßig aus, da die Erweiterung den Prompt als Fotografie neu rahmt und dazu neigt, die Metalness-Map auszuwaschen. Erweiterte Einstellung. | BOOLEAN | Ja | true<br>false |
| `safety_checker` | Die Inhaltsicherheitsprüfung des Anbieters für die Anfrage ausführen. Erweiterte Einstellung. Standard: False. | BOOLEAN | Ja | true<br>false |

### Benutzerdefinierte Bildgrößen-Eingaben

Diese Eingaben erscheinen, wenn `image_size` auf `"custom"` gesetzt ist.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `image_size.width` | Texturbreite in Pixeln. Standard: 1024. | INT | Ja | 512 bis 2048 (Schritt 16) |
| `image_size.height` | Texturhöhe in Pixeln. Standard: 1024. | INT | Ja | 512 bis 2048 (Schritt 16) |

**Einschränkungen und Verhalten:**

* Es ist erlaubt, keine Material-Map zu aktivieren: Der Node gibt dann nur die Basistextur zurück, und jeder Map-Ausgang bleibt ein 1x1-Platzhalter.
* Eine Maske erfordert ein Eingabebild; eine Maske allein löst einen Fehler aus.
* Ein 8K-Ergebnis entsteht durch 4-fache Hochskalierung der Maps eines 2048-Pixel-Renders, nicht durch eine einzelne 8K-Generierung.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `texture` | Die Basistextur des Materials, ohne angewendete Map. | IMAGE |
| `basecolor` | Die Basecolor-(Albedo-)Map oder ein 1x1-Platzhalter, wenn diese Map deaktiviert ist. | IMAGE |
| `normal` | Die Normal-Map oder ein 1x1-Platzhalter, wenn diese Map deaktiviert ist. | IMAGE |
| `roughness` | Die Roughness-Map oder ein 1x1-Platzhalter, wenn diese Map deaktiviert ist. | IMAGE |
| `metalness` | Die Metalness-Map oder ein 1x1-Platzhalter, wenn diese Map deaktiviert ist. | IMAGE |
| `height` | Die Height-(Displacement-)Map oder ein 1x1-Platzhalter, wenn diese Map deaktiviert ist. | IMAGE |
| `expanded_prompt` | Der Prompt, den der Anbieter tatsächlich verwendet hat, und der sich nur dann von der Eingabe unterscheidet, wenn `prompt_expansion` aktiviert ist. | STRING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PatinaMaterialNode/de.md)

---
**Source fingerprint (SHA-256):** `4e8305fa56a29dce72c54de12ae05207e8de39a1fea1f4753906c26e8af60383`
