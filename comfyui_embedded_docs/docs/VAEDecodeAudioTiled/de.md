# VAEDecodeAudioTiled

Dieser Node wandelt eine komprimierte Audiodarstellung (latente Samples) mithilfe eines Variational Autoencoders (VAE) zurück in eine Audiowellenform um. Die Daten werden in kleinere, überlappende Abschnitte (Kacheln) aufgeteilt, um den Speicherverbrauch zu steuern, wodurch er für die Verarbeitung längerer Audiosequenzen geeignet ist. Das decodierte Audio wird zudem normalisiert, um eine konsistente Lautstärke beizubehalten.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `samples` | Die komprimierte latente Repräsentation des zu decodierenden Audios. | LATENT | Ja | N/A |
| `vae` | Das Variational-Autoencoder-Modell, das zur Durchführung der Decodierung verwendet wird. | VAE | Ja | N/A |
| `tile_size` | Die Größe jeder Verarbeitungskachel. Das Audio wird in Abschnitten dieser Länge decodiert, um Speicher zu sparen (Standard: 512). Muss ein Vielfaches von 8 sein. | INT | Ja | 32 bis 8192 (Schritt 8) |
| `overlap` | Die Anzahl der Samples, um die benachbarte Kacheln überlappen. Dies hilft, Artefakte an den Grenzen zwischen Kacheln zu reduzieren (Standard: 64). Muss ein Vielfaches von 8 sein. | INT | Ja | 0 bis 1024 (Schritt 8) |

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `output` | Die decodierte Audiowellenform, einschließlich ihrer Abtastrateninformationen. | AUDIO |

Die Ausgabe-Abtastrate wird aus dem Eingabe-`samples` übernommen, wenn darin eine enthalten ist; andernfalls wird sie aus dem VAE-Modell gelesen (Standard: 44100 Hz).

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEDecodeAudioTiled/de.md)

---
**Source fingerprint (SHA-256):** `5ddedf218ba27ab9f463646c1e5288091172f2d7fae8f2980bb2b5e4d3dca89c`
