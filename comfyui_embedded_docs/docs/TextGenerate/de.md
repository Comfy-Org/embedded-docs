# TextGenerate

Der TextGenerate-Node verwendet ein CLIP-Modell, um Text basierend auf dem Prompt eines Benutzers zu erzeugen. Optional können Bilder, Video oder Audio als zusätzlicher Kontext verwendet werden, um die Textgenerierung zu steuern. Sie können die Länge der Ausgabe steuern, einen Thinking-Modus für unterstützte Modelle aktivieren und wählen, ob zufälliges Sampling mit verschiedenen Einstellungen verwendet oder Text ohne Sampling generiert wird.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `sampling_mode` | Steuert, ob während der Textgenerierung zufälliges Sampling verwendet wird. Bei Einstellung auf "on" werden zusätzliche Sampling-Parameter verfügbar. Bei Einstellung auf "off" generiert der Node Text ohne zufälliges Sampling. | DYNAMIC_COMBO | Ja | `"on"`<br>`"off"` |
| `clip` | Das CLIP-Modell, das zum Tokenisieren des Prompts und zur Textgenerierung verwendet wird. | CLIP | Ja | N/A |
| `prompt` | Der Text-Prompt, der die Generierung steuert. Dieses Feld unterstützt mehrere Zeilen und dynamische Prompts. Der Standardwert ist eine leere Zeichenkette. | STRING | Ja | N/A |
| `image` | Ein optionales Bild, das zusammen mit dem Text-Prompt verwendet werden kann, um den generierten Text zu beeinflussen. | IMAGE | Nein | N/A |
| `video` | Videoframes als Bild-Batch. Es wird von 24 FPS ausgegangen; intern auf 1 FPS unterabgetastet. | IMAGE | Nein | N/A |
| `audio` | Eine optionale Audioeingabe, die zusammen mit dem Text-Prompt verwendet werden kann, um den generierten Text zu beeinflussen. | AUDIO | Nein | N/A |
| `max_length` | Die maximale Anzahl an Tokens, die das Modell generiert. Der Standardwert ist 512. | INT | Ja | 1 bis 32768 |
| `thinking` | Im Thinking-Modus arbeiten, wenn das Modell dies unterstützt. Der Standardwert ist False. | BOOLEAN | Nein | True oder False |
| `use_default_template` | Verwendet den integrierten System-Prompt/das integrierte Template, falls das Modell eines besitzt. Der Standardwert ist True. Dies ist ein erweiterter Parameter. | BOOLEAN | Nein | True oder False |
| `mtp` | Spekulatives Decoding mit dem Multi-Token-Prediction-Kopf des Checkpoints. Hat ohne MTP-Gewichte keine Wirkung. `"auto"` passt die Draft-Tiefe an, `"2"` bis `"5"` legen sie fest. Gesampelte Ausgabe bleibt korrekt verteilt, unterscheidet sich jedoch bei gleichem Seed von der Nicht-MTP-Ausgabe (Standard: `"auto"`). | COMBO | Nein | `"auto"`<br>`"off"`<br>`"2"`<br>`"3"`<br>`"4"`<br>`"5"` |
| `system_prompt` | Ersetzt den System-Prompt im Chat-Template des Modells. Wird ignoriert, wenn das Standard-Template nicht verwendet wird. Eine STRING-Eingabe verbinden, anstatt im Node zu tippen (Standard: leer). | STRING | Nein | N/A |

### Sampling-Parameter (wenn `sampling_mode` auf "on" gesetzt ist)

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `temperature` | Steuert die Zufälligkeit der Ausgabe. Niedrigere Werte machen die Ausgabe vorhersehbarer, höhere Werte kreativer. Der Standardwert ist 0.7. | FLOAT | Ja | 0.01 bis 2.0 |
| `top_k` | Begrenzt den Sampling-Pool auf die K wahrscheinlichsten nächsten Tokens. Ein Wert von 0 deaktiviert diesen Filter. Der Standardwert ist 64. | INT | Ja | 0 bis 1000 |
| `top_p` | Verwendet Nucleus-Sampling: Es behält die kleinste Menge der wahrscheinlichsten Tokens, deren kumulative Wahrscheinlichkeit diesen Wert erreicht. Der Standardwert ist 0.95. | FLOAT | Ja | 0.0 bis 1.0 |
| `min_p` | Legt einen minimalen Wahrscheinlichkeitsschwellenwert fest, damit Tokens berücksichtigt werden. Der Standardwert ist 0.05. | FLOAT | Ja | 0.0 bis 1.0 |
| `repetition_penalty` | Bestraft Tokens, die bereits generiert wurden, um Wiederholungen zu reduzieren. Ein Wert von 1.0 bedeutet keine Bestrafung. Der Standardwert ist 1.05. | FLOAT | Ja | 0.0 bis 5.0 |
| `seed` | Eine Zahl, mit der der Zufallszahlengenerator initialisiert wird, um reproduzierbare Ergebnisse zu erhalten. Der Standardwert ist 0. | INT | Ja | 0 bis 18446744073709551615 |
| `presence_penalty` | Bestraft neue Tokens basierend darauf, ob sie bisher im Text vorgekommen sind, und ermutigt das Modell, über neue Themen zu sprechen. Der Standardwert ist 0.0. | FLOAT | Nein | 0.0 bis 5.0 |

**Hinweis:** Die obigen Sampling-Parameter sind nur aktiv und in der Node-Oberfläche sichtbar, wenn `sampling_mode` auf "on" gesetzt ist. Wenn `sampling_mode` auf "off" gesetzt ist, sind keine Sampling-Parameter verfügbar und der Node generiert Text ohne zufälliges Sampling.

**Hinweis:** Wenn der generierte Text einen Reasoning-Block enthält (er beginnt mit `<think>` oder der Prompt endet damit), wird der Reasoning getrennt zurückgegeben: `generated_text` enthält die Antwort und `thinking` enthält den Reasoning-Block, wobei das öffnende Tag entfernt wurde. Andernfalls enthält `generated_text` alles, was das Modell erzeugt hat, und `thinking` ist leer.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `generated_text` | Der vom Modell generierte Text basierend auf dem Eingabe-Prompt und optionalem Bild, Video oder Audio, wobei jeder Reasoning-Block in die `thinking`-Ausgabe ausgelagert wird. | STRING |
| `thinking` | Der vom Modell erzeugte Reasoning-Block, wobei das öffnende `<think>`-Tag entfernt wurde. Leer, wenn das Modell keinen Reasoning-Block erzeugt hat. | STRING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextGenerate/de.md)

---
**Source fingerprint (SHA-256):** `80813781c06dfb0c3b59ee72c8bd6ebced69a4de8152de916ebc15153a0757fa`
