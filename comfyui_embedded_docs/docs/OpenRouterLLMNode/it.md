# OpenRouter LLM

Il nodo OpenRouter LLM invia un prompt testuale a un insieme curato di modelli linguistici popolari disponibili tramite il servizio OpenRouter e restituisce la risposta testuale generata. Supporta modelli di Anthropic (Claude), OpenAI (GPT), Google (Gemini), xAI (Grok), DeepSeek, Qwen, Mistral, Z.AI (GLM), Moonshot (Kimi) e Perplexity Sonar, e può includere facoltativamente immagini o video come input di riferimento nella richiesta.

## Input

Quando si seleziona un modello nel selettore `model`, il nodo mostra widget specifici del modello oltre agli input comuni — reasoning effort, dimensione della ricerca web e/o slot per i media di riferimento — in base alle capacità del modello scelto.

### Input comuni

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `prompt` | Input testuale per il modello. | STRING | Sì | N/A |
| `model` | Il modello OpenRouter utilizzato per generare la risposta. | DYNAMIC_COMBO | Sì | Numerose opzioni disponibili (vedi le sezioni sui modelli di seguito) |
| `seed` | Seed per il campionamento. Impostare a 0 per ometterlo. La maggior parte dei modelli lo considera solo un suggerimento. (predefinito: 0) | INT | Sì | da 0 a 2147483647 |
| `system_prompt` | Istruzioni fondamentali che determinano il comportamento del modello. (predefinito: "") | STRING | No | N/A |

### Input dei modelli Anthropic Claude

Condivisi da `anthropic/claude-opus-5`, `anthropic/claude-opus-4.8`, `anthropic/claude-opus-4.7`, `anthropic/claude-fable-5`, `anthropic/claude-sonnet-5` e `anthropic/claude-haiku-4.5`.

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `reasoning_effort` | Sforzo di ragionamento. 'off' disabilita completamente il ragionamento. (predefinito: "off") | COMBO | No | "off"<br>"low"<br>"medium"<br>"high" |

Questi modelli supportano fino a 20 immagini di riferimento (vedi Input di riferimento).

### Input dei modelli OpenAI GPT

Condivisi da `openai/gpt-5.6-sol-pro`, `openai/gpt-5.6-sol`, `openai/gpt-5.6-terra-pro`, `openai/gpt-5.6-terra`, `openai/gpt-5.6-luna-pro`, `openai/gpt-5.6-luna`, `openai/gpt-5.5-pro` e `openai/gpt-5.5`.

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `reasoning_effort` | Sforzo di ragionamento. 'off' disabilita completamente il ragionamento. (predefinito: "off") | COMBO | No | "off"<br>"low"<br>"medium"<br>"high" |

Questi modelli supportano fino a 20 immagini di riferimento (vedi Input di riferimento).

### Input di Google Gemini 3.5 Flash

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `reasoning_effort` | Sforzo di ragionamento. 'off' disabilita completamente il ragionamento. (predefinito: "off") | COMBO | No | "off"<br>"low"<br>"medium"<br>"high" |

Questo modello supporta fino a 20 immagini di riferimento e fino a 4 video di riferimento (vedi Input di riferimento).

### Input dei modelli xAI Grok

Condivisi da `x-ai/grok-4.5`, `x-ai/grok-4.20` e `x-ai/grok-4.3`.

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `reasoning_effort` | Sforzo di ragionamento. 'off' disabilita completamente il ragionamento. (predefinito: "off") | COMBO | No | "off"<br>"low"<br>"medium"<br>"high" |

Questi modelli supportano fino a 20 immagini di riferimento (vedi Input di riferimento).

### Input dei modelli DeepSeek

Condivisi da `deepseek/deepseek-v4-pro`, `deepseek/deepseek-v4-flash` e `deepseek/deepseek-v3.2`.

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `reasoning_effort` | Sforzo di ragionamento. 'off' disabilita completamente il ragionamento. (predefinito: "off") | COMBO | No | "off"<br>"low"<br>"medium"<br>"high" |

