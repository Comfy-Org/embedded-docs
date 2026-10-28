# MiniMax H3 Latent Upscale With Model

MiniMax H3 Latent Upscale With Model ridimensiona la parte video di un latente MiniMax H3 a una larghezza e un'altezza target con un modello di upscale latente. Il latente audio rimane intatto, quindi la clip mantiene il suo suono e non è necessario alcun ricampionamento. Usalo dopo il campionamento di MiniMax H3 e prima della decodifica VAE H3 quando la clip deve risultare più grande.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `model` | Modello di upscale latente, solitamente caricato con Load Latent Upscale Model. Deve essere un upscaler latente 3D-conv di MiniMax H3. | LATENT_UPSCALE_MODEL | Sì | - |
| `samples` | Latente MiniMax H3 da ridimensionare. Un latente annidato mantiene la sua parte audio così com'è. | LATENT | Sì | - |
| `width` | Larghezza video target in pixel. Il latente viene ridimensionato a `width / 16` colonne, quindi il valore viene arrotondato per difetto a un multiplo di 16. (predefinito: 2560) | INT | Sì | 32 a 16384 (passo: 32) |
| `height` | Altezza video target in pixel, anch'essa arrotondata per difetto a un multiplo di 16. (predefinito: 1440) | INT | Sì | 32 a 16384 (passo: 32) |

Quando la dimensione richiesta corrisponde già al latente, il latente di input viene restituito invariato. Il latente di output non contiene `noise_mask`, quindi un latente parzialmente mascherato perde la sua maschera. La rete esegue le sue convoluzioni 3D in lastre temporali, il che mantiene l'uso della memoria su clip lunghe vicino a quello di una singola lastra.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `LATENT` | Il latente ridimensionato, pronto per la decodifica VAE H3. | LATENT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MiniMaxH3LatentUpscaleWithModel/it.md)

---
**Source fingerprint (SHA-256):** `cd659baace5a21620033dd3470b854cccbada01d09545a2f61273b949c3a004b`
