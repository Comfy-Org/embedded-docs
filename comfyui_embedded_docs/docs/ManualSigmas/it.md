# ManualSigmas

Il nodo ManualSigmas consente di definire manualmente una sequenza personalizzata di livelli di rumore (sigmas) per il processo di campionamento. Si inserisce un elenco di numeri come stringa e il nodo li converte in un tensore SIGMAS che può essere utilizzato da altri nodi di campionamento. È utile per test o per creare specifiche schedulazioni del rumore.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `sigmas` | Una stringa contenente i valori sigma. Il nodo estrae tutti i numeri da questa stringa, inclusi decimali e valori negativi. Ad esempio, "1, 0.5, 0.1" o "1 0.5 0.1". Predefinito: "1, 0.5". | STRING | Sì | Qualsiasi valore numerico separato da virgole o spazi |

Nota: questo nodo è contrassegnato come sperimentale.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `sigmas` | Un tensore contenente la sequenza di valori sigma estratti dalla stringa di input. | SIGMAS |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ManualSigmas/it.md)

---
**Source fingerprint (SHA-256):** `19d938ef0eac7343a3138393a039f63632b0763e3884636653c06b91b6f44ed6`
