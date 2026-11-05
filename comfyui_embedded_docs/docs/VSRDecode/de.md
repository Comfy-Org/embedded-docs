# VSR Decode

VSR Decode verwandelt die Keyframe-Latents aus RelayVSR Conditioning mit dem RelayVSR Flash Decoder wieder in ein vollständiges Video. Der Decoder ergänzt eine bikubische Hochskalierung der von Ihnen übergebenen Frames niedriger Qualität um sein Detail, mit dem x2- oder x4-Faktor des Decoders. Die Anzahl der Frames bleibt unverändert.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `vae` | Der RelayVSR Flash Decoder, geladen mit Load VAE: `relayvsr_flash_vae_x2_fp32.safetensors` oder `relayvsr_flash_vae_x4_fp32.safetensors`. Die Metadaten der Datei legen den Hochskalierungsfaktor fest, daher muss dieser zum Modell passen. | VAE | Ja | Nicht zutreffend |
| `samples` | Das vom Sampler zurückgegebene Latent, das einen Frame pro Keyframe enthält. | LATENT | Ja | Nicht zutreffend |
| `images` | Dasselbe Video niedriger Qualität, das an RelayVSR Conditioning übergeben wurde. | IMAGE | Ja | Nicht zutreffend |
| `detail` | Wie viel vom Detail des Decoders zusätzlich zur bikubischen Hochskalierung beibehalten wird: 1 ist die vollständige Modellausgabe, 0 ist die reine Hochskalierung. (Standard: 1.0) | FLOAT | Ja | 0.0 bis 1.0 (Schritt: 0.01) |

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `images` | Das hochskalierte Video mit jedem wiederhergestellten Frame. | IMAGE |

## Hinweise

- Übergeben Sie dasselbe Video niedriger Qualität an beide Nodes. Der Decoder liest es Frame für Frame, daher führt eine Abweichung bei Länge oder Auflösung zu einem falschen oder fehlerhaften Ergebnis.
- Ein Verringern von `detail` macht das wiederhergestellte Detail weicher und hält die Ausgabe näher an einer reinen bikubischen Hochskalierung, was bei sehr verrauschten Quellen helfen kann.

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VSRDecode/de.md)

---
**Source fingerprint (SHA-256):** `946ac04bc9f205fd6d1088554caaa16238086e570f212e747b166e3fb0d9b3c5`
