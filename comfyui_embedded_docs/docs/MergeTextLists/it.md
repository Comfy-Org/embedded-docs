# MergeTextLists

Questo nodo unisce più elenchi di testo in un unico elenco combinato. È progettato per ricevere input di testo come elenchi e concatenarli insieme. Il nodo registra il numero totale di testi nell'elenco unito.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `texts` | Gli elenchi di testo da unire. È possibile collegare più elenchi all'input e verranno concatenati in uno solo. | STRING | Sì | N/A |

**Nota:** Questo nodo è configurato come processo di gruppo (`is_group_process = True`), il che significa che gestisce automaticamente input di più elenchi concatenandoli prima dell'esecuzione della funzione di elaborazione principale.

**Nota:** Questo nodo è deprecato ed è stato sostituito dal nodo Create List.

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `texts` | L'elenco unico e unito contenente tutti i testi di input. | STRING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MergeTextLists/it.md)

---
**Source fingerprint (SHA-256):** `bb7f45725c2c41a18d8cd3040d093c11be2ceb03cf1849385aa55d12fd9eb555`
