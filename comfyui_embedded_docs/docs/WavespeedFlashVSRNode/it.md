# FlashVSR Video Upscale

WavespeedFlashVSRNode è un upscaler video veloce e di alta qualità che aumenta la risoluzione e ripristina la nitidezza di filmati a bassa risoluzione o sfocati. Elabora un video in input e restituisce in output un nuovo video alla risoluzione superiore selezionata dall'utente.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `video` | Il file video di input da sottoporre a upscaling. Deve essere in formato contenitore MP4 con una durata compresa tra 5 secondi e 10 minuti. | VIDEO | Sì | N/A |
| `target_resolution` | La risoluzione desiderata per il video di output sottoposto a upscaling. | STRING | Sì | `"720p"`<br>`"1080p"`<br>`"2K"`<br>`"4K"` |

**Vincoli di input:**

- Il file `video` di input deve essere in formato contenitore MP4.
- La durata del `video` di input deve essere compresa tra 5 secondi e 10 minuti (600 secondi).

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `output` | Il file video sottoposto a upscaling alla risoluzione target selezionata. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WavespeedFlashVSRNode/it.md)

---
**Source fingerprint (SHA-256):** `d7885eeb2dacfc2bc398d1bc991620be479f45d8edbdca7eb046a21500581529`
