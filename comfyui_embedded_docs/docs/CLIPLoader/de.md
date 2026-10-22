# ClipLoader

Der Node CLIPLoader lädt ein Textencoder-Modell (CLIP, T5 oder ähnlich) aus einer Datei und macht es für die Verwendung in anderen Nodes verfügbar, die Text-Prompts in numerische Repräsentationen umwandeln müssen. Er unterstützt eine Vielzahl von Modellarchitekturen, die jeweils einen bestimmten Encodertyp erfordern.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `clip_name` | Der Dateiname des zu ladenden Textencoder-Modells. Dies muss eine Datei im Verzeichnis `ComfyUI/models/text_encoders/` sein. | STRING | Ja | Liste der im Ordner `text_encoders` gefundenen Dateien |
| `type` | Der Architekturtyp des zu ladenden Modells. Dies bestimmt, welche spezifische Encoder-Variante verwendet wird (Standard: `"stable_diffusion"`). | COMBO | Ja | `"stable_diffusion"`<br>`"stable_cascade"`<br>`"sd3"`<br>`"stable_audio"`<br>`"mochi"`<br>`"ltxv"`<br>`"pixart"`<br>`"cosmos"`<br>`"lumina2"`<br>`"wan"`<br>`"hidream"`<br>`"chroma"`<br>`"ace"`<br>`"omnigen2"`<br>`"qwen_image"`<br>`"hunyuan_image"`<br>`"flux2"`<br>`"ovis"`<br>`"longcat_image"`<br>`"cogvideox"`<br>`"lens"`<br>`"pixeldit"`<br>`"ideogram4"`<br>`"boogu"`<br>`"krea2"`<br>`"joyimage"`<br>`"mage"`<br>`"minimax"`<br>`"yue2"`<br>`"flux3"`<br>`"moss_image"` |
| `device` | Das Gerät, auf das das Modell geladen wird. `"default"` verwendet die GPU, falls verfügbar, während `"cpu"` das Laden auf die CPU erzwingt. Dies ist eine erweiterte Option (Standard: `"default"`). | COMBO | Nein | `"default"`<br>`"cpu"` |

### Unterstützte Typ-zu-Encoder-Zuordnungen

Der Parameter `type` wählt den richtigen Encoder für eine gegebene Modellarchitektur aus. Im Folgenden sind gängige Zuordnungen aufgeführt:

| Typ | Encoder |
|------|---------|
| stable_diffusion | clip-l |
| stable_cascade | clip-g |
| sd3 | t5 xxl / clip-g / clip-l |
| stable_audio | t5 base |
| mochi | t5 xxl |
| cogvideox | t5 xxl (226-Token-Padding) |
| cosmos | old t5 xxl |
| lumina2 | gemma 2 2B |
| wan | umt5 xxl |
| hidream | llama-3.1 (empfohlen) oder t5 |
| omnigen2 | qwen vl 2.5 3B |
| joyimage | qwen3-vl 8B |
| lens | gpt-oss-20b |
| pixeldit | gemma 2 2B elm |
| minimax | MiniMax H3 Qwen3-VL oder Music3 Qwen/RVQ |
| flux3 | qwen3-vl 4B |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `CLIP` | Das geladene Textencoder-Modell, bereit, mit anderen Nodes für Textkodierung und Konditionierung verbunden zu werden. | CLIP |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPLoader/de.md)

---
**Source fingerprint (SHA-256):** `3abcb39dd6ce4935f51127d4d38a8474ecf80a4df70d702f3eea68d400be91a5`