Modelli solo testo — nessuna immagine o video di riferimento.

### Input di Qwen 3.6 Max Preview

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `reasoning_effort` | Sforzo di ragionamento. 'off' disabilita completamente il ragionamento. (predefinito: "off") | COMBO | No | "off"<br>"low"<br>"medium"<br>"high" |

Modello solo testo — nessuna immagine o video di riferimento.

### Input di Qwen 3.6 Plus e Qwen 3.6 Flash

Condivisi da `qwen/qwen3.6-plus` e `qwen/qwen3.6-flash`.

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `reasoning_effort` | Sforzo di ragionamento. 'off' disabilita completamente il ragionamento. (predefinito: "off") | COMBO | No | "off"<br>"low"<br>"medium"<br>"high" |

Questi modelli supportano fino a 10 immagini di riferimento e fino a 4 video di riferimento (vedi Input di riferimento).

### Input di Mistral Large 2512

Nessun input specifico del profilo (profilo standard). Questo modello supporta fino a 8 immagini di riferimento (vedi Input di riferimento).

### Input di Mistral Medium 3.5

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `reasoning_effort` | Sforzo di ragionamento. 'off' disabilita completamente il ragionamento. (predefinito: "off") | COMBO | No | "off"<br>"low"<br>"medium"<br>"high" |

Questo modello supporta fino a 8 immagini di riferimento (vedi Input di riferimento).

### Input dei modelli Z.AI GLM

Condivisi da `z-ai/glm-4.6` e `z-ai/glm-5`.

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `reasoning_effort` | Sforzo di ragionamento. 'off' disabilita completamente il ragionamento. (predefinito: "off") | COMBO | No | "off"<br>"low"<br>"medium"<br>"high" |

Modelli solo testo — nessuna immagine o video di riferimento.

### Input di Moonshot Kimi K3 e K2.6

Condivisi da `moonshotai/kimi-k3` e `moonshotai/kimi-k2.6`.

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `reasoning_effort` | Sforzo di ragionamento. 'off' disabilita completamente il ragionamento. (predefinito: "off") | COMBO | No | "off"<br>"low"<br>"medium"<br>"high" |

Questi modelli supportano fino a 10 immagini di riferimento (vedi Input di riferimento).

### Input di Moonshot Kimi K2 Thinking

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `reasoning_effort` | Sforzo di ragionamento. 'off' disabilita completamente il ragionamento. (predefinito: "off") | COMBO | No | "off"<br>"low"<br>"medium"<br>"high" |

Modello solo testo — nessuna immagine o video di riferimento.

### Input di Perplexity Sonar Pro

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `search_context_size` | Quanto contesto di ricerca web recuperare. Un valore maggiore = risposte più fondate ma più lente/costose. (predefinito: "medium") | COMBO | No | "low"<br>"medium"<br>"high" |

Modello solo testo — nessuna immagine o video di riferimento.

### Input di Perplexity Sonar Reasoning Pro e Sonar Deep Research

Condivisi da `perplexity/sonar-reasoning-pro` e `perplexity/sonar-deep-research`.

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `search_context_size` | Quanto contesto di ricerca web recuperare. Un valore maggiore = risposte più fondate ma più lente/costose. (predefinito: "medium") | COMBO | No | "low"<br>"medium"<br>"high" |
| `reasoning_effort` | Sforzo di ragionamento. 'off' disabilita completamente il ragionamento. (predefinito: "off") | COMBO | No | "off"<br>"low"<br>"medium"<br>"high" |

Modelli solo testo — nessuna immagine o video di riferimento.

