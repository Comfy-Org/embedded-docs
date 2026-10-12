# QuiverTextToSVGNodeV2

Genera una grafica vettoriale scalabile (SVG) da un prompt testuale con Quiver AI. Immagini di riferimento opzionali e istruzioni di stile possono guidare la generazione.

Selezionando un `model` vengono visualizzati i parametri specifici del modello elencati di seguito, e anche il numero massimo di immagini di riferimento dipende dal modello selezionato.

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `model` | Modello da utilizzare per la generazione SVG. | DYNAMIC_COMBO | Sì | `"arrow-2"`<br>`"arrow-2-telos"`<br>`"arrow-1.1"`<br>`"arrow-1.1-max"`<br>`"arrow-preview"` |
| `prompt` | Descrizione testuale dell'output SVG desiderato. Deve contenere almeno un carattere (predefinito: vuoto). | STRING | Sì | Qualsiasi testo |
| `instructions` | Indicazioni aggiuntive su stile o formattazione. Parametro avanzato opzionale (predefinito: vuoto). | STRING | No | Qualsiasi testo |
| `reference_images` | Slot espandibile: collega una o più immagini di riferimento opzionali (`ref_1`, `ref_2`, ...) che guidano la generazione. Il numero massimo di immagini dipende dal modello selezionato. | IMAGE | No | Fino a 14<br>Fino a 4 |
| `width` | Larghezza della tela SVG di output (viewBox), in unità utente. Imposta sia `width` sia `height` per controllare dimensione e proporzioni dell'output; lascia uno dei due a 0 per far scegliere al modello, che di solito produce una tela quadrata. Parametro avanzato (predefinito: 0). | INT | Sì | da 0 a 8192 |
| `height` | Altezza della tela SVG di output (viewBox), in unità utente. Imposta sia `width` sia `height` per controllare dimensione e proporzioni dell'output; lascia uno dei due a 0 per far scegliere al modello, che di solito produce una tela quadrata. Parametro avanzato (predefinito: 0). | INT | Sì | da 0 a 8192 |
| `seed` | Seed per determinare se il nodo deve essere rieseguito; i risultati effettivi sono non deterministici indipendentemente dal valore del seed. Questo parametro ha la funzionalità "control after generate" (predefinito: 42). | INT | Sì | da 0 a 2147483647 |

### Input specifici del modello

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `reasoning_effort` | Quanto ragionamento dedica il modello prima di disegnare. Livelli più alti migliorano il dettaglio e costano più token. Usato solo dai modelli `"arrow-2"` e `"arrow-2-telos"` (predefinito: `"high"`). | COMBO | Sì | `"low"`<br>`"medium"`<br>`"high"`<br>`"xhigh"` |
| `temperature` | Controllo della casualità. Valori più alti aumentano la casualità. Non usato dal modello `"arrow-2-telos"`. Parametro avanzato (predefinito: 1.0). | FLOAT | Sì | da 0.0 a 2.0 (passo 0.1) |
| `top_p` | Parametro di campionamento nucleus. Non usato dal modello `"arrow-2-telos"`. Parametro avanzato (predefinito: 1.0). | FLOAT | Sì | da 0.05 a 1.0 (passo 0.05) |
| `presence_penalty` | Penalità di presenza dei token. Non usato dal modello `"arrow-2-telos"`. Parametro avanzato (predefinito: 0.0). | FLOAT | Sì | da -2.0 a 2.0 (passo 0.1) |

**Nota:** Il numero massimo di `reference_images` è 14 per `"arrow-2"`, `"arrow-2-telos"` e `"arrow-1.1-max"`, e 4 per `"arrow-1.1"` e `"arrow-preview"`. Lascia `width` o `height` a 0 per far scegliere al modello la dimensione della tela.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `SVG` | L'output SVG generato. | SVG |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/QuiverTextToSVGNodeV2/it.md)

---
**Source fingerprint (SHA-256):** `809d2e5bd62386723e36b7649af2f8dda40b437dc39bac9236529db5b52d32e9`
