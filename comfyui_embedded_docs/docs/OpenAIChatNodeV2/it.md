# OpenAI ChatGPT

Questo nodo genera risposte testuali con i modelli GPT di OpenAI. Invia un prompt testuale e, facoltativamente, immagini o file come contesto, e restituisce la risposta come stringa. Ogni impostazione è contenuta nel selettore `model`: selezionando un modello vengono mostrati i livelli di `reasoning_effort`, il limite di token, il seed e il prompt di sistema specifici di quel modello, quindi non è necessario un nodo di configurazione separato. Questo nodo sostituisce il precedente nodo OpenAI ChatGPT, che il codice sorgente ora contrassegna come deprecato.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `model` | Il modello utilizzato per generare la risposta. Ogni modello espone i livelli di `reasoning_effort` supportati (predefinito: `"gpt-6.2-sol"`). | DYNAMIC_COMBO | Sì | `"gpt-6.2-sol"`<br>`"gpt-6.2-astra"`<br>`"gpt-6-astra"`<br>`"gpt-6.1-sol"`<br>`"gpt-6.1-terra"`<br>`"gpt-6-sol"`<br>`"gpt-6-luna"`<br>`"gpt-5.6-sol"`<br>`"gpt-5.6-terra"`<br>`"gpt-5.6-luna"`<br>`"gpt-5.5-pro"`<br>`"gpt-5.5"` |
| `prompt` | Input testuale per il modello (predefinito: stringa vuota). | STRING | Sì | - |
| `images` | Slot espandibile: collega da 1 a 16 elementi (`image_1`, `image_2`, ...). Immagine/i opzionale/i utilizzata/e come contesto per il modello. | IMAGE | No | 0 a 16 immagini |
| `files` | File opzionale/i utilizzato/i come contesto per il modello. Accetta input dal nodo OpenAI ChatGPT Input Files. | OPENAI_INPUT_FILES | No | - |
| `reasoning_effort` | Quanto il modello ragiona prima di rispondere. I livelli più alti usano più token e richiedono più tempo. I livelli offerti dipendono dal modello selezionato (predefinito: `"medium"`, `"high"` per `gpt-5.5-pro`). | COMBO | Sì | Vedi l'elenco per modello di seguito |
| `max_output_tokens` | Numero massimo di token da generare, inclusi i token di ragionamento. Un valore basso insieme a un `reasoning_effort` alto può non lasciare spazio per la risposta (predefinito: 32768). | INT | Sì | 16 a 128000 |
| `seed` | Il seed controlla se il nodo deve essere rieseguito; i risultati non sono deterministici indipendentemente dal seed (predefinito: 42). | INT | Sì | 0 a 2147483647 |
| `system_prompt` | Istruzioni di base che determinano il comportamento del modello (predefinito: stringa vuota). | STRING | No | - |

### Livelli di impegno di ragionamento per modello

- `gpt-6.2-sol`, `gpt-6.2-astra`, `gpt-6-astra`, `gpt-6.1-sol`: `"low"`, `"medium"`, `"high"`, `"xhigh"`, `"max"`, predefinito `"medium"`.
- `gpt-6.1-terra`, `gpt-6-sol`, `gpt-6-luna`, `gpt-5.6-sol`, `gpt-5.6-terra`, `gpt-5.6-luna`: `"none"`, `"low"`, `"medium"`, `"high"`, `"xhigh"`, `"max"`, predefinito `"medium"`.
- `gpt-5.5-pro`: `"medium"`, `"high"`, `"xhigh"`, predefinito `"high"`.
- `gpt-5.5`: `"none"`, `"low"`, `"medium"`, `"high"`, `"xhigh"`, predefinito `"medium"`.

### Note sul comportamento

- Viene restituito solo il testo della risposta. I messaggi che il modello emette nella fase di commento durante il ragionamento vengono ignorati.
- Se il budget di token si esaurisce prima che la risposta venga scritta, il nodo genera un errore che indica di aumentare `max_output_tokens`.
- Le immagini vengono inviate alla loro risoluzione con il livello di dettaglio automatico dell'API, quindi le immagini di grandi dimensioni usano più token.
- Ogni richiesta viene memorizzata lato OpenAI e il testo restituito unisce le parti della risposta con caratteri di nuova riga.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `output` | La risposta testuale generata dal modello OpenAI. | STRING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIChatNodeV2/it.md)

---
**Source fingerprint (SHA-256):** `129c13a6c7b76d142c0a23234ab5e707a1dd39a99055974277d46a39593aa7ba`
