# Hunyuan-Latent-Verfeinerer

Der Node HunyuanRefinerLatent bereitet Conditioning- und Latent-Daten für den Hunyuan-Video-Verfeinerungsprozess vor. Er hängt die eingegebenen latenten Bilddaten sowohl an das positive als auch an das negative Conditioning an, wendet einen Rausch-Augmentierungswert auf beide an und erstellt ein neues, mit Nullen gefülltes Latent mit 32 Kanälen für die weitere Verarbeitung.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `positive` | Der positive Conditioning-Eingang, der verarbeitet werden soll | CONDITIONING | Ja | - |
| `negative` | Der negative Conditioning-Eingang, der verarbeitet werden soll | CONDITIONING | Ja | - |
| `latent` | Die latente Repräsentationseingabe, die als latente Bilddaten für das Conditioning verwendet wird und die Dimensionen des Ausgabe-Latents definiert | LATENT | Ja | - |
| `noise_augmentation` | Die Menge der anzuwendenden Rausch-Augmentierung (Standard: 0.10). Dieser Parameter wird im erweiterten Abschnitt des Nodes angezeigt. | FLOAT | Ja | 0.0 - 1.0 |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `positive` | Das verarbeitete positive Conditioning mit angehängten latenten Bilddaten und angewendeter Rausch-Augmentierung | CONDITIONING |
| `negative` | Das verarbeitete negative Conditioning mit angehängten latenten Bilddaten und angewendeter Rausch-Augmentierung | CONDITIONING |
| `latent` | Ein neues, mit Nullen gefülltes Latent mit derselben Batch-Größe und denselben letzten drei Dimensionen wie das Eingabe-Latent sowie 32 Kanälen | LATENT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanRefinerLatent/de.md)

---
**Source fingerprint (SHA-256):** `4c5669cf2ad5ba00e176876741b7d8d3f092cc58d2163871a10fd769ee4ff84c`
