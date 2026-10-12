# SetModelHooksOnCond

Questo nodo collega hook personalizzati ai dati di condizionamento, consentendo di intercettare e modificare il processo di condizionamento durante l'esecuzione del modello. Riceve un insieme di hook e li applica ai dati di condizionamento forniti, abilitando una personalizzazione avanzata del flusso di generazione da testo a immagine. I dati di condizionamento modificati con gli hook collegati vengono quindi restituiti per l'uso nelle fasi di elaborazione successive.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `conditioning` | I dati di condizionamento a cui verranno collegati gli hook | CONDITIONING | Sì | - |
| `hooks` | Le definizioni degli hook che verranno applicate ai dati di condizionamento | HOOKS | Sì | - |

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `conditioning` | I dati di condizionamento modificati con gli hook collegati | CONDITIONING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SetModelHooksOnCond/it.md)

---
**Source fingerprint (SHA-256):** `a6e63a3a4d94d1b66a82d449af5ae001e1fc4a04f0f81d9fb5c4f8c13e5bdf8b`
