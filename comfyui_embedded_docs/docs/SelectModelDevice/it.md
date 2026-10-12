# Seleziona Dispositivo Modello

Il nodo Select Model Device consente di scegliere manualmente su quale dispositivo (CPU o una GPU specifica) viene eseguito un modello di diffusione. Può spostare un modello su un dispositivo diverso e gestisce automaticamente i conflitti con altri nodi multi-GPU. Selezionando `"default"` si ripristina il dispositivo originale scelto dal caricatore del modello.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model` | Il modello di diffusione da posizionare su un dispositivo specifico. | MODEL | Sì |  |
| `device` | Il dispositivo di destinazione per il modello. Le opzioni vengono generate dinamicamente in base ai dispositivi disponibili sulla macchina corrente. (predefinito: `"default"`) | COMBO | Sì | `"default"`<br>`"cpu"`<br>`"gpu:0"`<br>`"gpu:1"`<br>... (una voce `"gpu:N"` per ogni GPU rilevata) |

**Dettagli dei parametri:**
- `"default"`: Ripristina i dispositivi di caricamento e offload assegnati dal caricatore del modello, anche dopo una precedente chiamata a Select Model Device.
- `"cpu"`: Fissa sia il dispositivo di caricamento sia quello di offload sulla CPU.
- `"gpu:N"`: Fissa il dispositivo di caricamento all'N-esima GPU disponibile (ad esempio, `"gpu:0"` per la prima GPU). Il dispositivo di offload viene ripristinato alla scelta originale del caricatore.

**Note importanti:**
- Se il dispositivo richiesto non esiste sulla macchina corrente (ad esempio, un workflow creato su una macchina con 2 GPU viene aperto su una macchina con 1 GPU), il nodo passa il modello invariato e registra un messaggio invece di fallire. I valori `gpu:N` sconosciuti sono consentiti durante la validazione dell'input, così i workflow portatili non generano errori in anticipo.
- Se il modello è già sul dispositivo richiesto, il nodo usa un percorso rapido e non ricarica il modello.
- Quando il dispositivo richiesto differisce da quello su cui si trova già il modello di input, viene generato un nuovo modello usando la factory di ricaricamento del caricatore, in modo che il nuovo patcher possieda pesi indipendenti sul nuovo dispositivo.
- Se il caricatore del modello non supporta il multi-GPU (nessuna factory di ricaricamento), il nodo passa il modello invariato e registra un avviso.
- Quando un clone di MultiGPU CFG Split occupa già il dispositivo selezionato, quel clone viene rimosso, così due modelli non sono associati allo stesso dispositivo.
- Quando viene selezionato un dispositivo non predefinito (CPU o GPU), il nodo regola anche il compute dtype del modello su uno supportato da quel dispositivo.
- Posizionare questo nodo dopo un nodo che ha già consumato il modello (ad esempio, un KSampler) non è consigliato, perché qualsiasi stato modificato dal nodo precedente verrà osservato se il dispositivo corrisponde all'originale.

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `model` | Il modello di diffusione, ora posizionato sul dispositivo selezionato. Se il dispositivo non era valido o non disponibile, il modello viene passato invariato. | MODEL |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SelectModelDevice/it.md)

---
**Source fingerprint (SHA-256):** `d02a8bd9612861cf696f03969fe693088351de5a72ccbd4c1aed405b104eb71e`
