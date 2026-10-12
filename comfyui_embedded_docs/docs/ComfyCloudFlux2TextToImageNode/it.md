# ComfyCloudFlux2TextToImageNode

Esegue il modello Flux 2 dev text-to-image su una GPU di Comfy Cloud e restituisce l'immagine generata. L'opzione `turbo` applica il Turbo LoRA con una pianificazione breve per un'esecuzione molto più rapida al costo di una lieve perdita di fedeltà; disattivandola si esegue il passaggio dev completo senza il LoRA. Questo è un set di nodi beta, fatturato in crediti in base alla durata di esecuzione.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `prompt` | Il prompt testuale che descrive l'immagine da generare. Gli spazi bianchi iniziali e finali vengono rimossi prima dell'invio. | STRING | Sì | Da 1 a 4096 caratteri |
| `seed` | Seme casuale che controlla il risultato generato per la riproducibilità (predefinito: 42). | INT | Sì | Da 0 a 18446744073709551615 |
| `aspect_ratio` | Rapporto d'aspetto dell'immagine di output (predefinito: "1:1"). | COMBO | Sì | "1:1"<br>"3:4"<br>"2:3"<br>"3:2"<br>"4:3"<br>"16:9"<br>"9:16"<br>"21:9" |
| `megapixels` | Budget totale di pixel. 1.0 corrisponde a circa 1024x1024 con proporzioni quadrate (predefinito: 1.0). | FLOAT | Sì | Da 0.1 a 16.0 (passo 0.1) |
| `turbo` | Esegue il Turbo LoRA con una pianificazione breve, scambiando un po' di fedeltà con un'esecuzione molto più rapida. Disattivato esegue il passaggio dev completo senza LoRA (predefinito: True). | BOOLEAN | Sì | True / False |

## Output

| Nome dell'output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `IMAGE` | L'immagine generata dal prompt testuale, restituita come tensore immagine ComfyUI che può essere passato ad altri nodi. | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyCloudFlux2TextToImageNode/it.md)

---
**Source fingerprint (SHA-256):** `1b51a8ab89ae7c355dec4256a1a25a09a15e192c72fc8d1862c652dbdf337fcb`
