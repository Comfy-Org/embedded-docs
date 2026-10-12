# Struttura latent Trellis2 vuota

Questo nodo crea una struttura latente vuota per il modello Trellis2, in cui tutti i valori sono impostati a zero. Produce un tensore latente 3D vuoto con 32 canali a una risoluzione di 16×16×16, dimensionato per il numero specificato di elementi nel batch.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `batch_size` | Il numero di immagini latenti nel batch (predefinito: 1). | INT | Sì | 1 to 4096 |

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|-------------|
| `LATENT` | Una struttura latente Trellis2 vuota. I campioni sono un tensore riempito di zeri con la forma (batch_size, 32, 16, 16, 16), e il tipo di latente è impostato su "trellis2". | LATENT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyTrellis2LatentStructure/it.md)

---
**Source fingerprint (SHA-256):** `a551f0e05e58b025df03a3babee36f57fd900b5e02926fbdbd67a512ebead078`
