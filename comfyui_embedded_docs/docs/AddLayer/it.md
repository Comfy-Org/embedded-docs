# Aggiungi livello

Il nodo Add Layer trasforma un'immagine di input in un livello e la posiziona su un canvas, iniziando un nuovo stack di livelli o aggiungendola a uno esistente. Puoi impostare il nome del livello, la posizione, la dimensione, la rotazione, l'opacità, la modalità di fusione, l'ordine di impilamento e il capovolgimento orizzontale o verticale. Questo nodo è contrassegnato come sperimentale.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `layers` | Stack di livelli a cui aggiungere. Lascia non connesso per iniziare un nuovo stack. | LAYERS | No | — |
| `image` | Contenuto del livello alla sua dimensione nativa. Un batch si espande in livelli consecutivi. | IMAGE | Sì | — |
| `mask` | Maschera di trasparenza per questo livello. Le aree mascherate (valore 1) diventano trasparenti, moltiplicandosi con qualsiasi canale alpha già presente nell'immagine. | MASK | No | — |
| `name` | Nome del livello mostrato nell'editor del compositor. (predefinito: "") | STRING | No | — |
| `x` | Posizionamento orizzontale iniziale sul canvas. (predefinito: 0) | INT | No | -MAX_RESOLUTION a MAX_RESOLUTION |
| `y` | Posizionamento verticale iniziale sul canvas. (predefinito: 0) | INT | No | -MAX_RESOLUTION a MAX_RESOLUTION |
| `opacity` | Opacità iniziale del livello. (predefinito: 1.0) | FLOAT | No | 0.0 a 1.0 (passo: 0.01) |
| `blend_mode` | Modalità di fusione iniziale, applicata rispetto ai livelli sottostanti. Sul livello in basso sopra lo sfondo trasparente predefinito, le modalità diverse da normal producono trasparenza. (predefinito: "normal") | COMBO | No | Più opzioni disponibili |
| `rotation` | Rotazione iniziale in gradi, in senso orario. (predefinito: 0.0) | FLOAT | No | -360.0 a 360.0 (passo: 1.0) |
| `width` | Larghezza di visualizzazione iniziale. 0 mantiene la larghezza nativa dell'immagine. (predefinito: 0) | INT | No | 0 a MAX_RESOLUTION |
| `height` | Altezza di visualizzazione iniziale. 0 mantiene l'altezza nativa dell'immagine. (predefinito: 0) | INT | No | 0 a MAX_RESOLUTION |
| `z_index` | Sovrascrittura dell'impilamento. I livelli vengono ordinati in modo stabile in base a z_index; i valori uguali mantengono il loro ordine nella lista. (predefinito: 0) | INT | No | -1000 a 1000 |
| `flip_h` | Capovolgi il livello orizzontalmente. (predefinito: False) | BOOLEAN | No | false / true |
| `flip_v` | Capovolgi il livello verticalmente. (predefinito: False) | BOOLEAN | No | false / true |

Note:
- Solo `image` è obbligatorio; tutti gli altri input sono opzionali.
- Quando `layers` viene lasciato non connesso, viene creato un nuovo stack di livelli. Quando uno stack di livelli è connesso, il nuovo livello vi viene aggiunto.
- Un batch di immagini nell'input `image` crea più livelli consecutivi.
- `width` e `height` hanno come valore predefinito 0, che mantiene le dimensioni native dell'immagine. Valori maggiori di 0 sovrascrivono la dimensione di visualizzazione.
- `opacity`, `blend_mode`, `rotation`, `width` e `height` vengono applicati solo quando differiscono dai loro valori predefiniti.
- La dimensione del canvas di uno stack di livelli connesso viene preservata nell'output.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|-----------|
| `layers` | Stack di livelli con questo livello aggiunto. | LAYERS |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AddLayer/it.md)

---
**Source fingerprint (SHA-256):** `b7bf1a012d17cb5768b49d5c0617e13562ba015f695e6c9b1d1bbefba4150f9e`
