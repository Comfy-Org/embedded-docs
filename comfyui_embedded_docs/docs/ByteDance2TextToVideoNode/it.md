# ByteDance2TextToVideoNode

Questo nodo genera un video da un prompt testuale usando i modelli Seedance 2.5 o 2.0 di ByteDance. Invia il prompt al modello selezionato, attende il completamento dell'elaborazione del video e restituisce il file video risultante. Selezionando il modello `Seedance 2.5 Draft` si ottiene invece un'anteprima rapida a 480p; collega il `draft_task_id` risultante al nodo ByteDance Seedance 2.5 Draft to Final Video per renderizzare il finale a 1080p.

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `model` | Il modello Seedance da usare per la generazione video. Seedance 2.5 è il modello più recente, supporta video fino a 30 secondi e output mp4; Seedance 2.5 Draft genera un'anteprima rapida a 480p il cui output `draft_task_id` produce il finale a 1080p nel nodo ByteDance Seedance 2.5 Draft to Final Video; Seedance 2.0 è per la massima qualità e 4k; Seedance 2.0 Fast è per l'ottimizzazione della velocità; Seedance 2.0 Mini è per la generazione più rapida e a costo più basso. Selezionando un modello vengono mostrati input aggiuntivi per prompt, risoluzione, rapporto d'aspetto, durata e generazione audio. | DYNAMIC_COMBO | Sì | `"Seedance 2.5"`<br>`"Seedance 2.5 Draft"`<br>`"Seedance 2.0"`<br>`"Seedance 2.0 Fast"`<br>`"Seedance 2.0 Mini"` |
| `seed` | Controlla se il nodo deve essere rieseguito; i risultati non sono deterministici indipendentemente dal seed. (predefinito: 0) | INT | No | 0 a 2147483647 |
| `watermark` | Indica se aggiungere una filigrana al video. (predefinito: False) Questa è un'impostazione avanzata. | BOOLEAN | No | True / False |

### Input di Seedance 2.5

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Prompt testuale per la generazione video. Metti le battute parlate tra virgolette doppie per guidare il dialogo generato. | STRING | Sì | — |
| `resolution` | Risoluzione del video di output. (predefinito: `"720p"`) | COMBO | Sì | `"480p"`<br>`"720p"`<br>`"1080p"` |
| `ratio` | Rapporto d'aspetto del video di output. (predefinito: `"16:9"`) | COMBO | Sì | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | Durata del video di output in secondi. (predefinito: 5) | INT | Sì | da 4 a 30 |
| `generate_audio` | Abilita la generazione audio per il video di output. (predefinito: True) | BOOLEAN | Sì | True / False |
| `output_format` | Formato contenitore del video di output. (predefinito: `"mp4"`) | COMBO | Sì | `"mp4"` |

### Input di Seedance 2.5 Draft

Questi input compaiono quando è selezionato `Seedance 2.5 Draft`. Il set di parametri corrisponde a Seedance 2.5 sopra, tranne per il fatto che `resolution` offre solo `"480p"` (predefinito `"480p"`).

### Input di Seedance 2.0

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Prompt testuale per la generazione video. | STRING | Sì | — |
| `resolution` | Risoluzione del video di output. | COMBO | Sì | `"480p"`<br>`"720p"`<br>`"1080p"`<br>`"4k"` |
| `ratio` | Rapporto d'aspetto del video di output. (predefinito: `"16:9"`) | COMBO | Sì | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | Durata del video di output in secondi. (predefinito: 7) | INT | Sì | da 4 a 15 |
| `generate_audio` | Abilita la generazione audio per il video di output. (predefinito: True) | BOOLEAN | Sì | True / False |

### Input di Seedance 2.0 Fast e Seedance 2.0 Mini

Condivisi da Seedance 2.0 Fast e Seedance 2.0 Mini; entrambi i modelli espongono gli stessi parametri.

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Prompt testuale per la generazione video. | STRING | Sì | — |
| `resolution` | Risoluzione del video di output. | COMBO | Sì | `"480p"`<br>`"720p"` |
| `ratio` | Rapporto d'aspetto del video di output. (predefinito: `"16:9"`) | COMBO | Sì | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | Durata del video di output in secondi. (predefinito: 7) | INT | Sì | da 4 a 15 |
| `generate_audio` | Abilita la generazione audio per il video di output. (predefinito: True) | BOOLEAN | Sì | True / False |

**Nota:** Il selettore `model` è dinamico; gli input mostrati sotto la sezione di ciascun modello compaiono quando quel modello è selezionato. Il prompt deve contenere almeno 1 carattere dopo aver rimosso gli spazi. I limiti di risoluzione e durata dipendono dal modello selezionato: Seedance 2.5 supporta 480p/720p/1080p e da 4 a 30 secondi, Seedance 2.0 supporta 480p/720p/1080p/4k e da 4 a 15 secondi, mentre Seedance 2.0 Fast e Seedance 2.0 Mini supportano solo 480p/720p e da 4 a 15 secondi; Seedance 2.5 Draft supporta solo 480p e da 4 a 30 secondi. Ogni esecuzione restituisce il proprio ID attività come `draft_task_id`, ma solo l'ID di un'esecuzione `Seedance 2.5 Draft` può essere renderizzato dal nodo ByteDance Seedance 2.5 Draft to Final Video, quindi con qualsiasi altro modello l'output deve essere lasciato non connesso, altrimenti l'esecuzione fallisce. Il valore `seed` controlla solo se il nodo viene rieseguito; non rende i risultati deterministici.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|-----------|
| `video` | Il file video generato. | VIDEO |
| `draft_task_id` | ID attività restituito dall'esecuzione. Solo un'esecuzione `Seedance 2.5 Draft` produce una bozza che il nodo ByteDance Seedance 2.5 Draft to Final Video può renderizzare; con qualsiasi altro modello l'output deve essere lasciato non connesso, altrimenti l'esecuzione fallisce. | STRING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2TextToVideoNode/it.md)

---
**Source fingerprint (SHA-256):** `2abad0c4eab5a1286c8da9237bcec52b275c40188b3b7dc9eede5d5f4cbb11d3`
