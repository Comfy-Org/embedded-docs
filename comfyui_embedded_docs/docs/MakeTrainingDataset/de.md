# Trainingsdatensatz erstellen

Dieser Node bereitet Daten für das Training vor, indem er Bilder und Text kodiert. Er nimmt eine Liste von Bildern und eine entsprechende Liste von Textbeschriftungen entgegen und verwendet dann ein VAE-Modell, um die Bilder in Latent-Darstellungen umzuwandeln, sowie ein CLIP-Modell, um den Text in Conditioning-Daten umzuwandeln. Die resultierenden gepaarten Latents und Conditioning-Daten werden als Listen ausgegeben und sind für die Verwendung in Trainings-Workflows bereit.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `images` | Liste der zu kodierenden Bilder. | IMAGE | Ja | N/A |
| `vae` | VAE-Modell zum Kodieren von Bildern in Latents. | VAE | Ja | N/A |
| `clip` | CLIP-Modell zum Kodieren von Text in Conditioning. | CLIP | Ja | N/A |
| `texts` | Liste von Textbeschriftungen. Kann die Länge n haben (entsprechend den Bildern), 1 (für alle wiederholt) oder weggelassen werden (verwendet eine leere Zeichenkette). | STRING | Nein | 0, 1 oder n Elemente (n = Anzahl der Bilder) |

**Parametereinschränkungen:**

* Dieser Node verwendet Listen-Eingaben: `images` und `texts` werden als Listen verarbeitet, während `vae` und `clip` jeweils ein einzelnes Modell akzeptieren (das erste Element der übergebenen Liste wird verwendet).
* Die Anzahl der Elemente in der `texts`-Liste muss 0, 1 betragen oder genau mit der Anzahl der Elemente in der `images`-Liste übereinstimmen. Wenn sie 0 ist oder weggelassen wird, wird für alle Bilder eine leere Zeichenkette verwendet. Wenn sie 1 ist, wird dieser einzelne Text für alle Bilder wiederholt. Jede andere Länge löst einen Fehler aus.
* Die Ausgabelisten `latents` und `conditioning` enthalten immer dieselbe Anzahl von Elementen wie die `images`-Liste, sodass jedes Latent mit dem Conditioning für die zugehörige Beschriftung gepaart ist.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `latents` | Liste von Latent-Dictionaries. | LATENT |
| `conditioning` | Liste von Conditioning-Listen. | CONDITIONING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MakeTrainingDataset/de.md)

---
**Source fingerprint (SHA-256):** `244adc98810a874cfe42f834e89f96da300d883faeb5791dff19607c13d0c0db`
