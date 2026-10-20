# Bria FIBO 2.0 Image Generate

Genera una nuova immagine da un prompt testuale, un prompt JSON strutturato o una singola immagine di riferimento utilizzando Bria FIBO 2.0. Il nodo invia la richiesta all'API Bria, attende il completamento della generazione e restituisce l'immagine insieme a un prompt strutturato che può ricrearla o perfezionarla in un'esecuzione successiva.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `prompt` | Descrizione in linguaggio naturale dell'immagine da generare (predefinito: vuoto). | STRING | Sì | Testo multiriga |
| `structured_prompt` | Prompt strutturato JSON da un precedente risultato Bria FIBO. Con lo stesso seed ricrea quell'immagine; modifica il JSON o aggiungi un prompt per perfezionarla (predefinito: vuoto). | STRING | Sì | Testo multiriga |
| `aspect_ratio` | Proporzioni dell'output (predefinito: `"1:1"`). Le proporzioni da `"16:10"` in poi sono dimensioni FIBO 2.0 con requisiti aggiuntivi, elencati di seguito. | COMBO | Sì | `"1:1"`<br>`"2:3"`<br>`"3:2"`<br>`"3:4"`<br>`"4:3"`<br>`"4:5"`<br>`"5:4"`<br>`"9:16"`<br>`"16:9"`<br>`"16:10"`<br>`"10:16"`<br>`"2:1"`<br>`"1:2"`<br>`"21:9"`<br>`"9:21"`<br>`"3:1"`<br>`"1:3"`<br>`"4:1"`<br>`"1:4"`<br>`"5:1"`<br>`"1:5"` |
| `resolution` | Risoluzione dell'output in megapixel (predefinito: `"1MP"`). | COMBO | Sì | `"1MP"`<br>`"4MP"` |
| `seed` | Seed che inizializza la generazione (predefinito: 42). | INT | Sì | Da 1 a 2147483647 |
| `moderation` | Impostazioni di moderazione. Selezionando `"true"` vengono mostrati gli input di moderazione elencati di seguito. | DYNAMIC_COMBO | Sì | `"false"`<br>`"true"` |
| `image` | Immagine di riferimento opzionale da cui trarre spunto. Il risultato è una nuova immagine con le proporzioni selezionate, non una modifica di questa immagine. | IMAGE | No | - |

### Input di moderazione

Quando `moderation` è impostato su `"true"`, questi input aggiuntivi diventano disponibili:

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `prompt_content_moderation` | Se moderare il testo del prompt; la richiesta fallisce quando la moderazione lo rifiuta (predefinito: false). | BOOLEAN | No | `true`<br>`false` |
| `visual_input_moderation` | Se moderare l'immagine di riferimento; la richiesta fallisce quando la moderazione la rifiuta (predefinito: false). | BOOLEAN | No | `true`<br>`false` |
| `visual_output_moderation` | Se moderare l'immagine generata; la richiesta fallisce quando la moderazione la rifiuta (predefinito: false). | BOOLEAN | No | `true`<br>`false` |

**Vincoli importanti:**

- Fornisci almeno uno tra `prompt`, `structured_prompt` o un'`image` di riferimento. Se tutti e tre sono vuoti, il nodo genera un errore.
- Un'immagine di riferimento non può essere combinata con `structured_prompt`: usa uno o l'altro.
- Le proporzioni FIBO 2.0 (`"16:10"`, `"10:16"`, `"2:1"`, `"1:2"`, `"21:9"`, `"9:21"`, `"3:1"`, `"1:3"`, `"4:1"`, `"1:4"`, `"5:1"`, `"1:5"`) richiedono `resolution` `"1MP"` ed esattamente uno tra `prompt` o `structured_prompt`.
- Questo nodo è un nodo API a pagamento; ogni esecuzione costa circa 0,0572 USD.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `IMAGE` | L'immagine generata restituita dall'API Bria. | IMAGE |
| `structured_prompt` | Descrizione strutturata dell'immagine generata, per ricrearla o perfezionarla con questo nodo. | STRING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaImageGenerate/it.md)

---
**Source fingerprint (SHA-256):** `4d53fe457e2e349ac41b5c8a0d3d5599eafa53cb653c470335853f1d4517688f`
