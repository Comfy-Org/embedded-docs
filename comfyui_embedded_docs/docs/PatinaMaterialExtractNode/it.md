# Patina Material Extract

Estrae un materiale PBR piastrellabile senza giunture da una regione di un'immagine di input, guidato da un prompt che specifica cosa prelevare: una parete, un pavimento, un tessuto. Restituisce la texture di base estratta oltre a un massimo di cinque mappe materiale, con upscaling opzionale delle mappe tramite SeedVR. Usalo per trasformare la foto di una superficie reale in un materiale riutilizzabile e piastrellabile.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `image` | L'immagine da cui estrarre una texture. | IMAGE | Sì | - |
| `prompt` | Descrizione di quale texture estrarre dall'immagine, ad esempio `"the wall"`. | STRING | Sì | Multiline text |
| `image_size` | Dimensione della texture di output. `"custom"` mostra gli input `width` e `height`. Predefinito: `"1:1 (1024x1024)"`. | DYNAMIC_COMBO | Sì | `"1:1 (1024x1024)"`<br>`"1:1 (512x512)"`<br>`"4:3 (1024x768)"`<br>`"3:4 (768x1024)"`<br>`"16:9 (1024x576)"`<br>`"9:16 (576x1024)"`<br>`"custom"` |
| `basecolor` | Genera la mappa basecolor (albedo). Predefinito: True. | BOOLEAN | Sì | true<br>false |
| `normal` | Genera la mappa normal. Predefinito: True. | BOOLEAN | Sì | true<br>false |
| `roughness` | Genera la mappa roughness. Predefinito: False. | BOOLEAN | Sì | true<br>false |
| `metalness` | Genera la mappa metalness. Predefinito: False. | BOOLEAN | Sì | true<br>false |
| `height` | Genera la mappa height (displacement). Predefinito: False. | BOOLEAN | Sì | true<br>false |
| `upscale_factor` | Upscaling SeedVR senza giunture delle mappe PBR. La texture di base non viene sottoposta a upscaling e 4x trasforma una mappa da 2048 pixel in una mappa 8K. Predefinito: 0 (disattivato). | INT | Sì | 0 a 4 (passo: 2) |
| `seed` | Seed per una generazione riproducibile. Predefinito: 42. | INT | Sì | 0 a 2147483646 |
| `strength` | Quanto trasformare l'immagine di input. Impostazione avanzata. Predefinito: 0.6. | FLOAT | Sì | 0.01 a 1.0 (passo: 0.01) |
| `tiling_mode` | Direzione del tiling: omnidirezionale, orizzontale o verticale. Impostazione avanzata. Predefinito: `"both"`. | COMBO | Sì | `"both"`<br>`"horizontal"`<br>`"vertical"` |
| `num_inference_steps` | Passaggi di denoising per la generazione della texture. Impostazione avanzata. Predefinito: 8. | INT | Sì | 1 a 8 |
| `tile_size` | Dimensione del tile nello spazio latente, dove 64 significa 512 pixel e 128 significa 1024 pixel. Impostazione avanzata. Predefinito: 128. | INT | Sì | 32 a 256 (passo: 2) |
| `tile_stride` | Stride del tile nello spazio latente. Impostazione avanzata. Predefinito: 64. | INT | Sì | 16 a 128 (passo: 2) |
| `prompt_expansion` | Espande il prompt con un modello linguistico per ottenere dettagli della texture più ricchi. Disattivato per impostazione predefinita, perché l'espansione riformula il prompt come una fotografia e tende a diluire la mappa metalness. Impostazione avanzata. | BOOLEAN | Sì | true<br>false |
| `safety_checker` | Esegue il controllo di sicurezza dei contenuti del provider sulla richiesta. Impostazione avanzata. Predefinito: False. | BOOLEAN | Sì | true<br>false |

### Input per dimensioni immagine personalizzate

Questi input compaiono quando `image_size` è impostato su `"custom"`.

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `image_size.width` | Larghezza della texture in pixel. Predefinito: 1024. | INT | Sì | 512 a 2048 (passo: 16) |
| `image_size.height` | Altezza della texture in pixel. Predefinito: 1024. | INT | Sì | 512 a 2048 (passo: 16) |

**Vincoli e comportamento:**

* Almeno una mappa materiale deve essere abilitata; in caso contrario l'esecuzione fallisce.
* Il prompt è obbligatorio e non deve essere vuoto; specifica la regione da estrarre nel modo più preciso possibile.
* Un risultato 8K deriva dall'upscaling 4x delle mappe di un render da 2048 pixel, non da una singola generazione 8K.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|-----------|
| `texture` | La texture di base estratta, senza alcuna mappa applicata. | IMAGE |
| `basecolor` | La mappa basecolor (albedo), oppure un placeholder 1x1 quando quella mappa è disabilitata. | IMAGE |
| `normal` | La mappa normal, oppure un placeholder 1x1 quando quella mappa è disabilitata. | IMAGE |
| `roughness` | La mappa roughness, oppure un placeholder 1x1 quando quella mappa è disabilitata. | IMAGE |
| `metalness` | La mappa metalness, oppure un placeholder 1x1 quando quella mappa è disabilitata. | IMAGE |
| `height` | La mappa height (displacement), oppure un placeholder 1x1 quando quella mappa è disabilitata. | IMAGE |
| `expanded_prompt` | Il prompt effettivamente usato dal provider, che differisce dall'input solo quando `prompt_expansion` è abilitato. | STRING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PatinaMaterialExtractNode/it.md)

---
**Source fingerprint (SHA-256):** `484b8eaa57388541e352cd88c8998c63aa0b2a99d98cd8e602252625064f16ba`
