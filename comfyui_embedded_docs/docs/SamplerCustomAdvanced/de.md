# SamplerCustomAdvanced

Der Node `SamplerCustomAdvanced` führt erweitertes Sampling im latenten Raum unter Verwendung benutzerdefinierter Rausch-, Guidance- und Sampling-Konfigurationen durch. Er verarbeitet ein latentes Bild in einem geführten Sampling-Prozess mit einem anpassbaren Rauschgenerator und Sigma-Zeitplan und erzeugt sowohl die endgültige gesampelte Ausgabe als auch, sofern verfügbar, eine entrauschte Version.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `noise` | Der Rauschgenerator, der das anfängliche Rauschmuster und den Seed für den Sampling-Prozess bereitstellt | NOISE | Ja | - |
| `guider` | Das Guidance-Modell, das den Sampling-Prozess auf die gewünschte Ausgabe ausrichtet | GUIDER | Ja | - |
| `sampler` | Der Sampling-Algorithmus, der definiert, wie der latente Raum während der Generierung durchlaufen wird | SAMPLER | Ja | - |
| `sigmas` | Der Sigma-Zeitplan, der die Rauschpegel über die Sampling-Schritte hinweg steuert | SIGMAS | Ja | - |
| `latent_image` | Die anfängliche latente Repräsentation, die als Ausgangspunkt für das Sampling dient. Unterstützt einen optionalen Schlüssel `noise_mask` für selektives Entrauschen sowie optionale Schlüssel `downscale_ratio_spacial` und `downscale_ratio_temporal` für erweiterte Latent-Verarbeitung | LATENT | Ja | - |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `output` | Die endgültige gesampelte latente Repräsentation nach Abschluss des Sampling-Prozesses. Alle Schlüssel `downscale_ratio_spacial` oder `downscale_ratio_temporal` aus dem Eingabe-Latent werden aus dieser Ausgabe entfernt | LATENT |
| `denoised_output` | Eine entrauschte Version der Ausgabe, wenn der Sampling-Prozess eine saubere Zwischenvorhersage (x0) erzeugt; andernfalls wird dasselbe wie bei `output` zurückgegeben. Sofern verfügbar, stellt dies die beste Schätzung des Modells für das saubere Latent dar | LATENT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerCustomAdvanced/de.md)

---
**Source fingerprint (SHA-256):** `23cffad0f7cf74dcd494c2828b2116bb4d00a1e55e42ded074b587ac20183290`
