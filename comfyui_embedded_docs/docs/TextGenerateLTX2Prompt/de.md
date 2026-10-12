# LTX2-Prompt generieren

Der Node TextGenerateLTX2Prompt erweitert einen kurzen Benutzer-Prompt zu einer detaillierten audiovisuellen Beschreibung, die zur Videogenerierung mit der LTX-2-Serie von Videomodellen geeignet ist. Er fügt automatisch aufgabenspezifische Systemanweisungen hinzu, sendet den formatierten Prompt an ein Sprachmodell und gibt den erweiterten Text zurück. Wenn ein optionales Referenzbild bereitgestellt wird, wechselt der Node in den Bild-zu-Video-Modus und erweitert den Prompt ausgehend vom Inhalt dieses Bildes.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `clip` | Das für die Textkodierung verwendete CLIP-Modell. Der Node prüft den Tokenizer-Namen des Modells, um die passenden Anweisungen auszuwählen: Modelle auf Gemma-4-Basis verwenden das LTX-2.4-Format, während andere Modelle das LTX-2-(Gemma-3)-Format verwenden. | CLIP | Ja | - |
| `prompt` | Die Rohtexteingabe, die die Szene oder das Konzept beschreibt, das zu einem detaillierten Prompt zur Videogenerierung erweitert werden soll. | STRING | Ja | - |
| `image` | Ein optionales Eingabebild, das als erstes Einzelbild des Videos verwendet wird. Wenn es bereitgestellt wird, wechselt der Node in den Bild-zu-Video-Modus und verwendet einen System-Prompt, der den Benutzer-Prompt basierend auf dem Inhalt des Bildes erweitert. | IMAGE | Nein | - |
| `video` | Eine optionale Videoeingabe, die als zusätzlicher Kontext verwendet wird. Wird als Bildstapel an das Sprachmodell übergeben; es wird angenommen, dass sie 24 FPS hat, und intern auf 1 FPS unterabgetastet. | IMAGE | Nein | - |
| `audio` | Eine optionale Audioeingabe, die als zusätzlicher Kontext für die Generierung verwendet werden kann. | AUDIO | Nein | - |
| `max_length` | Die maximale Anzahl von Tokens, die das Sprachmodell generieren darf (Standard: 512). | INT | Ja | 1 bis 32768 |
| `sampling_mode` | Steuert, ob während der Textgenerierung zufälliges Sampling verwendet wird. Wenn auf `"on"` gesetzt, werden die unten stehenden Sampling-Parameter verfügbar; bei `"off"` generiert der Node Text ohne zufälliges Sampling. | DYNAMIC_COMBO | Ja | `"on"`<br>`"off"` |
| `thinking` | Wenn aktiviert, wird das Modell angewiesen, vor der Antwort Schlussfolgerungen anzustellen. Jeder Reasoning-Block wird auf der Ausgabe `thinking` statt in `generated_text` zurückgegeben (Standard: False). | BOOLEAN | Nein | True/False |
| `use_default_template` | Wenn aktiviert, verwendet der Node die Standard-Chat-Vorlage zur Formatierung (Standard: True). Erweiterte Einstellung. | BOOLEAN | Nein | True/False |
| `mtp` | Spekulatives Decoding mit dem Multi-Token-Prediction-Kopf des Checkpoints. Ohne MTP-Gewichte hat es keine Wirkung. `"auto"` passt die Entwurfstiefe an, `"2"` bis `"5"` legen sie fest. Die gesampelte Ausgabe bleibt korrekt verteilt, unterscheidet sich jedoch bei demselben Seed von der Nicht-MTP-Ausgabe (Standard: `"auto"`). | COMBO | Nein | `"auto"`<br>`"off"`<br>`"2"`<br>`"3"`<br>`"4"`<br>`"5"` |
| `system_prompt` | Ersetzt den integrierten LTX-2-System-Prompt. Wenn er leer gelassen wird, verwendet der Node seine eigenen Anweisungen: den Bild-zu-Video-Prompt, wenn ein `image` verbunden ist, andernfalls den Text-zu-Video-Prompt. Verbinden Sie eine STRING-Eingabe, anstatt im Node zu tippen (Standard: leer). | STRING | Nein | - |

