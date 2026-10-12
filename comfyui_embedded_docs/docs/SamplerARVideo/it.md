# Sampler AR Video

Il nodo Sampler AR Video fornisce un metodo di campionamento specializzato per modelli video autoregressivi, come quelli che utilizzano tecniche Causal Forcing o Self-Forcing. Gestisce tutti i parametri relativi al ciclo autoregressivo (AR) direttamente all'interno del workflow, rendendo semplice configurare il modo in cui il modello genera i fotogrammi video un passo alla volta.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `num_frame_per_block` | Fotogrammi per blocco autoregressivo. Un valore di 1 indica che il modello genera un fotogramma alla volta (framewise), mentre un valore di 3 indica che ne genera tre insieme (chunkwise). Questa impostazione deve corrispondere alla modalità di addestramento del checkpoint. Predefinito: 1. | INT | Sì | Da 1 a 64 |

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `SAMPLER` | Un oggetto sampler configurato che utilizza la funzione di campionamento "ar_video" con i parametri autoregressivi specificati. | SAMPLER |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerARVideo/it.md)

---
**Source fingerprint (SHA-256):** `9ec72f52f5b77746f1587e64966bfa6cfd80ce8bb40a4fcb267f5197d09189fc`
