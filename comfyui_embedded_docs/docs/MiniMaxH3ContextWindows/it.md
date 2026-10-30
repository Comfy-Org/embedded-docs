# MiniMax H3 Context Windows

Suddivide il campionamento in finestre di contesto sovrapposte, in modo che un video MiniMax H3 possa essere più lungo della finestra a passaggio singolo del modello. Le finestre vengono posizionate sui blocchi da 17 frame del modello, il che mantiene allineati il video e l'audio generati attraverso i confini delle finestre. Collegare il modello restituito al sampler al posto del modello originale.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model` | Il modello a cui applicare le finestre di contesto durante il campionamento. | MODEL | Sì | - |
| `context_length` | La lunghezza della finestra di contesto in frame reali. Deve essere 17*n + 5 (predefinito: 124). | INT | Sì | da 22 a 16384 (MAX_RESOLUTION), passo 17 |
| `context_overlap` | La sovrapposizione della finestra di contesto in frame reali. Deve essere 17*n + 5 (predefinito: 39). | INT | Sì | 5 o superiore, passo 17 |
| `fuse_method` | Il metodo usato per fondere le finestre di contesto (predefinito: `"pyramid"`). | COMBO | Sì | `"pyramid"`<br>`"relative"`<br>`"flat"`<br>`"overlap-linear"` |
| `freenoise` | Se applicare il mescolamento del rumore FreeNoise, che migliora la fusione delle finestre (predefinito: True, parametro avanzato). | BOOLEAN | Sì | true<br>false |
| `split_conds_to_windows` | Se suddividere più conditioning (creati da ConditionCombine) in ciascuna finestra in base all'indice di regione (predefinito: False, parametro avanzato). | BOOLEAN | Sì | true<br>false |

Entrambe le lunghezze sono espresse in frame reali e convertite in latenti prima del campionamento: `context_length` diventa 2 latenti con 5 frame o meno, altrimenti `((frames - 5) / 17) * 5 + 2`. `context_overlap` viene convertito allo stesso modo e poi limitato a `context_length` meno 5, così la sovrapposizione lascia sempre un blocco completo per avanzare. Il nodo usa sempre la pianificazione statica con uno stride di 1, applica le finestre sulla dimensione temporale latente e non aggiunge il frame di correzione causale, poiché ogni finestra inizia su un confine di blocco. `split_conds_to_windows` prevede più conditioning creati dal nodo ConditionCombine.

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `model` | Il modello con la configurazione delle finestre di contesto applicata. | MODEL |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MiniMaxH3ContextWindows/it.md)

---
**Source fingerprint (SHA-256):** `e9e019d0bc870abfe226ef1aafb2607f55c0cc1b297884db35fe98c465cc0d91`
