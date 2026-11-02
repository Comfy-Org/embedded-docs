# MiniMax H3 Latent Upscale With Model

MiniMax H3 Latent Upscale With Model skaliert den Videoteil eines MiniMax H3-Latents mit einem Latent-Upscale-Modell auf eine Zielbreite und -höhe. Das Audio-Latent bleibt unverändert, sodass der Clip seinen Ton behält und kein erneutes Sampling erforderlich ist. Verwenden Sie ihn nach dem MiniMax H3-Sampling und vor dem H3 VAE-Decode, wenn der Clip größer ausgegeben werden soll.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model` | Latent-Upscale-Modell, das normalerweise mit Load Latent Upscale Model geladen wird. Es muss ein MiniMax H3 3D-Conv-Latent-Upscaler sein. | LATENT_UPSCALE_MODEL | Ja | - |
| `samples` | MiniMax H3-Latent, dessen Größe geändert werden soll. Bei einem verschachtelten Latent bleibt der Audioteil unverändert. | LATENT | Ja | - |
| `width` | Zielbreite des Videos in Pixeln. Das Latent wird auf `width / 16` Spalten skaliert, daher wird der Wert auf ein Vielfaches von 16 abgerundet. (Standard: 2560) | INT | Ja | 32 bis 16384 (Schritt 32) |
| `height` | Zielhöhe des Videos in Pixeln, ebenfalls auf ein Vielfaches von 16 abgerundet. (Standard: 1440) | INT | Ja | 32 bis 16384 (Schritt 32) |

Wenn die angeforderte Größe bereits dem Latent entspricht, wird das Eingabe-Latent unverändert zurückgegeben. Ein neu skaliertes Latent enthält keinen `noise_mask`, sodass ein teilweise maskiertes Latent seine Maske verliert. Das Netzwerk führt seine 3D-Faltungen in zeitlichen Slabs aus, wodurch der Speicherverbrauch bei langen Clips nahe dem eines einzelnen Slabs bleibt.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `LATENT` | Das skalierte Latent, bereit für den H3 VAE-Decode. | LATENT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MiniMaxH3LatentUpscaleWithModel/de.md)

---
**Source fingerprint (SHA-256):** `cd659baace5a21620033dd3470b854cccbada01d09545a2f61273b949c3a004b`
