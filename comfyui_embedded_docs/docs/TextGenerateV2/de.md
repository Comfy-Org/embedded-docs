# Generate Text

Der Node Generate Text verwendet ein CLIP-Modell, um aus einem Prompt Text zu erzeugen. Anders als der ältere Node mit einem einzelnen Anhang akzeptiert er erweiterbare Stapel von Bildern, Videos und Audiodateien als zusätzlichen Kontext, sodass Sie ein komplettes Referenzset in einem einzigen Node übergeben können. Sie steuern die Ausgabelänge, ob Sampling verwendet wird und ob die eigene Chat-Vorlage und der Thinking-Modus des Modells angewendet werden.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `clip` | Das CLIP-Modell, das verwendet wird, um den Prompt zu tokenisieren und den Text zu erzeugen. | CLIP | Ja | - |
| `prompt` | Der Prompt, der die Generierung steuert. Unterstützt mehrere Zeilen und dynamische Prompts (Standard: leerer String). | STRING | Ja | - |
| `images` | Erweiterbare Gruppe von bis zu 50 Bildern, `image1` bis `image50`, die als visueller Kontext für das Modell dient. | AUTOGROW | Nein | 0 bis 50 Bilder |
| `videos` | Erweiterbare Gruppe von bis zu 100 Videoeingaben, `video1` bis `video100`. Jedes Video ist ein Stapel von Frames, für die 24 FPS angenommen und die intern auf 1 FPS unterabgetastet werden. | AUTOGROW | Nein | 0 bis 100 Videos |
| `audios` | Erweiterbare Gruppe von bis zu 100 Audioeingaben, `audio1` bis `audio100`, die als Audiokontext für das Modell dient. | AUTOGROW | Nein | 0 bis 100 Audiodateien |
| `max_length` | Maximale Anzahl der zu erzeugenden Tokens (Standard: 512). | INT | Ja | 1 bis 32768 |
| `sampling_mode` | `on` sampelt die Ausgabe und zeigt die unten aufgeführten Sampling-Parameter an. `off` erzeugt gierig ohne Zufalls-Sampling. | DYNAMIC_COMBO | Ja | `"on"`<br>`"off"` |
| `thinking` | Arbeitet im Thinking-Modus, wenn das Modell dies unterstützt (Standard: False). | BOOLEAN | Nein | True oder False |
| `use_default_template` | Verwendet den eingebauten System-Prompt oder die Chat-Vorlage, falls das Modell eine besitzt (Standard: True). Erweiterter Parameter. | BOOLEAN | Nein | True oder False |
| `mtp` | Spekulative Dekodierung mit dem Multi-Token-Prediction-Kopf des Checkpoints. Ohne MTP-Gewichte hat dies keine Wirkung. `"auto"` passt die Draft-Tiefe und -Breite an die beobachteten Token-Übereinstimmungen und Ausführungskosten an, `"2"` bis `"5"` legen eine konstante Draft-Tiefe fest, und die `tree`-Modi fixieren sowohl Breite als auch Tiefe. Die gesampelte Ausgabe bleibt korrekt verteilt, unterscheidet sich jedoch für denselben Seed von der Nicht-MTP-Ausgabe (Standard: `"auto"`). | COMBO | Nein | `"auto"`<br>`"off"`<br>`"2"`<br>`"3"`<br>`"4"`<br>`"5"`<br>`"tree2s1"`<br>`"tree2s2"`<br>`"tree3s1"`<br>`"tree4s1m8"` |
| `system_prompt` | Ersetzt den System-Prompt in der Chat-Vorlage des Modells. Wird ignoriert, wenn die Standardvorlage nicht verwendet wird. Verbinden Sie eine STRING-Eingabe, anstatt sie im Node einzugeben (Standard: leer). | STRING | Nein | - |

### Sampling-Parameter (wenn `sampling_mode` `"on"` ist)

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `temperature` | Steuert die Zufälligkeit der Ausgabe. Niedrigere Werte machen die Ausgabe vorhersagbarer, höhere Werte kreativer (Standard: 0.7). | FLOAT | Ja | 0.01 bis 2.0 |
| `top_k` | Begrenzt den Sampling-Pool auf die K wahrscheinlichsten nächsten Tokens. Ein Wert von 0 deaktiviert den Filter (Standard: 64). | INT | Ja | 0 bis 1000 |
| `top_p` | Nucleus-Sampling: behält die kleinste Menge der wahrscheinlichsten Tokens, deren kumulative Wahrscheinlichkeit diesen Wert erreicht (Standard: 0.95). | FLOAT | Ja | 0.0 bis 1.0 |
| `min_p` | Mindestwahrscheinlichkeit, die ein Token erreichen muss, um im Pool zu bleiben (Standard: 0.05). | FLOAT | Ja | 0.0 bis 1.0 |
| `repetition_penalty` | Bestraft bereits erzeugte Tokens, um Wiederholungen zu reduzieren. Ein Wert von 1.0 bewirkt keine Strafe (Standard: 1.05). | FLOAT | Ja | 0.0 bis 5.0 |
| `presence_penalty` | Bestraft neue Tokens danach, ob sie bisher im Text vorkamen, und ermutigt das Modell, zu neuen Themen zu wechseln (Standard: 0.0). | FLOAT | Ja | 0.0 bis 5.0 |
| `seed` | Zahl zur Initialisierung des Zufallszahlengenerators für reproduzierbare Ergebnisse (Standard: 0). | INT | Ja | 0 bis 18446744073709551615 |

**Hinweis:** Die oben genannten Sampling-Parameter existieren nur, wenn `sampling_mode` `"on"` ist. Bei `"off"` erzeugt der Node Text ohne Zufalls-Sampling, und die Parameter sind ausgeblendet.

**Hinweis:** Wenn die Ausgabe des Modells einen Reasoning-Block mit `<think>` öffnet, teilt der Node ihn auf: `generated_text` enthält die Antwort und `thinking` enthält das Reasoning, wobei das öffnende Tag entfernt wurde. Andernfalls enthält `generated_text` alles, was das Modell erzeugt hat, und `thinking` ist leer. Reasoning, das durch `max_length` abgeschnitten wurde, bleibt in `generated_text`.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `generated_text` | Der vom Modell erzeugte Text, wobei ein etwaiger Reasoning-Block in die Ausgabe `thinking` ausgelagert wird. | STRING |
| `thinking` | Der vom Modell erzeugte Reasoning-Block mit entferntem öffnendem Tag `<think>`. Leer, wenn das Modell keinen Reasoning-Block erzeugt hat. | STRING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextGenerateV2/de.md)

---
**Source fingerprint (SHA-256):** `b61210726faa495a342a5eaaebe64f800ec1d2af4e2fc1321d8c3d7c594bd9ca`
