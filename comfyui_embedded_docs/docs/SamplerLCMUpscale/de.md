# SamplerLCMUpscale

Dieser Node bietet eine spezialisierte Sampling-Methode, die Latent Consistency Model (LCM)-Sampling mit progressiver Bild-Hochskalierung kombiniert. Während des Samplings wird das Bild mithilfe einer gewählten Interpolationsmethode schrittweise auf ein Ziel-Skalierungsverhältnis hochskaliert, wodurch in einem einzigen Sampling-Durchlauf Ergebnisse mit höherer Auflösung möglich sind. Der Node gibt ein konfiguriertes Sampler-Objekt aus, das mit einem Sampling-Node verbunden werden kann.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `scale_ratio` | Der gesamte Skalierungsfaktor, der während der Hochskalierung angewendet wird. Ein Wert von 1.0 behält die ursprüngliche Auflösung bei (Standard: 1.0) | FLOAT | Ja | 0.1 - 20.0 |
| `scale_steps` | Die Anzahl der Schritte, die für den Hochskalierungsprozess verwendet werden. Verwenden Sie -1 für die automatische Berechnung basierend auf dem Sampling-Zeitplan (Standard: -1) | INT | Ja | -1 - 1000 |
| `upscale_method` | Die Interpolationsmethode, die bei jedem Hochskalierungsschritt zum Hochskalieren des Bildes verwendet wird (Standard: "bislerp") | COMBO | Ja | "bislerp"<br>"nearest-exact"<br>"bilinear"<br>"area"<br>"bicubic" |

`scale_ratio` und `scale_steps` sind erweiterte Parameter. Das Bild wird über die Hochskalierungsschritte hinweg schrittweise von seiner ursprünglichen Größe auf den Zielwert `scale_ratio` hochskaliert. Wenn `scale_steps` -1 ist, wird die Anzahl der Hochskalierungsschritte automatisch als etwa die Hälfte der Anzahl der Sampling-Schritte berechnet, mit einem Minimum von 2; bei einem positiven Wert passt der Node ihn intern an und begrenzt ihn basierend auf der Gesamtzahl der Sampling-Schritte.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `sampler` | Ein konfiguriertes Sampler-Objekt, das LCM-Sampling mit progressiver Hochskalierung durchführt und für die Verwendung in der Sampling-Pipeline bereit ist | SAMPLER |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerLCMUpscale/de.md)

---
**Source fingerprint (SHA-256):** `5d6f6472fbb4d2c66a8a8b9d6dc34dcc52ac8272589fd6c29e4084d6cab3141b`
