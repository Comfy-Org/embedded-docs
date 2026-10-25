# Branch

Branch seleziona uno tra diversi input collegati in base al nome e lo passa all'output. Funziona come un interruttore lazy: viene valutato solo il ramo selezionato, quindi gli altri rami possono restare non collegati o contenere output che non vuoi calcolare. Ogni nuova connessione aggiunge un altro input di ramo, gli input possono essere rinominati facendo doppio clic su di essi e il ramo attivo viene scelto dal selettore `branch`.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `autogrow` | I rami collegati. Ogni connessione aggiunge un nuovo input di ramo, fino a 32; tutti i rami devono usare lo stesso tipo di dati, che diventa il tipo dell'output. | AUTOGROW | Sì | da 1 a 32 rami |
| `branch` | Nome del ramo passato all'output. Le opzioni sono i nomi degli input di ramo collegati e un input può essere rinominato facendo doppio clic su di esso. | STRING | Sì | Nomi dei rami collegati |
| `branch_names` | Elenco interno dei nomi dei rami collegati, mantenuto sincronizzato dal frontend. Associa il nome selezionato al relativo ramo e non è pensato per essere modificato manualmente. | ARRAY | Sì | - |

**Nota:** Viene richiesto solo il ramo selezionato, quindi gli altri rami non vengono valutati. Il nodo genera un errore quando il nome selezionato non è collegato.

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `output` | Il valore del ramo selezionato, passato senza modifiche. | MATCH_TYPE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BranchNode/it.md)

---
**Source fingerprint (SHA-256):** `2b4dca360c1b459a9f05eb54fedb7cdea6842fb0c606ee6f937ed00f715ee23a`
