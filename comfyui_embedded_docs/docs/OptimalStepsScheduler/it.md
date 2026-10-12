# OptimalStepsScheduler

Il nodo OptimalStepsScheduler crea una pianificazione del rumore (una sequenza di valori sigma) da utilizzare durante il campionamento di diffusione. Seleziona i livelli di rumore di base dal tipo di modello selezionato, regola la pianificazione quando la denoising è applicata solo parzialmente e interpola i livelli in modo che i sigma restituiti corrispondano al numero di passaggi richiesto.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model_type` | Il tipo di modello di diffusione da utilizzare per il calcolo del livello di rumore. Ogni opzione utilizza la propria tabella predefinita di livelli di rumore. | COMBO | Sì | "FLUX"<br>"Wan"<br>"Chroma" |
| `steps` | Il numero totale di passaggi di campionamento da calcolare (predefinito: 20). | INT | Sì | 3 to 1000 |
| `denoise` | Controlla la forza di denoising, che regola il numero effettivo di passaggi (predefinito: 1.0). | FLOAT | Sì | 0.0 to 1.0 (step: 0.01) |

**Nota:** La tabella dei livelli di rumore di base per il `model_type` selezionato viene ricampionata con interpolazione log-lineare ogni volta che la sua lunghezza non è uguale a `steps + 1`, in modo che l'output corrisponda sempre al numero di passaggi richiesto.

**Nota:** Quando `denoise` è inferiore a 1.0, il nodo utilizza `round(steps * denoise)` come numero totale di passaggi effettivi e mantiene solo la coda corrispondente della pianificazione. Se `denoise` è 0.0 o inferiore, il nodo restituisce un tensore vuoto.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `sigmas` | Una sequenza di valori sigma che rappresenta la pianificazione del rumore per il campionamento di diffusione. Il valore finale nella sequenza è sempre impostato a 0. | SIGMAS |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OptimalStepsScheduler/it.md)

---
**Source fingerprint (SHA-256):** `fd48c94ca16c8a3d8e6f0138018e7b13c15d100d6147807bcb23d838899045b7`
