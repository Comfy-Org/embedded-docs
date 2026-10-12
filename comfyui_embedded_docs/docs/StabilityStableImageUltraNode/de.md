# StabilityStableImageUltraNode

Erzeugt Bilder synchron auf Basis von Prompt und Auflösung. Dieser Node erstellt Bilder mit dem Stable Image Ultra-Modell von Stability AI, verarbeitet Ihren Text-Prompt und generiert ein entsprechendes Bild mit dem angegebenen Seitenverhältnis und Stil.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Was Sie im Ausgabebild sehen möchten. Ein starker, beschreibender Prompt, der Elemente, Farben und Motive klar definiert, führt zu besseren Ergebnissen. Um die Gewichtung eines bestimmten Wortes zu steuern, verwenden Sie das Format `(word:weight)`, wobei `word` das Wort ist, dessen Gewichtung Sie steuern möchten, und `weight` ein Wert zwischen 0 und 1 ist. Zum Beispiel: `The sky was a crisp (blue:0.3) and (green:0.8)` würde einen Himmel vermitteln, der blau und grün war, aber grüner als blau. | STRING | Ja | - |
| `aspect_ratio` | Seitenverhältnis des generierten Bildes (Standard: "1:1"). | COMBO | Ja | `"1:1"`<br>`"16:9"`<br>`"21:9"`<br>`"2:3"`<br>`"3:2"`<br>`"4:5"`<br>`"5:4"`<br>`"9:16"`<br>`"9:21"` |
| `style_preset` | Optionaler gewünschter Stil des generierten Bildes. Wählen Sie „None“, um keine Stilvoreinstellung anzuwenden. | COMBO | Nein | `"3d-model"`<br>`"analog-film"`<br>`"anime"`<br>`"cinematic"`<br>`"comic-book"`<br>`"digital-art"`<br>`"enhance"`<br>`"fantasy-art"`<br>`"isometric"`<br>`"line-art"`<br>`"low-poly"`<br>`"modeling-compound"`<br>`"neon-punk"`<br>`"origami"`<br>`"photographic"`<br>`"pixel-art"`<br>`"tile-texture"` |
| `seed` | Der zufällige Seed, der zum Erzeugen des Rauschens verwendet wird. | INT | Ja | 0 - 4294967294 |
| `image` | Optionales Eingabebild für die Bild-zu-Bild-Generierung. | IMAGE | Nein | - |
| `negative_prompt` | Ein kurzer Text, der beschreibt, was Sie nicht im Ausgabebild sehen möchten. Dies ist eine erweiterte Funktion. | STRING | Nein | - |
| `image_denoise` | Denoising des Eingabebildes; 0.0 ergibt ein Bild, das mit der Eingabe identisch ist, 1.0 ist, als ob gar kein Bild bereitgestellt wurde (Standard: 0.5). | FLOAT | Nein | 0.0 - 1.0 |

**Hinweis:** Wenn kein Eingabebild bereitgestellt wird, wird der Parameter `image_denoise` automatisch deaktiviert und ignoriert.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `output` | Das generierte Bild basierend auf den Eingabeparametern. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StabilityStableImageUltraNode/de.md)

---
**Source fingerprint (SHA-256):** `86a9ace60a1f9f2b872865381c695bd0e3e3578e0dd3453f1ab3be58bae2e2f0`
