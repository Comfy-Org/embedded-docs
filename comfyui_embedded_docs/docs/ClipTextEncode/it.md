# ClipTextEncode

Codifica un prompt testuale utilizzando un modello CLIP in un embedding che può essere usato per guidare il modello di diffusione verso la generazione di immagini specifiche.

`CLIP Text Encode (CLIPTextEncode)` agisce come un traduttore, convertendo le tue descrizioni testuali in un formato che l'IA può comprendere. Questo aiuta l'IA a interpretare il tuo input e a generare l'immagine desiderata.

Immagina di comunicare con un artista che parla una lingua diversa. Il modello CLIP, addestrato su enormi quantità di coppie immagine-testo, colma questo divario convertendo le tue descrizioni in "istruzioni" che il modello di IA può seguire.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `text` | Il testo da codificare. Supporta input multilinea e prompt dinamici. | STRING | Sì | Qualsiasi testo |
| `clip` | Il modello CLIP usato per codificare il testo. | CLIP | Sì | Modelli CLIP caricati |

Nota: se l'input `clip` è None (ad esempio, quando proviene da un caricatore di checkpoint il cui checkpoint non contiene un modello CLIP o text encoder valido), il nodo genera un errore.

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `CONDITIONING` | Un conditioning contenente il testo incorporato usato per guidare il modello di diffusione. | CONDITIONING |

## Funzionalità dei prompt

### Modelli di embedding

I modelli di embedding consentono di applicare effetti artistici o stili specifici. I formati supportati includono `.safetensors`, `.pt` e `.bin`. Per usare un modello di embedding:

1. Colloca il file nella cartella `ComfyUI/models/embeddings`.
2. Fai riferimento ad esso nel tuo testo usando `embedding:model_name`.

Esempio: se hai un modello chiamato `EasyNegative.pt` nella cartella `ComfyUI/models/embeddings`, puoi usarlo così:

```
worst quality, embedding:EasyNegative, bad quality
```

**IMPORTANTE**: quando usi modelli di embedding, verifica che il nome del file corrisponda e sia compatibile con l'architettura del tuo modello. Ad esempio, un embedding progettato per SD1.5 non funzionerà correttamente con un modello SDXL.

### Regolazione del peso del prompt

Puoi regolare l'importanza di alcune parti della tua descrizione usando le parentesi. Ad esempio:

- `(beautiful:1.2)` aumenta il peso di "beautiful".
- `(beautiful:0.8)` diminuisce il peso di "beautiful".
- Le parentesi semplici `(beautiful)` applicheranno un peso predefinito di 1.1.

Puoi usare le scorciatoie da tastiera `ctrl + up/down arrow` per regolare rapidamente i pesi. La dimensione del passo di regolazione del peso può essere modificata nelle impostazioni.

Se vuoi includere parentesi letterali nel tuo prompt senza modificare il peso, puoi effettuare l'escape usando una barra rovesciata, ad es. `\(word\)`.

### Wildcard/Prompt dinamici

Usa `{}` per creare prompt dinamici. Ad esempio, `{day|night|morning}` selezionerà casualmente un'opzione ogni volta che il prompt viene elaborato.

Se vuoi includere parentesi graffe letterali nel tuo prompt senza attivare il comportamento dinamico, puoi effettuare l'escape usando una barra rovesciata, ad es. `\{word\}`.

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ClipTextEncode/it.md)

---
**Source fingerprint (SHA-256):** `ace7988df7aaa3ac26419b16a9bd8908a327da6e82c21c2b2704af091d2e76e7`
