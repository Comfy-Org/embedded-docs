# Ottieni immagine dal batch

Il nodo `ImageFromBatch` è progettato per estrarre un segmento specifico di immagini da un batch in base all'indice e alla lunghezza forniti. Consente un controllo più granulare sulle immagini raggruppate in batch, abilitando operazioni su singole immagini o su sottoinsiemi di immagini all'interno di un batch più grande.

## Input

| Campo | Descrizione | Tipo di dati |
| --- | --- | --- |
| `image` | Il batch di immagini da cui verrà estratto un segmento. Questo parametro è essenziale per specificare il batch di origine. | `IMAGE` |
| `batch_index` | L'indice iniziale all'interno del batch da cui inizia l'estrazione. Determina la posizione iniziale del segmento da estrarre dal batch. | `INT` |
| `length` | Il numero di immagini da estrarre dal batch a partire da `batch_index`. Questo parametro definisce la dimensione del segmento da estrarre. | `INT` |

## Output

| Campo | Descrizione | Tipo di dati |
| --- | --- | --- |
| `image` | Il segmento di immagini estratto dal batch specificato. Questo output rappresenta un sottoinsieme del batch originale, determinato dai parametri `batch_index` e `length`. | `IMAGE` |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageFromBatch/it.md)
