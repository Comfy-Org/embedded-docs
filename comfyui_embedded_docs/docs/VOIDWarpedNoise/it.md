# VOIDWarpedNoise

Genera rumore correlato temporalmente per il secondo passaggio del processo di raffinamento video VOID. Prende il video di output del Pass 1 e applica un warp al rumore gaussiano lungo i vettori di flusso ottico, affinché il rumore si muova in modo coerente con il contenuto video. Il rumore con warp risultante viene utilizzato come latente iniziale per il Pass 2, migliorando la coerenza temporale nell'output finale.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `optical_flow` | Modello di flusso ottico da OpticalFlowLoader (RAFT-large). | OPTICAL_FLOW | Sì | - |
| `video` | Fotogrammi video di output del Pass 1 [T, H, W, 3]. | IMAGE | Sì | - |
| `width` | Larghezza target in pixel (predefinito: 672). Il video di input viene ridimensionato a questa larghezza prima che venga generato il rumore, e la larghezza latente è derivata come width ÷ 8. | INT | Sì | da 16 a MAX_RESOLUTION (passo 8) |
| `height` | Altezza target in pixel (predefinito: 384). Il video di input viene ridimensionato a questa altezza prima che venga generato il rumore, e l'altezza latente è derivata come height ÷ 8. | INT | Sì | da 16 a MAX_RESOLUTION (passo 8) |
| `length` | Numero di fotogrammi in pixel. Arrotondato per difetto per rendere latent_t pari (requisito patch_size_t=2), ad es. da 49 a 45 (predefinito: 45). | INT | Sì | da 1 a MAX_RESOLUTION (passo 1) |
| `batch_size` | Numero di sequenze identiche di rumore con warp da produrre (predefinito: 1). Il rumore generato viene ripetuto questo numero di volte lungo la dimensione batch. | INT | Sì | da 1 a 64 |

**Nota sul parametro `length`:** Il valore di `length` viene automaticamente arrotondato per difetto al valore più vicino che produce una dimensione `latent_t` pari, come richiesto dal vincolo `patch_size_t=2` del modello CogVideoX-Fun-V1.5 (ad esempio, 49 diventa 45). Il nodo registra un avviso quando avviene questo arrotondamento. I fotogrammi oltre il `length` modificato vengono ignorati e il rumore viene ricampionato al numero di fotogrammi latenti risultante.

**Nota su `width` e `height`:** Questi valori vengono usati sia per ridimensionare i fotogrammi video in ingresso (bilineare, ritaglio centrale) sia per determinare la risoluzione latente finale (divisa per 8). Se il rumore generato non corrisponde alla dimensione latente richiesta, viene ridimensionato per adattarsi.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `warped_noise` | Un tensore 5D (B, C, T, H, W) contenente rumore gaussiano con warp da flusso ottico, pronto per l'uso come latente iniziale nel Pass 2 di VOID. | LATENT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VOIDWarpedNoise/it.md)

---
**Source fingerprint (SHA-256):** `f46b0a73b09a5d2d0bc25676f9571563c6bb8bad8d835e7564ac092c72136107`
