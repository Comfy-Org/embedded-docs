# BriaGenFill

Questo nodo genera oggetti o paesaggi all'interno di una regione mascherata di un'immagine utilizzando Bria. Carica l'immagine e la maschera, invia il prompt al servizio di riempimento generativo di Bria, attende il completamento dell'operazione e restituisce l'immagine modificata. Questa è un'operazione API a pagamento (0,0429 USD per richiesta).

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `image` | L'immagine di input da modificare. | IMAGE | Sì | - |
| `mask` | Le aree bianche vengono riempite con il contenuto generato, le aree nere vengono preservate. La maschera viene binarizzata prima dell'invio con una soglia del 50%: solo le aree dipinte con opacità superiore al 50% contano come bianche. Deve avere lo stesso rapporto d'aspetto dell'immagine. | MASK | Sì | - |
| `prompt` | Descrizione di ciò che si desidera generare all'interno della regione mascherata. Deve contenere almeno 1 carattere. (predefinito: "") | STRING | Sì | - |
| `negative_prompt` | Un prompt che descrive il contenuto da evitare nel risultato generato. Se lasciato vuoto, non viene inviato all'API. (predefinito: "") | STRING | Sì | - |
| `refine_prompt` | Regola automaticamente il prompt per ottenere risultati migliori; disabilita per usare il prompt esattamente come scritto. (predefinito: true) | BOOLEAN | Sì | true<br>false |
| `seed` | Seme per il processo di generazione. (predefinito: 42) | INT | Sì | 1 to 2147483647 |
| `moderation` | Impostazioni di moderazione. Quando è impostato su "true", vengono applicate le opzioni di moderazione riportate di seguito. (predefinito: "false") | DYNAMIC_COMBO | Sì | "false"<br>"true" |

### Input di moderazione (quando `moderation` = "true")

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `prompt_content_moderation` | Applica la moderazione dei contenuti al prompt. (predefinito: false) | BOOLEAN | No | true<br>false |
| `visual_input_moderation` | Applica la moderazione dei contenuti all'immagine di input. (predefinito: false) | BOOLEAN | No | true<br>false |
| `visual_output_moderation` | Applica la moderazione dei contenuti all'immagine di output. (predefinito: false) | BOOLEAN | No | true<br>false |

**Nota:** Il `prompt` non deve essere vuoto. La `mask` deve avere lo stesso rapporto d'aspetto dell'`image`. La maschera viene binarizzata con opacità al 50%, quindi le aree dipinte con opacità inferiore alla metà vengono ignorate; se la maschera non contiene aree bianche dopo la binarizzazione, il nodo genera un errore.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|-----------|
| `image` | L'immagine risultante con la regione mascherata riempita dal contenuto generato. | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaGenFill/it.md)

---
**Source fingerprint (SHA-256):** `b23e29d4457f859181d68eaeb4b0238de28f4b18932d68438fa2954739cdc66a`
