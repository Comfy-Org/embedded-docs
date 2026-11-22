# PatchModelAddDownscale (Kohya Deep Shrink)

PatchModelAddDownscale (Kohya Deep Shrink) applica la tecnica Kohya Deep Shrink a un modello riducendo le feature intermedie a un blocco scelto e poi riportandole alla loro dimensione originale. La riduzione avviene solo durante una parte selezionata del processo di denoising, il che può ridurre il costo di elaborazione mantenendo il risultato finale vicino all'originale.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `modello` | Il modello a cui applicare la patch di ridimensionamento verso il basso | MODEL | Sì | - |
| `numero_blocco` | Il numero specifico del blocco in cui verrà applicato il ridimensionamento verso il basso (predefinito: 3) | INT | Sì | 1-32 |
| `fattore_riduzione` | Il fattore con cui ridimensionare verso il basso le feature (predefinito: 2.0) | FLOAT | Sì | 0.1-9.0 |
| `percentuale_inizio` | Il punto di inizio nel processo di denoising in cui inizia il ridimensionamento verso il basso (predefinito: 0.0) | FLOAT | Sì | 0.0-1.0 |
| `percentuale_fine` | Il punto di fine nel processo di denoising in cui termina il ridimensionamento verso il basso (predefinito: 0.35) | FLOAT | Sì | 0.0-1.0 |
| `riduci_dopo_skip` | Indica se applicare il ridimensionamento verso il basso dopo le connessioni skip (predefinito: True) | BOOLEAN | Sì | - |
| `metodo_riduzione` | Il metodo di interpolazione utilizzato per le operazioni di ridimensionamento verso il basso (predefinito: "bicubic") | COMBO | Sì | "bicubic"<br>"nearest-exact"<br>"bilinear"<br>"area"<br>"bislerp" |
| `metodo_ingrandimento` | Il metodo di interpolazione utilizzato per le operazioni di ridimensionamento verso l'alto (predefinito: "bicubic") | COMBO | Sì | "bicubic"<br>"nearest-exact"<br>"bilinear"<br>"area"<br>"bislerp" |

La patch di ridimensionamento verso il basso viene applicata solo quando il passo di denoising corrente rientra nell'intervallo definito da `start_percent` e `end_percent`, e solo nel blocco selezionato da `block_number`. Quando `downscale_after_skip` è abilitato, la patch viene applicata dopo la connessione skip; quando è disabilitato, viene applicata prima della connessione skip. Le feature vengono successivamente riportate alla loro dimensione originale, ma solo quando la dimensione corrente delle feature non corrisponde più alla dimensione registrata prima del ridimensionamento verso il basso.

I parametri `block_number`, `start_percent`, `end_percent` e `downscale_after_skip` sono contrassegnati come opzioni avanzate nell'interfaccia del nodo.

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `model` | Il modello modificato con la patch di ridimensionamento verso il basso applicata | MODEL |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PatchModelAddDownscale/it.md)

---
**Source fingerprint (SHA-256):** `aa9434a521ab585b290a3bd8db804469bd3bb02103a0d830b6be6eb8e8c26a5e`
