# Patina Material Extract

Extrahiert ein nahtlos kachelbares PBR-Material aus einem Bereich eines Eingabebilds, gesteuert durch einen Prompt, der benennt, was entnommen werden soll: eine Wand, ein Boden, ein Stoff. Es gibt die extrahierte Basistextur sowie bis zu fünf Material-Maps zurück, mit optionalem SeedVR-Upscaling der Maps. Verwenden Sie es, um ein Foto einer realen Oberfläche in ein wiederverwendbares, kachelbares Material umzuwandeln.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `image` | Das Bild, aus dem eine Textur extrahiert werden soll. | IMAGE | Ja | - |
| `prompt` | Beschreibung, welche Textur aus dem Bild extrahiert werden soll, zum Beispiel `"the wall"`. | STRING | Ja | Mehrzeiliger Text |
| `image_size` | Ausgabegröße der Textur. `"custom"` blendet die Eingaben `width` und `height` ein. Standard: `"1:1 (1024x1024)"`. | DYNAMIC_COMBO | Ja | `"1:1 (1024x1024)"`<br>`"1:1 (512x512)"`<br>`"4:3 (1024x768)"`<br>`"3:4 (768x1024)"`<br>`"16:9 (1024x576)"`<br>`"9:16 (576x1024)"`<br>`"custom"` |
| `basecolor` | Die Basecolor-(Albedo-)Map generieren. Standard: True. | BOOLEAN | Ja | true<br>false |
| `normal` | Die Normal-Map generieren. Standard: True. | BOOLEAN | Ja | true<br>false |
| `roughness` | Die Roughness-Map generieren. Standard: False. | BOOLEAN | Ja | true<br>false |
| `metalness` | Die Metalness-Map generieren. Standard: False. | BOOLEAN | Ja | true<br>false |
| `height` | Die Height-(Displacement-)Map generieren. Standard: False. | BOOLEAN | Ja | true<br>false |
| `upscale_factor` | Nahtloses SeedVR-Upscaling der PBR-Maps. Die Basistextur wird nicht hochskaliert, und 4x verwandelt eine 2048-Pixel-Map in eine 8K-Map. Standard: 0 (aus). | INT | Ja | 0 bis 4 (Schritt 2) |
| `seed` | Seed für reproduzierbare Generierung. Standard: 42. | INT | Ja | 0 bis 2147483646 |
| `strength` | Wie stark das Eingabebild transformiert wird. Erweiterte Einstellung. Standard: 0.6. | FLOAT | Ja | 0.01 bis 1.0 (Schritt 0.01) |
| `tiling_mode` | Kachelrichtung: omnidirektional, horizontal oder vertikal. Erweiterte Einstellung. Standard: `"both"`. | COMBO | Ja | `"both"`<br>`"horizontal"`<br>`"vertical"` |
| `num_inference_steps` | Denoising-Schritte für die Texturgenerierung. Erweiterte Einstellung. Standard: 8. | INT | Ja | 1 bis 8 |
| `tile_size` | Kachelgröße im latenten Raum, wobei 64 512 Pixel und 128 1024 Pixel bedeutet. Erweiterte Einstellung. Standard: 128. | INT | Ja | 32 bis 256 (Schritt 2) |
| `tile_stride` | Kachel-Schrittweite im latenten Raum. Erweiterte Einstellung. Standard: 64. | INT | Ja | 16 bis 128 (Schritt 2) |
| `prompt_expansion` | Den Prompt mit einem Sprachmodell erweitern, um reichere Texturdetails zu erhalten. Standardmäßig deaktiviert, da die Erweiterung den Prompt als Fotografie neu formuliert und dazu neigt, die Metalness-Map auszuwaschen. Erweiterte Einstellung. | BOOLEAN | Ja | true<br>false |
| `safety_checker` | Die Inhaltsicherheitsprüfung des Anbieters für die Anfrage ausführen. Erweiterte Einstellung. Standard: False. | BOOLEAN | Ja | true<br>false |

### Benutzerdefinierte Bildgrößen-Eingaben

Diese Eingaben erscheinen, wenn `image_size` auf `"custom"` gesetzt ist.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `image_size.width` | Texturbreite in Pixeln. Standard: 1024. | INT | Ja | 512 bis 2048 (Schritt 16) |
| `image_size.height` | Texturhöhe in Pixeln. Standard: 1024. | INT | Ja | 512 bis 2048 (Schritt 16) |

**Einschränkungen und Verhalten:**

* Mindestens eine Material-Map muss aktiviert sein, andernfalls schlägt die Ausführung fehl.
* Der Prompt ist erforderlich und darf nicht leer sein; benennen Sie den zu extrahierenden Bereich so präzise wie möglich.
* Ein 8K-Ergebnis entsteht durch 4x-Upscaling der Maps eines 2048-Pixel-Renderings, nicht durch eine einzelne 8K-Generierung.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `texture` | Die extrahierte Basistextur, ohne angewendete Map. | IMAGE |
| `basecolor` | Die Basecolor-(Albedo-)Map oder ein 1x1-Platzhalter, wenn diese Map deaktiviert ist. | IMAGE |
| `normal` | Die Normal-Map oder ein 1x1-Platzhalter, wenn diese Map deaktiviert ist. | IMAGE |
| `roughness` | Die Roughness-Map oder ein 1x1-Platzhalter, wenn diese Map deaktiviert ist. | IMAGE |
| `metalness` | Die Metalness-Map oder ein 1x1-Platzhalter, wenn diese Map deaktiviert ist. | IMAGE |
| `height` | Die Height-(Displacement-)Map oder ein 1x1-Platzhalter, wenn diese Map deaktiviert ist. | IMAGE |
| `expanded_prompt` | Der Prompt, den der Anbieter tatsächlich verwendet hat; er weicht nur dann vom Eingabe-Prompt ab, wenn `prompt_expansion` aktiviert ist. | STRING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PatinaMaterialExtractNode/de.md)

---
**Source fingerprint (SHA-256):** `484b8eaa57388541e352cd88c8998c63aa0b2a99d98cd8e602252625064f16ba`
