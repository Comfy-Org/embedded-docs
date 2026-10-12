# LatentApplyOperationCFG

Der LatentApplyOperationCFG-Knoten wendet eine latente Operation innerhalb des Classifier-Free-Guidance-(CFG-)Schritts des Sampling-Prozesses eines Modells an. Er fängt die vor der CFG erzeugten Conditioning-Ausgaben ab, wendet die verbundene Operation auf die latenten Werte an und gibt das Modell mit diesem geänderten Sampling-Verhalten zurück.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model` | Das Modell, auf das die CFG-Operation angewendet wird | MODEL | Ja | - |
| `operation` | Die latente Operation, die während des CFG-Sampling-Prozesses angewendet wird | LATENT_OPERATION | Ja | - |
| `start_percent` | Anteil des Denoising-Zeitplans, ab dem die Operation angewendet wird; 0 ist der Beginn des Zeitplans (Standard: 0.0) | FLOAT | Nein | 0.0 bis 1.0 (Schritt 0.001) |
| `end_percent` | Anteil des Denoising-Zeitplans, bei dem die Operation nicht mehr angewendet wird; 1 ist das Ende des Zeitplans (Standard: 1.0) | FLOAT | Nein | 0.0 bis 1.0 (Schritt 0.001) |

Hinweis: Dieser Knoten ist als experimentell gekennzeichnet. Die Operation wird während des CFG-Sampling-Prozesses auf die Conditioning-Ausgaben des Modells angewendet. Wenn zwei Conditioning-Ausgaben vorhanden sind, wird die Operation auf die Differenz zwischen der ersten und der zweiten Ausgabe angewendet und die zweite Ausgabe wieder zum Ergebnis addiert. Wenn nur eine Conditioning-Ausgabe vorhanden ist, wird die Operation direkt darauf angewendet. Die Operation läuft nur zwischen den Punkten `start_percent` und `end_percent` des Denoising-Zeitplans, sodass sie auf einen Teil des Zeitplans beschränkt werden kann; außerhalb dieses Fensters werden die Conditioning-Ausgaben unverändert zurückgegeben.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `model` | Das geänderte Modell mit der auf seinen Sampling-Prozess angewendeten CFG-Operation | MODEL |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentApplyOperationCFG/de.md)

---
**Source fingerprint (SHA-256):** `6a5f59f02eaec38334c63d871e48e89aa983a5ac2ca10801161cdc9e13cacdf2`
