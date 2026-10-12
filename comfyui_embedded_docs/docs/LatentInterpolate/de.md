# LatentInterpolate

Der Node LatentInterpolate dient dazu, eine Interpolation zwischen zwei Sätzen von Latent-Samples auf Basis eines angegebenen Verhältnisses durchzuführen und die Eigenschaften beider Sätze zu mischen, um einen neuen, intermediären Satz von Latent-Samples zu erzeugen.

## Eingaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `samples1` | Der erste Satz von Latent-Samples, der interpoliert werden soll. Er dient als Ausgangspunkt für den Interpolationsprozess. | `LATENT` |
| `samples2` | Der zweite Satz von Latent-Samples, der interpoliert werden soll. Er dient als Endpunkt für den Interpolationsprozess. | `LATENT` |
| `ratio` | Ein Gleitkommawert, der die Gewichtung jedes Sample-Satzes in der interpolierten Ausgabe bestimmt. Ein Verhältnis von 0 erzeugt eine Kopie des ersten Satzes, während ein Verhältnis von 1 eine Kopie des zweiten Satzes erzeugt. | `FLOAT` |

## Ausgaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `latent` | Die Ausgabe ist ein neuer Satz von Latent-Samples, der einen interpolierten Zustand zwischen den beiden Eingabesätzen auf Basis des angegebenen Verhältnisses darstellt. | `LATENT` |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentInterpolate/de.md)
