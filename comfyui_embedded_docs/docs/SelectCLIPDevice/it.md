# Seleziona Dispositivo CLIP

## Panoramica

Il nodo Select CLIP Device consente di scegliere su quale dispositivo (CPU o una GPU specifica) viene eseguito il codificatore di testo CLIP. Per impostazione predefinita, il dispositivo viene assegnato dal caricatore del modello, ma è possibile sovrascriverlo per usare la CPU o una GPU particolare. Se il dispositivo richiesto non esiste sulla macchina, il nodo restituisce semplicemente il CLIP inalterato e registra un messaggio anziché generare un errore.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `clip` | Il codificatore di testo CLIP da assegnare a un dispositivo specifico. | CLIP | Sì |  |
| `device` | Il dispositivo su cui posizionare il codificatore di testo CLIP. `"default"` ripristina il dispositivo assegnato dal caricatore. `"cpu"` fissa sia il dispositivo di caricamento sia quello di offload sulla CPU. `"gpu:N"` fissa il dispositivo di caricamento sull'N-esima GPU disponibile (predefinito: `"default"`). | COMBO | Sì | `"default"`<br>`"cpu"`<br>`"gpu:0"`<br>`"gpu:1"`<br>`"gpu:2"`<br>`"gpu:3"`<br>`"gpu:4"`<br>`"gpu:5"`<br>`"gpu:6"`<br>`"gpu:7"` |

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `clip` | Il codificatore di testo CLIP assegnato al dispositivo selezionato, oppure il CLIP originale restituito inalterato se il dispositivo richiesto non è disponibile. | CLIP |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SelectCLIPDevice/it.md)

---
**Source fingerprint (SHA-256):** `92af94d9f5eea27095cc008debdf7339d26888a0e2cc8bd71ae9c9ba8718eb01`
