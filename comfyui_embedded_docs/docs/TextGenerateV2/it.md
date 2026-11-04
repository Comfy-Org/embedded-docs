# Generate Text

Il nodo Generate Text utilizza un modello CLIP per produrre testo da un prompt. A differenza del precedente nodo a singolo allegato, accetta stack espandibili di immagini, video e file audio come contesto aggiuntivo, così puoi fornire un intero set di riferimento in un unico nodo. Puoi controllare la lunghezza dell'output, se viene utilizzato il campionamento e se si applicano il template chat e la modalità thinking del modello.

## Input

| Parametro | Descrizione | Tipo di dati | Richiesto | Intervallo |
| --- | --- | --- | --- | --- |
| `clip` | Il modello CLIP utilizzato per tokenizzare il prompt e generare il testo. | CLIP | Sì | - |
| `prompt` | Il prompt che guida la generazione. Supporta più righe e prompt dinamici (predefinito: stringa vuota). | STRING | Sì | - |
| `images` | Gruppo espandibile di fino a 50 immagini, da `image1` a `image50`, utilizzato come contesto visivo per il modello. | AUTOGROW | No | 0 a 50 immagini |
| `videos` | Gruppo espandibile di fino a 100 input video, da `video1` a `video100`. Ogni video è un batch di frame considerato a 24 FPS e sottocampionato internamente a 1 FPS. | AUTOGROW | No | 0 a 100 video |
| `audios` | Gruppo espandibile di fino a 100 input audio, da `audio1` a `audio100`, utilizzato come contesto audio per il modello. | AUTOGROW | No | 0 a 100 file audio |
| `max_length` | Numero massimo di token da generare (predefinito: 512). | INT | Sì | 1 a 32768 |
| `sampling_mode` | `on` campiona l'output e mostra i parametri di campionamento sottostanti. `off` genera in modo greedy senza campionamento casuale. | DYNAMIC_COMBO | Sì | `"on"`<br>`"off"` |
| `thinking` | Opera in modalità thinking se il modello la supporta (predefinito: False). | BOOLEAN | No | True o False |
| `use_default_template` | Utilizza il system prompt o il template chat predefiniti se il modello ne dispone (predefinito: True). Parametro avanzato. | BOOLEAN | No | True o False |
| `mtp` | Decodifica speculativa con la testa di previsione multi-token del checkpoint. Non ha effetto senza i pesi MTP. `"auto"` adatta la profondità e l'ampiezza della bozza alle corrispondenze osservate dei token e al costo di esecuzione, `"2"` a `"5"` fissano una profondità della bozza costante, e le modalità `tree` fissano sia l'ampiezza che la profondità. L'output campionato rimane correttamente distribuito ma differisce dall'output non-MTP per lo stesso seed (predefinito: `"auto"`). | COMBO | No | `"auto"`<br>`"off"`<br>`"2"`<br>`"3"`<br>`"4"`<br>`"5"`<br>`"tree2s1"`<br>`"tree2s2"`<br>`"tree3s1"`<br>`"tree4s1m8"` |
| `system_prompt` | Sostituisce il system prompt nel template chat del modello. Ignorato quando il template predefinito non viene utilizzato. Collega un input STRING anziché digitare nel nodo (predefinito: vuoto). | STRING | No | - |

### Parametri di campionamento (quando `sampling_mode` è `"on"`)

| Parametro | Descrizione | Tipo di dati | Richiesto | Intervallo |
| --- | --- | --- | --- | --- |
| `temperature` | Controlla la casualità dell'output. Valori più bassi rendono l'output più prevedibile, valori più alti lo rendono più creativo (predefinito: 0.7). | FLOAT | Sì | 0.01 a 2.0 |
| `top_k` | Limita il pool di campionamento ai K token successivi più probabili. Un valore di 0 disabilita il filtro (predefinito: 64). | INT | Sì | 0 a 1000 |
| `top_p` | Campionamento nucleus: mantiene il più piccolo insieme di token più probabili la cui probabilità cumulativa raggiunge questo valore (predefinito: 0.95). | FLOAT | Sì | 0.0 a 1.0 |
| `min_p` | Probabilità minima che un token deve raggiungere per rimanere nel pool (predefinito: 0.05). | FLOAT | Sì | 0.0 a 1.0 |
| `repetition_penalty` | Penalizza i token già generati per ridurre le ripetizioni. Un valore di 1.0 non applica alcuna penalità (predefinito: 1.05). | FLOAT | Sì | 0.0 a 5.0 |
| `presence_penalty` | Penalizza i nuovi token in base alla loro presenza nel testo finora, incoraggiando il modello a passare a nuovi argomenti (predefinito: 0.0). | FLOAT | Sì | 0.0 a 5.0 |
| `seed` | Numero utilizzato per inizializzare il generatore di numeri casuali per risultati riproducibili (predefinito: 0). | INT | Sì | 0 a 18446744073709551615 |

**Nota:** I parametri di campionamento sopra esistono solo quando `sampling_mode` è `"on"`. Con `"off"` il nodo genera testo senza campionamento casuale e i parametri sono nascosti.

**Nota:** Quando l'output del modello apre un blocco di ragionamento con `<think>`, il nodo lo suddivide: `generated_text` trasporta la risposta e `thinking` trasporta il ragionamento con il tag di apertura rimosso. Altrimenti `generated_text` trasporta tutto ciò che il modello ha prodotto e `thinking` è vuoto. Il ragionamento interrotto da `max_length` rimane in `generated_text`.

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `generated_text` | Il testo generato dal modello, con qualsiasi blocco di ragionamento separato nell'output `thinking`. | STRING |
| `thinking` | Il blocco di ragionamento prodotto dal modello, con il tag di apertura `<think>` rimosso. Vuoto quando il modello non ha prodotto alcun blocco di ragionamento. | STRING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextGenerateV2/it.md)

---
**Source fingerprint (SHA-256):** `b61210726faa495a342a5eaaebe64f800ec1d2af4e2fc1321d8c3d7c594bd9ca`