### Input di riferimento

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `images` | Immagine/i di riferimento facoltativa/e, inviate come URL. Slot espandibile: collegare da 1 a N input immagine (`image_1`, `image_2`, ...); il limite di quantità dipende dal modello selezionato (vedi le sezioni sui modelli). | IMAGE | No | da 0 a 20 (dipende dal modello: 8, 10 o 20) |
| `videos` | Video di riferimento facoltativo/i, inviati come URL. Slot espandibile: collegare da 1 a N input video (`video_1`, `video_2`, ...); il limite di quantità dipende dal modello selezionato (vedi le sezioni sui modelli). | VIDEO | No | da 0 a 4 (dipende dal modello) |

**Note:**

- **Modelli disponibili:** Le opzioni di modello disponibili vengono generate dinamicamente e includono modelli con capacità diverse. L'elenco completo dei 34 modelli è il seguente:
  - Anthropic: `anthropic/claude-opus-5`, `anthropic/claude-opus-4.8`, `anthropic/claude-opus-4.7`, `anthropic/claude-fable-5`, `anthropic/claude-sonnet-5`, `anthropic/claude-haiku-4.5`
  - OpenAI: `openai/gpt-5.6-sol-pro`, `openai/gpt-5.6-sol`, `openai/gpt-5.6-terra-pro`, `openai/gpt-5.6-terra`, `openai/gpt-5.6-luna-pro`, `openai/gpt-5.6-luna`, `openai/gpt-5.5-pro`, `openai/gpt-5.5`
  - Google: `google/gemini-3.5-flash`
  - xAI: `x-ai/grok-4.5`, `x-ai/grok-4.20`, `x-ai/grok-4.3`
  - DeepSeek: `deepseek/deepseek-v4-pro`, `deepseek/deepseek-v4-flash`, `deepseek/deepseek-v3.2`
  - Qwen: `qwen/qwen3.6-max-preview`, `qwen/qwen3.6-plus`, `qwen/qwen3.6-flash`
  - Mistral: `mistralai/mistral-large-2512`, `mistralai/mistral-medium-3-5`
  - Z.AI: `z-ai/glm-4.6`, `z-ai/glm-5`
  - Moonshot: `moonshotai/kimi-k3`, `moonshotai/kimi-k2.6`, `moonshotai/kimi-k2-thinking`
  - Perplexity: `perplexity/sonar-pro`, `perplexity/sonar-reasoning-pro`, `perplexity/sonar-deep-research`

- **Vincoli su immagini e video:** Il numero massimo di immagini e video di riferimento dipende dal modello selezionato. Il nodo genera un errore se il numero totale di immagini o video forniti supera il limite del modello. I modelli privi di supporto per immagini o video non mostrano gli slot di riferimento corrispondenti.

- **Comportamento del ragionamento:** Quando `reasoning_effort` è impostato su un valore diverso da "off", la richiesta chiede al provider di ragionare internamente senza restituire la traccia del ragionamento.

- **Comportamento del seed:** Il parametro `seed` ha un comportamento "control_after_generate", ovvero può essere impostato per cambiare automaticamente (ad esempio in modo casuale, incrementale o fisso) dopo ogni esecuzione del nodo, in base alle impostazioni del widget dell'utente.

- **System prompt:** Il parametro `system_prompt` è facoltativo ed è contrassegnato come parametro avanzato nell'interfaccia utente.

- **Casi di errore:** Il nodo genera un errore se il prompt è vuoto dopo la rimozione degli spazi bianchi, se OpenRouter restituisce un errore, se il modello selezionato rifiuta di rispondere o se la risposta non contiene scelte né messaggi. Un badge del prezzo sul nodo mostra una stima approssimativa del costo per 1K token in base al modello selezionato.

## Output

| Nome dell'output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `output` | La risposta testuale generata dal modello OpenRouter. | STRING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenRouterLLMNode/it.md)

---
**Source fingerprint (SHA-256):** `534ab9ecc12e35a23a4d8f3e10f4f82d95db8e902ac8a2f2ee0ea68246516f62`
