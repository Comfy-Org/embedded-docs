# LatentComposite

Der LatentComposite-Node dient dazu, zwei Latent-Repräsentationen zu einer einzigen Ausgabe zu mischen oder zusammenzuführen. Dieser Prozess ist essenziell, um zusammengesetzte Bilder oder Merkmale zu erstellen, indem die Eigenschaften der Eingabe-Latents auf kontrollierte Weise kombiniert werden.

## Eingaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `samples_to` | Die `samples_to`-Latent-Repräsentation, auf die `samples_from` zusammengesetzt wird. Sie dient als Basis für den Compositing-Vorgang. | `LATENT` |
| `samples_from` | Die `samples_from`-Latent-Repräsentation, die auf `samples_to` zusammengesetzt werden soll. Sie trägt ihre Merkmale oder Eigenschaften zur endgültigen zusammengesetzten Ausgabe bei. | `LATENT` |
| `x` | Die x-Koordinate (horizontale Position), an der die `samples_from`-Latent-Repräsentation auf `samples_to` platziert wird. Sie bestimmt die horizontale Ausrichtung des Composites. | `INT` |
| `y` | Die y-Koordinate (vertikale Position), an der die `samples_from`-Latent-Repräsentation auf `samples_to` platziert wird. Sie bestimmt die vertikale Ausrichtung des Composites. | `INT` |
| `feather` | Ein boolescher Wert, der angibt, ob die `samples_from`-Latent-Repräsentation vor dem Compositing in der Größe angepasst werden soll, damit sie zu `samples_to` passt. Dies kann den Maßstab und die Proportion des zusammengesetzten Ergebnisses beeinflussen. | `INT` |

## Ausgaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `latent` | Die Ausgabe ist eine zusammengesetzte Latent-Repräsentation, die die Merkmale sowohl der `samples_to`- als auch der `samples_from`-Latents basierend auf den angegebenen Koordinaten und der Größenanpassungsoption kombiniert. | `LATENT` |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentComposite/de.md)
