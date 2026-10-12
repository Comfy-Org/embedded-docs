# BriaEraser

Bria Eraser rimuove oggetti o aree da un'immagine utilizzando l'API Bria. Fornisci un'immagine e una maschera che delimita le regioni da rimuovere; il nodo carica entrambe su Bria, esegue il processo di cancellazione, attende il completamento e restituisce l'immagine modificata con le aree mascherate cancellate.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `image` | L'immagine di input contenente gli oggetti o le aree da rimuovere. | IMAGE | Sì | - |
| `mask` | Le aree bianche vengono cancellate, quelle nere conservate. La maschera viene binarizzata prima dell'invio con una soglia del 50%: solo le aree dipinte con opacità superiore al 50% contano come bianche. Deve avere lo stesso rapporto d'aspetto dell'immagine. | MASK | Sì | - |
| `mask_type` | Il tipo di origine della maschera. "manual" è per maschere disegnate a mano o con il pennello; "automatic" è per maschere prodotte da modelli di segmentazione come SAM. | COMBO | Sì | "manual"<br>"automatic" |
| `moderation` | Impostazioni di moderazione. Imposta su "true" per abilitare la moderazione dei contenuti visivi sulle immagini di input e/o output. | DYNAMIC_COMBO | Sì | "false"<br>"true" |

Quando `moderation` è impostato su "true", diventano disponibili due impostazioni booleane aggiuntive:

- `visual_input_moderation` — applica la moderazione dei contenuti visivi all'immagine di input (predefinito: false)
- `visual_output_moderation` — applica la moderazione dei contenuti visivi all'immagine di output (predefinito: false)

Nota: la maschera deve corrispondere al rapporto d'aspetto dell'immagine, altrimenti la richiesta fallisce. La maschera viene convertita in una maschera binaria (bianco e nero) prima di essere inviata all'API: le aree dipinte con opacità inferiore alla metà vengono ignorate, mentre le aree parzialmente dipinte vengono trattate come bianche e saranno cancellate. La maschera deve contenere almeno una porzione bianca; una maschera vuota causa il fallimento della richiesta perché non c'è nulla da cancellare.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|-----------|
| `image` | L'immagine modificata con gli oggetti o le aree mascherate rimossi. | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaEraser/it.md)

---
**Source fingerprint (SHA-256):** `5528b7a3cb4d0a7b1b28acbc642a8bd21e2eacf5aa225403d6344c29f0cdba80`
