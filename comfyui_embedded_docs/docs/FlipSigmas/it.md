# Inverti Sigmas

Il nodo `FlipSigmas` è progettato per manipolare la sequenza di valori sigma utilizzata nei modelli di diffusione, invertendone l'ordine e assicurando che il primo valore sia diverso da zero se originariamente zero. Questa operazione è cruciale per adattare i livelli di rumore in ordine inverso, facilitando il processo di generazione nei modelli che operano riducendo gradualmente il rumore dai dati.

## Input

| Parametro | Descrizione | Tipo di dato |
| --- | --- | --- |
| `sigmas` | Il parametro `sigmas` rappresenta la sequenza di valori sigma da invertire. Questa sequenza è cruciale per controllare i livelli di rumore applicati durante il processo di diffusione, e invertirla è essenziale per il processo di generazione inversa. | `SIGMAS` |

## Output

| Parametro | Descrizione | Tipo di dato |
| --- | --- | --- |
| `sigmas` | L'output è la sequenza modificata di valori sigma, invertita e regolata per assicurare che il primo valore sia diverso da zero se originariamente zero, pronta per l'uso nelle successive operazioni del modello di diffusione. | `SIGMAS` |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FlipSigmas/it.md)
