# SenseNova Conditioning

Prepara il condizionamento SenseNova per la generazione di immagini o per un output intercalato di testo e immagini. Il selettore `task` imposta il template del prompt e il comportamento di arresto, e il nodo segnala se il modello richiede un'immagine, così un ciclo sa quando eseguire il sampler.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `clip` | Modello CLIP SenseNova, collegato da CLIP Text Encode. Obbligatorio per ogni attività, tranne quando il condizionamento in ingresso è già completato. | CLIP | No | - |
| `conditioning` | Condizionamento testuale SenseNova da CLIP Text Encode. | CONDITIONING | Sì | - |
| `negative` | Condizionamento negativo opzionale. Viene aggiornato e restituito per le attività `interleave` e `self-correction`. | CONDITIONING | No | - |
| `task` | Attività da eseguire. `"image"` codifica il prompt per un sampler standard, `"image thinking"` consente al modello di ragionare prima di rispondere, `"interleave"` produce testo e immagini in un'unica passata e `"self-correction"` consente al modello di correggere il proprio output precedente. | DYNAMIC_COMBO | Sì | `"image"`<br>`"image thinking"`<br>`"interleave"`<br>`"self-correction"` |
| `max_tokens` | Numero massimo di token generati durante questa chiamata. Predefinito: 1024. | INT | Sì | 1 a 8192 |

### Input di `interleave`

Questi input compaiono quando `task` è impostato su `"interleave"`.

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `thinking` | Consente al modello di ragionare prima di rispondere. Predefinito: True. | BOOLEAN | Sì | True<br>False |
| `samples` | Output precedente del sampler, collegato quando si continua dopo una richiesta di immagine. | LATENT | No | - |

### Input di `self-correction`

Questi input compaiono quando `task` è impostato su `"self-correction"`.

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `samples` | Output precedente del sampler, collegato quando si continua dopo una richiesta di immagine. | LATENT | No | - |

**Vincoli e comportamento:**

* L'input `clip` richiede l'output CLIP SenseNova di CLIP Text Encode; qualsiasi altro CLIP genera un errore.
* `"image thinking"` richiede esattamente una voce di condizionamento positivo; `"interleave"` e `"self-correction"` richiedono una voce positiva e una negativa.
* Quando il modello è in attesa di un'immagine, collegare l'output LATENT del sampler precedente a `samples`. Passare `samples` prima che sia stata richiesta un'immagine è un errore.
* Quando il condizionamento in ingresso è già completato, il nodo lo restituisce invariato con `generated_text` vuoto e `image_requested` impostato a False.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `conditioning` | Condizionamento per il sampler, esteso con il testo generato da questa chiamata. | CONDITIONING |
| `generated_text` | Testo generato da questa chiamata. Utilizzare SenseNova Interleave Decode per il risultato completo. | STRING |
| `negative` | Condizionamento negativo aggiornato per le attività `interleave` e `self-correction`. | CONDITIONING |
| `image_requested` | True quando il modello richiede un'immagine: eseguire il sampler, quindi reimmettere il loop in questo nodo. | BOOLEAN |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SenseNovaConditioning/it.md)

---
**Source fingerprint (SHA-256):** `97fcdc26ccf80f48c5628f695a4ae8231b065b67414c93dec9bced6bb8d4c77c`
