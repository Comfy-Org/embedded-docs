# VOIDInpaintConditioning

Il nodo VOIDInpaintConditioning prepara i dati di condizionamento necessari per l'inpainting con i modelli CogVideoX. Prende un video sorgente e una quadmask preprocessata, li codifica tramite il VAE e li combina in un segnale di condizionamento a 32 canali (16 canali dalla maschera + 16 canali dal video mascherato) che il modello usa per riempire le aree mascherate.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `positive` | Il condizionamento positivo da aumentare con le informazioni latenti di inpainting | CONDITIONING | Sì | - |
| `negative` | Il condizionamento negativo da aumentare con le informazioni latenti di inpainting | CONDITIONING | Sì | - |
| `vae` | Il modello VAE usato per codificare la maschera e il video mascherato nello spazio latente | VAE | Sì | - |
| `video` | Fotogrammi del video sorgente [T, H, W, 3] | IMAGE | Sì | - |
| `quadmask` | Quadmask preprocessata da VOIDQuadmaskPreprocess [T, H, W] | MASK | Sì | - |
| `width` | La larghezza a cui ridimensionare il video e la maschera (predefinito: 672) | INT | Sì | 16 a MAX_RESOLUTION (passo: 8) |
| `height` | L'altezza a cui ridimensionare il video e la maschera (predefinito: 384) | INT | Sì | 16 a MAX_RESOLUTION (passo: 8) |
| `length` | Numero di fotogrammi pixel da elaborare. Per CogVideoX-Fun-V1.5 (patch_size_t=2), latent_t deve essere pari — le lunghezze che producono un latent_t dispari vengono arrotondate per difetto (ad es. 49 → 45) (predefinito: 45) | INT | Sì | 1 a MAX_RESOLUTION (passo: 1) |
| `batch_size` | La dimensione del batch per il latente di rumore in output (predefinito: 1) | INT | Sì | 1 a 64 |

**Nota:** Poiché CogVideoX-Fun-V1.5 usa `patch_size_t=2`, il latente codificato deve avere una dimensione temporale pari. Se `length` producesse un `latent_t` dispari, il nodo lo arrotonda automaticamente per difetto al valore valido più vicino e registra un avviso. Usare un `latent_t` dispari corrompe l'ultimo fotogramma tramite padding circolare, il che può causare jitter visibile o soggetti che scompaiono vicino alla fine del video decodificato.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `positive` | Il condizionamento positivo con le informazioni latenti di inpainting aggiunte | CONDITIONING |
| `negative` | Il condizionamento negativo con le informazioni latenti di inpainting aggiunte | CONDITIONING |
| `latent` | Un tensore latente di rumore riempito di zeri con forma [batch_size, 16, latent_t, latent_h, latent_w] | LATENT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VOIDInpaintConditioning/it.md)

---
**Source fingerprint (SHA-256):** `885e462c0f17a3e9610146a05ba3b9c879db0112d3961c95a83f63ba2cd511f1`
