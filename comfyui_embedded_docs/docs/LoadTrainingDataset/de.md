# LoadTrainingDataset

Dieser Node lädt einen codierten Trainingsdatensatz (Latents und Conditioning), der zuvor auf der Festplatte gespeichert wurde. Er liest alle `shard_*.pkl`-Datenshard-Dateien aus einem ausgewählten Datensatzordner im datasets-Verzeichnis und gibt die kombinierten Latent-Vektoren und Conditioning-Daten zur Verwendung in Trainings-Workflows zurück.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `folder_name` | Gespeicherter Datensatz zum Laden aus dem datasets-Verzeichnis. | COMBO | Ja | Eine Option pro Datensatzordner, der im datasets-Verzeichnis gefunden wird |

Hinweis: Die `folder_name`-Optionen werden automatisch durch Scannen des datasets-Verzeichnisses erstellt. Ein Unterordner wird als Datensatz aufgeführt, wenn er eine `metadata.json`-Datei oder mindestens eine `.safetensors`-Datei enthält (der Scan steigt nicht in einen Ordner ab, der die Kriterien erfüllt). Der ausgewählte Datensatzordner wird über alle konfigurierten Dataset-Wurzelverzeichnisse hinweg gesucht, und der Ordnername muss sich in einen Unterordner innerhalb eines dieser Wurzelverzeichnisse auflösen. Der Node liest alle Dateien mit dem Namen `shard_*.pkl` im ausgewählten Ordner in sortierter Reihenfolge und löst einen Fehler aus, wenn keine Shard-Dateien gefunden werden oder der Ordner nicht gefunden werden kann.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `latents` | Liste von Latent-Dicts (Ausgabeliste), wobei jedes Dict einen Schlüssel `"samples"` mit einem Tensor enthält. | LATENT |
| `conditioning` | Liste von Conditioning-Listen (Ausgabeliste), wobei jede innere Liste Conditioning-Daten für das entsprechende Sample enthält. | CONDITIONING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadTrainingDataset/de.md)

---
**Source fingerprint (SHA-256):** `9f914b27f067460f6f3b54f3f2a7bb793c65b99c85e8aa14ab64894be26bd816`
