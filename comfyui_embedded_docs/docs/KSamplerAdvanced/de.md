# KSampler (Erweitert)

Der Node KSamplerAdvanced wurde entwickelt, um den Sampling-Prozess durch erweiterte Konfigurationen und Techniken zu verbessern. Er soll anspruchsvollere Optionen für die Generierung von Samples aus einem Modell bieten und die grundlegenden Funktionen des KSampler erweitern.

## Eingaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `model` | Gibt das Modell an, aus dem Samples generiert werden sollen, und spielt eine entscheidende Rolle im Sampling-Prozess. | MODEL |
| `add_noise` | Legt fest, ob dem Sampling-Prozess Rauschen hinzugefügt werden soll, was die Vielfalt und Qualität der generierten Samples beeinflusst. | COMBO[STRING] |
| `noise_seed` | Legt den Seed für die Rauschgenerierung fest, um Reproduzierbarkeit im Sampling-Prozess zu gewährleisten. | INT |
| `steps` | Definiert die Anzahl der im Sampling-Prozess auszuführenden Schritte, was Detailgrad und Qualität der Ausgabe beeinflusst. | INT |
| `cfg` | Steuert den Konditionierungsfaktor und beeinflusst Richtung und Raum des Sampling-Prozesses. | FLOAT |
| `sampler_name` | Wählt den spezifischen Sampler aus, der verwendet werden soll, und ermöglicht eine Anpassung der Sampling-Technik. | COMBO[STRING] |
| `scheduler` | Wählt den Scheduler zur Steuerung des Sampling-Prozesses aus, was den Fortschritt und die Qualität der Samples beeinflusst. | COMBO[STRING] |
| `positive` | Gibt die positive Konditionierung an, um das Sampling in Richtung gewünschter Attribute zu lenken. | CONDITIONING |
| `negative` | Gibt die negative Konditionierung an, um das Sampling von bestimmten Attributen wegzulenken. | CONDITIONING |
| `latent_image` | Stellt das anfängliche latente Bild bereit, das im Sampling-Prozess verwendet werden soll, und dient als Ausgangspunkt. | LATENT |
| `start_at_step` | Bestimmt den Startschritt des Sampling-Prozesses und ermöglicht die Steuerung des Sampling-Fortschritts. | INT |
| `end_at_step` | Legt den Endschritt des Sampling-Prozesses fest und definiert den Umfang des Samplings. | INT |
| `return_with_leftover_noise` | Gibt an, ob das Sample mit verbleibendem Rauschen zurückgegeben werden soll, was das Erscheinungsbild der endgültigen Ausgabe beeinflusst. | COMBO[STRING] |

## Ausgaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `latent` | Die Ausgabe stellt das aus dem Modell generierte latente Bild dar und spiegelt die angewendeten Konfigurationen und Techniken wider. | LATENT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KSamplerAdvanced/de.md)
