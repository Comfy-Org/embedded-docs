# LTXVAudioVAEDecode

Der Node LTXV Audio VAE Decode wandelt eine latente Repräsentation von Audio zurück in eine Audio-Wellenform um. Er verwendet ein spezialisiertes Audio-VAE-Modell für diesen Dekodierungsprozess und erzeugt eine Audio-Ausgabe mit der zugehörigen Abtastrate.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `samples` | Das zu dekodierende Latent. | LATENT | Ja | N/A |
| `audio_vae` | Das Audio-VAE-Modell, das zum Dekodieren des Latents verwendet wird. | VAE | Ja | N/A |

**Hinweis:** Wenn das bereitgestellte Latent verschachtelt ist (mehrere Latents enthält), verwendet der Node automatisch das letzte Latent in der Sequenz zur Dekodierung.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `Audio` | Die dekodierte Audio-Wellenform und ihre zugehörige Abtastrate. Die Wellenform wird auf demselben Gerät wie das Eingabe-Latent platziert, und die Abtastrate wird durch das Audio-VAE-Modell bestimmt. | AUDIO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVAudioVAEDecode/de.md)

---
**Source fingerprint (SHA-256):** `fc94f3cb78ede86ada374444d613411cc9bb5849e5cdb8a24074babee50719b1`
