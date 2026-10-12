# ByteDance Seed

Genera risposte testuali con i modelli Seed 2.0 di ByteDance. Fornisci un prompt testuale e, facoltativamente, collega immagini o video per fornire al modello un contesto aggiuntivo. Il modello viene scelto tra le varianti Seed 2.0 disponibili e il nodo restituisce la risposta testuale del modello.

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `prompt` | Input testuale per il modello. (predefinito: "") | STRING | Sì | N/A |
| `model` | Il modello Seed utilizzato per generare la risposta. Questo selettore espone anche i sotto-parametri del modello. | DYNAMIC_COMBO | Sì | `"Seed 2.0 Pro"`<br>`"Seed 2.0 Lite"`<br>`"Seed 2.0 Mini"` |
| `seed` | Il seed controlla se il nodo deve essere rieseguito; i risultati non sono deterministici indipendentemente dal seed. (predefinito: 0) | INT | Sì | da 0 a 2147483647 |
| `system_prompt` | Istruzioni fondamentali che determinano il comportamento del modello. (predefinito: "") | STRING | No | N/A |

### Input del modello (condivisi da Seed 2.0 Pro, Seed 2.0 Lite e Seed 2.0 Mini)

Tutti e tre i modelli Seed espongono gli stessi sotto-parametri quando selezionati.

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `temperature` | Controlla la casualità. 0.0 è deterministico, valori più alti sono più casuali. (predefinito: 1.0) | FLOAT | Sì | da 0.0 a 2.0 (passo: 0.01) |

### Input di riferimento

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `images` | Immagini facoltative da usare come contesto per il modello. Fino a 20 immagini. Slot espandibile: collega da 1 a 20 elementi, ad es. da `image_1` a `image_20`. | IMAGE | No | da 0 a 20 immagini |
| `videos` | Video facoltativi da usare come contesto per il modello. Fino a 4 video. Slot espandibile: collega da 1 a 4 elementi, ad es. da `video_1` a `video_4`. | VIDEO | No | da 0 a 4 video |

**Nota:** Il parametro `model` è un combo dinamico che rivela i sotto-parametri di riferimento e temperatura una volta selezionato un modello. Gli slot `images` e `videos` sono espandibili, quindi puoi collegare diversi input per il contesto multimodale.

- `prompt` è obbligatorio e deve contenere almeno un carattere non di spaziatura; altrimenti viene generato un errore.
- È supportato un massimo di 20 immagini per richiesta. Questo limite conta tutte le immagini nei batch collegati.
- È supportato un massimo di 4 video per richiesta.
- Viene generato un errore se il modello restituisce una risposta vuota o se rifiuta di rispondere (viene riportato il testo del rifiuto).

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `output` | La risposta testuale generata dal modello Seed. | STRING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceSeedNode/it.md)

---
**Source fingerprint (SHA-256):** `23c9b0e9983a65ce859e2e92acfe71604297f16d711fa094a6617a9915a46020`
