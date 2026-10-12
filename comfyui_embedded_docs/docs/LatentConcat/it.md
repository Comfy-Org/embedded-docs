# Concatena Latent

Il nodo LatentConcat combina due campioni latenti unendoli lungo una dimensione scelta. Riceve due input latenti e li concatena lungo l'asse x, y o t, con l'opzione di controllare quale campione viene prima. Il nodo adatta automaticamente la dimensione del batch del secondo input per farla corrispondere al primo prima di eseguire la concatenazione.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `samples1` | Il primo campione latente da concatenare | LATENT | Sì | - |
| `samples2` | Il secondo campione latente da concatenare | LATENT | Sì | - |
| `dim` | La dimensione lungo la quale concatenare i campioni latenti. I valori positivi (x, y, t) posizionano samples1 prima di samples2 nel risultato. I valori negativi (-x, -y, -t) posizionano samples2 prima di samples1. La mappatura delle dimensioni è: x = larghezza, y = altezza, t = tempo/frame | COMBO | Sì | `"x"`<br>`"-x"`<br>`"y"`<br>`"-y"`<br>`"t"`<br>`"-t"` |

**Nota:** Il secondo campione latente (`samples2`) viene ripetuto automaticamente secondo necessità per corrispondere alla dimensione del batch del primo campione latente (`samples1`) prima della concatenazione.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `output` | I campioni latenti concatenati risultanti dalla combinazione dei due campioni di input lungo la dimensione specificata | LATENT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentConcat/it.md)

---
**Source fingerprint (SHA-256):** `dfe27f76ad12e16623d62c9e7f0b2772df6ecadb543a4eee430bc38ab04a12f2`
