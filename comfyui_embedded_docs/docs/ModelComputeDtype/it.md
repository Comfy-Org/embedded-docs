# ModelComputeDtype

Il nodo ModelComputeDtype modifica il tipo di dato computazionale (precisione) utilizzato da un modello durante l'elaborazione. Crea una copia del modello di input e applica l'impostazione di precisione selezionata, il che può aiutare a ottimizzare l'utilizzo della memoria e le prestazioni in base all'hardware. È utile per il debug e il test di diverse configurazioni di precisione.

## Input

| Parametro | Descrizione | Tipo di dato | Richiesto | Intervallo |
| --- | --- | --- | --- | --- |
| `model` | Il modello di input da modificare con un nuovo tipo di dato computazionale | MODEL | Sì | - |
| `dtype` | Il tipo di dato computazionale da applicare al modello (predefinito: "default"). Questo parametro è contrassegnato come opzione avanzata. | COMBO | Sì | "default"<br>"fp32"<br>"fp16"<br>"bf16" |

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `model` | Il modello modificato con il nuovo tipo di dato computazionale applicato | MODEL |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelComputeDtype/it.md)

---
**Source fingerprint (SHA-256):** `ad9c39e1217fd2e343ad4f49df9d1acabbc4708966dadec5340bb975adb59854`
