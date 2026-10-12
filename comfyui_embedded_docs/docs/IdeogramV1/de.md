# IdeogramV1

Der IdeogramV1-Node generiert Bilder mithilfe des Ideogram V1-Modells über eine API. Er nimmt Text-Prompts und verschiedene Generierungseinstellungen entgegen, um basierend auf Ihrer Eingabe ein oder mehrere Bilder zu erstellen. Der Node unterstützt verschiedene Seitenverhältnisse und Generierungsmodi, um die Ausgabe anzupassen.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Prompt für die Bilderzeugung (Standard: leer) | STRING | Ja | - |
| `turbo` | Ob der Turbo-Modus verwendet werden soll (schnellere Generierung, möglicherweise geringere Qualität) (Standard: False) | BOOLEAN | Ja | - |
| `aspect_ratio` | Das Seitenverhältnis für die Bilderzeugung (Standard: "1:1") | COMBO | Nein | "1:1"<br>"4:3"<br>"3:4"<br>"16:9"<br>"9:16"<br>"2:1"<br>"1:2"<br>"3:2"<br>"2:3"<br>"4:5"<br>"5:4" |
| `magic_prompt_option` | Legt fest, ob MagicPrompt bei der Generierung verwendet werden soll (Standard: "AUTO") | COMBO | Nein | "AUTO"<br>"ON"<br>"OFF" |
| `seed` | Zufälliger Seed-Wert für die Generierung (Standard: 0) | INT | Nein | 0-2147483647 |
| `negative_prompt` | Beschreibung dessen, was vom Bild ausgeschlossen werden soll (Standard: leer) | STRING | Nein | - |
| `num_images` | Anzahl der zu generierenden Bilder (Standard: 1) | INT | Nein | 1-8 |

**Hinweis:** Der Parameter `num_images` hat eine Obergrenze von 8 Bildern pro Generierungsanfrage.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `output` | Das/die vom Ideogram V1-Modell generierte(n) Bild(er) | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/IdeogramV1/de.md)

---
**Source fingerprint (SHA-256):** `c9b336054cf5d66228aeccab615985d2e9c9bdf7dce5d607212fed8a35c2c793`
