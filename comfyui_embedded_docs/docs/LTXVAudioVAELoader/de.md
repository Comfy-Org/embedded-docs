# LTXVAudioVAELoader

Der Node LTXV Audio VAE Loader lädt ein vortrainiertes Audio-Variational-Autoencoder-(VAE-)Modell aus einer Checkpoint-Datei. Er liest den angegebenen Checkpoint, behält die Gewichte des Audio-VAE und des Vocoders bei und bereitet das Modell für die Verwendung in Audio-Generierungs- oder -Verarbeitungs-Workflows innerhalb von ComfyUI vor.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `ckpt_name` | Zu ladender Audio-VAE-Checkpoint. Dies ist eine Dropdown-Liste, die mit allen Dateien gefüllt wird, die im Verzeichnis `checkpoints` Ihrer ComfyUI-Installation gefunden werden. | COMBO | Ja | Alle Dateien im Ordner `checkpoints`. Die Liste wird zur Laufzeit generiert. |

Die ausgewählte Datei muss ein gültiger LTXV-Audio-VAE-Checkpoint sein. Der Node behält nur die Gewichte des Audio-VAE und des Vocoders aus der Datei bei und löst einen Fehler aus, wenn das geladene Modell kein gültiges VAE ist.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `Audio VAE` | Das geladene Audio-Variational-Autoencoder-Modell, bereit, mit anderen Audioverarbeitungs-Nodes verbunden zu werden. | VAE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVAudioVAELoader/de.md)

---
**Source fingerprint (SHA-256):** `c91956645a9de0b8f56191f6c0c6bef43f13724ba59078ec9a885168bf2650e8`
