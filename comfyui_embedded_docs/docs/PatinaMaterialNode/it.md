# Patina Material

Genera un materiale PBR completo e perfettamente piastrellabile da una descrizione testuale: una texture di base più fino a cinque mappe del materiale, con upscaling SeedVR opzionale delle mappe. Un'immagine di input può guidare il risultato come passaggio image-to-image, e un'immagine di input con una maschera lo trasforma in un passaggio di inpainting. Usalo per produrre superfici pronte per giochi o per il 3D senza scansionare un materiale reale.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Descrizione del materiale o della texture da generare. | STRING | Sì | Testo multiriga |
| `image_size` | Dimensione della texture di output. `"custom"` mostra gli input `width` e `height`. Predefinito: `"1:1 (1024x1024)"`. | DYNAMIC_COMBO | Sì | `"1:1 (1024x1024)"`<br>`"1:1 (512x512)"`<br>`"4:3 (1024x768)"`<br>`"3:4 (768x1024)"`<br>`"16:9 (1024x576)"`<br>`"9:16 (576x1024)"`<br>`"custom"` |
| `basecolor` | Genera la mappa basecolor (albedo). Predefinito: True. | BOOLEAN | Sì | true<br>false |
| `normal` | Genera la mappa normale. Predefinito: True. | BOOLEAN | Sì | true<br>false |
| `roughness` | Genera la mappa di rugosità. Predefinito: False. | BOOLEAN | Sì | true<br>false |
| `metalness` | Genera la mappa metalness. Predefinito: False. | BOOLEAN | Sì | true<br>false |
| `height` | Genera la mappa di altezza (displacement). Predefinito: False. | BOOLEAN | Sì | true<br>false |
| `upscale_factor` | Upscaling SeedVR senza cuciture delle mappe PBR. La texture di base non viene sottoposta a upscaling, e 4x trasforma una mappa da 2048 pixel in una da 8K. Predefinito: 0 (disattivato). | INT | Sì | 0-4 (passo 2) |
| `seed` | Seed per una generazione riproducibile. Predefinito: 42. | INT | Sì | 0-2147483646 |
| `tiling_mode` | Direzione della piastrellatura: omnidirezionale, orizzontale o verticale. Impostazione avanzata. Predefinito: `"both"`. | COMBO | Sì | `"both"`<br>`"horizontal"`<br>`"vertical"` |
| `num_inference_steps` | Passaggi di denoising per la generazione della texture. Impostazione avanzata. Predefinito: 8. | INT | Sì | 1-8 |
| `tile_size` | Dimensione del tile nello spazio latente, dove 64 significa 512 pixel e 128 significa 1024 pixel. Impostazione avanzata. Predefinito: 128. | INT | Sì | 32-256 (passo 2) |
| `tile_stride` | Passo (stride) del tile nello spazio latente. Impostazione avanzata. Predefinito: 64. | INT | Sì | 16-128 (passo 2) |
| `image` | Immagine sorgente opzionale. Da sola esegue image-to-image; insieme a una maschera esegue un passaggio di inpainting. | IMAGE | No | - |
| `mask` | Maschera di inpainting opzionale, richiede un'immagine di input. Le aree bianche vengono rigenerate e le aree nere vengono mantenute. | MASK | No | - |
| `strength` | Quanto trasformare l'immagine di input. Usato solo quando è collegata un'immagine. Impostazione avanzata. Predefinito: 0.6. | FLOAT | Sì | 0.01-1.0 (passo 0.01) |
| `prompt_expansion` | Espande il prompt con un modello linguistico per ottenere dettagli della texture più ricchi. Disattivato per impostazione predefinita, perché l'espansione riformula il prompt come una fotografia e tende a diluire la mappa metalness. Impostazione avanzata. | BOOLEAN | Sì | true<br>false |
| `safety_checker` | Esegue il controllo di sicurezza dei contenuti del provider sulla richiesta. Impostazione avanzata. Predefinito: False. | BOOLEAN | Sì | true<br>false |

### Input di dimensione immagine personalizzata

Questi input compaiono quando `image_size` è impostato su `"custom"`.

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `image_size.width` | Larghezza della texture in pixel. Predefinito: 1024. | INT | Sì | 512-2048 (passo 16) |
| `image_size.height` | Altezza della texture in pixel. Predefinito: 1024. | INT | Sì | 512-2048 (passo 16) |

**Vincoli e comportamento:**

* È consentito non abilitare alcuna mappa del materiale: in tal caso il nodo restituisce solo la texture di base e ogni output di mappa rimane un segnaposto 1x1.
* Una maschera richiede un'immagine di input; una maschera da sola genera un errore.
* Un risultato 8K deriva dall'upscaling 4x delle mappe di un render da 2048 pixel, non da una singola generazione 8K.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|-----------|
| `texture` | La texture di base del materiale, senza alcuna mappa applicata. | IMAGE |
| `basecolor` | La mappa basecolor (albedo), oppure un segnaposto 1x1 quando quella mappa è disabilitata. | IMAGE |
| `normal` | La mappa normale, oppure un segnaposto 1x1 quando quella mappa è disabilitata. | IMAGE |
| `roughness` | La mappa di rugosità, oppure un segnaposto 1x1 quando quella mappa è disabilitata. | IMAGE |
| `metalness` | La mappa metalness, oppure un segnaposto 1x1 quando quella mappa è disabilitata. | IMAGE |
| `height` | La mappa di altezza (displacement), oppure un segnaposto 1x1 quando quella mappa è disabilitata. | IMAGE |
| `expanded_prompt` | Il prompt effettivamente utilizzato dal provider, che differisce dall'input solo quando `prompt_expansion` è abilitato. | STRING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PatinaMaterialNode/it.md)

---
**Source fingerprint (SHA-256):** `4e8305fa56a29dce72c54de12ae05207e8de39a1fea1f4753906c26e8af60383`
