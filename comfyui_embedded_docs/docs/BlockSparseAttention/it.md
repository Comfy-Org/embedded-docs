# Attenzione sparsa del modello

Il nodo **Block Sparse Attention** modifica un modello affinché i suoi layer di attenzione si concentrino solo sulle parti più rilevanti dell'input invece che su tutto contemporaneamente, riducendo il lavoro di calcolo necessario per le sequenze lunghe. I risparmi aumentano con la lunghezza della sequenza, poiché le sequenze brevi sono di solito più veloci con l'attenzione normale (densa).

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `model` | Il modello a cui applicare la patch. | MODEL | Sì | N/A |
| `selection` | Metodo utilizzato per scegliere i blocchi chiave per l'attenzione completa a livello di token (visualizzato come `method`). <br>`sol-attn`: Sparsifying Online Attention utilizza una soglia adattiva senza addestramento per ogni testa di attenzione e blocco query.<br>`sla`: Sparse-Linear Attention mantiene una percentuale fissa dei blocchi chiave con punteggio più alto; usare solo con pesi del modello addestrati per questo pattern.<br>`vsa`: Video Sparse Attention (FastVideo) utilizza il tiling 3D in cubetti video e un ramo di attenzione grossolana appreso; richiede pesi del modello FastH3. | DYNAMIC_COMBO | Sì | `"sol-attn"`<br>`"sla"`<br>`"vsa"` |
| `start_percent` | Punto percentuale in cui inizia l'attenzione sparsa. Prima di questo punto, l'attenzione rimane densa. Predefinito: 0.2. | FLOAT | No | min: 0.0, max: 1.0, passo: 0.01 |
| `end_percent` | Punto percentuale in cui termina l'attenzione sparsa. Dopo questo punto, l'attenzione torna densa. Predefinito: 1.0. | FLOAT | No | min: 0.0, max: 1.0, passo: 0.01 |
| `dense_blocks` | Blocchi Transformer che vengono sempre eseguiti in modalità densa, ad es. '0, 1, 47-49'. Predefinito: "" (vuoto). Input avanzato. | STRING | No | Predefinito: "" |
| `min_tokens` | Le sequenze più brevi di questo valore rimangono dense. Predefinito: 12288. Input avanzato. | INT | No | min: 0, max: 1048576, passo: 512 |
| `extra_tokens` | Token extra con punteggio più alto a cui ogni blocco query presta attenzione oltre ai blocchi selezionati. Più vicino alla modalità densa per un maggiore tempo di attenzione; 256 consigliato, 0 disabilita. Ignorato per VSA. Predefinito: 256. Input avanzato. | INT | No | min: 0, max: 256, passo: 64 |
| `sink_conditioning` | Solo per MiniMax-H3. `exact_kv`: ogni query presta attenzione esattamente alle righe impacchettate di testo/audio/riferimento (circa il 3% del costo). `exact_kv_and_rows`: esegue inoltre in modalità densa le righe query dell'audio target (mantiene intatto l'audio generato). `off` disabilita questo comportamento. Predefinito: "exact_kv_and_rows". Input avanzato. | COMBO | No | `"exact_kv"`<br>`"exact_kv_and_rows"`<br>`"off"` |
| `verbose` | Registra nei log se ogni forma di attenzione ha usato l'attenzione sparsa o perché è rimasta densa. Predefinito: False. Input avanzato. | BOOLEAN | No | Predefinito: False |

### Input di sol-attn

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `tau` | Soglia in sigma della distribuzione dei punteggi. Un valore più alto rende l'attenzione più sparsa: 1.0 mantiene esatti circa il 16% dei blocchi chiave, 1.5 circa il 7%, 2.0 circa il 2,7%. Predefinito: 1.3. | FLOAT | No | min: 0.0, max: 4.0, passo: 0.05 |

### Input di sla

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `keep_percent` | Percentuale di blocchi chiave che ogni blocco query mantiene esattamente (i sink e la diagonale si aggiungono in più). Le LoRA in stile SLA per la selezione sono distillate in base a questo valore; senza una LoRA di questo tipo, un valore più alto è più vicino alla modalità densa. Predefinito: 10.0. | FLOAT | No | min: 0.5, max: 95.0, passo: 0.5 |

### Input di vsa

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `keep_percent` | Percentuale di cubetti video che ogni cubetto query mantiene; i checkpoint FastH3-VSA sono addestrati a 10. Utilizza i layer `to_gate_compress` del modello per il ramo grossolano, quando presenti. Predefinito: 10.0. | FLOAT | No | min: 0.5, max: 95.0, passo: 0.5 |

**Nota:** Nell'interfaccia vengono mostrati solo i parametri appartenenti al metodo attualmente selezionato.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `model` | Il modello con attenzione block-sparse applicata. | MODEL |

## Vincoli e limitazioni

- Le sequenze più brevi di `min_tokens`, i blocchi elencati in `dense_blocks` e i passi di campionamento al di fuori della finestra da `start_percent` a `end_percent` ricadono sul backend di attenzione densa del modello selezionato dal nodo Model Attention Backend.
- `extra_tokens` viene ignorato quando è selezionato il metodo `vsa`. Viene registrato un messaggio perché i pesi VSA sono stati addestrati in base al loro pattern sparso.
- Il metodo `vsa` richiede un modello MiniMax-H3; qualsiasi altro modello genera un errore. Se il modello non dispone dei layer `to_gate_compress`, la fase fine viene eseguita senza il ramo grossolano e viene registrato un avviso.
- `dense_blocks` viene ignorato per i modelli che non riportano gli indici dei blocchi, cosa che viene annotata nel log quando `verbose` è abilitato.
- `sink_conditioning` si applica solo ai modelli MiniMax-H3 che riportano un layout corrispondente alla lunghezza della sequenza corrente.

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BlockSparseAttention/it.md)

---
**Source fingerprint (SHA-256):** `0c34876b49a04db0ab265526e2bb5f784e150591aab631713ad2ab420a3327c4`
