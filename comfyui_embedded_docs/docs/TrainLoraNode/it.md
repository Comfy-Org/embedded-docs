# Addestra LoRA

Il nodo TrainLoraNode crea e addestra un modello LoRA (Low-Rank Adaptation) su un modello di diffusione utilizzando i latenti e i dati di condizionamento forniti. Consente di mettere a punto un modello con parametri di addestramento personalizzati, ottimizzatori e funzioni di perdita. Il nodo restituisce in output i pesi LoRA addestrati, una mappa della cronologia della perdita e il numero totale di passi di addestramento completati.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `model` | Il modello su cui addestrare il LoRA. | MODEL | Sì | - |
| `latents` | I latenti da utilizzare per l'addestramento; fungono da dataset/input del modello. | LATENT | Sì | - |
| `positive` | Il condizionamento positivo da utilizzare per l'addestramento. | CONDITIONING | Sì | - |
| `batch_size` | La dimensione del batch da utilizzare per l'addestramento (predefinito: 1). | INT | Sì | 1-10000 |
| `grad_accumulation_steps` | Il numero di passi di accumulo del gradiente da utilizzare per l'addestramento (predefinito: 1). | INT | Sì | 1-1024 |
| `steps` | Il numero di passi per cui addestrare il LoRA (predefinito: 16). | INT | Sì | 1-100000 |
| `learning_rate` | Il tasso di apprendimento da utilizzare per l'addestramento (predefinito: 0.0005). | FLOAT | Sì | 0.0000001-1.0 |
| `rank` | Il rango dei livelli LoRA (predefinito: 8). | INT | Sì | 1-128 |
| `optimizer` | L'ottimizzatore da utilizzare per l'addestramento (predefinito: "AdamW"). | COMBO | Sì | "AdamW"<br>"Adam"<br>"SGD"<br>"RMSprop" |
| `loss_function` | La funzione di perdita da utilizzare per l'addestramento (predefinito: "MSE"). | COMBO | Sì | "MSE"<br>"L1"<br>"Huber"<br>"SmoothL1" |
| `seed` | Il seed da utilizzare per l'addestramento (usato nel generatore per l'inizializzazione dei pesi LoRA e il campionamento del rumore) (predefinito: 0). | INT | Sì | 0-18446744073709551615 |
| `training_dtype` | Il dtype da utilizzare per l'addestramento. 'none' conserva il dtype di calcolo nativo del modello invece di sovrascriverlo. Per i modelli fp16, GradScaler viene abilitato automaticamente (predefinito: "bf16"). | COMBO | Sì | "bf16"<br>"fp32"<br>"none" |
| `lora_dtype` | Il dtype da utilizzare per il LoRA (predefinito: "bf16"). | COMBO | Sì | "bf16"<br>"fp32" |
| `quantized_backward` | Quando si utilizza training_dtype 'none' e si addestra su un modello quantizzato, esegue il backward con matmul quantizzata quando abilitato (predefinito: False). | BOOLEAN | Sì | - |
| `algorithm` | L'algoritmo da utilizzare per l'addestramento. | COMBO | Sì | Più opzioni disponibili |
| `gradient_checkpointing` | Utilizza il gradient checkpointing per l'addestramento (predefinito: True). | BOOLEAN | Sì | - |
| `checkpoint_depth` | Livello di profondità per il gradient checkpointing (predefinito: 1). | INT | Sì | 1-5 |
| `offloading` | Scarica i pesi del modello sulla CPU durante l'addestramento per risparmiare memoria GPU (predefinito: False). | BOOLEAN | Sì | - |
| `existing_lora` | Il LoRA esistente a cui aggiungere. Impostare su None per un nuovo LoRA (predefinito: "[None]"). | COMBO | Sì | Più opzioni disponibili |
| `bucket_mode` | Abilita la modalità bucket di risoluzione. Quando abilitata, si aspetta latenti già suddivisi in bucket dal nodo ResolutionBucket (predefinito: False). | BOOLEAN | Sì | - |
| `bypass_mode` | Abilita la modalità bypass per l'addestramento. Quando è abilitata, gli adattatori vengono applicati tramite forward hook invece della modifica dei pesi. Utile per modelli quantizzati in cui i pesi non possono essere modificati direttamente (predefinito: False). | BOOLEAN | Sì | - |

**Nota:** Il numero di input di condizionamento positivo deve corrispondere al numero di immagini latenti. Se viene fornito un solo condizionamento positivo con più immagini, verrà ripetuto automaticamente per tutte le immagini.

**Nota su `training_dtype`:** Quando è impostato su "none", il dtype di calcolo nativo del modello viene preservato. Per i modelli fp16, GradScaler viene abilitato automaticamente per evitare underflow durante il calcolo del gradiente. Se anche `fp16_accumulation` è abilitato (tramite i flag `--fast`), questa combinazione può essere numericamente instabile e può causare valori NaN.

**Nota su `quantized_backward`:** Questo parametro è rilevante solo quando `training_dtype` è impostato su "none" e il modello è un modello quantizzato. Abilita la moltiplicazione di matrici quantizzata durante il passaggio backward.

**Nota su `bypass_mode`:** Quando è abilitato, gli adattatori vengono applicati tramite forward hook invece di modificare direttamente i pesi del modello. Questo è particolarmente utile per i modelli quantizzati in cui i pesi non possono essere modificati direttamente.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `lora` | I pesi LoRA addestrati che possono essere salvati o applicati ad altri modelli. | LORA_MODEL |
| `loss_map` | Un dizionario contenente i valori della perdita di addestramento nel tempo. | LOSS_MAP |
| `steps` | Il numero totale di passi di addestramento completati (inclusi eventuali passi precedenti dal LoRA esistente). | INT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TrainLoraNode/it.md)

---
**Source fingerprint (SHA-256):** `39e88045270d36855442024b62d6a225a58b34842f45ac04fbc6c1ade6768a76`
