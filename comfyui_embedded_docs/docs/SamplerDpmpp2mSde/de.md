# SamplerDpmpp2mSde

Dieser Node ist darauf ausgelegt, einen Sampler für das DPMPP_2M_SDE-Modell zu erzeugen, wodurch Samples basierend auf angegebenen Solver-Typen, Rauschpegeln und Präferenzen für Rechengeräte generiert werden können. Er abstrahiert die Komplexität der Sampler-Konfiguration und bietet eine optimierte Schnittstelle zum Generieren von Samples mit benutzerdefinierten Einstellungen.

## Eingaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `solver_type` | Gibt den im Sampling-Prozess zu verwendenden Solver-Typ an und bietet Optionen zwischen 'midpoint' und 'heun'. Diese Auswahl beeinflusst die während des Samplings angewendete numerische Integrationsmethode. | COMBO[STRING] |
| `eta` | Bestimmt die Schrittweite in der numerischen Integration und beeinflusst die Granularität des Sampling-Prozesses. Ein höherer Wert bedeutet eine größere Schrittweite. | `FLOAT` |
| `s_noise` | Steuert den Grad des während des Sampling-Prozesses eingeführten Rauschens und beeinflusst die Variabilität der generierten Samples. | `FLOAT` |
| `noise_device` | Gibt das Rechengerät ('gpu' oder 'cpu') an, auf dem der Rauschgenerierungsprozess ausgeführt wird, was Leistung und Effizienz beeinflusst. | COMBO[STRING] |

## Ausgaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `sampler` | Die Ausgabe ist ein entsprechend den angegebenen Parametern konfigurierter Sampler, der zum Generieren von Samples bereit ist. | `SAMPLER` |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerDpmpp2mSde/de.md)
