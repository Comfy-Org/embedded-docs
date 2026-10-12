# Decodifica texture VAE Trellis2

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `samples` | Il latente di texture da decodificare. Contiene le feature dei campioni e coordinate sparse, e può includere metadati opzionali come conteggi delle coordinate (`coord_counts`), frame del modello (`model_frame`, predefinito: "y_up") e risoluzione delle coordinate (`coord_resolution`). | LATENT | Sì | — |
| `vae` | Il VAE Trellis2 usato per decodificare il latente di texture in colori voxel. | VAE | Sì | — |
| `shape_subdivides` | Informazioni sulla forma usate per guidare una ricostruzione più dettagliata durante la decodifica. Aiuta a preservare la coerenza della struttura a risoluzioni più elevate. | SHAPE_SUBDIVIDES | Sì | — |

Nota: quando il latente `samples` include `coord_counts`, i conteggi devono essere non negativi, il loro totale deve corrispondere al numero di righe delle coordinate, e ogni batch deve contenere esattamente il numero previsto di righe; in caso contrario, il nodo genera un errore. Se il `model_frame` del latente è "z_up", le coordinate voxel decodificate vengono rimappate in Y-up in modo che si allineino ai vertici della mesh. Quando viene fornito `coord_resolution`, la risoluzione della texture di output è quel valore moltiplicato per 16. Altrimenti viene inferita dalla coordinata voxel più grande più uno, arrotondata per eccesso a uno tra 256, 512, 1024, 1536 o 2048; se il valore necessario supera 2048, viene usato quel valore più grande. Se non sono disponibili coordinate, la risoluzione predefinita è 1024.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `voxel_colors` | Dati voxel decodificati contenenti coordinate, feature di colore e risoluzione della texture. Ogni voxel ha 6 canali di colore: colore di base (RGB), metallic, roughness e alpha, tutti nell'intervallo [0, 1]. I consumatori di vertex color come PaintMesh usano i primi 3 canali. | VOXEL |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VaeDecodeTextureTrellis/it.md)

---
**Source fingerprint (SHA-256):** `952ea7d7a0147519392bebe352a0da731462db278c8640fa527aa5b6f64e4aa7`
