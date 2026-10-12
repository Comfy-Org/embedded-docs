# Rimuovi immagini duplicate

Questo nodo rimuove da un batch le immagini duplicate o molto simili. Funziona creando un hash percettivo per ogni immagine — una semplice impronta numerica basata sul suo contenuto visivo — e poi confrontandoli. Le immagini i cui hash risultano più simili di una soglia impostata vengono considerate duplicate e filtrate.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `images` | Il batch di immagini da elaborare per la deduplicazione. | IMAGE | Sì | - |
| `similarity_threshold` | Soglia di similarità (0-1). Un valore più alto richiede una maggiore similarità. Le immagini con similarità superiore a questa soglia vengono considerate duplicate. (predefinito: 0.95) | FLOAT | No | 0.0 - 1.0 |

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `images` | L'elenco filtrato di immagini con i duplicati rimossi. | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageDeduplication/it.md)

---
**Source fingerprint (SHA-256):** `d0c40694853c3dd0952d58b920bf735a4626cb2921928bb982ba479dc58fbe53`
