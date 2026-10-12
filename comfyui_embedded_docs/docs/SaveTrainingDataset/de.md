# SaveTrainingDataset

Dieser Node speichert einen kodierten Trainingsdatensatz zur effizienten Ladung während des Trainings auf der Festplatte. Er nimmt Bild-Latents und die dazu passende Textkonditionierung entgegen, teilt sie in kleinere Dateien namens Shards auf und speichert sie in einem Ordner innerhalb des datasets-Verzeichnisses. Außerdem schreibt er eine Metadatendatei, die den Datensatz beschreibt.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `latents` | Liste von Latent-Dictionaries aus MakeTrainingDataset. | LATENT | Ja | N/A |
| `conditioning` | Liste von Conditioning-Listen aus MakeTrainingDataset. | CONDITIONING | Ja | N/A |
| `folder_name` | Name des Ordners, in dem der Datensatz innerhalb des datasets-Verzeichnisses gespeichert wird. Unterordner wie 'project/run1' sind erlaubt. (Standard: "training_dataset") | STRING | Ja | N/A |
| `shard_size` | Anzahl der Samples pro Shard-Datei. (Standard: 1000) | INT | Ja | 1 bis 100000 |

**Hinweis:** Die Anzahl der Einträge in `latents` muss exakt mit der Anzahl der Einträge in `conditioning` übereinstimmen; der Node löst einen Fehler aus, wenn diese Anzahlen nicht übereinstimmen. Der `folder_name` muss einen Unterordner des datasets-Verzeichnisses benennen (zum Beispiel `my_dataset`) – er darf nicht das datasets-Verzeichnis selbst sein, und Ordnernamen, die außerhalb des datasets-Verzeichnisses aufgelöst würden, werden abgelehnt. Der Parameter `shard_size` ist eine erweiterte Einstellung.

## Ausgaben

Dieser Node erzeugt keine Ausgabedaten. Seine Funktion besteht darin, Dateien auf Ihrer Festplatte zu speichern. Jeder Shard wird als Datei `shard_XXXX.pkl` im ausgewählten Ordner gespeichert, und eine Datei `metadata.json` zeichnet die Gesamtzahl der Samples, die Anzahl der Shards und die Shard-Größe auf.

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveTrainingDataset/de.md)

---
**Source fingerprint (SHA-256):** `6d7b63a24ac42907b0f4a1358712cd0ed085982ecd308bce87e5376d9bbc2274`
