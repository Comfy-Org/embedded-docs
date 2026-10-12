# LazyCache

LazyCache è una versione sperimentale e amatoriale di EasyCache che aggiunge il caching durante il campionamento per ridurre la computazione. È progettata per una compatibilità universale con i modelli in ComfyUI, sebbene in genere abbia prestazioni peggiori di EasyCache e possa funzionare meglio solo in rari casi.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model` | Il modello a cui aggiungere LazyCache. | MODEL | Sì | - |
| `reuse_threshold` | La soglia per riutilizzare i passaggi in cache. Predefinito: 0.2. | FLOAT | Sì | 0.0 - 3.0 (step 0.01) |
| `start_percent` | Il passo di campionamento relativo con cui iniziare a usare LazyCache. Predefinito: 0.15. | FLOAT | Sì | 0.0 - 1.0 (step 0.01) |
| `end_percent` | Il passo di campionamento relativo con cui terminare l'uso di LazyCache. Predefinito: 0.95. | FLOAT | Sì | 0.0 - 1.0 (step 0.01) |
| `verbose` | Indica se registrare informazioni dettagliate. Predefinito: False. | BOOLEAN | Sì | - |

Nota: `reuse_threshold`, `start_percent`, `end_percent` e `verbose` sono contrassegnati come input avanzati.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `model` | Il modello con la funzionalità LazyCache aggiunta. | MODEL |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LazyCache/it.md)

---
**Source fingerprint (SHA-256):** `78f9c13473567e068fc2be35b2f8f5aa459d43d3f13300a6ea858af98d3e2a44`
