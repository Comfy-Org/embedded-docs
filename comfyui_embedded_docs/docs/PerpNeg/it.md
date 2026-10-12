# Perp-Neg (DEPRECATO da Perp-Neg Guider)

Il nodo PerpNeg applica una guida negativa perpendicolare al processo di campionamento di un modello. Questo nodo modifica la funzione di configurazione del modello per regolare le previsioni del rumore utilizzando condizionamento negativo e fattori di scala. È stato deprecato e sostituito dal nodo PerpNegGuider per funzionalità migliorate.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model` | Il modello a cui applicare la guida negativa perpendicolare | MODEL | Sì | - |
| `empty_conditioning` | Condizionamento vuoto utilizzato per i calcoli della guida negativa | CONDITIONING | Sì | - |
| `neg_scale` | Fattore di scala per la guida negativa (predefinito: 1.0) | FLOAT | No | 0.0 - 100.0 |

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `model` | Il modello modificato con la guida negativa perpendicolare applicata | MODEL |

**Nota**: Questo nodo è deprecato ed è stato sostituito da PerpNegGuider. È contrassegnato come sperimentale e non dovrebbe essere utilizzato in flussi di lavoro di produzione.

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PerpNeg/it.md)

---
**Source fingerprint (SHA-256):** `016bd9a9a9ee42855c15b3e582ada03557297df9a786d977439edd9d3363a5ba`
