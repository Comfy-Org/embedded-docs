# LatentBatchSeedBehavior

Der Node LatentBatchSeedBehavior dient dazu, das Seed-Verhalten eines Stapels latenter Samples zu ändern. Er ermöglicht es, den Seed über den Stapel hinweg entweder zu randomisieren oder festzulegen, wodurch der Generierungsprozess beeinflusst wird, indem entweder Variabilität eingeführt oder Konsistenz in den generierten Ausgaben beibehalten wird.

## Eingaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `samples` | Der Parameter `samples` stellt den zu verarbeitenden Stapel latenter Samples dar. Seine Modifikation hängt vom gewählten Seed-Verhalten ab und beeinflusst die Konsistenz oder Variabilität der generierten Ausgaben. | `LATENT` |
| `seed_behavior` | Der Parameter `seed_behavior` legt fest, ob der Seed für den Stapel latenter Samples randomisiert oder festgelegt werden soll. Diese Wahl hat erheblichen Einfluss auf den Generierungsprozess, indem sie entweder Variabilität einführt oder Konsistenz innerhalb des Stapels sicherstellt. | COMBO[STRING] |

## Ausgaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `latent` | Die Ausgabe ist eine modifizierte Version der eingegebenen latenten Samples, wobei Anpassungen auf Grundlage des angegebenen Seed-Verhaltens vorgenommen werden. Sie behält entweder den Batch-Index bei oder ändert ihn, um das gewählte Seed-Verhalten widerzuspiegeln. | `LATENT` |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentBatchSeedBehavior/de.md)
