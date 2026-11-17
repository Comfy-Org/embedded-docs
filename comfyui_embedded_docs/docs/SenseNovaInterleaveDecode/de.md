# SenseNova Interleave Decode

Wandelt den von SenseNova Conditioning hinterlassenen Interleave-Verlauf in nutzbaren Text, Bilder und Denken um. Führe ihn am Ende der Schleife aus, wobei „End Loop accumulate" deaktiviert ist, um alles zu sammeln, was das Modell in einem Durchlauf erzeugt hat.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `clip` | SenseNova CLIP-Modell, das zum Dekodieren der generierten Tokens verwendet wird. | CLIP | Ja | - |
| `conditioning` | Interleave-Conditioning von SenseNova Conditioning. | CONDITIONING | Ja | - |
| `samples` | Letzter KSampler-Pixel-Latent, erforderlich, wenn die Schleife mit einer Bildanforderung endete. | LATENT | Nein | - |

**Einschränkungen und Verhalten:**

* Das Conditioning muss von SenseNova Conditioning in der Aufgabe `interleave` oder `self-correction` stammen; alles andere löst einen Fehler aus.
* Wenn das Modell auf ein Bild wartet, verbinde die LATENT-Ausgabe des Samplers mit `samples`.
* Referenzbilder, die zu Beginn des Laufs verbunden wurden, sind von der Ausgabe ausgeschlossen, und Bildkonsumenten werden übersprungen, wenn kein Bild generiert wurde.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `text` | Aus dem Interleave-Verlauf dekodierter Text, wobei Bildmarker durch Leerzeilen ersetzt sind. | STRING |
| `images` | Die Bilder, die das Modell während des Laufs generiert hat. | IMAGE |
| `thinking` | Der Denktext des Modells, wenn es einen erzeugt hat. | STRING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SenseNovaInterleaveDecode/de.md)

---
**Source fingerprint (SHA-256):** `62c7ded50c1348e2242319209729a17d543d80e4d01ddf173cf8b77e4fd0be50`
