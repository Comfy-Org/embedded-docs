# LTXVReferenceAudio

LTXV Reference Audio überträgt die Stimmidentität eines Sprechers aus einem Referenzaudioclip auf das generierte Audio. Es kodiert das Referenzaudio in die Konditionierung und patcht optional das Modell mit Identitätsführung, wodurch bei jedem Schritt ein zusätzlicher Forward-Pass ohne Referenz ausgeführt wird, um den Effekt der Sprecheridentität zu verstärken.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model` | Das Modell, das mit Identitätsführung gepatcht werden soll. | MODEL | Ja | - |
| `positive` | Die positive Konditionierungseingabe. | CONDITIONING | Ja | - |
| `negative` | Die negative Konditionierungseingabe. | CONDITIONING | Ja | - |
| `reference_audio` | Referenzaudioclip, dessen Stimmidentität übertragen werden soll. ~5 Sekunden empfohlen (Trainingsdauer). Kürzere oder längere Clips können die Übertragung der Stimmidentität beeinträchtigen. | AUDIO | Ja | - |
| `audio_vae` | LTXV Audio VAE zum Kodieren. | VAE | Ja | - |
| `identity_guidance_scale` | Stärke der Identitätsführung. Führt bei jedem Schritt einen zusätzlichen Forward-Pass ohne Referenz aus, um die Sprecheridentität zu verstärken. Auf 0 setzen, um zu deaktivieren (kein zusätzlicher Durchlauf). (Standard: 3.0) | FLOAT | Ja | 0.0 - 100.0 |
| `start_percent` | Start des Sigma-Bereichs, in dem die Identitätsführung aktiv ist. (Standard: 0.0) | FLOAT | Ja | 0.0 - 1.0 |
| `end_percent` | Ende des Sigma-Bereichs, in dem die Identitätsführung aktiv ist. (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |

Hinweis: Die Identitätsführung wird nur angewendet, wenn `identity_guidance_scale` größer als 0 ist und der aktuelle Sampling-Schritt innerhalb des durch `start_percent` und `end_percent` definierten Bereichs liegt. Das Referenzaudio wird auf die Abtastrate des Audio-VAE neu abgetastet, falls die beiden voneinander abweichen.

Hinweis: `start_percent` und `end_percent` sind erweiterte Parameter und werden nur angezeigt, wenn die erweiterten Optionen in der Oberfläche aktiviert sind.

## Ausgaben

| Ausgabenamen | Beschreibung | Datentyp |
| --- | --- | --- |
| `model` | Das Modell, das mit der Identitätsführungsfunktion gepatcht wurde. | MODEL |
| `positive` | Die positive Konditionierung, die nun die kodierten Referenzaudiodaten enthält. | CONDITIONING |
| `negative` | Die negative Konditionierung, die nun die kodierten Referenzaudiodaten enthält. | CONDITIONING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVReferenceAudio/de.md)

---
**Source fingerprint (SHA-256):** `ae15c5838656324667d099614b325b863341f05afda43054658999574522dd49`
