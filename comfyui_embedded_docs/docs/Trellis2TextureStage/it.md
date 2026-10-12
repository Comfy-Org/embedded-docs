# Trellis2TextureStage

Questo nodo imposta il passaggio di campionamento dello stadio texture per la generazione Trellis2. Legge il layout delle coordinate e il latent della forma per voxel dal latent della forma in ingresso, costruisce un latent sparso vuoto con 32 canali sullo stesso layout delle coordinate e allega i metadati richiesti dello stadio texture al condizionamento.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `positive` | Il condizionamento positivo utilizzato per la passata di generazione della texture. A esso vengono allegati i metadati dello stadio texture. | CONDITIONING | Sì | - |
| `negative` | Il condizionamento negativo utilizzato per la passata di generazione della texture. A esso vengono allegati i metadati dello stadio texture. | CONDITIONING | Sì | - |
| `shape_latent` | Il dizionario latent prodotto da Trellis2ShapeStage o Trellis2UpsampleStage. Deve contenere `coords` (il layout delle coordinate, shape [N, 4]) e `samples` (il latent della forma per voxel); `coord_resolution` e `model_frame` sono opzionali. | LATENT | Sì | - |

Note:
- `shape_latent` deve essere l'output di Trellis2ShapeStage o Trellis2UpsampleStage; fornisce il layout delle coordinate e il latent della forma per voxel utilizzati dalla passata texture.
- Il layout delle coordinate viene convalidato: gli id di batch nella prima colonna di `coords` devono essere non negativi e contigui, e il numero totale di righe deve corrispondere ai conteggi delle coordinate.
- Il latent della forma viene accettato sia come tensore sparso 4D (che viene appiattito insieme alle sue coordinate) sia già in forma appiattita.
- Quando `positive` contiene un pacchetto di feature di proiezione (condizionamento Pixal3D) e `shape_latent` include `coord_resolution`, le feature di proiezione alla risoluzione texture di 1024 vengono calcolate e allegate al condizionamento.
- Il frame del modello viene letto da `shape_latent`; quando è assente, il valore predefinito è `"y_up"` se sono presenti feature di proiezione e `"z_up"` in caso contrario.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `positive` | Il condizionamento positivo con i metadati dello stadio texture allegati (modalità di generazione, coordinate, conteggi delle coordinate, latent della forma, frame del modello e feature di proiezione quando applicabili). | CONDITIONING |
| `negative` | Il condizionamento negativo con gli stessi metadati dello stadio texture allegati. | CONDITIONING |
| `latent` | Un nuovo latent sparso vuoto con 32 canali sullo stesso layout di coordinate del latent della forma in ingresso. Il suo dizionario include `samples`, `type` ("trellis2"), `coords`, `coord_counts` e `model_frame`; `coord_resolution` è incluso quando disponibile. | LATENT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Trellis2TextureStage/it.md)

---
**Source fingerprint (SHA-256):** `ae612021af7c74cd09206d905e7b800fa48367a22daf9b0335b444c854a78b1e`
