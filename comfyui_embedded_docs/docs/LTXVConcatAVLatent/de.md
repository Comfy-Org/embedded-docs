# LTXVConcatAVLatent

Dieser Node führt ein Video-Latent und ein Audio-Latent zu einem einzigen gemeinsamen Audio-Video-Latent (AV-Latent) zusammen, das für AV-Modelle wie LTXV oder MiniMax H3 bereit ist. Wenn die Videoeingabe bereits ein AV-Latent ist, wird ihr Videostream beibehalten und nur der Audiostream durch das bereitgestellte Audio-Latent ersetzt.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `video_latent` | Die latente Repräsentation der Videodaten. Wenn sie bereits sowohl Video- als auch Audiostreams enthält, behält der Node ihren Videostream bei und ersetzt den Audiostream durch das Audio aus `audio_latent`. | LATENT | Ja |  |
| `audio_latent` | Die latente Repräsentation der Audiodaten. Ihre Länge wird an den Videostream angepasst: Längeres Audio wird gekürzt, kürzeres Audio wird mit Nullen aufgefüllt. | LATENT | Ja |  |

**Hinweis:** Die Samples aus beiden Eingaben werden als Paar aus Video- und Audiostreams in einem verschachtelten Tensor kombiniert. Wenn eine der beiden Eingaben eine `noise_mask` enthält, enthält die Ausgabe eine kombinierte; eine fehlende Maske wird durch eine Maske aus lauter Einsen ersetzt, die der Form der zugehörigen Samples entspricht. Wenn kürzeres Audio aufgefüllt wird, bleibt der aufgefüllte Bereich unmaskiert, damit das Modell ihn generieren kann. Der Node löst einen Fehler aus, wenn das Audio-Latent nicht an das Video-Latent angepasst werden kann, zum Beispiel wenn sich die beiden Latents in mehr als einer Dimension unterscheiden oder wenn sie sich in den Batch- oder Kanal-Dimensionen unterscheiden.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `latent` | Ein Latent, das die Video- und Audio-Samples als zwei Streams zusammengepackt enthält, plus eine kombinierte `noise_mask`, wenn mindestens eine Eingabe eine bereitstellt. | LATENT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVConcatAVLatent/de.md)

---
**Source fingerprint (SHA-256):** `0231f9db2ce73132d8555fbb33f295b68aa68a0c1c54e4a0c5d2e1f67b5611cb`
