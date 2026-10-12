# Cache Qwen Image 2.1

Il nodo QwenImage21Cache configura la cache del prefisso KV del modello Qwen-Image 2.1: dove vengono memorizzate le chiavi e i valori in cache e con quale precisione. I token di testo e di riferimento vengono calcolati una sola volta e riutilizzati tra i passaggi di campionamento, ed è da qui che deriva la maggior parte dell'accelerazione nei workflow di modifica; questo nodo consente di scambiare memoria con velocità oppure di escludere completamente la cache. Questo nodo è contrassegnato come sperimentale.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model` | Il modello Qwen-Image 2.1 di cui viene configurata la cache del prefisso. | MODEL | Sì | - |
| `device` | Dove vengono memorizzate le chiavi e i valori in cache. `"auto"` (predefinito) usa prima la VRAM libera e poi la RAM; `"gpu"` archivia la cache nella VRAM; `"cpu"` la archivia nella RAM ed esegue il prefetch in background rispetto al calcolo, con una perdita di velocità minima; `"off"` ricalcola il prefisso a ogni passaggio, il che è più lento ma è l'unico modo per escludere la cache. | COMBO | Sì | `"auto"`<br>`"gpu"`<br>`"cpu"`<br>`"off"` |
| `dtype` | Precisione di memorizzazione della cache. `"default"` è senza perdita; `"int8"` dimezza la cache con una precisione all'incirca pari a bf16; `"int4"` la riduce a un quarto ma raddoppia all'incirca l'errore per passaggio. | COMBO | Sì | `"default"`<br>`"int8"`<br>`"int4"` |

Quando la cache non entra nella memoria disponibile, il modello ricalcola il prefisso invece di espellere lo slot dell'altro ramo, quindi un'impostazione sovradimensionata degrada la velocità anziché far fallire l'esecuzione.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `MODEL` | Il modello con il dispositivo e la precisione della cache applicati, pronto per il campionamento. | MODEL |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/QwenImage21Cache/it.md)

---
**Source fingerprint (SHA-256):** `0c10cdb465d1ee4063273ffbb4913def3830f7e329694cd0a2e292d6f3c37ae4`
