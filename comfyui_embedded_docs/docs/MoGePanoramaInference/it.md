# MoGePanoramaInference

Questo nodo esegue la stima della profondità su immagini panoramiche equirettangolari. Suddivide il panorama in 12 viste prospettiche, esegue il modello di stima della profondità MoGe su ciascuna vista e unisce i risultati per vista in un'unica mappa di profondità che copre l'intero panorama. Le normali previste per vista e la scala metrica vengono ignorate, poiché le scale per vista non sarebbero allineate lungo le giunzioni di sovrapposizione.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `moge_model` | Il modello MoGe da utilizzare per l'inferenza. | MOGE_MODEL | Sì |  |
| `image` | Panorama equirettangolare (qualsiasi rapporto d'aspetto). Il nodo accetta solo una singola immagine; passare un batch di immagini genera un errore. Vengono utilizzati solo i primi 3 canali di colore (RGB). | IMAGE | Sì |  |
| `resolution_level` | Livello di dettaglio per vista (0 = più veloce, 9 = più dettagliato) (predefinito: 9). | INT | Sì | 0 a 9 |
| `split_resolution` | Risoluzione di ciascuna suddivisione prospettica (predefinito: 512). | INT | Sì | 256 a 1024 |
| `merge_resolution` | Risoluzione del lato lungo della mappa di distanza equirettangolare unita (predefinito: 1920). | INT | Sì | 256 a 8192 |
| `batch_size` | Viste per batch di inferenza (12 suddivisioni in totale) (predefinito: 4). | INT | Sì | 1 a 12 |
| `refine_steps` | Solo MoGe-3: passaggi di raffinamento volumetrico sparso sulla profondità prevista. Più passaggi rendono più nitidi dettagli fini e bordi con un costo approssimativamente lineare. 0 disabilita il raffinamento. Ignorato da MoGe-1 / MoGe-2 (predefinito: 3). | INT | Sì | 0 a 8 |

**Note:**

- L'input deve essere una singola immagine. Se `image` contiene più di un'immagine nel batch, il nodo genera un errore.
- `merge_resolution` viene considerato come dimensione massima del lato lungo. Se il panorama è più piccolo di questo valore, la mappa unita viene prodotta alla dimensione originale del panorama invece di essere ingrandita. Il risultato unito viene ridimensionato alla risoluzione originale del panorama prima di essere restituito.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `moge_geometry` | Un dizionario contenente la geometria stimata: `points` (nuvola di punti 3D), `depth` (mappa di profondità), `mask` (maschera delle aree valide) e `image` (l'immagine di input). | MOGE_GEOMETRY |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoGePanoramaInference/it.md)

---
**Source fingerprint (SHA-256):** `7f21452d035b2fe9d30b0cd15ddad10916439492b1d682a8b28f1a79e375df58`
