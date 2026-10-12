# Finestre di contesto (Manuale)

Il nodo Context Windows (Manual) consente di configurare manualmente le finestre di contesto per un modello durante il campionamento, creando segmenti di contesto sovrapposti con lunghezza, sovrapposizione e schema di pianificazione specificati, in modo che i dati vengano elaborati in blocchi gestibili mantenendo la continuità tra i segmenti. Offre opzioni avanzate per controllare come vengono applicate le finestre di contesto, tra cui shuffling del rumore, conservazione del conditioning e correzioni delle finestre causali. Questo nodo è sperimentale.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model` | Il modello a cui applicare le finestre di contesto durante il campionamento. | MODEL | Sì | - |
| `context_length` | La lunghezza della finestra di contesto (predefinito: 16). | INT | Sì | 1+ |
| `context_overlap` | La sovrapposizione della finestra di contesto (predefinito: 4). | INT | Sì | 0+ |
| `context_schedule` | Algoritmo di pianificazione dipendente dagli step per le finestre di contesto (predefinito: STATIC_STANDARD). | COMBO | Sì | `STATIC_STANDARD`<br>`UNIFORM_STANDARD`<br>`UNIFORM_LOOPED`<br>`BATCHED` |
| `context_stride` | Lo stride della finestra di contesto; applicabile solo agli schemi uniformi (predefinito: 1). | INT | Sì | 1+ |
| `closed_loop` | Indica se chiudere il ciclo della finestra di contesto; applicabile solo agli schemi con loop (predefinito: False). | BOOLEAN | Sì | - |
| `fuse_method` | Il metodo da usare per fondere le finestre di contesto (predefinito: PYRAMID). | COMBO | Sì | Metodi di fusione statici (vedi `ContextFuseMethods.LIST_STATIC`) |
| `dim` | La dimensione a cui applicare le finestre di contesto (predefinito: 0). | INT | Sì | 0-5 |
| `freenoise` | Indica se applicare lo shuffling del rumore FreeNoise, migliora la fusione delle finestre (predefinito: False). | BOOLEAN | Sì | - |
| `cond_retain_index_list` | Elenco di indici latenti da conservare nei tensori di conditioning per ciascuna finestra. Per i modelli I2V in stile concat (ad es. Wan I2V, HunyuanVideo I2V, Cosmos I2V, SVD) l'immagine iniziale codificata risiede nei canali di conditioning c_concat; impostando questo valore su '0' si conserverà il contenuto di quell'immagine iniziale alla sotto-posizione 0 di ogni finestra (predefinito: ""). | STRING | No | - |
| `split_conds_to_windows` | Indica se suddividere più conditioning (creati da ConditionCombine) su ciascuna finestra in base all'indice di regione (predefinito: False). | BOOLEAN | No | - |
| `latent_retain_index_list` | Elenco di indici latenti da conservare nel latente di rumore stesso per ciascuna finestra. Da usare per flussi di lavoro in cui il contenuto di riferimento (ad es. un'immagine iniziale) risiede direttamente nel latente di rumore anziché in canali di conditioning separati (ad es. I2V in stile inplace come LTXV, AnimateDiff). Indipendente da cond_retain_index_list (predefinito: ""). | STRING | No | - |
| `causal_window_fix` | Indica se aggiungere un frame di correzione causale alle finestre di contesto con indice diverso da 0 (predefinito: True). | BOOLEAN | No | - |

**Vincoli sui parametri:**

- `context_stride` viene usato solo quando è selezionato uno schema uniforme (`UNIFORM_STANDARD` o `UNIFORM_LOOPED`).
- `closed_loop` è applicabile solo agli schemi con loop (`UNIFORM_LOOPED`).
- `dim` deve essere compreso tra 0 e 5 inclusi.
- `cond_retain_index_list` e `latent_retain_index_list` si aspettano un elenco di indici interi separati da virgole, come stringa (ad es., "0,1,2").
- `latent_retain_index_list` è indipendente da `cond_retain_index_list`.

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `model` | Il modello con le finestre di contesto applicate durante il campionamento. | MODEL |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ContextWindowsManual/it.md)

---
**Source fingerprint (SHA-256):** `39dc39ece3d3c10c13ca8c4b85af4fbbebbcaba8a019145a6d4727c3df7b302b`
