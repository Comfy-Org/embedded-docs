# TextEncodeBooguEdit

Questo nodo prepara il condizionamento per la modifica delle immagini con Boogu. Elabora le immagini di riferimento per creare output di condizionamento sia positivi sia negativi. L'immagine di riferimento viene utilizzata due volte: i token di visione dell'immagine vengono aggiunti solo al condizionamento positivo per amplificare l'istruzione di modifica, mentre un latente di riferimento VAE viene aggiunto sia al condizionamento positivo sia a quello negativo in modo che si annulli sotto CFG, preservando l'identità dell'immagine originale; il tokenizer seleziona automaticamente il prompt di sistema appropriato in base alla presenza di immagini e prompt negativi vuoti.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `clip` | Il modello CLIP utilizzato per la codifica del testo | CLIP | Sì | |
| `prompt` | Il prompt testuale che descrive la modifica desiderata. Supporta testo multilinea e prompt dinamici. | STRING | Sì | |
| `negative_prompt` | Il prompt testuale che descrive cosa evitare nella modifica. Può essere lasciato vuoto per eliminare il condizionamento negativo. Parametro avanzato. | STRING | Sì | |
| `vae` | Il modello VAE utilizzato per codificare le immagini di riferimento nello spazio latente. Necessario per aggiungere i latenti di riferimento agli output di condizionamento. | VAE | No | |
| `images` | Immagine/i di riferimento da modificare. Boogu si concentra su un riferimento per campione; ne sono ammesse altre. | IMAGE | No | Fino a 16 immagini |

I latenti di riferimento vengono aggiunti a entrambi gli output di condizionamento solo quando `vae` viene fornito insieme ad almeno un `image` di riferimento. Se `vae` viene omesso, l'output positivo riceve comunque i token di visione dalle immagini di riferimento, ma nessuno dei due output include i latenti di riferimento.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|-----------|
| `positive` | Condizionamento contenente sia il prompt testuale con i token di visione sia i latenti di riferimento | CONDITIONING |
| `negative` | Condizionamento contenente il prompt testuale negativo e i latenti di riferimento | CONDITIONING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeBooguEdit/it.md)

---
**Source fingerprint (SHA-256):** `170979acf5b2e9f25f96231a4b23a4376cfddcd4bda2fdd6e03528417e6931b0`
