# SelfAttentionGuidance

Il nodo Self-Attention Guidance applica una guida ai modelli di diffusione modificando il meccanismo di attenzione durante il processo di campionamento. Cattura i punteggi di attenzione dai passaggi di denoising incondizionato e li usa per creare mappe di guida sfocate che influenzano l'output finale. Questa tecnica aiuta a guidare il processo di generazione sfruttando i pattern di attenzione del modello stesso.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model` | Il modello di diffusione a cui applicare la guida self-attention | MODEL | Sì | - |
| `scale` | L'intensità dell'effetto della guida self-attention (predefinito: 0.5) | FLOAT | No | da -2.0 a 5.0 |
| `blur_sigma` | La quantità di sfocatura applicata per creare la mappa di guida (predefinito: 2.0) | FLOAT | No | da 0.0 a 10.0 |

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `model` | Il modello modificato con la guida self-attention applicata | MODEL |

**Nota:** Questo nodo è attualmente sperimentale e presenta limitazioni con i batch suddivisi in blocchi. Può salvare i punteggi di attenzione solo da una chiamata UNet e potrebbe non funzionare correttamente con dimensioni di batch maggiori.

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SelfAttentionGuidance/it.md)

---
**Source fingerprint (SHA-256):** `ab8f7a0cf19c85f8e77b2d6b380c0224a407a900a42341de7503f5394a3216fb`
