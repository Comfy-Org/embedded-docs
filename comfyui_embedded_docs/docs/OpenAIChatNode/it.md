# OpenAI ChatGPT

Questo nodo genera risposte testuali da un modello OpenAI. Invia il tuo prompt di testo, e opzionalmente immagini o file, a un modello OpenAI e restituisce la risposta testuale generata.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `prompt` | Input testuali per il modello, utilizzati per generare una risposta (predefinito: stringa vuota). | STRING | Sì | - |
| `persist_context` | Questo parametro è deprecato e non ha alcun effetto (predefinito: False). | BOOLEAN | Sì | - |
| `model` | Il modello utilizzato per generare la risposta (predefinito: `gpt-5`) | COMBO | Sì | `gpt-6-astra`<br>`gpt-6-sol`<br>`gpt-6-luna`<br>`gpt-5.6-sol`<br>`gpt-5.6-terra`<br>`gpt-5.6-luna`<br>`gpt-5.5-pro`<br>`gpt-5.5`<br>`gpt-5`<br>`gpt-5-mini`<br>`gpt-5-nano`<br>`gpt-4.1`<br>`gpt-4.1-mini`<br>`gpt-4.1-nano`<br>`o4-mini`<br>`o3`<br>`o1-pro`<br>`o1` |
| `images` | Immagini opzionali da usare come contesto per il modello. Per includere più immagini, puoi usare il nodo Batch Images. | IMAGE | No | - |
| `files` | File opzionali da usare come contesto per il modello. Accetta input dal nodo OpenAI Chat Input Files. | OPENAI_INPUT_FILES | No | - |
| `advanced_options` | Configurazione opzionale per il modello. Accetta input dal nodo OpenAI Chat Advanced Options. | OPENAI_CHAT_CONFIG | No | - |

Nota: quando viene collegata una configurazione `advanced_options` che imposta uno sforzo di ragionamento, il `model` selezionato deve supportare quel valore di sforzo. Ad esempio, la famiglia di modelli gpt-4.1 non supporta alcuno sforzo di ragionamento, `gpt-6-sol` e `gpt-6-luna` supportano none, low, medium, high, xhigh e max, `gpt-5.5` supporta none, low, medium, high e xhigh, mentre `gpt-5.5-pro` supporta medium, high e xhigh. Se lo sforzo di ragionamento non è supportato dal modello selezionato, il nodo genera un errore.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `output_text` | La risposta testuale generata dal modello OpenAI. | STRING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIChatNode/it.md)

---
**Source fingerprint (SHA-256):** `46b4558f1368191e2b4eb68f79e098f289c9eb80e1e05f7a516123c098295f2b`
