# Anthropic Claude

Genera risposte testuali dai modelli Claude di Anthropic. Fornisci un prompt testuale e, facoltativamente, una o più immagini per il contesto multimodale; il nodo restituisce la risposta testuale generata dal modello.

## Input

Gli input sono raggruppati in impostazioni comuni, impostazioni specifiche del modello che compaiono quando viene selezionato un modello e immagini di riferimento opzionali.

### Input comuni

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `model` | Il modello Claude utilizzato per generare la risposta. Selezionando un modello vengono mostrate di seguito le impostazioni specifiche del modello. | DYNAMIC_COMBO | Sì | `"Opus 5.5"`<br>`"Opus 5"`<br>`"Opus 4.8"`<br>`"Fable 5.1"`<br>`"Fable 5"`<br>`"Sonnet 5.5"`<br>`"Sonnet 5"`<br>`"Opus 4.7"`<br>`"Opus 4.6"`<br>`"Sonnet 4.6"`<br>`"Sonnet 4.5"`<br>`"Haiku 4.5"` |
| `prompt` | Input testuale per il modello. (predefinito: stringa vuota) | STRING | Sì | N/D |
| `seed` | Il seed controlla se il nodo deve essere rieseguito; i risultati non sono deterministici indipendentemente dal seed. (predefinito: 0) | INT | Sì | da 0 a 2147483647 |
| `system_prompt` | Istruzioni di base che determinano il comportamento del modello. (predefinito: stringa vuota) | STRING | No | N/D |

### Input di Opus 5.5, Opus 5, Fable 5.1 e Fable 5

Questi quattro modelli condividono le stesse impostazioni. Non espongono un'impostazione della temperatura e il ragionamento è sempre abilitato.

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `max_tokens` | Numero massimo di token da generare (include i token di ragionamento quando abilitati). (predefinito: 32768) | INT | Sì | da 1024 a 64000 (Opus 5.5)<br>da 4096 a 64000 (Opus 5, Fable 5.1, Fable 5) |
| `reasoning_effort` | Livello di impegno del pensiero esteso. Il ragionamento è sempre abilitato per questo modello. (predefinito: `"high"`) | COMBO | Sì | `"low"`<br>`"medium"`<br>`"high"`<br>`"xhigh"`<br>`"max"` |

### Input di Opus 4.8, Sonnet 5.5 e Sonnet 5

Questi tre modelli condividono le stesse impostazioni. Non espongono un'impostazione della temperatura.

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `max_tokens` | Numero massimo di token da generare (include i token di ragionamento quando abilitati). (predefinito: 32768) | INT | Sì | da 1024 a 64000 (Sonnet 5.5)<br>da 4096 a 64000 (Opus 4.8, Sonnet 5) |
| `reasoning_effort` | Livello di impegno del pensiero esteso. `"off"` disabilita il ragionamento. (predefinito: `"off"`) | COMBO | Sì | `"off"`<br>`"low"`<br>`"medium"`<br>`"high"`<br>`"xhigh"`<br>`"max"` |

### Input di Opus 4.7, Opus 4.6, Sonnet 4.6 e Sonnet 4.5

Questi quattro modelli condividono le stesse impostazioni.

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `max_tokens` | Numero massimo di token da generare (include i token di ragionamento quando abilitati). (predefinito: 32768) | INT | Sì | da 4096 a 64000 |
| `temperature` | Controlla la casualità. 0.0 è deterministico, 1.0 è il massimo della casualità. Ignorato per Opus 4.7 e per qualsiasi modello quando `reasoning_effort` è impostato. (predefinito: 1.0) | FLOAT | Sì | da 0.0 a 1.0 (passo: 0.01) |
| `reasoning_effort` | Livello di impegno del pensiero esteso. `"off"` disabilita il ragionamento. (predefinito: `"off"`) | COMBO | Sì | `"off"`<br>`"low"`<br>`"medium"`<br>`"high"` |

`reasoning_effort` offre `"off"`, `"low"`, `"medium"` e `"high"` su tutti e quattro i modelli. Opus 4.7, Opus 4.6 e Sonnet 4.6 accettano inoltre `"max"`, e Opus 4.7 accetta anche `"xhigh"`.

### Input di Haiku 4.5

Questo modello non espone un'impostazione `reasoning_effort`.

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `max_tokens` | Numero massimo di token da generare (include i token di ragionamento quando abilitati). (predefinito: 32768) | INT | Sì | da 4096 a 64000 |
| `temperature` | Controlla la casualità. 0.0 è deterministico, 1.0 è il massimo della casualità. Ignorato per Opus 4.7 e per qualsiasi modello quando `reasoning_effort` è impostato. (predefinito: 1.0) | FLOAT | Sì | da 0.0 a 1.0 (passo: 0.01) |

### Input di riferimento

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `images` | Immagini opzionali da usare come contesto per il modello. Fino a 20 immagini. Slot espandibile: collega da 1 a 20 elementi (`image_1` ... `image_20`). | IMAGE | No | da 0 a 20 immagini |

### Vincoli dei parametri

- **Limite immagini:** È possibile fornire un massimo di 20 immagini per richiesta. Collegare più di 20 immagini genera un errore.
- **Prompt obbligatorio:** Il prompt deve contenere almeno un carattere non di spaziatura. Un prompt vuoto genera un errore di convalida.
- **Gestione della temperatura:** Quando il pensiero è abilitato, l'API Anthropic richiede che la temperatura non sia impostata (il valore predefinito è 1.0). Opus 5.5, Opus 5, Opus 4.8, Fable 5.1, Fable 5, Sonnet 5.5 e Sonnet 5 non espongono un'impostazione della temperatura. Opus 4.7 ignora `temperature` e qualsiasi modello con `reasoning_effort` impostato su un valore diverso da `"off"` la ignora a sua volta.
- **Comportamento di ragionamento/pensiero:** L'impostazione `reasoning_effort` controlla se il pensiero è abilitato. Opus 5.5, Opus 5, Fable 5.1 e Fable 5 hanno sempre il ragionamento abilitato. Haiku 4.5 non supporta il ragionamento. Quando il pensiero è abilitato, il nodo usa la modalità di pensiero appropriata per il modello selezionato, adattiva o basata su budget. In modalità budget, il budget di token di ragionamento viene limitato per lasciare almeno 1024 token alla risposta effettiva. Quando `reasoning_effort` è `"off"` su Sonnet 5.5, la richiesta usa il pensiero `between_tools` invece del pensiero disabilitato, quindi la risposta continua a non contenere ragionamento.
- **Minimo di `max_tokens`:** `max_tokens` accetta valori a partire da 1024 su Opus 5.5 e Sonnet 5.5, e da 4096 su tutti gli altri modelli.
- **Rifiuto per sicurezza:** Se Claude rifiuta di rispondere alla richiesta per motivi di sicurezza, il nodo genera un errore che invita a riformulare il prompt o a provare un modello diverso.
- **Testo di output:** I blocchi di pensiero e ragionamento non sono inclusi nell'output; viene restituito solo il testo generato.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `output` | La risposta testuale generata dal modello Claude. I blocchi di pensiero/ragionamento non sono inclusi. Se non viene generato alcun testo, restituisce "Empty response from Claude model." | STRING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ClaudeNode/it.md)

---
**Source fingerprint (SHA-256):** `35b737da0f4c3a9da72910bf2053b18ae6a5c60989dc9607b61037623bc94e38`
