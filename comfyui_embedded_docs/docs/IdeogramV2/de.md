# IdeogramV2

Der Ideogram V2-Node erzeugt Bilder mit dem Ideogram V2 KI-Modell. Er verwendet Text-Prompts und verschiedene Generierungseinstellungen, um Bilder über einen API-Dienst zu erstellen. Der Node unterstützt verschiedene Seitenverhältnisse, Auflösungen und Stiloptionen, um die Ausgabebilder anzupassen.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Prompt für die Bilderzeugung (Standard: leerer String) | STRING | Ja | - |
| `turbo` | Ob der Turbo-Modus verwendet werden soll (schnellere Generierung, möglicherweise geringere Qualität) (Standard: False) | BOOLEAN | Nein | - |
| `aspect_ratio` | Das Seitenverhältnis für die Bilderzeugung. Wird ignoriert, wenn `resolution` nicht auf AUTO gesetzt ist. (Standard: "1:1") | COMBO | Nein | "1:1"<br>"4:3"<br>"3:4"<br>"16:9"<br>"9:16"<br>"2:1"<br>"1:2"<br>"3:2"<br>"2:3"<br>"4:5"<br>"5:4" |
| `resolution` | Die Auflösung für die Bilderzeugung. Wenn nicht auf AUTO gesetzt, überschreibt dies die Einstellung `aspect_ratio`. (Standard: "Auto") | COMBO | Nein | "Auto"<br>"512 x 1536"<br>"576 x 1408"<br>"576 x 1472"<br>"576 x 1536"<br>"640 x 1024"<br>"640 x 1344"<br>"640 x 1408"<br>"640 x 1472"<br>"640 x 1536"<br>"704 x 1152"<br>"704 x 1216"<br>"704 x 1280"<br>"704 x 1344"<br>"704 x 1408"<br>"704 x 1472"<br>"720 x 1280"<br>"736 x 1312"<br>"768 x 1024"<br>"768 x 1088"<br>"768 x 1152"<br>"768 x 1216"<br>"768 x 1232"<br>"768 x 1280"<br>"768 x 1344"<br>"832 x 960"<br>"832 x 1024"<br>"832 x 1088"<br>"832 x 1152"<br>"832 x 1216"<br>"832 x 1248"<br>"864 x 1152"<br>"896 x 960"<br>"896 x 1024"<br>"896 x 1088"<br>"896 x 1120"<br>"896 x 1152"<br>"960 x 832"<br>"960 x 896"<br>"960 x 1024"<br>"960 x 1088"<br>"1024 x 640"<br>"1024 x 768"<br>"1024 x 832"<br>"1024 x 896"<br>"1024 x 960"<br>"1024 x 1024"<br>"1088 x 768"<br>"1088 x 832"<br>"1088 x 896"<br>"1088 x 960"<br>"1120 x 896"<br>"1152 x 704"<br>"1152 x 768"<br>"1152 x 832"<br>"1152 x 864"<br>"1152 x 896"<br>"1216 x 704"<br>"1216 x 768"<br>"1216 x 832"<br>"1232 x 768"<br>"1248 x 832"<br>"1280 x 704"<br>"1280 x 720"<br>"1280 x 768"<br>"1280 x 800"<br>"1312 x 736"<br>"1344 x 640"<br>"1344 x 704"<br>"1344 x 768"<br>"1408 x 576"<br>"1408 x 640"<br>"1408 x 704"<br>"1472 x 576"<br>"1472 x 640"<br>"1472 x 704"<br>"1536 x 512"<br>"1536 x 576"<br>"1536 x 640" |
| `magic_prompt_option` | Legt fest, ob MagicPrompt bei der Generierung verwendet werden soll (Standard: "AUTO") | COMBO | Nein | "AUTO"<br>"ON"<br>"OFF" |
| `seed` | Zufälliger Seed für die Generierung (Standard: 0) | INT | Nein | 0-2147483647 |
| `style_type` | Stiltyp für die Generierung (nur V2) (Standard: "NONE") | COMBO | Nein | "AUTO"<br>"GENERAL"<br>"REALISTIC"<br>"DESIGN"<br>"RENDER_3D"<br>"ANIME" |
| `negative_prompt` | Beschreibung dessen, was aus dem Bild ausgeschlossen werden soll (Standard: leerer String) | STRING | Nein | - |
| `num_images` | Anzahl der zu generierenden Bilder (Standard: 1) | INT | Nein | 1-8 |

**Hinweis:** Wenn `resolution` nicht auf "Auto" gesetzt ist, überschreibt es die Einstellung `aspect_ratio`. Der Parameter `num_images` hat eine Obergrenze von 8 Bildern pro Generierung.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `output` | Das/die vom Ideogram V2-Modell generierte(n) Bild(er) | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/IdeogramV2/de.md)

---
**Source fingerprint (SHA-256):** `a034a57996ac0b3902cab36096ac6b8401bb544faa00b8ed213bf752fdd423e2`
