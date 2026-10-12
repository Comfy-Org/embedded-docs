# ResolutionBucket

Questo nodo organizza un elenco di immagini latenti e i relativi dati di condizionamento in base alla loro risoluzione. Raggruppa insieme gli elementi che condividono la stessa altezza e larghezza, creando batch separati per ogni risoluzione unica. Questo processo è utile per preparare i dati a un addestramento efficiente, poiché consente ai modelli di elaborare insieme più elementi della stessa dimensione.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `latents` | Elenco di dizionari latenti da raggruppare per risoluzione. | LATENT | Sì | N/A |
| `conditioning` | Elenco di liste di condizionamento (deve corrispondere alla lunghezza di `latents`). | CONDITIONING | Sì | N/A |

**Nota:** Entrambi gli input sono input di tipo lista, il che significa che il nodo riceve un elenco di elementi per ciascuno. Il numero di elementi nell'elenco `latents` deve corrispondere esattamente al numero di elementi nell'elenco `conditioning`; se i conteggi non corrispondono, il nodo genera un errore. Ogni dizionario latente può contenere un batch di campioni, e la lista di condizionamento corrispondente deve contenere un numero corrispondente di elementi di condizionamento per quel batch, poiché ogni campione nel batch è abbinato alla propria voce di condizionamento. I campioni latenti possono avere una forma di (B, C, H, W) per le immagini o (B, T, C, H, W) per i video; il nodo li raggruppa solo per altezza e larghezza.

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `latents` | Elenco di dizionari latenti raggruppati in batch, uno per bucket di risoluzione. | LATENT |
| `conditioning` | Elenco di liste di condizionamento, una per bucket di risoluzione. | CONDITIONING |

**Nota:** Entrambi gli output sono output di tipo lista. Ogni elenco di output contiene una voce per ogni risoluzione unica (altezza e larghezza) trovata nell'input, nell'ordine in cui le risoluzioni sono state incontrate per la prima volta. I dati latenti all'interno di ciascun bucket sono impilati lungo una nuova dimensione batch.

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ResolutionBucket/it.md)

---
**Source fingerprint (SHA-256):** `11687f9916895136c7c5b8146cd7519cbf6c296720e453bac52fe4da237403cd`
