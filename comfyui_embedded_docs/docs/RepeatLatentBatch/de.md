# RepeatLatentBatch

Der Node RepeatLatentBatch ist darauf ausgelegt, einen bestimmten Batch latenter Repräsentationen eine festgelegte Anzahl von Malen zu replizieren, möglicherweise einschließlich zusätzlicher Daten wie Rauschmasken und Batch-Indizes. Diese Funktionalität ist entscheidend für Vorgänge, die mehrere Instanzen derselben latenten Daten erfordern, wie Daten-Augmentierung oder bestimmte generative Aufgaben.

## Eingaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `samples` | Der Parameter `samples` stellt die latenten Repräsentationen dar, die repliziert werden sollen. Er ist wesentlich, um die Daten zu definieren, die wiederholt werden. | `LATENT` |
| `amount` | Der Parameter `amount` gibt an, wie oft die Eingabe-Samples wiederholt werden sollen. Er beeinflusst direkt die Größe des Ausgabe-Batches und damit den Rechenaufwand sowie die Vielfalt der erzeugten Daten. | `INT` |

## Ausgaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `latent` | Die Ausgabe ist eine modifizierte Version der latenten Eingaberepräsentationen, die entsprechend dem angegebenen `amount` repliziert wurde. Falls zutreffend, kann sie replizierte Rauschmasken und angepasste Batch-Indizes enthalten. | `LATENT` |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RepeatLatentBatch/de.md)
