# OpenAIChatConfig

Il nodo OpenAIChatConfig definisce opzioni avanzate che controllano il modo in cui il nodo OpenAI Chat genera le risposte. Consente di impostare la strategia di troncamento, limitare il numero di token di output, fornire istruzioni personalizzate e scegliere quanto ragionamento il modello deve applicare prima di rispondere.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `truncation` | La strategia di troncamento da usare per la risposta del modello. auto: se il contesto di questa risposta e delle precedenti supera la dimensione della finestra di contesto del modello, il modello troncherà la risposta per adattarla alla finestra di contesto eliminando gli elementi di input al centro della conversazione. disabled: se una risposta del modello supererà la dimensione della finestra di contesto per un modello, la richiesta fallirà con un errore 400 (predefinito: "auto") | COMBO | Sì | "auto"<br>"disabled" |
| `max_output_tokens` | Un limite massimo al numero di token che possono essere generati per una risposta, inclusi i token di output visibili e i token di ragionamento (predefinito: 4096) | INT | No | 16 a 16384 |
| `instructions` | Istruzioni per il modello su come generare la risposta (input multilinea supportato) | STRING | No | - |
| `reasoning_effort` | Quanto il modello ragiona prima di rispondere. "default" lascia la scelta al modello. I livelli supportati variano in base al modello: GPT-6 Astra low-max, GPT-6 Sol/Luna e GPT-5.6 none-max (senza minimal), GPT-5.5 none-xhigh, GPT-5.5 Pro medium-xhigh, GPT-5 minimal-high, serie o low-high; GPT-4.1 non ha ragionamento. I livelli non supportati vengono rifiutati prima che la richiesta venga inviata. (predefinito: "default") | COMBO | No | "default"<br>"none"<br>"minimal"<br>"low"<br>"medium"<br>"high"<br>"xhigh"<br>"max" |

Nota: sebbene `top_p` e `temperature` siano elencati come proprietà nella specifica API, non sono supportati da tutti i modelli e pertanto non sono esposti come input.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `OPENAI_CHAT_CONFIG` | Oggetto di configurazione contenente le impostazioni avanzate specificate, per l'uso con i nodi OpenAI Chat | OPENAI_CHAT_CONFIG |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIChatConfig/it.md)

---
**Source fingerprint (SHA-256):** `4237ad464230c464223c184eab38c7d707a29ba5f47da04c2ec2034cd4347207`
