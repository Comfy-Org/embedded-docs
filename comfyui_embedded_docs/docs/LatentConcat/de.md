# LatentConcat

Der LatentConcat-Node kombiniert zwei latente Samples, indem er sie entlang einer ausgewählten Dimension aneinanderfügt. Er nimmt zwei latente Eingaben entgegen und verkettet sie entlang der x-, y- oder t-Achse, wobei gesteuert werden kann, welches Sample zuerst kommt. Der Node passt vor der Verkettung automatisch die Batch-Größe der zweiten Eingabe an die der ersten an.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `samples1` | Das erste latente Sample, das verkettet werden soll | LATENT | Ja | - |
| `samples2` | Das zweite latente Sample, das verkettet werden soll | LATENT | Ja | - |
| `dim` | Die Dimension, entlang derer die latenten Samples verkettet werden. Positive Werte (x, y, t) platzieren samples1 vor samples2 im Ergebnis. Negative Werte (-x, -y, -t) platzieren samples2 vor samples1. Die Dimensionszuordnung ist: x = Breite, y = Höhe, t = Zeit/Frames | COMBO | Ja | `"x"`<br>`"-x"`<br>`"y"`<br>`"-y"`<br>`"t"`<br>`"-t"` |

**Hinweis:** Das zweite latente Sample (`samples2`) wird vor der Verkettung automatisch so oft wiederholt, wie nötig, um die Batch-Größe des ersten latenten Samples (`samples1`) zu erreichen.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `output` | Die verketteten latenten Samples, die sich aus der Kombination der beiden Eingabe-Samples entlang der angegebenen Dimension ergeben | LATENT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentConcat/de.md)

---
**Source fingerprint (SHA-256):** `dfe27f76ad12e16623d62c9e7f0b2772df6ecadb543a4eee430bc38ab04a12f2`
