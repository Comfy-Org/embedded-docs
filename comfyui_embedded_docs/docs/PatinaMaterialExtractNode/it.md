# Patina Material Extract

Estrae un materiale PBR tileabile senza cuciture da una regione di un'immagine di input, guidato da un prompt che indica cosa prelevare: una parete, un pavimento, un tessuto. Restituisce la texture di base estratta più fino a cinque mappe del materiale, con upscaling SeedVR opzionale delle mappe. Usalo per trasformare la foto di una superficie reale in un materiale riutilizzabile e tileabile.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `image` | L'immagine da cui estrarre una texture. | IMAGE | Sì | - |
| `prompt` | Descrizione di quale texture estrarre dall'immagine, ad esempio `"the wall"`. | STRING | Sì | Testo multiriga |
| `image_size` | Dimensione della texture di output. `"custom"` mostra gli input `width` e `height`. Predefinito: `"1:1 (1024x1024)"`. | DYNAMIC_COMBO | Sì | `"1:1 (1024x1024)"`<br>`"1:1 (512x512)"`<br>`"4:3 (1024x768)"`<br>`"3:4 (768x1024)"`<br>`"16:9 (1024x576)"`<br>`"9:16 (576x1024)"`<br>`"custom"` |
| `basecolor` | Genera la mappa basecolor (albedo). Predefinito: True. | BOOLEAN | Sì | true<br>false |
| `normal` | Genera la mappa normal. Predefinito: True. | BOOLEAN | Sì | true<br>false |
| `roughness` | Genera la mappa roughness. Predefinito: False. | BOOLEAN | Sì | true<br>false |
| `metalness` | Genera la mappa metalness. Predefinito: False. | BOOLEAN | Sì | true<br>false |
| `height` | Genera la mappa height (displacement). Predefinito: False. | BOOLEAN | Sì | true<br>false |
| `upscale_factor` | Upscaling SeedVR senza cuciture delle mappe PBR. La texture di base non viene sottoposta a upscaling e 4x trasforma una mappa da 2048 pixel in una da 8K. Predefinito: 0 (disattivato). | INT | Sì | 0 a 4 (passo 2) |
| `seed` | Seme per una generazione riproducibile. Predefinito: 42. | INT | Sì | 0 a 2147483646 |
| `strength` | Quanto trasformare l'immagine di input. Impostazione avanzata. Predefinito: 0.6. | FLOAT | Sì | 0.01 a 1.0 (passo 0.01) |
| `tiling_mode` | Direzione del tiling: omnidirezionale, orizzontale o verticale. Impostazione avanzata. Predefinito: `"both"`. | COMBO | Sì | `"both"`<br>`"horizontal"`<br>`"vertical"` |
| `num_inference_steps` | Passi di denoising per la generazione della texture. Impostazione avanzata. Predefinito: 8. | INT | Sì | 1 a 8 |
| `tile_size` | Dimensione del tile nello spazio latente, dove 64 indica 512 pixel e 128 indica 1024 pixel. Impostazione avanzata. Predefinito: 128. | INT | Sì | 32 a 256 (passo 2) |
| `tile_stride` | Stride del tile nello spazio latente. Impostazione avanzata. Predefinito: 64. | INT | Sì | 16 a 128 (passo 2) |
| `prompt_expansion` | Espande il prompt con un modello linguistico per ottenere dettagli più ricchi della texture. Disattivato per impostazione predefinita, perché l'espansione riformula il prompt come una fotografia e tende a diluire la mappa metalness. Impostazione avanzata. | BOOLEAN | Sì | true<br>false |
| `safety_checker` | Esegue il controllo di sicurezza dei contenuti del fornitore sulla richiesta. Impostazione avanzata. Predefinito: False. | BOOLEAN | Sì | true<br>false |

### Input per dimensione immagine personalizzata

Questi input compaiono quando `image_size` è impostato su `"custom"`.

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `image_size.width` | Larghezza della texture in pixel. Predefinito: 1024. | INT | Sì | 512 a 2048 (passo 16) |
| `image_size.height` | Altezza della texture in pixel. Predefinito: 1024. | INT | Sì | 512 a 2048 (passo 16) |

**Vincoli e comportamento:**

* È consentito non abilitare alcuna mappa del materiale: in tal caso il nodo restituisce solo la texture di base e ogni output di mappa resta un placeholder 1x1.
* Il prompt è obbligatorio e non deve essere vuoto; indica la regione da estrarre nel modo più preciso possibile.
* Un risultato 8K deriva dall'upscaling 4x delle mappe di un render da 2048 pixel, non da una singola generazione 8K.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `texture` | La texture di base estratta, senza alcuna mappa applicata. | IMAGE |
| `basecolor` | La mappa basecolor (albedo), oppure un placeholder 1x1 quando tale mappa è disabilitata. | IMAGE |
| `normal` | La mappa normal, oppure un placeholder 1x1 quando tale mappa è disabilitata. | IMAGE |
| `roughness` | La mappa roughness, oppure un placeholder 1x1 quando tale mappa è disabilitata. | IMAGE |
| `metalness` | La mappa metalness, oppure un placeholder 1x1 quando tale mappa è disabilitata. | IMAGE |
| `height` | La mappa height (displacement), oppure un placeholder 1x1 quando tale mappa è disabilitata. | IMAGE |
| `expanded_prompt` | Il prompt effettivamente utilizzato dal fornitore, che differisce dall'input solo quando `prompt_expansion` è abilitato. | STRING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PatinaMaterialExtractNode/it.md)

---
**Source fingerprint (SHA-256):** `484b8eaa57388541e352cd88c8998c63aa0b2a99d98cd8e602252625064f16ba`
