# Patina Material

Genera un materiale PBR completo e piastrellabile senza giunture a partire da una descrizione testuale: una texture di base più fino a cinque mappe del materiale, con upscaling SeedVR opzionale delle mappe. Un'immagine di input può guidare il risultato come passaggio image-to-image, mentre un'immagine di input con una maschera lo trasforma in un passaggio di inpaint. Usalo per produrre superfici pronte per giochi o per la 3D senza scansionare un materiale reale.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `prompt` | Descrizione del materiale o della texture da generare. | STRING | Sì | Testo multilinea |
| `image_size` | Dimensione della texture di output. `"custom"` mostra gli input `width` e `height`. Predefinito: `"1:1 (1024x1024)"`. | DYNAMIC_COMBO | Sì | `"1:1 (1024x1024)"`<br>`"1:1 (512x512)"`<br>`"4:3 (1024x768)"`<br>`"3:4 (768x1024)"`<br>`"16:9 (1024x576)"`<br>`"9:16 (576x1024)"`<br>`"custom"` |
| `basecolor` | Genera la mappa basecolor (albedo). Predefinito: True. | BOOLEAN | Sì | true<br>false |
| `normal` | Genera la mappa normal. Predefinito: True. | BOOLEAN | Sì | true<br>false |
| `roughness` | Genera la mappa roughness. Predefinito: False. | BOOLEAN | Sì | true<br>false |
| `metalness` | Genera la mappa metalness. Predefinito: False. | BOOLEAN | Sì | true<br>false |
| `height` | Genera la mappa height (displacement). Predefinito: False. | BOOLEAN | Sì | true<br>false |
| `upscale_factor` | Upscaling SeedVR senza giunture delle mappe PBR. La texture di base non viene sottoposta a upscaling e 4x trasforma una mappa da 2048 pixel in una da 8K. Predefinito: 0 (disattivato). | INT | Sì | da 0 a 4 (passo 2) |
| `seed` | Seme per una generazione riproducibile. Predefinito: 42. | INT | Sì | da 0 a 2147483646 |
| `tiling_mode` | Direzione del tiling: omnidirezionale, orizzontale o verticale. Impostazione avanzata. Predefinito: `"both"`. | COMBO | Sì | `"both"`<br>`"horizontal"`<br>`"vertical"` |
| `num_inference_steps` | Passi di denoising per la generazione della texture. Impostazione avanzata. Predefinito: 8. | INT | Sì | da 1 a 8 |
| `tile_size` | Dimensione dei tile nello spazio latente, dove 64 indica 512 pixel e 128 indica 1024 pixel. Impostazione avanzata. Predefinito: 128. | INT | Sì | da 32 a 256 (passo 2) |
| `tile_stride` | Stride dei tile nello spazio latente. Impostazione avanzata. Predefinito: 64. | INT | Sì | da 16 a 128 (passo 2) |
| `image` | Immagine sorgente opzionale. Da sola esegue un passaggio image-to-image; insieme a una maschera esegue un passaggio di inpaint. | IMAGE | No | - |
| `mask` | Maschera di inpaint opzionale; richiede un'immagine di input. Le aree bianche vengono rigenerate e le aree nere vengono mantenute. | MASK | No | - |
| `strength` | Quanto trasformare l'immagine di input. Usato solo quando è collegata un'immagine. Impostazione avanzata. Predefinito: 0.6. | FLOAT | Sì | da 0.01 a 1.0 (passo 0.01) |
| `prompt_expansion` | Espande il prompt con un modello linguistico per ottenere dettagli più ricchi della texture. Disattivato per impostazione predefinita, perché l'espansione riformula il prompt come una fotografia e tende a sbiadire la mappa metalness. Impostazione avanzata. | BOOLEAN | Sì | true<br>false |
| `safety_checker` | Esegue il controllo di sicurezza dei contenuti del provider sulla richiesta. Impostazione avanzata. Predefinito: False. | BOOLEAN | Sì | true<br>false |

### Input per dimensione immagine personalizzata

Questi input compaiono quando `image_size` è impostato su `"custom"`.

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `image_size.width` | Larghezza della texture in pixel. Predefinito: 1024. | INT | Sì | da 512 a 2048 (passo 16) |
| `image_size.height` | Altezza della texture in pixel. Predefinito: 1024. | INT | Sì | da 512 a 2048 (passo 16) |

**Vincoli e comportamento:**

* Almeno una mappa del materiale deve essere abilitata, altrimenti l'esecuzione fallisce.
* Una maschera richiede un'immagine di input; una maschera da sola provoca un errore.
* Un risultato 8K deriva dall'upscaling 4x delle mappe di un rendering da 2048 pixel, non da una singola generazione 8K.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `texture` | La texture di base del materiale, senza alcuna mappa applicata. | IMAGE |
| `basecolor` | La mappa basecolor (albedo), oppure un segnaposto 1x1 quando quella mappa è disabilitata. | IMAGE |
| `normal` | La mappa normal, oppure un segnaposto 1x1 quando quella mappa è disabilitata. | IMAGE |
| `roughness` | La mappa roughness, oppure un segnaposto 1x1 quando quella mappa è disabilitata. | IMAGE |
| `metalness` | La mappa metalness, oppure un segnaposto 1x1 quando quella mappa è disabilitata. | IMAGE |
| `height` | La mappa height (displacement), oppure un segnaposto 1x1 quando quella mappa è disabilitata. | IMAGE |
| `expanded_prompt` | Il prompt effettivamente usato dal provider, che differisce dall'input solo quando `prompt_expansion` è abilitato. | STRING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PatinaMaterialNode/it.md)

---
**Source fingerprint (SHA-256):** `4e8305fa56a29dce72c54de12ae05207e8de39a1fea1f4753906c26e8af60383`
