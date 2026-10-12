# StableCascade_EmptyLatentImage

Il nodo StableCascade_EmptyLatentImage crea tensori latenti vuoti per i modelli Stable Cascade. Genera due rappresentazioni latenti separate - una per lo stage C e un'altra per lo stage B - con dimensioni calcolate dalla risoluzione di input e dalle impostazioni di compressione. Questo nodo fornisce un punto di partenza per la pipeline di generazione di Stable Cascade.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `width` | La larghezza dell'immagine di output in pixel (predefinito: 1024, passo: 8) | INT | Sì | da 256 a MAX_RESOLUTION |
| `height` | L'altezza dell'immagine di output in pixel (predefinito: 1024, passo: 8) | INT | Sì | da 256 a MAX_RESOLUTION |
| `compression` | Il fattore di compressione che determina le dimensioni latenti per lo stage C (predefinito: 42, passo: 1). Questo è un parametro avanzato. | INT | Sì | da 4 a 128 |
| `batch_size` | Il numero di campioni latenti da generare in un batch (predefinito: 1) | INT | Sì | da 1 a 4096 |

Nota: il valore di `compression` controlla la dimensione latente dello stage C: la sua altezza e la sua larghezza si ottengono dividendo `height` e `width` di input per `compression`. Il latente dello stage B usa sempre una compressione fissa di 4.

## Output

| Nome dell'output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `stage_c` | Il tensore latente dello stage C con dimensioni [batch_size, 16, height//compression, width//compression] | LATENT |
| `stage_b` | Il tensore latente dello stage B con dimensioni [batch_size, 4, height//4, width//4] | LATENT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableCascade_EmptyLatentImage/it.md)

---
**Source fingerprint (SHA-256):** `f336f87d0ec14b3716efda2cfaa194b1f80707d64821bb56ade7d88d9bd5b53f`
