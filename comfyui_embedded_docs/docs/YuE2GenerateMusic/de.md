# YuE2GenerateMusic

Erzeugt Musik-Tokens und akustische Konditionierung aus einem Stil, Liedtext und einer ABC-Notation. Es gibt die Konditionierung und die erzeugte Dauer in Sekunden zurück, die an den Empty YuE2 Latent Audio-Node übergeben werden sollten. Wenn die ABC-Eingabe leer bleibt, wird der ausgewählte Modus ignoriert und automatisch der Off-Modus verwendet.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `clip` | Das CLIP-Modell, das zum Tokenisieren und Kodieren der Musikeingaben verwendet wird. | CLIP | Ja | - |
| `style` | Text, der den Musikstil beschreibt. Unterstützt mehrzeilige Eingaben und dynamische Prompts. | STRING | Ja | Mehrzeiliger Text |
| `lyrics` | Liedtext für die erzeugte Musik. Unterstützt mehrzeilige Eingaben und dynamische Prompts. | STRING | Ja | Mehrzeiliger Text |
| `abc` | Verbinden Sie den ABC-Generator oder stellen Sie eine bearbeitete Partitur bereit. Leer lassen, um automatisch den Off-Modus zu verwenden. Standard: "" | STRING | Ja | Mehrzeiliger Text |
| `seed` | Zufälliger Seed für die Generierung. Standard: 0 | INT | Ja | 0 bis 18446744073709551615 |
| `mode` | full: erzeugt Melodie und Akkorde; melody: erzeugt nur die Melodie, empfohlen für Cover. Standard: "full" | COMBO | Ja | "full"<br>"melody" |
| `max_duration` | Maximale Dauer in Sekunden. Wird bei langen Prompts automatisch reduziert; die Generierung kann früher stoppen. Standard: 360.0 | FLOAT | Ja | 0.04 bis 900.0 |
| `temperature` | Sampling-Temperatur für die Generierung. Standard: 1.0 (erweitert) | FLOAT | Ja | 0.0 bis 5.0 |
| `top_p` | Wahrscheinlichkeitsschwelle für Nucleus-Sampling. Standard: 0.95 (erweitert) | FLOAT | Ja | 0.01 bis 1.0 |
| `top_k` | Top-k-Sampling-Limit. Standard: 100 (erweitert) | INT | Ja | 1 bis 32768 |
| `repetition_penalty` | Strafe für wiederholte Tokens. Standard: 1.2 (erweitert) | FLOAT | Ja | 0.01 bis 10.0 |
| `cfg_scale` | Autoregressive Führung für Stil und Liedtext. 1.0 deaktiviert CFG, passend zum ABC-Workflow. Verwenden Sie 1.01, um der ursprünglichen Off-Modus-Führung zu entsprechen. Standard: 1.0 (erweitert, optional) | FLOAT | Nein | 0.0 bis 100.0 |

Hinweis: Wenn `abc` leer ist oder nur Leerzeichen enthält, wird die Auswahl von `mode` ignoriert und automatisch der Off-Modus verwendet.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `CONDITIONING` | Akustische Konditionierung, die aus den Musik-Tokens erzeugt wird. | CONDITIONING |
| `seconds` | Die erzeugte Audiodauer in Sekunden. Übergeben Sie diesen Wert an den Empty YuE2 Latent Audio-Node. | FLOAT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/YuE2GenerateMusic/de.md)

---
**Source fingerprint (SHA-256):** `5a88e185d2998c51acff7f0c76c8c35ca30b80b88cb541d97f9ab91566b5a3ed`
