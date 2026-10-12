# MoGeInference

Esegui MoGe sulle immagini per stimare profondità e geometria. Questo nodo elabora un'immagine di input tramite il modello MoGe per generare una nuvola di punti 3D, una mappa di profondità, i parametri intrinseci della camera, una maschera e le normali di superficie.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `moge_model` | Il modello MoGe da usare per l'inferenza. | MOGE_MODEL | Sì | N/A |
| `image` | L'immagine di input per la stima di profondità e geometria. Vengono usati solo i primi tre canali di colore (RGB). | IMAGE | Sì | N/A |
| `resolution_level` | Controlla la risoluzione di elaborazione. 0 = più veloce, 9 = maggior dettaglio. (predefinito: 9) | INT | Sì | 0 to 9 |
| `fov_x_degrees` | (Avanzato) Campo visivo orizzontale della camera sorgente. Imposta la lunghezza focale usata per retroproiettare la mappa di profondità in 3D. 0 = recupero automatico dai punti previsti. (predefinito: 0.0) | FLOAT | Sì | 0.0 to 170.0 (step 0.1) |
| `batch_size` | Immagini per chiamata di inferenza. Riduci in caso di OOM su un video lungo / set di immagini. (predefinito: 4) | INT | Sì | 1 to 64 |
| `force_projection` | (Avanzato) Forza la proiezione dei punti previsti. (predefinito: True) | BOOLEAN | Sì | True/False |
| `apply_mask` | (Avanzato) Imposta i pixel mascherati (cielo / non validi) a inf nei punti e nella profondità, così la generazione della mesh li esclude. Disabilita per mantenere la geometria prevista grezza ovunque; la maschera viene comunque restituita separatamente. (predefinito: True) | BOOLEAN | Sì | True/False |
| `refine_steps` | (Avanzato) Solo MoGe-3: passaggi di raffinamento volumetrico sparso sulla profondità prevista. Più passaggi affinano dettagli fini e bordi con un costo approssimativamente lineare. 0 disabilita il raffinamento. Ignorato da MoGe-1 / MoGe-2. (predefinito: 3) | INT | Sì | 0 to 8 |

Nota: quando l'`image` di input contiene più frame di `batch_size`, il nodo li elabora in più chiamate di inferenza e combina i risultati in un'unica geometria di output.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `moge_geometry` | Un dizionario contenente la geometria stimata. Include l'`image` originale e può contenere `points` (nuvola di punti 3D), `depth` (mappa di profondità), `intrinsics` (matrice dei parametri intrinseci della camera), `mask` (maschera che identifica i pixel validi) e `normal` (normali di superficie). | MOGE_GEOMETRY |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoGeInference/it.md)

---
**Source fingerprint (SHA-256):** `10f3399d9b6bc4ff8a940c940f538a8ec8f38a15e7d65f162499c5ab264fad65`
