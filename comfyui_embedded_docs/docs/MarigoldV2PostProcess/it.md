# MarigoldV2PostProcess

Questo nodo converte una previsione Marigold V2 decodificata in un'immagine visualizzabile. Prende il tensore di previsione grezzo e lo formatta in base al tipo di previsione: profondità normalizzata (gli oggetti vicini appaiono luminosi), normali di superficie a lunghezza unitaria oppure albedo sRGB.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `image` | La previsione Marigold V2 decodificata da convertire in un'immagine visualizzabile. | IMAGE | Sì | - |
| `prediction` | Il tipo di previsione contenuto nell'input, che determina come vengono convertiti i dati. `"depth"` normalizza i valori di profondità in modo che le superfici vicine siano luminose e quelle lontane scure, quindi copia il risultato in tutti e tre i canali di colore. `"normals"` riscala i valori nell'intervallo -1..1, li normalizza in normali di superficie a lunghezza unitaria e li riporta a 0..1. `"albedo"` applica una conversione da lineare a sRGB ai valori. | COMBO | Sì | `"depth"`<br>`"normals"`<br>`"albedo"` |

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|-----------|
| `IMAGE` | L'immagine elaborata nella rappresentazione selezionata: profondità normalizzata (scala di grigi ripetuta su tre canali), normali di superficie a lunghezza unitaria oppure albedo sRGB. | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MarigoldV2PostProcess/it.md)

---
**Source fingerprint (SHA-256):** `848b29e2dfcd34c44cf9707b9b26cb13c18e82bb16618a15afbe477a1d620e1e`
