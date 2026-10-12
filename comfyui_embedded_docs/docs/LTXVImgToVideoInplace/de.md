# LTXVImgToVideoInplace

LTXVImgToVideoInplace kodiert ein Eingabebild in den latenten Raum und platziert diese kodierten Frames am Anfang eines vorhandenen latenten Videos. Der Wert `strength` steuert, wie stark das kodierte Bild diese Anfangs-Frames konditioniert, und wenn `bypass` aktiviert ist, wird das Eingabe-Latent unverändert zurückgegeben.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `vae` | Das VAE-Modell, das verwendet wird, um das Eingabebild in den latenten Raum zu kodieren. | VAE | Ja | - |
| `image` | Das Eingabebild, das kodiert und zur Konditionierung des Video-Latents verwendet wird. | IMAGE | Ja | - |
| `latent` | Die Ziel-Latent-Videorepräsentation, die geändert werden soll. | LATENT | Ja | - |
| `strength` | Steuert, wie stark das kodierte Bild die Anfangs-Frames des Latents konditioniert. Ein Wert von 1.0 konditioniert die Anfangs-Frames vollständig mit dem kodierten Bild, während niedrigere Werte sie weniger stark konditionieren. Die Rauschmaske für die Anfangs-Frames wird auf `1.0 - strength` gesetzt. (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `bypass` | Umgeht die Konditionierung. Wenn aktiviert, gibt der Node das Eingabe-Latent unverändert zurück. (Standard: False) | BOOLEAN | Ja | True or False |

**Hinweis:** Das `image` wird automatisch auf die vom `vae` für die Kodierung benötigten räumlichen Abmessungen skaliert, basierend auf Breite und Höhe der Eingabe `latent`. Von `image` werden nur die RGB-Kanäle für die Kodierung verwendet.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `latent` | Die resultierende latente Videorepräsentation. Wenn Bypass deaktiviert ist, enthält sie die aktualisierten `samples` und eine `noise_mask`, welche die Konditionierungsstärke auf die Anfangs-Frames anwendet. Wenn Bypass aktiviert ist, ist sie das unverändert zurückgegebene Eingabe-Latent. | LATENT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVImgToVideoInplace/de.md)

---
**Source fingerprint (SHA-256):** `69faa4b2e7b0fedeee531dc5a8809e23a79c9ce03e9760afb865160594fef30d`
