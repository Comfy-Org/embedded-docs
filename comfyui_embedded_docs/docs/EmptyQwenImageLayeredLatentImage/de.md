# Leeres Qwen Image Layered Latent

Empty Qwen Image Layered Latent bereitet die leere Leinwand vor, auf die das Qwen-Image-Layered-Modell malt. Stellen Sie es sich wie einen Stapel sauberer Transparentpapierbögen vor, die in Reihenfolge zusammengeklammert sind: Das Modell füllt den ersten Bogen mit dem vollständigen Bild und jeden weiteren Bogen mit einem Teil dieses Bildes. Dieser Node entscheidet, wie groß die Bögen sind und wie viele es gibt. Er zeichnet selbst nichts.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `width` | Die Breite des zu erstellenden Latent-Bildes. Der Wert muss durch 16 teilbar sein. (Standard: 640) | INT | Ja | 16 bis MAX_RESOLUTION (Schrittweite 16) |
| `height` | Die Höhe des zu erstellenden Latent-Bildes. Der Wert muss durch 16 teilbar sein. (Standard: 640) | INT | Ja | 16 bis MAX_RESOLUTION (Schrittweite 16) |
| `layers` | Wie viele Ebenen das Bild aufgeteilt werden soll. Ein zusätzlicher Bogen ist immer für das vollständige Bild reserviert, daher erhalten Sie `layers + 1` Bilder zurück, nicht `layers`. Setzen Sie ihn auf 2, erhalten Sie das vollständige Bild plus 2 Ebenen. Setzen Sie ihn auf 0, erhalten Sie nur das vollständige Bild. (Standard: 3) | INT | Ja | 0 bis MAX_RESOLUTION (Schrittweite 1) |
| `batch_size` | Die Anzahl der in einem Batch zu erzeugenden Latent-Samples. (Standard: 1) | INT | Ja | 1 bis 4096 |

**Hinweis:** Die Parameter `width` und `height` werden intern durch 8 geteilt, um die räumlichen Dimensionen des Ausgabe-Latent-Tensors zu bestimmen.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `samples` | Ein mit Nullen gefüllter Latent-Tensor. Seine Form ist `[batch_size, 16, layers + 1, height // 8, width // 8]`. | LATENT |

## Warum Sie ein Bild mehr erhalten, als Sie angefordert haben

Qwen-Image-Layered zerlegt nicht nur ein Bild. Es zeichnet auch das vollständige Bild auf einem eigenen Bogen zusammen mit den Ebenen neu. Deshalb ist der Stapel immer einen Bogen höher als die Anzahl der Ebenen, die Sie angefordert haben.

- **Das erste Bild ist das vollständige Bild, keine Ebene.** Es ist dasselbe Bild, das Sie bereits haben; werfen Sie es also weg, wenn Sie nur die Ebenen möchten.
- **Legen Sie alle Ebenen wieder übereinander, erhalten Sie erneut das vollständige Bild.** Wenn sie sich nicht wieder zu diesem ersten Bild zusammensetzen, hat die Trennung nicht wie gewünscht funktioniert; dies ist also eine schnelle Möglichkeit, das Ergebnis zu prüfen.
- **Halten Sie die Bögen in der richtigen Reihenfolge.** Der Stapel ist die einzige Aufzeichnung darüber, welche Ebene über welcher liegt. Auf den Bögen selbst steht nichts, was angibt, wohin sie gehören; daher bedeutet eine Neuanordnung oder ein Weglassen von Bildern eine Neuanordnung oder einen Verlust von Ebenen.
- **Die Ebenen werden mit Transparenz ausgegeben**, sodass sie gestapelt werden können, ohne dass die darunterliegenden von einem undurchsichtigen Hintergrund verdeckt werden.

## Nutzungshinweise

Senden Sie die Ausgabe so wie einen normalen leeren Latent an den Sampler und platzieren Sie dann LatentCutToBatch mit `dim` auf `t` gesetzt vor VAE Decode. Das ist der Schritt, der den Stapel in separate Bilder zerlegt, in der Reihenfolge, beginnend mit dem vollständigen Bild.

Beginnen Sie mit dem Standardwert von 3 Ebenen. Mehr Ebenen anzufordern bedeutet eine längere Generierung und eine feinere Trennung, und es lohnt sich nicht, den Wert zu erhöhen, bevor Sie gesehen haben, was das Modell mit einer kleinen Anzahl macht.

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyQwenImageLayeredLatentImage/de.md)

---
**Source fingerprint (SHA-256):** `5ccac979fcbcefb65f28867a89401c095cb330e09c13270008c32feeeafb1287`
