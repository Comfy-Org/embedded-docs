# Carica modello corpo SAM3D

Carica un modello SAM3D Body da un file di checkpoint archiviato nella cartella detection e lo prepara per l'uso nel rilevamento 3D del corpo. Il nodo carica i pesi del modello, rileva e applica le impostazioni di quantizzazione, se presenti, e incapsula il modello per la gestione automatica della memoria.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `model_file` | Il file di checkpoint SAM3D Body da caricare. Il file deve essere inserito nella cartella detection. Tutti i file modello disponibili nella cartella detection sono elencati come opzioni. | COMBO | Sì | Tutti i file modello disponibili nella cartella detection |

Nota: il file modello deve trovarsi nella cartella detection. Il caricamento non riesce e restituisce un errore se le chiavi del dizionario di stato del checkpoint non corrispondono alla struttura del modello SAM3D Body.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|-----------|
| `sam3d_body_model` | Il modello SAM3D Body caricato, incapsulato per la gestione automatica della memoria tra GPU e CPU. I pesi per il rilevamento delle mani vengono rimossi, quindi il modello è specializzato solo per il rilevamento del corpo. | SAM3D_BODY_MODEL |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SAM3DBody_Loader/it.md)

---
**Source fingerprint (SHA-256):** `c66a1639b5f19dafcfb1466d68908969a4d33ab0d01c30e8b31d1f1ce41fd782`
