# Dividi Latent SeedVR2

Questo nodo suddivide un latent video SeedVR2 in chunk temporali più piccoli che possono essere elaborati uno alla volta entro la VRAM disponibile. Calcola automaticamente la dimensione ottimale dei chunk in base alla memoria della GPU oppure consente di specificare manualmente la dimensione del chunk, e restituisce i chunk in ordine sequenziale per l'elaborazione.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `latent` | Il latent SeedVR2 codificato VAE da suddividere. Deve essere un tensore 5-D (B, C, T, H, W) con il numero di canali latent atteso per SeedVR2. | LATENT | Sì | - |
| `temporal_overlap` | Frame latent condivisi tra chunk adiacenti e sottoposti a crossfade al momento dell'unione; 0 significa nessuna sovrapposizione (predefinito: 0). La sovrapposizione effettiva è limitata a uno in meno rispetto al numero di frame latent del chunk. | INT | No | da 0 a 16384 |
| `chunking_mode` | `"manual"` usa esattamente `frames_per_chunk`; `"auto"` stima il chunk più grande che entra nella VRAM libera. | COMBO | Sì | `"auto"`<br>`"manual"` |

Quando `chunking_mode` è impostato su `"manual"`, diventa disponibile un parametro aggiuntivo:

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `frames_per_chunk` | Frame in pixel per chunk temporale (4n+1: 1, 5, 9, 13, 17, 21, ...); l'interfaccia avanza di 4 (predefinito: 21). | INT | Sì | da 1 a 16384 |

Nota: il parametro `frames_per_chunk` compare solo quando `chunking_mode` è impostato su `"manual"`. Il valore deve soddisfare la formula `(frames_per_chunk - 1) % 4 == 0`, quindi deve essere uno tra: 1, 5, 9, 13, 17, 21, ecc. Il latent in input deve essere 5-dimensionale e contenere il numero di canali latent atteso per SeedVR2; in caso contrario il nodo genera un errore. Se il numero totale di frame in pixel nel latent è uguale o inferiore alla dimensione del chunk scelta (o calcolata automaticamente), il nodo restituisce il latent originale come singolo chunk con sovrapposizione zero.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|-----------|
| `latents` | I chunk temporali in ordine sequenziale. Ogni chunk è un LATENT con lo stesso batch, canali, altezza e larghezza ma con dimensione temporale ridotta. | LATENT |
| `temporal_overlap` | La sovrapposizione effettiva in frame latent tra chunk adiacenti, per Merge SeedVR2 Latents. | INT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SeedVR2TemporalChunk/it.md)

---
**Source fingerprint (SHA-256):** `40af2b690f74555efbe38f4cf76825417f52735ce90296a9ad662f78cfe4c6bf`
