# MiniMax Music3 Text Encode

MiniMax Music3 Text Encode verwendet ein MiniMax Music3 CLIP-Modell, um Textbeschreibungen und Liedtexte in eine akustische Konditionierungssequenz für die Musikgenerierung umzuwandeln. Der Node gibt die resultierenden CONDITIONING-Daten zusammen mit der tatsächlichen Audiodauer in Sekunden zurück, die aus der eingegebenen Maximaldauer berechnet wird.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `clip` | Das MiniMax Music3 CLIP-Modell, das für die Textkodierung und die Generierung der Konditionierungssequenz verwendet wird. | CLIP | Ja | - |
| `caption` | Text, der die zu generierende Musik beschreibt. Unterstützt mehrzeiligen Text und dynamische Prompts. | STRING | Ja | - |
| `lyrics` | Der Liedtext, der zur Musikgenerierung verwendet wird. Unterstützt mehrzeiligen Text und dynamische Prompts. | STRING | Ja | - |
| `seed` | Reproduzierbarer Zufallsseed für den Generierungsprozess. Standard: 0. Ein Widget zur Steuerung nach der Generierung wird bereitgestellt. | INT | Ja | 0 to 18446744073709551615 (0xffffffffffffffff) |
| `max_duration` | Maximale Dauer in Sekunden; das Modell kann das Lied früher beenden. Standard: 120.0. | FLOAT | Ja | 0.04 bis zur maximalen Audiodauer des Modells (MAX_AUDIO_FRAMES / AUDIO_FRAMES_PER_SECOND), Schrittweite 0.04 |
| `cfg_scale` | Classifier-Free-Guidance-Skala. Standard: Modellkonstante CFG_SCALE. Erweiterter Parameter. | FLOAT | Ja | 0.0 bis 100.0, Schrittweite 0.1 (behält 2 Dezimalstellen) |
| `top_k` | Top-k-Sampling-Wert, der für die Auswahl akustischer Token verwendet wird. Standard: Modellkonstante CFG_TOP_K. Erweiterter Parameter. | INT | Ja | 1 bis zur Vokabulargröße des Modells (C0_VOCAB_SIZE) |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `conditioning` | Die generierte akustische Konditionierungssequenz, die zur Steuerung der nachfolgenden Musikgenerierung verwendet wird. | CONDITIONING |
| `seconds` | Die tatsächliche Dauer der Konditionierungssequenz in Sekunden. | FLOAT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MiniMaxMusic3TextEncode/de.md)

---
**Source fingerprint (SHA-256):** `c3fbfd189d0358ebf081dd4f9c32be9231a9d0b97fd767401ea4b7955224c25c`
