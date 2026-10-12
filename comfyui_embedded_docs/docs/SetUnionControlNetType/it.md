# SetUnionControlNetType

Il nodo SetUnionControlNetType consente di scegliere quale tipo di controllo utilizza una rete di controllo. Prende una rete di controllo esistente e crea una copia modificata con il tipo di controllo selezionato, lasciando invariata la rete di controllo originale. Quando viene selezionato "auto", il tipo di controllo memorizzato viene cancellato in modo che il tipo possa essere rilevato automaticamente.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `control_net` | La rete di controllo da modificare con una nuova impostazione di tipo | CONTROL_NET | Sì | - |
| `type` | Il tipo di controllo da applicare. Usa "auto" per il rilevamento automatico del tipo oppure seleziona un tipo di controllo specifico tra le opzioni disponibili (predefinito: "auto") | COMBO | Sì | `"auto"`<br>`"openpose"`<br>`"depth"`<br>`"hed/pidi/softedge"`<br>`"canny"`<br>`"scribble"`<br>`"seg"`<br>`"tile"`<br>`"inpaint"`<br>`"lineart"`<br>`"blur"`<br>`"mlsd"`<br>`"normalbae"`<br>`"mask"` |

Quando `type` è impostato su `"auto"`, il nodo cancella il tipo di controllo memorizzato in modo che il tipo possa essere rilevato automaticamente. Quando viene selezionato un tipo specifico, il nodo memorizza il tipo di controllo corrispondente nella rete di controllo copiata. La rete di controllo di input non viene mai modificata sul posto; viene invece restituita una copia modificata.

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `control_net` | La rete di controllo modificata con l'impostazione del tipo specificato applicata | CONTROL_NET |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SetUnionControlNetType/it.md)

---
**Source fingerprint (SHA-256):** `db4b1a3cebafcff2be3172faa09cecbd5e19331376491c491cbe359013ed3da3`
