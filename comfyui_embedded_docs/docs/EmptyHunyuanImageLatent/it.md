# Latent immagine Hunyuan vuoto

Il nodo EmptyHunyuanImageLatent crea uno spazio latente vuoto, composto interamente da zeri, per i modelli di generazione immagini Hunyuan. Produce un latente iniziale vuoto usando la larghezza, l'altezza e la dimensione batch fornite, che può poi essere passato ai nodi a valle nel workflow. Il tensore latente contiene 64 canali e ogni dimensione spaziale è pari alla corrispondente dimensione in pixel divisa per 32.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `width` | La larghezza dell'immagine latente generata in pixel (predefinito: 2048, passo: 32) | INT | Sì | 64 a MAX_RESOLUTION |
| `height` | L'altezza dell'immagine latente generata in pixel (predefinito: 2048, passo: 32) | INT | Sì | 64 a MAX_RESOLUTION |
| `batch_size` | Il numero di campioni latenti da generare in un batch (predefinito: 1) | INT | Sì | 1 a 4096 |

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|-----------|
| `LATENT` | Un tensore latente vuoto con 64 canali e dimensioni pari ad altezza ÷ 32 per larghezza ÷ 32, pronto per l'elaborazione delle immagini Hunyuan | LATENT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyHunyuanImageLatent/it.md)

---
**Source fingerprint (SHA-256):** `31fc10d43c224810709870cf40256b6fccd4743445ea9d98d148d443bc591d7a`
