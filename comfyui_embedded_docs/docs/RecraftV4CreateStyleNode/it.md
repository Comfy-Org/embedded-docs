# RecraftV4CreateStyleNode

Questo nodo crea uno stile Recraft V4 riutilizzabile da 1 a 10 immagini di riferimento. L'ID dello stile restituito funziona con ogni modello Recraft V4 e V4.1 dello stesso tipo di output (raster o vettoriale) e può essere riutilizzato nei passaggi successivi di generazione delle immagini. La dimensione totale di tutte le immagini di riferimento è limitata a 10 MB.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `model` | Modello per cui viene creato lo stile. Standard e Pro condividono un unico pool di stili: gli stili raster funzionano con ogni modello raster Recraft V4 e V4.1, gli stili vettoriali (`*_vector`) con ogni modello vettoriale V4 e V4.1. | COMBO | Sì | "recraftv4_styles"<br>"recraftv4_styles_vector"<br>"recraftv4_styles_pro"<br>"recraftv4_styles_pro_vector" |
| `images` | Immagini di riferimento che definiscono lo stile. Riferimenti simili affinano la corrispondenza, riferimenti vari la ampliano. Slot espandibile: collega da 1 a 10 immagini (da `image_1` a `image_10`). | IMAGE | Sì | 1 to 10 images |

### Note

- È richiesta almeno un'immagine di riferimento; il nodo genera un errore se non ne viene fornita alcuna.
- Sono consentite al massimo 10 immagini di riferimento; il nodo genera un errore se ne vengono fornite di più.
- La dimensione codificata totale di tutte le immagini di riferimento non deve superare 10 MB; il nodo genera un errore se il limite viene superato.
- Ogni immagine di riferimento viene ridimensionata a un massimo di 2048×2048 pixel e codificata come WebP prima di essere inviata all'API Recraft.
- I modelli che terminano in `_vector` creano stili vettoriali; le altre opzioni creano stili raster. I modelli Standard e Pro condividono gli stessi pool di stili all'interno di ciascun tipo di output.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `style_id` | Identificatore univoco dello stile creato, utilizzabile con ogni modello Recraft V4 e V4.1 dello stesso tipo di output. | STRING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftV4CreateStyleNode/it.md)

---
**Source fingerprint (SHA-256):** `7b907a975ed88dcca6bf1e0431ef7a9b561852ca7263a4f3298df980fe9431e5`
