# Bria Espandi immagine

Bria Expand Image espande un'immagine oltre i suoi bordi originali generando nuovi contenuti con Bria. Ti consente di scegliere un rapporto d'aspetto target, un rapporto personalizzato oppure di definire una tela con posizionamento manuale dell'immagine originale. L'espansione può essere guidata con un prompt testuale e Bria ne genererà uno automaticamente se il prompt viene lasciato vuoto.

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `image` | L'immagine di input da espandere. | IMAGE | Sì | — |
| `expand_mode` | Forma target dell'immagine espansa: un rapporto d'aspetto predefinito, un rapporto personalizzato oppure posizionamento manuale dell'immagine originale su una tela. La modalità `manual` è l'unica che può raggiungere una tela più alta di 1:2. Selezionando `custom_ratio` si rivelano `ratio_width` e `ratio_height`. Selezionando `manual` si rivelano i parametri della tela e del posizionamento dell'immagine. | DYNAMIC_COMBO | Sì | `"1:1"`<br>`"2:3"`<br>`"3:2"`<br>`"3:4"`<br>`"4:3"`<br>`"4:5"`<br>`"5:4"`<br>`"9:16"`<br>`"16:9"`<br>`"custom_ratio"`<br>`"manual"` |
| `prompt` | Descrizione opzionale della scena espansa; quando è vuoto, Bria ne genera una dall'immagine. Predefinito: stringa vuota. | STRING | Sì | Qualsiasi stringa |
| `negative_prompt` | Un prompt negativo opzionale per l'espansione. Predefinito: stringa vuota. | STRING | Sì | Qualsiasi stringa |
| `seed` | Seme per il processo di generazione casuale. Predefinito: 42. | INT | Sì | 1–2147483647 |
| `moderation` | Impostazioni di moderazione. Quando è impostato su `true`, vengono mostrate opzioni di moderazione aggiuntive. | DYNAMIC_COMBO | Sì | `"false"`<br>`"true"` |

### Input per rapporto personalizzato

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `ratio_width` | Lato larghezza del rapporto target: 21 e 9 danno 21:9. Predefinito: 21. | INT | Sì | 1–100 |
| `ratio_height` | Lato altezza del rapporto target: 21 e 9 danno 21:9. Bria accetta solo rapporti larghezza/altezza tra 0.5 e 3.0, quindi qualsiasi cosa più alta di 1:2 richiede la modalità manuale. Predefinito: 9. | INT | Sì | 1–100 |

### Input manuali

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `canvas_width` | Larghezza della tela di output in pixel. Predefinito: 1000. | INT | Sì | 64–5000 |
| `canvas_height` | Altezza della tela di output in pixel. Predefinito: 1000. | INT | Sì | 64–5000 |
| `image_width` | Larghezza dell'immagine originale all'interno della tela. Predefinito: 500. | INT | Sì | 1–5000 |
| `image_height` | Altezza dell'immagine originale all'interno della tela. Predefinito: 500. | INT | Sì | 1–5000 |
| `image_x` | Posizione X dell'angolo in alto a sinistra dell'immagine all'interno della tela; può trovarsi fuori dalla tela, ritagliando l'immagine. Predefinito: 250. | INT | Sì | -5000–5000 |
| `image_y` | Posizione Y dell'angolo in alto a sinistra dell'immagine all'interno della tela; può trovarsi fuori dalla tela, ritagliando l'immagine. Predefinito: 250. | INT | Sì | -5000–5000 |

### Input di moderazione

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `prompt_content_moderation` | Se abilitato, modera il contenuto del prompt. Predefinito: false. Disponibile solo quando `moderation` è `true`. | BOOLEAN | Sì | true/false |
| `visual_input_moderation` | Se abilitato, modera l'input visivo. Predefinito: false. Disponibile solo quando `moderation` è `true`. | BOOLEAN | Sì | true/false |
| `visual_output_moderation` | Se abilitato, modera l'output visivo. Predefinito: false. Disponibile solo quando `moderation` è `true`. | BOOLEAN | Sì | true/false |

Le opzioni di rapporto d'aspetto predefinito (`1:1`, `2:3`, `3:2`, `3:4`, `4:3`, `4:5`, `5:4`, `9:16`, `16:9`) non hanno input aggiuntivi.

Quando `expand_mode` è `custom_ratio`, `ratio_width` e `ratio_height` definiscono un rapporto d'aspetto target. Bria accetta solo rapporti larghezza/altezza tra 0.5 e 3.0. Se il rapporto è al di fuori di questo intervallo, viene generato un errore e si dovrebbe usare invece la modalità `manual`.

Quando `expand_mode` è `manual`, l'immagine originale viene posizionata su una tela con la dimensione e la posizione specificate. L'immagine può estendersi oltre la tela, nel qual caso la porzione esterna viene ritagliata.

Quando `moderation` è `true`, i tre booleani di moderazione vengono inviati a Bria. Quando `moderation` è `false`, vengono ignorati.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `image` | L'immagine espansa generata da Bria. | IMAGE |
| `prompt` | Il prompt utilizzato per l'espansione; generato automaticamente da Bria quando l'input `prompt` è vuoto. | STRING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaExpandImage/it.md)

---
**Source fingerprint (SHA-256):** `d2c9431837f200ccbcb39037f7b26013494c4dea3d40d899db4e717ddbbea71c`
