# TextEncodeFibo2

Codifica un prompt di Fibo 2.0 in condizionamento e in un latente vuoto corrispondente. Il prompt è testo semplice oppure una didascalia JSON strutturata; con immagini collegate diventa l'istruzione di modifica, oppure una didascalia JSON del risultato con una chiave `edit_instruction`, e le immagini agiscono come latenti di riferimento per entrambi gli output quando è collegato un VAE. Campiona l'output `latent`, la cui dimensione è quella a cui vengono ritagliate le immagini.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `clip` | L'encoder di testo Fibo 2.0 usato per tokenizzare e codificare il prompt. | CLIP | Sì | - |
| `prompt` | La didascalia da cui generare, oppure l'istruzione di modifica quando sono collegate delle immagini. Fai riferimento alle immagini come `<image_1>`, `<image_2>` e così via. Funziona anche una didascalia JSON del risultato atteso, con la modifica descritta nella sua chiave `edit_instruction`. | STRING | Sì | - |
| `negative_prompt` | Didascalia da cui allontanarsi, codificata come condizionamento negativo. Il valore vuoto corrisponde alla didascalia nulla con cui Fibo 2.0 è stato addestrato per il classifier-free guidance (predefinito: vuoto). | STRING | Sì | - |
| `vae` | VAE usato per codificare le immagini in latenti di riferimento. Senza di esso le immagini condizionano solo la codifica del testo. | VAE | No | - |
| `images` | Immagini da modificare, fino a 16. Una singola immagine viene ridimensionata e ritagliata al centro alla dimensione del risultato, perché la modifica si allinea con essa pixel per pixel; più immagini vengono ciascuna ridimensionata alla propria dimensione di addestramento. | IMAGE | No | 0 a 16 immagini |
| `width` | Larghezza del risultato, arrotondata per difetto a un multiplo di 16. 0 usa la dimensione con cui Fibo 2.0 è stato addestrato per le proporzioni della prima immagine, circa 1 megapixel, oppure 1024 senza immagini (predefinito: 0). | INT | Sì | 0 a 16384 (passo: 16) |
| `height` | Altezza del risultato, arrotondata per difetto a un multiplo di 16. 0 usa la dimensione con cui Fibo 2.0 è stato addestrato per le proporzioni della prima immagine, circa 1 megapixel, oppure 1024 senza immagini (predefinito: 0). | INT | Sì | 0 a 16384 (passo: 16) |
| `batch_size` | Numero di latenti da creare nel batch (predefinito: 1). | INT | Sì | 1 a 4096 |

I latenti di riferimento sono collegati a entrambi gli output, quindi le immagini viaggiano con il condizionamento anziché solo con il ramo positivo. Quando il VAE non è collegato, le immagini sono viste solo dall'encoder di testo e non viene aggiunto alcun latente di riferimento.

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `positive` | Condizionamento del prompt, con i latenti di riferimento quando sono collegati un VAE e delle immagini. | CONDITIONING |
| `negative` | Condizionamento di `negative_prompt`, solo testo, con gli stessi latenti di riferimento. | CONDITIONING |
| `latent` | Latente vuoto alla dimensione richiesta, pronto per il campionamento. | LATENT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeFibo2/it.md)

---
**Source fingerprint (SHA-256):** `f400d041a3dd224e30c0fa2acc803e3de11d6c10654bde122e8d569fa1cd1d79`
