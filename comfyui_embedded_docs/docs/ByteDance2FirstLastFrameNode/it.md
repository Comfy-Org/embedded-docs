# ByteDance2FirstLastFrameNode

Questo nodo genera un video da un'immagine obbligatoria del primo fotogramma e un'immagine opzionale dell'ultimo fotogramma usando i modelli ByteDance Seedance. Descrivi il video con un prompt testuale; il primo fotogramma guida l'inizio del video e l'ultimo fotogramma ne guida la fine. Supporta Seedance 2.5 e la famiglia Seedance 2.0 (Seedance 2.0, Seedance 2.0 Fast e Seedance 2.0 Mini). Selezionando il modello `Seedance 2.5 Draft` viene invece renderizzata un'anteprima veloce a 480p; collega il `draft_task_id` risultante al nodo ByteDance Seedance 2.5 Draft to Final Video per renderizzare il finale a 1080p.

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `model` | Seedance 2.5 per il modello più recente, video fino a 30 secondi e output mp4; Seedance 2.5 Draft per un'anteprima veloce a 480p il cui output `draft_task_id` renderizza il finale a 1080p nel nodo ByteDance Seedance 2.5 Draft to Final Video; Seedance 2.0 per la massima qualità e 4k; Fast per l'ottimizzazione della velocità; Mini per la generazione più rapida e a costo più basso. Selezionando un modello vengono mostrati di seguito gli input specifici del modello. | DYNAMIC_COMBO | Sì | `"Seedance 2.5"`<br>`"Seedance 2.5 Draft"`<br>`"Seedance 2.0"`<br>`"Seedance 2.0 Fast"`<br>`"Seedance 2.0 Mini"` |
| `first_frame` | Immagine del primo fotogramma per il video. | IMAGE | No | - |
| `last_frame` | Immagine dell'ultimo fotogramma per il video. | IMAGE | No | - |
| `first_frame_asset_id` | asset_id Seedance da usare come primo fotogramma. Mutuamente esclusivo con l'input immagine `first_frame`. Il valore predefinito è una stringa vuota. | STRING | No | - |
| `last_frame_asset_id` | asset_id Seedance da usare come ultimo fotogramma. Mutuamente esclusivo con l'input immagine `last_frame`. Il valore predefinito è una stringa vuota. | STRING | No | - |
| `seed` | Il seed controlla se il nodo deve rieseguirsi; i risultati non sono deterministici indipendentemente dal seed. Il valore predefinito è 0. | INT | Sì | 0 to 2147483647 |
| `watermark` | Indica se aggiungere una filigrana al video. Il valore predefinito è False. | BOOLEAN | Sì | False<br>True |

### Input di Seedance 2.5

Questi input vengono visualizzati quando è selezionato `Seedance 2.5`.

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `prompt` | Prompt testuale per la generazione del video. Inserisci le battute parlate tra virgolette doppie per guidare il dialogo generato. | STRING | Sì | - |
| `resolution` | Risoluzione del video di output. Il valore predefinito è 720p. | COMBO | Sì | `"480p"`<br>`"720p"`<br>`"1080p"` |
| `duration` | Durata del video di output in secondi (4-30). Il valore predefinito è 5. | INT | Sì | 4 to 30 |
| `generate_audio` | Abilita la generazione audio per il video di output. Il valore predefinito è True. | BOOLEAN | Sì | False<br>True |
| `output_format` | Formato contenitore del video di output. Il valore predefinito è mp4. | COMBO | Sì | `"mp4"` |

### Input di Seedance 2.5 Draft

Questi input vengono visualizzati quando è selezionato `Seedance 2.5 Draft`. L'insieme dei parametri corrisponde a Seedance 2.5 sopra, tranne per il fatto che `resolution` offre solo `"480p"` (predefinito `"480p"`).

### Input di Seedance 2.0

Questi input vengono visualizzati quando è selezionato `Seedance 2.0`.

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `prompt` | Prompt testuale per la generazione del video. | STRING | Sì | - |
| `resolution` | Risoluzione del video di output. | COMBO | Sì | `"480p"`<br>`"720p"`<br>`"1080p"`<br>`"4k"` |
| `ratio` | Rapporto d'aspetto del video di output. Il valore predefinito è `adaptive`, che usa il rapporto supportato più vicino al rapporto d'aspetto del fotogramma di input. | COMBO | Sì | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | Durata del video di output in secondi (4-15). Il valore predefinito è 7. | INT | Sì | 4 to 15 |
| `generate_audio` | Abilita la generazione audio per il video di output. Il valore predefinito è True. | BOOLEAN | Sì | False<br>True |

### Input di Seedance 2.0 Fast e Seedance 2.0 Mini

Condivisi da `Seedance 2.0 Fast` e `Seedance 2.0 Mini`.

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `prompt` | Prompt testuale per la generazione del video. | STRING | Sì | - |
| `resolution` | Risoluzione del video di output. | COMBO | Sì | `"480p"`<br>`"720p"` |
| `ratio` | Rapporto d'aspetto del video di output. Il valore predefinito è `adaptive`, che usa il rapporto supportato più vicino al rapporto d'aspetto del fotogramma di input. | COMBO | Sì | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | Durata del video di output in secondi (4-15). Il valore predefinito è 7. | INT | Sì | 4 to 15 |
| `generate_audio` | Abilita la generazione audio per il video di output. Il valore predefinito è True. | BOOLEAN | Sì | False<br>True |

**Vincoli dei parametri**

- Devi fornire il primo fotogramma come immagine `first_frame` oppure come `first_frame_asset_id`. Fornire entrambi genera un errore; non fornire nessuno dei due genera anch'esso un errore.
- Gli input `last_frame` e `last_frame_asset_id` sono opzionali, ma non puoi fornirli entrambi per lo stesso fotogramma.
- Gli asset ID devono fare riferimento ad asset immagine Seedance esistenti e attivi.
- L'input `prompt` è obbligatorio e non può essere vuoto.
- Ogni esecuzione restituisce il proprio ID attività come `draft_task_id`, ma solo l'ID di un'esecuzione con `Seedance 2.5 Draft` può essere renderizzato dal nodo ByteDance Seedance 2.5 Draft to Final Video. Con qualsiasi altro modello l'output deve essere lasciato non connesso, altrimenti l'esecuzione fallisce.
- Con `Seedance 2.5`, il rapporto d'aspetto di output è sempre adattivo e segue il rapporto d'aspetto del primo fotogramma stesso, quindi non viene mostrato alcun input `ratio`.
- Con i modelli della famiglia Seedance 2.0 e immagini dei fotogrammi locali, le immagini vengono ritagliate al centro e ridimensionate alla risoluzione e al rapporto di output target prima della generazione. Quando `ratio` è `adaptive`, viene usato il rapporto supportato più vicino all'immagine di input.
- Le immagini dei fotogrammi locali vengono convalidate per rapporto d'aspetto e dimensioni supportati; le immagini sovradimensionate vengono ridimensionate verso il basso.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `output` | Il video generato. | VIDEO |
| `draft_task_id` | ID attività restituito dall'esecuzione. Solo un'esecuzione con `Seedance 2.5 Draft` produce una bozza che il nodo ByteDance Seedance 2.5 Draft to Final Video può renderizzare; con qualsiasi altro modello l'output deve essere lasciato non connesso, altrimenti l'esecuzione fallisce. | STRING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2FirstLastFrameNode/it.md)

---
**Source fingerprint (SHA-256):** `363f1baac1685c2dada0e64a0b339f6ab2671161dccb002eb81f6b4f0d0aa243`
