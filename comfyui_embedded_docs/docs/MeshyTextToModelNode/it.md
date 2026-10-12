# Meshy: Text to Model

Il nodo Meshy: Text to Model utilizza l'API Meshy per generare un modello 3D da una descrizione testuale. Invia una richiesta all'API con il tuo prompt e le impostazioni, quindi attende il completamento della generazione e scarica i file del modello risultanti.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `model` | Specifica la versione del modello AI da utilizzare per la generazione. | COMBO | Sì | `"meshy-7.1"`<br>`"meshy-7"`<br>`"meshy-6"`<br>`"latest"` |
| `prompt` | La descrizione testuale del modello 3D che desideri generare. Deve essere compresa tra 1 e 600 caratteri. Il valore predefinito è una stringa vuota. | STRING | Sì | 1 - 600 caratteri |
| `style` | Lo stile artistico per il modello 3D generato. | COMBO | Sì | `"realistic"` |
| `should_remesh` | Se impostato su false, restituisce una mesh triangolare non elaborata. Selezionando "true" vengono rivelati parametri aggiuntivi per la topologia e il numero di poligoni target. | DYNAMIC_COMBO | Sì | `"true"`<br>`"false"` |
| `topology` | Il tipo di poligono target per il modello rimagliato. Questo parametro è disponibile solo quando `should_remesh` è impostato su "true". | COMBO | No* | `"triangle"`<br>`"quad"` |
| `target_polycount` | Il numero target di poligoni per il modello rimagliato. Il valore predefinito è 300000. Questo parametro è disponibile solo quando `should_remesh` è impostato su "true". | INT | No* | 100 - 300000 |
| `symmetry_mode` | Controlla la simmetria nel modello generato. Questo è un parametro avanzato. Le opzioni sono `"auto"`, `"on"` e `"off"`. | COMBO | Sì | `"auto"`<br>`"on"`<br>`"off"` |
| `pose_mode` | Specifica la modalità posa per il modello generato. Una stringa vuota significa che non viene richiesta una posa specifica. Questo è un parametro avanzato. | COMBO | Sì | `""`<br>`"A-pose"`<br>`"T-pose"` |
| `seed` | Il seed controlla se il nodo deve essere rieseguito; i risultati non sono deterministici indipendentemente dal seed. Il valore predefinito è 0. | INT | Sì | 0 - 2147483647 |
| `ultra_mode` | Esegue un passaggio di rifinitura extra per una geometria a maggiore fedeltà con dettagli superficiali più fini. Il valore predefinito è false. | BOOLEAN | Sì | true<br>false |
| `ultra_resolution` | Risoluzione del passaggio ultra: `"2k"` lo esegue a 2048³, `"4k"` a 4096³ per il massimo dettaglio superficiale. 4k richiede il modello `"meshy-7.1"` o `"latest"`. Utilizzato solo quando `ultra_mode` è abilitato (predefinito: `"2k"`). | COMBO | No | `"2k"`<br>`"4k"` |

*Nota: I parametri `topology` e `target_polycount` sono disponibili in modo condizionale. Appaiono solo quando il parametro `should_remesh` è impostato su "true".

Quando `ultra_mode` è abilitato, il parametro `model` deve essere impostato su `"meshy-7.1"`, `"meshy-7"` o `"latest"`; qualsiasi altro modello genera un errore. Con `"meshy-7"` il passaggio ultra viene sempre eseguito a 2048³, e la risoluzione ultra `"4k"` richiede `"meshy-7.1"` o `"latest"`.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|-----------|
| `model_file` | Il nome file del modello GLB generato. Questo output è fornito per retrocompatibilità. | STRING |
| `meshy_task_id` | L'identificatore univoco per l'attività dell'API Meshy. | MESHY_TASK_ID |
| `GLB` | Il file del modello 3D generato in formato GLB. | FILE3DGLB |
| `FBX` | Il file del modello 3D generato in formato FBX. | FILE3DFBX |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyTextToModelNode/it.md)

---
**Source fingerprint (SHA-256):** `a02a5ae28bcae343c628d11ba3efa952b61b8bdf867669f58f1beb0f7c9e49f9`
