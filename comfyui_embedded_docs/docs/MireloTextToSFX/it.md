# Mirelo Text to SFX

Genera un effetto sonoro da una descrizione testuale con Mirelo SFX. Descrivi il suono stesso, non l'immagine a cui appartiene, e il nodo restituisce una singola traccia audio della durata richiesta. Usalo per foley, ambienti, impatti e brevi texture musicali senza girare o caricare video.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model` | Modello da utilizzare. Selezionando un modello vengono visualizzati i parametri specifici: `prompt`, `negative_prompt`, `duration` e `seed`. | DYNAMIC_COMBO | Sì | `"sfx-2.0"` |
| `prompt` | Descrivi il suono, non l'immagine. Da 1 a 2000 caratteri. | STRING | Sì | Da 1 a 2000 caratteri |
| `negative_prompt` | Suoni da evitare, come breve elenco separato da virgole. Può essere lasciato vuoto (predefinito: vuoto). Massimo 1000 caratteri. | STRING | Sì | Fino a 1000 caratteri |
| `duration` | Durata del suono in secondi. (predefinito: 5.0) | FLOAT | Sì | Da 0.1 a 600.0 (passo 0.1) |
| `seed` | Il seed per la richiesta. I risultati non sono deterministici, quindi lo stesso seed non ripete un suono. (predefinito: 42) | INT | Sì | Da 0 a 4294967295 |

Il nodo si interrompe con un errore quando `prompt` è vuoto o supera i 2000 caratteri, e quando `negative_prompt` supera i 1000 caratteri.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `AUDIO` | L'effetto sonoro generato, con durata pari a `duration`. | AUDIO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MireloTextToSFX/it.md)

---
**Source fingerprint (SHA-256):** `b09a9562cea636702acd9fc50feb38b272a558f8b8509da21f5fada2abd9fd48`
