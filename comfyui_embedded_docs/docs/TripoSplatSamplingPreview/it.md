# TripoSplat Sampling Preview

Questo nodo applica una patch a un modello TripoSplat in modo che, quando viene utilizzato con il nodo KSampler standard, mostri un'anteprima in tempo reale della gaussian splat decodificata a ogni passo di campionamento. Funziona avvolgendo la callback del sampler per decodificare l'output del modello in un'immagine di anteprima dopo ogni passo.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `model` | Il modello TripoSplat su cui applicare la patch per l'anteprima in tempo reale (fornisce la lunghezza del token di condizionamento usata per stimare il fabbisogno di memoria) | MODEL | Sì | |
| `vae` | Decoder VAE di TripoSplat | VAE | Sì | |
| `octree_level` | Profondità dell'octree per la decodifica dell'anteprima (valore più basso = meno costoso/più grossolano). Predefinito: 5 | INT | No | da 2 a 8 |
| `num_gaussians` | Numero di gaussiane da produrre per l'anteprima (arrotondato a un multiplo di 32). Predefinito: 16384 | INT | No | da 1024 a 262144 (passo: 32) |
| `yaw` | Imbardata della camera di anteprima in gradi. Predefinito: 90.0 | FLOAT | No | da -360.0 a 360.0 (passo: 1.0) |
| `pitch` | Inclinazione della camera di anteprima in gradi. Predefinito: 15.0 | FLOAT | No | da -89.0 a 89.0 (passo: 1.0) |
| `point_size` | Raggio massimo dello splat in pixel. Ogni gaussiana viene dimensionata in base alla sua scala e limitata a questo valore; valore più basso = più fine/puntiforme, valore più alto = più massiccio. Predefinito: 3 | INT | No | da 1 a 16 |

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `MODEL` | Il modello TripoSplat modificato con l'aggiunta della funzionalità di anteprima in tempo reale | MODEL |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoSplatSamplingPreview/it.md)

---
**Source fingerprint (SHA-256):** `78678b65df325da964cfd3e8cd0dc07fa25b92d26bb2057117db413a205e9535`
