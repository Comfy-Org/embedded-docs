# SAM3 Traccia in Maschera

## Panoramica

Seleziona oggetti tracciati specifici da una sessione di tracciamento SAM3 in base ai loro numeri di indice e li combina in un'unica maschera di output. Ciò consente di scegliere quali oggetti mantenere e quali ignorare dai risultati del tracciamento.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `track_data` | L'output dei dati di tracciamento da un nodo tracker SAM3, contenente le maschere impacchettate e le dimensioni originali dell'immagine. | SAM3TRACKDATA | Sì | N/A |
| `object_indices` | Indici degli oggetti separati da virgole da includere nella maschera di output (ad es. '0,2,3'). Se lasciato vuoto, vengono inclusi tutti gli oggetti tracciati. | STRING | No | Qualsiasi elenco di numeri interi separati da virgola |

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `masks` | Una singola maschera binaria per ogni frame, in cui gli oggetti selezionati sono combinati in un'unica maschera. Se non viene selezionato alcun oggetto o non esistono dati di tracciamento, restituisce una maschera di zeri. | MASK |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SAM3_TrackToMask/it.md)

---
**Source fingerprint (SHA-256):** `77c9f5142f2078fabb81e58979df01ad9ec41d3de953939570bebb4f2687f8ad`
