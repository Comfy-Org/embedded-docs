# Text kodieren Qwen Image Edit Plus

Der Node TextEncodeQwenImageEditPlus verarbeitet einen Text-Prompt und bis zu drei optionale Bilder, um Conditioning-Daten für Bildgenerierungs- oder Bildbearbeitungsaufgaben zu erzeugen. Er verwendet eine spezialisierte Vorlage, die das Modell zunächst auffordert, die wichtigsten Merkmale der Eingabebilder zu beschreiben, und dann zu erklären, wie die Textanweisung des Benutzers sie verändern soll, sodass das kodierte Ergebnis sowohl die Bilder als auch die gewünschte Änderung versteht. Wenn ein VAE bereitgestellt wird, erstellt der Node außerdem Referenz-Latents aus den Eingabebildern.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `clip` | Das CLIP-Modell, das für Tokenisierung und Kodierung verwendet wird | CLIP | Ja | - |
| `prompt` | Textanweisung, die die gewünschte Bildänderung beschreibt (unterstützt mehrzeilige Eingabe und dynamische Prompts) | STRING | Ja | - |
| `vae` | Optionales VAE-Modell zum Erzeugen von Referenz-Latents aus den Eingabebildern | VAE | Nein | - |
| `image1` | Erstes optionales Eingabebild für Analyse und Änderung | IMAGE | Nein | - |
| `image2` | Zweites optionales Eingabebild für Analyse und Änderung | IMAGE | Nein | - |
| `image3` | Drittes optionales Eingabebild für Analyse und Änderung | IMAGE | Nein | - |

**Hinweis:** Wenn ein VAE bereitgestellt wird, erzeugt der Node Referenz-Latents aus allen bereitgestellten Eingabebildern. Es können bis zu drei Bilder gleichzeitig verarbeitet werden. Bilder werden für die Vision-Language-Verarbeitung auf eine Zielfläche von 384x384 Pixeln skaliert (Seitenverhältnis beibehalten) und für die VAE-Kodierung auf Abmessungen, die durch 8 teilbar sind (mit einer Zielfläche von 1024x1024 Pixeln).

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `CONDITIONING` | Kodierte Conditioning-Daten, die Text-Tokens und optionale Referenz-Latents für die Bildgenerierung enthalten | CONDITIONING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeQwenImageEditPlus/de.md)

---
**Source fingerprint (SHA-256):** `5eea53a84045924b44d445244e6149b341188d22573aaaced87bac8a139dac96`
