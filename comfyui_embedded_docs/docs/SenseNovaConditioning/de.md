# SenseNova Conditioning

Bereitet SenseNova-Conditioning für die Bildgenerierung oder für verschachtelte Text-und-Bild-Ausgabe vor. Der `task`-Selektor legt die Prompt-Vorlage und das Stoppverhalten fest, und der Node meldet, ob das Modell ein Bild anfordert, sodass eine Schleife weiß, wann der Sampler ausgeführt werden muss.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `clip` | SenseNova-CLIP-Modell. Verbinden Sie den CLIP-Loader, der auch CLIP Text Encode versorgt; die Encoder-Ausgabe geht an `conditioning`. Erforderlich für jede Aufgabe, außer wenn das eingehende Conditioning leer oder bereits abgeschlossen ist. | CLIP | Nein | - |
| `Conditioning` | SenseNova-Text-Conditioning aus CLIP Text Encode. | CONDITIONING | Ja | - |
| `negativ` | Optionales negatives Conditioning. Es wird für die Aufgaben `interleave` und `self-correction` aktualisiert und zurückgegeben. | CONDITIONING | Nein | - |
| `Aufgabe` | Auszuführende Aufgabe. `"image"` kodiert den Prompt für einen Standardsampler, `"image thinking"` lässt das Modell vor der Antwort nachdenken, `"interleave"` erzeugt Text und Bilder in einem Durchgang und `"self-correction"` ermöglicht es dem Modell, seine eigene vorherige Ausgabe zu korrigieren. | DYNAMIC_COMBO | Ja | `"image"`<br>`"image thinking"`<br>`"interleave"`<br>`"self-correction"` |
| `max_tokens` | Maximale Anzahl an Tokens, die während dieses Aufrufs generiert werden. Standard: 1024. | INT | Ja | 1 bis 8192 |

### `interleave` Eingaben

Diese Eingaben erscheinen, wenn `task` auf `"interleave"` gesetzt ist.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `thinking` | Lässt das Modell vor der Antwort nachdenken. Standard: True. | BOOLEAN | Ja | True<br>False |
| `samples` | Vorherige Sampler-Ausgabe, verbunden, wenn nach einer Bildanforderung fortgesetzt wird. | LATENT | Nein | - |

### `self-correction` Eingaben

Diese Eingaben erscheinen, wenn `task` auf `"self-correction"` gesetzt ist.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `samples` | Vorherige Sampler-Ausgabe, verbunden, wenn nach einer Bildanforderung fortgesetzt wird. | LATENT | Nein | - |

**Einschränkungen und Verhalten:**

* Die Eingabe `clip` erwartet das SenseNova-CLIP-Modell selbst, nicht die Ausgabe von CLIP Text Encode (das ist `CONDITIONING`). Ist das eingehende Conditioning leer oder bereits abgeschlossen, gibt der Node das Ergebnis zurück, ohne `clip` zu verwenden; andernfalls ist ein fehlendes `clip` oder eines, das kein SenseNova-CLIP ist, ein Fehler.
* `"image thinking"` benötigt genau einen positiven Conditioning-Eintrag; `"interleave"` und `"self-correction"` benötigen einen positiven und einen negativen Eintrag.
* Wenn das Modell auf ein Bild wartet, verbinden Sie die LATENT-Ausgabe des vorherigen Samplers mit `samples`. Das Übergeben von Samples, bevor ein Bild angefordert wurde, ist ein Fehler.
* Wenn das eingehende Conditioning bereits abgeschlossen ist, gibt der Node es unverändert zurück, mit einem leeren `generated_text` und `image_requested` auf False gesetzt.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `conditioning` | Conditioning für den Sampler, erweitert um den durch diesen Aufruf generierten Text. | CONDITIONING |
| `generated_text` | Durch diesen Aufruf generierter Text. Verwenden Sie SenseNova Interleave Decode für das vollständige Ergebnis. | STRING |
| `negative` | Aktualisiertes negatives Conditioning für die Aufgaben `interleave` und `self-correction`. | CONDITIONING |
| `image_requested` | True, wenn das Modell ein Bild angefordert hat: Sampler ausführen und dann die Schleife zurück in diesen Node führen. | BOOLEAN |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SenseNovaConditioning/de.md)

---
**Source fingerprint (SHA-256):** `97fcdc26ccf80f48c5628f695a4ae8231b065b67414c93dec9bced6bb8d4c77c`
