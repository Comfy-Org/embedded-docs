# LTXVAddGuide

Il nodo LTXVAddGuide codifica immagini o video di input tramite un encoder VAE e li aggiunge come fotogrammi chiave di guida a una sequenza video latente. Aggiorna sia il condizionamento positivo sia quello negativo e restituisce il latente modificato, con opzioni per impostare il frame iniziale, l'intensità del condizionamento, una maschera di attenzione opzionale e parametri IC-LoRA opzionali.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `positive` | Input di condizionamento positivo da modificare con la guida dei fotogrammi chiave. | CONDITIONING | Sì | - |
| `negative` | Input di condizionamento negativo da modificare con la guida dei fotogrammi chiave. | CONDITIONING | Sì | - |
| `vae` | Modello VAE utilizzato per codificare i frame immagine/video di input. | VAE | Sì | - |
| `latent` | Sequenza latente di input che riceverà i frame di condizionamento. | LATENT | Sì | - |
| `image` | Immagine o video su cui condizionare il video latente. Deve avere 8*n + 1 frame. Se il video non ha 8*n + 1 frame, verrà ritagliato ai più vicini 8*n + 1 frame. | IMAGE | Sì | - |
| `frame_idx` | Indice del frame da cui iniziare il condizionamento. Per immagini a frame singolo o video con 1-8 frame, qualsiasi valore di `frame_idx` è accettabile. Per video con 9+ frame, `frame_idx` deve essere divisibile per 8, altrimenti verrà arrotondato per difetto al multiplo di 8 più vicino. I valori negativi vengono contati dalla fine del video. Predefinito: 0. | INT | Sì | da -9999 a 9999 |
| `strength` | Intensità dell'influenza del condizionamento, dove 1.0 applica il condizionamento completo e 0.0 non applica alcun condizionamento. Predefinito: 1.0. | FLOAT | Sì | da 0.0 a 10.0 |
| `attention_mask` | Maschera spaziale opzionale nello spazio dei pixel. Controlla l'influenza del condizionamento per regione tramite self-attention, moltiplicata per `strength`. | MASK | No | - |
| `iclora_parameters` | Parametri IC-LoRA opzionali da un nodo Get IC-LoRA Parameters. Usati per regolare l'elaborazione della guida come richiesto da certi IC-LoRA (ad es., quelli con un `reference_downscale_factor` > 1). Quando concatenati, ciascun LTXVAddGuide usa solo i parametri a esso collegati. | IC_LORA_PARAMETERS | No | - |

**Nota:** L'immagine/video di input deve avere un numero di frame che segua il pattern 8*n + 1 (ad es., 1, 9, 17, 25 frame). Se l'input supera questo pattern, verrà automaticamente ritagliato al numero di frame valido più vicino.

**Nota su `iclora_parameters`:** Quando si usano parametri IC-LoRA con un `reference_downscale_factor` maggiore di 1, le dimensioni spaziali del latente (larghezza e altezza) devono essere divisibili per quel fattore. Il nodo genererà un errore se questa condizione non è soddisfatta.

**Nota:** I frame guida codificati devono rientrare nella sequenza latente nella posizione del frame selezionata. Se i frame condizionati superano la lunghezza della sequenza latente, il nodo genera un errore.

**Nota:** L'aggiunta di una guida a un latente che combina canali audio e video non è supportata e genererà un errore.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `positive` | Condizionamento positivo aggiornato con le informazioni di guida dei fotogrammi chiave. | CONDITIONING |
| `negative` | Condizionamento negativo aggiornato con le informazioni di guida dei fotogrammi chiave. | CONDITIONING |
| `latent` | Sequenza latente con frame di condizionamento incorporati e maschera del rumore aggiornata. | LATENT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVAddGuide/it.md)

---
**Source fingerprint (SHA-256):** `031bc9030dafed85b5ff1cbceae36234e9d5f77f7f4b040267067ecd16a27929`
