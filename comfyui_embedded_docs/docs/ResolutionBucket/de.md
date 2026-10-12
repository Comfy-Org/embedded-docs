# Auflösungs-Bucket

Dieser Node organisiert eine Liste von latenten Bildern und ihre zugehörigen Conditioning-Daten nach ihrer Auflösung. Er gruppiert Elemente mit derselben Höhe und Breite und erstellt separate Batches für jede eindeutige Auflösung. Dieser Prozess ist nützlich, um Daten für effizientes Training vorzubereiten, da er Modellen ermöglicht, mehrere Elemente derselben Größe zusammen zu verarbeiten.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `latents` | Liste von Latent-Dicts, die nach Auflösung gruppiert werden sollen. | LATENT | Ja | N/A |
| `conditioning` | Liste von Conditioning-Listen (muss mit der Länge von `latents` übereinstimmen). | CONDITIONING | Ja | N/A |

**Hinweis:** Beide Eingaben sind Listen-Eingaben, d. h. der Node erhält für jede eine Liste von Elementen. Die Anzahl der Elemente in der `latents`-Liste muss exakt mit der Anzahl der Elemente in der `conditioning`-Liste übereinstimmen; wenn die Anzahl nicht übereinstimmt, wirft der Node einen Fehler. Jedes Latent-Dictionary kann einen Batch von Samples enthalten, und die zugehörige Conditioning-Liste muss eine passende Anzahl von Conditioning-Einträgen für diesen Batch enthalten, da jedes Sample im Batch mit seinem eigenen Conditioning-Eintrag gepaart wird. Latent-Samples können eine Form von (B, C, H, W) für Bilder oder (B, T, C, H, W) für Videos haben; der Node gruppiert sie nur nach Höhe und Breite.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `latents` | Liste gebatchter Latent-Dicts, eine pro Auflösungs-Bucket. | LATENT |
| `conditioning` | Liste von Conditioning-Listen, eine pro Auflösungs-Bucket. | CONDITIONING |

**Hinweis:** Beide Ausgaben sind Listen-Ausgaben. Jede Ausgabeliste enthält einen Eintrag pro eindeutiger Auflösung (Höhe und Breite), die in der Eingabe gefunden wurde, in der Reihenfolge, in der die Auflösungen zuerst aufgetreten sind. Latents innerhalb jedes Buckets werden entlang einer neuen Batch-Dimension gestapelt.

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ResolutionBucket/de.md)

---
**Source fingerprint (SHA-256):** `11687f9916895136c7c5b8146cd7519cbf6c296720e453bac52fe4da237403cd`
