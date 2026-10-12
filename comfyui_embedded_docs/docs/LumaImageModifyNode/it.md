# Luma Da Immagine a Immagine

Modifica le immagini in modo sincrono in base a un prompt testuale e al rapporto d'aspetto dell'immagine originale. Questo nodo riceve un'immagine di input e la trasforma in base al prompt fornito, usando un peso immagine configurabile per controllare quanto l'immagine originale venga alterata.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `image` | L'immagine di input da modificare | IMAGE | Sì | - |
| `prompt` | Prompt per la generazione dell'immagine (predefinito: "") | STRING | Sì | - |
| `image_weight` | Peso dell'immagine; più è vicino a 1.0, meno l'immagine verrà modificata (predefinito: 0.1). Internamente, questo valore viene invertito (1.0 - image_weight) e limitato tra 0.0 e 0.98. | FLOAT | No | 0.0-0.98 |
| `model` | Il modello Luma da usare per la modifica dell'immagine. Modelli diversi hanno costi diversi. | STRING | Sì | `"photon-flash-1"`<br>`"photon-1"`<br>`"photon"` |
| `seed` | Seed per determinare se il nodo deve essere rieseguito; i risultati effettivi non sono deterministici indipendentemente dal seed (predefinito: 0) | INT | No | 0-18446744073709551615 |

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|-----------|
| `image` | L'immagine modificata generata dal modello Luma | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaImageModifyNode/it.md)

---
**Source fingerprint (SHA-256):** `56b13600f6fb8cd6ff80bc8c8184db059273c2ef648630ff1ef10a7ed6b04b7c`
