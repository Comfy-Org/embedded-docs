# Bria Sostituisci oggetto

Sostituisce un oggetto in un'immagine con un altro descritto in testo semplice, utilizzando la modifica delle immagini guidata dal testo di Bria. Bria renderizza nuovamente l'intero fotogramma a circa 1 megapixel, quindi il risultato non è allineato a livello di pixel con l'input.

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `image` | L'immagine contenente l'oggetto da sostituire. Il canale alfa viene eliminato prima che l'immagine venga caricata. | IMAGE | Sì | - |
| `instruction` | Cosa sostituire con cosa, ad esempio "Sostituisci la mela rossa con una pera verde". Deve contenere almeno 1 carattere. | STRING | Sì | Testo multilinea; predefinito: "" (vuoto) |
| `seed` | Bria non accetta alcun seed qui e reimmagina la modifica a ogni chiamata, quindi esecuzioni ripetute possono differire. Il valore non viene mai inviato: cambia solo la chiave della cache di questo nodo, così che un grafo per il resto identico esegua di nuovo la modifica invece di restituire il risultato memorizzato nella cache. | INT | Sì | da 0 a 2147483647, passo 1; predefinito: 42; controllo dopo generazione abilitato |

### Input di moderazione

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `moderation` | Impostazioni di moderazione. Selezionando "true" vengono mostrate le sotto-opzioni di moderazione riportate di seguito, che altrimenti non sono visualizzate. | DYNAMIC_COMBO | Sì | `"false"`<br>`"true"` |
| `visual_input_moderation` | Abilita la moderazione dell'immagine di input. Disponibile solo quando `moderation` è impostato su "true". | BOOLEAN | No | `true` / `false`; predefinito: false |
| `visual_output_moderation` | Abilita la moderazione dell'immagine di output generata. Disponibile solo quando `moderation` è impostato su "true". | BOOLEAN | No | `true` / `false`; predefinito: false |

Nota: `instruction` viene convalidato prima che la richiesta venga inviata e deve contenere almeno 1 carattere. Il valore di `seed` non viene trasmesso a Bria; influisce solo sul fatto che il nodo riesegua la modifica o restituisca un risultato memorizzato nella cache.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `image` | L'immagine modificata con la sostituzione dell'oggetto descritta applicata. | IMAGE |
| `structured_prompt` | Descrizione strutturata dell'immagine modificata, per una modifica successiva con Bria FIBO Image Edit. | STRING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaReplaceObject/it.md)

---
**Source fingerprint (SHA-256):** `75a45d5c0d6cde96a1e961db627edc1a59c07cc37b974402745cefc62864cc26`
