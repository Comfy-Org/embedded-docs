# Decodifica struttura VAE Trellis2

Questo nodo converte i campioni latenti della struttura Trellis in una griglia voxel 3D utilizzando il decodificatore di struttura di un VAE. Legge solo i primi 8 canali del latente, ricostruisce l'occupazione dei voxel e regola la risoluzione di output a 32 o 64 come richiesto.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `samples` | La rappresentazione latente della struttura da decodificare. Solo i primi 8 canali del latente vengono utilizzati per la decodifica. | LATENT | Sì | - |
| `vae` | Il VAE il cui decodificatore di struttura converte il latente in una griglia voxel. La decodifica viene eseguita in batch. | VAE | Sì | - |
| `resolution` | La risoluzione spaziale target della griglia voxel di output (predefinito: "32"). Se la griglia decodificata ha una risoluzione diversa, viene sottocampionata per corrispondere. | COMBO | Sì | "32"<br>"64" |

Nota: quando la risoluzione della griglia voxel decodificata differisce dalla `resolution` selezionata, la griglia viene sottocampionata utilizzando il max pooling 3D alla dimensione richiesta.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `voxel` | Una griglia di occupazione voxel binaria come tensore float con forma [batch, depth, height, width]. I valori sono 1.0 per i voxel occupati e 0.0 per i voxel vuoti. | VOXEL |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VaeDecodeStructureTrellis2/it.md)

---
**Source fingerprint (SHA-256):** `37764ef7351b3619d4cddb57b11d9a0da24dadeedc0fc0f70d089038d37e03b0`
