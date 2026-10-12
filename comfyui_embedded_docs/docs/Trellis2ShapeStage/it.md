# Trellis2ShapeStage

Questo nodo configura il primo passaggio di campionamento per la generazione della forma della pipeline Trellis2. Prende il voxel a struttura densa prodotto da VaeDecodeStructureTrellis2, estrae le coordinate sparse dei voxel riempiti, crea un latent sparso vuoto e allega i metadati di campionamento al condizionamento in modo che il modello possa leggerli durante il campionamento. Per il secondo passaggio della forma dopo l'upsampling, usare invece Trellis2UpsampleStage, che combina la cascata e la configurazione dello stadio del secondo passaggio.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `positive` | Il condizionamento positivo da preparare per lo stadio della forma. Può essere un condizionamento Trellis2 standard o un condizionamento Pixal3D che fornisce un pacchetto di feature di proiezione; quando sono presenti feature di proiezione, vengono calcolate per lo stadio selezionato e allegate al condizionamento di output. | CONDITIONING | Sì | Qualsiasi condizionamento Trellis2 o Pixal3D |
| `negative` | Il condizionamento negativo da preparare per lo stadio della forma. Gli stessi metadati dello stadio della forma vengono allegati anche a esso, come per il condizionamento positivo. | CONDITIONING | Sì | Qualsiasi condizionamento Trellis2 o Pixal3D |
| `voxel` | Voxel a struttura densa da VaeDecodeStructureTrellis2. | VOXEL | Sì | Qualsiasi griglia di voxel; la risoluzione della griglia (voxel per asse) seleziona lo stadio della pipeline |

### Note

- La risoluzione della griglia di voxel seleziona lo stadio della pipeline: una risoluzione pari o inferiore a 32 utilizza la modalità `shape_generation_512` con lo stadio `shape_512`; una risoluzione superiore a 32 utilizza la modalità `shape_generation` con lo stadio `shape_1024`.
- Il voxel deve contenere almeno un voxel riempito; un voxel vuoto genera un errore. Gli indici del batch derivati dal voxel devono essere non negativi e contigui.
- Quando il condizionamento `positive` contiene un `proj_feat_pack` (come fornito dal condizionamento Pixal3D), le feature di proiezione vengono calcolate per lo stadio selezionato e il model frame del latent di output viene impostato su `y_up`. In caso contrario, non vengono allegate feature di proiezione e il model frame viene impostato su `z_up`.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `positive` | Il condizionamento positivo con i metadati dello stadio della forma allegati: modalità di generazione, coordinate sparse, conteggi delle coordinate per batch e feature di proiezione quando il condizionamento di origine le fornisce. | CONDITIONING |
| `negative` | Il condizionamento negativo con gli stessi metadati dello stadio della forma allegati. | CONDITIONING |
| `latent` | Un tensore latent sparso vuoto (forma: dimensione batch, 32, numero di token, 1) insieme alle coordinate sparse estratte, ai conteggi delle coordinate per batch, alla risoluzione delle coordinate, al marcatore di tipo `trellis2` e all'orientamento del model frame. | LATENT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Trellis2ShapeStage/it.md)

---
**Source fingerprint (SHA-256):** `7dbee8a5b6ef7111f07def4dbe1cc4908533e00ffcb775f5a284099360c7eed3`
