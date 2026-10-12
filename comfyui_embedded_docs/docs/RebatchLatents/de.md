# RebatchLatents

Der Node RebatchLatents ist darauf ausgelegt, einen Batch latenter Repräsentationen auf Grundlage einer angegebenen Batch-Größe in eine neue Batch-Konfiguration umzuorganisieren. Er stellt sicher, dass die latenten Samples entsprechend gruppiert werden, wobei Variationen in Dimensionen und Größen berücksichtigt werden, um die weitere Verarbeitung oder Modellinferenz zu erleichtern.

## Eingaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `latents` | Der Parameter `latents` stellt die latenten Eingaberepräsentationen dar, die neu gebatcht werden sollen. Er ist entscheidend für die Bestimmung der Struktur und des Inhalts des Ausgabe-Batches. | `LATENT` |
| `batch_size` | Der Parameter `batch_size` gibt die gewünschte Anzahl von Samples pro Batch in der Ausgabe an. Er beeinflusst direkt die Gruppierung und Aufteilung der Eingabe-Latents in neue Batches. | `INT` |

## Ausgaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `latent` | Die Ausgabe ist ein neu organisierter Batch latenter Repräsentationen, der entsprechend der angegebenen Batch-Größe angepasst wurde. Sie erleichtert die weitere Verarbeitung oder Analyse. | `LATENT` |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RebatchLatents/de.md)
