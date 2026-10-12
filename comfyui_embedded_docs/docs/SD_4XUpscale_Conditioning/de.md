# SD_4XUpscale_Conditioning

Der Node SD_4XUpscale_Conditioning bereitet Conditioning-Daten für das Hochskalieren von Bildern mit Diffusionsmodellen vor. Er skaliert die Eingabebilder mit einem gewählten Faktor, fügt optional eine Rauschaugmentierung hinzu und gibt modifizierte positive und negative Conditioning-Daten zusammen mit einem leeren Latent für die hochskalierte Größe zurück.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `images` | Eingabebilder, die hochskaliert werden sollen. | IMAGE | Ja | - |
| `positive` | Positive Conditioning-Daten, die die Generierung in Richtung gewünschter Inhalte lenken. | CONDITIONING | Ja | - |
| `negative` | Negative Conditioning-Daten, die die Generierung von unerwünschten Inhalten weglenken. | CONDITIONING | Ja | - |
| `scale_ratio` | Multiplikator, der auf die Abmessungen der Eingabebilder angewendet wird, wenn die hochskalierten Conditioning-Daten und das Latent vorbereitet werden (Standard: 4.0). | FLOAT | Ja | 0.0 - 10.0 (Schrittweite 0.01) |
| `noise_augmentation` | Menge des Rauschens, die während des Hochskalierungsprozesses hinzugefügt wird (Standard: 0.0). | FLOAT | Ja | 0.0 - 1.0 (Schrittweite 0.001) |

Hinweis: `noise_augmentation` ist ein erweiterter Parameter, der in der Node-Oberfläche unter dem Umschalter „Erweitert“ angezeigt wird.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `positive` | Modifizierte positive Conditioning-Daten, bei denen die skalierten Bilddaten und die Einstellungen für die Rauschaugmentierung angewendet wurden. | CONDITIONING |
| `negative` | Modifizierte negative Conditioning-Daten, bei denen die skalierten Bilddaten und die Einstellungen für die Rauschaugmentierung angewendet wurden. | CONDITIONING |
| `latent` | Leere Latent-Darstellung, die den hochskalierten Abmessungen entspricht. | LATENT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SD_4XUpscale_Conditioning/de.md)

---
**Source fingerprint (SHA-256):** `f215e890bd86f42d4da9c6f575fc92e65844e2e2056c5610310d8089e5d61902`
