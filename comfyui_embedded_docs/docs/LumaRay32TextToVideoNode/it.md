# LumaRay32TextToVideoNode

Questo nodo genera un video da un prompt testuale utilizzando il modello Ray 3.2 di Luma. Invia il prompt e le impostazioni video all'API di Luma e restituisce il video generato insieme a un ID di generazione.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `prompt` | Prompt testuale per la generazione del video. | STRING | Sì | da 1 a 6000 caratteri |
| `aspect_ratio` | Le proporzioni del video generato. | STRING | Sì | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"`<br>`"21:9"` |
| `resolution` | La risoluzione di output del video (predefinita: "720p"). | STRING | Sì | `"360p"`<br>`"540p"`<br>`"720p"`<br>`"1080p"` |
| `duration` | La durata del video generato. | STRING | Sì | `"5s"`<br>`"10s"` |
| `loop` | Rende il video riproducibile in loop senza interruzioni. Disponibile solo con durata di 5s. | BOOLEAN | No | True/False (predefinito: False) |
| `seed` | Seme per una generazione riproducibile. | INT | No | da 0 a 2147483647 |

**Nota:** Il parametro `loop` può essere abilitato solo quando `duration` è impostato su "5s". Se imposti `duration` su "10s" e abiliti `loop`, il nodo restituisce un errore.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `VIDEO` | Il file video generato. | VIDEO |
| `generation_id` | L'identificatore univoco per la richiesta di generazione del video. | STRING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaRay32TextToVideoNode/it.md)

---
**Source fingerprint (SHA-256):** `04358a872530e5a2622bf0f148a694f2c707ce8535586d8f860bdf9911e1fa6a`
