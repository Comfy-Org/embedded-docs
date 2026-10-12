# FlipSigmas

Der `FlipSigmas`-Node dient dazu, die Reihenfolge der in Diffusionsmodellen verwendeten Sigma-Werte umzukehren und sicherzustellen, dass der erste Wert ungleich null ist, falls er ursprünglich null war. Dieser Vorgang ist entscheidend, um die Rauschpegel in umgekehrter Reihenfolge anzupassen und so den Generierungsprozess in Modellen zu ermöglichen, die durch schrittweises Reduzieren des Rauschens aus den Daten arbeiten.

## Eingaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `sigmas` | Der Parameter `sigmas` repräsentiert die Sequenz der umzukehrenden Sigma-Werte. Diese Sequenz ist entscheidend für die Steuerung der während des Diffusionsprozesses angewendeten Rauschpegel, und ihre Umkehrung ist wesentlich für den umgekehrten Generierungsprozess. | `SIGMAS` |

## Ausgaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `sigmas` | Die Ausgabe ist die modifizierte Sequenz der Sigma-Werte, umgekehrt und angepasst, um sicherzustellen, dass der erste Wert ungleich null ist, falls er ursprünglich null war, bereit zur Verwendung in nachfolgenden Diffusionsmodell-Operationen. | `SIGMAS` |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FlipSigmas/de.md)