### Sampling-Parameter (wenn `sampling_mode` auf "on" gesetzt ist)

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `temperature` | Steuert die Zufälligkeit der Ausgabe. Niedrigere Werte machen die Ausgabe vorhersehbarer, höhere Werte kreativer (Standard: 0.7). | FLOAT | Ja | 0.01 bis 2.0 |
| `top_k` | Begrenzt den Sampling-Pool auf die K wahrscheinlichsten nächsten Tokens. Ein Wert von 0 deaktiviert diesen Filter (Standard: 64). | INT | Ja | 0 bis 1000 |
| `top_p` | Verwendet Nucleus-Sampling: Es behält die kleinste Menge der wahrscheinlichsten Tokens, deren kumulative Wahrscheinlichkeit diesen Wert erreicht (Standard: 0.95). | FLOAT | Ja | 0.0 bis 1.0 |
| `min_p` | Legt einen minimalen Wahrscheinlichkeitsschwellenwert fest, damit Tokens berücksichtigt werden (Standard: 0.05). | FLOAT | Ja | 0.0 bis 1.0 |
| `repetition_penalty` | Bestraft Tokens, die bereits generiert wurden, um Wiederholungen zu verringern. Ein Wert von 1.0 bedeutet keine Bestrafung (Standard: 1.05). | FLOAT | Ja | 0.0 bis 5.0 |
| `seed` | Eine Zahl, die verwendet wird, um den Zufallszahlengenerator für reproduzierbare Ergebnisse zu initialisieren (Standard: 0). | INT | Ja | 0 bis 18446744073709551615 |
| `presence_penalty` | Bestraft neue Tokens danach, ob sie bisher im Text vorgekommen sind, und ermutigt das Modell, über neue Themen zu sprechen (Standard: 0.0). | FLOAT | Nein | 0.0 bis 5.0 |

**Hinweis:** Die oben genannten Sampling-Parameter sind nur dann aktiv und in der Node-Oberfläche sichtbar, wenn `sampling_mode` auf "on" gesetzt ist. Bei "off" sind keine Sampling-Parameter verfügbar, und der Node generiert Text ohne zufälliges Sampling.

**Hinweis:** Das Verhalten des Nodes ändert sich je nach seinen Eingaben:

- Wenn ein `image` bereitgestellt wird, wird der generierte Prompt für eine Bild-zu-Video-Aufgabe formatiert, und zwar mit einem System-Prompt, der beschreibt, wie der Prompt basierend auf dem Inhalt des Bildes erweitert wird. Wenn kein Bild bereitgestellt wird, erfolgt die Formatierung für eine Text-zu-Video-Aufgabe mit einem System-Prompt, der den Prompt zu einer detaillierten Beschreibung zur Videogenerierung erweitert.
- Wenn der Name des CLIP-Tokenizers "gemma4" enthält, verwendet der Node die LTX-2.4-System-Prompts und das Gemma-4-Chat-Format. Andernfalls verwendet er die LTX-2-(Gemma-3)-System-Prompts und das Chat-Format.
- Wenn `thinking` mit einem Gemma-4-Modell aktiviert ist, wird das Modell auf seinem Reasoning-Kanal geöffnet; wenn es deaktiviert ist, wird das Modell direkt auf dem Endantwort-Kanal geöffnet. Bei Nicht-Gemma-4-Modellen wird `thinking` an den zugrunde liegenden Generierungsschritt durchgereicht.
- Ein `system_prompt` ersetzt die integrierten Anweisungen für den ausgewählten Modus (Bild-zu-Video oder Text-zu-Video); wenn er leer ist, wird der integrierte Prompt verwendet.
- Jeder Reasoning-Block wird auf der Ausgabe `thinking` statt in `generated_text` zurückgegeben.
- Wenn das Sprachmodell keinen verwendbaren Text erzeugt, gibt der Node stattdessen den ursprünglichen `prompt` zurück.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `generated_text` | Der vom Sprachmodell erzeugte verbesserte Prompt zur Videogenerierung, wobei jeder Reasoning-Block in die Ausgabe `thinking` ausgelagert wird. Wenn das Ergebnis leer ist, wird der ursprüngliche Benutzer-Prompt zurückgegeben. | STRING |
| `thinking` | Der vom Modell erzeugte Reasoning-Block, wobei das öffnende `<think>`-Tag entfernt wurde. Leer, wenn das Modell keinen Reasoning-Block erzeugt hat; bei Gemma-4-Modellen wird ein Reasoning-Block nur erwartet, wenn `thinking` aktiviert ist. | STRING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextGenerateLTX2Prompt/de.md)

---
**Source fingerprint (SHA-256):** `a601a8bff65e8ee148d09f04ac0afc201dbc9ba5e09a65856400e9be37e085bb`
