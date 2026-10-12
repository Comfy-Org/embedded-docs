# Latent-Rauschmaske festlegen

Dieser Node ist darauf ausgelegt, eine Rauschmaske auf eine Gruppe latenter Samples anzuwenden. Er modifiziert die Eingabe-Samples durch Einbindung einer angegebenen Maske und verändert dadurch deren Rauscheigenschaften.

## Eingaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `samples` | Die latenten Samples, auf die die Rauschmaske angewendet wird. Dieser Parameter ist entscheidend für die Bestimmung des Basis Inhalts, der modifiziert wird. | `LATENT` |
| `mask` | Die auf die latenten Samples anzuwendende Maske. Sie definiert die Bereiche und die Intensität der Rauschveränderung innerhalb der Samples. | `MASK` |

## Ausgaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `latent` | Die modifizierten latenten Samples mit der angewendeten Rauschmaske. | `LATENT` |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SetLatentNoiseMask/de.md)
