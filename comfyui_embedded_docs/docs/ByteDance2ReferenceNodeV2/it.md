# ByteDance2ReferenceNodeV2

ByteDance Seedance 2.5 Reference to Video genera, modifica o estende video utilizzando i modelli ByteDance Seedance (Seedance 2.5, 2.5 Draft, 2.0, 2.0 Fast e 2.0 Mini) guidati da un prompt testuale e da immagini, video, audio di riferimento opzionali o asset della libreria caricati in precedenza. Carica i riferimenti, invia un'attività di generazione, attende il completamento e restituisce il file video finito. Selezionando `Seedance 2.5 Draft` viene invece eseguito il rendering di un'anteprima rapida a 480p; collega il `draft_task_id` risultante al nodo ByteDance Seedance 2.5 Draft to Final Video per eseguire il rendering del finale a 1080p.

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Range |
|-----------|-------------|-----------|----------|-------|
| `model` | Selettore del modello. Seedance 2.5 per il modello più recente, video fino a 30 secondi e output mp4; Seedance 2.5 Draft per un'anteprima rapida a 480p il cui output `draft_task_id` esegue il rendering del finale a 1080p nel nodo ByteDance Seedance 2.5 Draft to Final Video; Seedance 2.0 per la massima qualità e 4k; Fast per l'ottimizzazione della velocità; Mini per la generazione più rapida e a costo più basso. La selezione di un modello cambia i widget di input mostrati di seguito. | DYNAMIC_COMBO | Sì | "Seedance 2.5"<br>"Seedance 2.5 Draft"<br>"Seedance 2.0"<br>"Seedance 2.0 Fast"<br>"Seedance 2.0 Mini" |
| `seed` | Il seed controlla se il nodo deve essere rieseguito; i risultati non sono deterministici indipendentemente dal seed. Predefinito: 0. | INT | Sì | 0 a 2147483647 |
| `watermark` | Indica se aggiungere una filigrana al video. Predefinito: False. Impostazione avanzata. | BOOLEAN | Sì | true<br>false |

### Input di Seedance 2.5

Questi input compaiono quando `model` è impostato su "Seedance 2.5".

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Range |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Prompt testuale per la generazione del video. Inserisci le battute parlate tra virgolette doppie per guidare il dialogo generato. Predefinito: stringa vuota. | STRING | Sì | Testo multilinea |
| `resolution` | Risoluzione del video di output. Predefinito: 720p. | COMBO | Sì | "480p"<br>"720p"<br>"1080p" |
| `ratio` | Rapporto d'aspetto del video di output. Predefinito: 16:9. | COMBO | Sì | "16:9"<br>"4:3"<br>"1:1"<br>"3:4"<br>"9:16"<br>"21:9"<br>"adaptive" |
| `duration` | Durata del video di output in secondi (4-30). Predefinito: 5. | INT | Sì | 4 a 30 |
| `generate_audio` | Abilita la generazione audio per il video di output. Predefinito: True. | BOOLEAN | Sì | true<br>false |
| `task_type` | Cosa fare con i media di riferimento. Ogni valore diverso da auto viene convalidato al momento dell'invio dell'attività, quindi impostazioni non corrispondenti falliscono prima dell'avvio della generazione.<br>auto: il modello deduce l'attività dal prompt e dagli input, e le impostazioni in conflitto con la sua interpretazione falliscono solo dopo l'avvio della generazione.<br>reference: genera un nuovo video guidato dalle immagini, dai video e dagli audio di riferimento.<br>edit: modifica un video di riferimento collegato (aggiungi, rimuovi, sostituisci); l'output mantiene la lunghezza e il rapporto d'aspetto del clip di origine, e i widget `duration` e `ratio` vengono ignorati.<br>extend: continua un video di riferimento collegato in avanti o all'indietro; il prompt dovrebbe dire "extend forward", "extend backward" o "continue", il rapporto d'aspetto segue il clip di origine, e l'output contiene solo il segmento appena generato della durata impostata, non il clip di origine. Predefinito: auto. | COMBO | Sì | "auto"<br>"reference"<br>"edit"<br>"extend" |
| `output_format` | Formato contenitore del video di output. Predefinito: mp4. | COMBO | Sì | "mp4" |

### Input di Seedance 2.5 Draft

Questi input compaiono quando `model` è impostato su "Seedance 2.5 Draft". L'insieme dei parametri corrisponde a Seedance 2.5 sopra, tranne per il fatto che `resolution` offre solo `"480p"` (predefinito `"480p"`).

### Input di Seedance 2.0

Questi input compaiono quando `model` è impostato su "Seedance 2.0".

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Range |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Prompt testuale per la generazione del video. Predefinito: stringa vuota. | STRING | Sì | Testo multilinea |
| `resolution` | Risoluzione del video di output. | COMBO | Sì | "480p"<br>"720p"<br>"1080p"<br>"4k" |
| `ratio` | Rapporto d'aspetto del video di output. Predefinito: adaptive. | COMBO | Sì | "16:9"<br>"4:3"<br>"1:1"<br>"3:4"<br>"9:16"<br>"21:9"<br>"adaptive" |
| `duration` | Durata del video di output in secondi (4-15). Predefinito: 7. | INT | Sì | 4 a 15 |
| `generate_audio` | Abilita la generazione audio per il video di output. Predefinito: True. | BOOLEAN | Sì | true<br>false |

### Input di Seedance 2.0 Fast e Seedance 2.0 Mini

Questi input compaiono quando `model` è impostato su "Seedance 2.0 Fast" o "Seedance 2.0 Mini". Entrambi i modelli condividono lo stesso insieme di input.

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Range |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Prompt testuale per la generazione del video. Predefinito: stringa vuota. | STRING | Sì | Testo multilinea |
| `resolution` | Risoluzione del video di output. | COMBO | Sì | "480p"<br>"720p" |
| `ratio` | Rapporto d'aspetto del video di output. Predefinito: adaptive. | COMBO | Sì | "16:9"<br>"4:3"<br>"1:1"<br>"3:4"<br>"9:16"<br>"21:9"<br>"adaptive" |
| `duration` | Durata del video di output in secondi (4-15). Predefinito: 7. | INT | Sì | 4 a 15 |
| `generate_audio` | Abilita la generazione audio per il video di output. Predefinito: True. | BOOLEAN | Sì | true<br>false |

### Input di riferimento

Questi slot di riferimento espandibili sono disponibili per tutti i modelli. Il numero massimo di slot varia in base al modello: Seedance 2.5 supporta fino a 30 immagini, 10 video, 10 audio e 30 asset; Seedance 2.0, 2.0 Fast e 2.0 Mini supportano fino a 9 immagini, 3 video, 3 audio e 9 asset.

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Range |
|-----------|-------------|-----------|----------|-------|
| `reference_images` | Slot espandibile: collega 1..N immagini di riferimento che guidano l'output. Il limite di conteggio dipende dal modello (vedi sezioni del modello). Le immagini vengono convalidate in base al rapporto d'aspetto (da 0.4 a 2.5) e ridimensionate automaticamente verso il basso fino a un lato massimo di 6000 pixel. | IMAGE | No | 1..9 slot (famiglia Seedance 2.0)<br>1..30 slot (Seedance 2.5) |
| `reference_videos` | Slot espandibile: collega 1..N video di riferimento. Il limite di conteggio dipende dal modello (vedi sezioni del modello). Ogni video deve durare almeno 1.8 secondi e deve rispettare i limiti di pixel per il modello e la risoluzione selezionati. | VIDEO | No | 1..3 slot (famiglia Seedance 2.0)<br>1..10 slot (Seedance 2.5) |
| `reference_audios` | Slot espandibile: collega 1..N tracce audio di riferimento. Il limite di conteggio dipende dal modello (vedi sezioni del modello). Ogni audio deve durare almeno 1.8 secondi. | AUDIO | No | 1..3 slot (famiglia Seedance 2.0)<br>1..10 slot (Seedance 2.5) |
| `reference_assets` | Slot espandibile: collega 1..N stringhe di ID asset per media già caricati nella libreria virtuale Seedance. Ogni asset deve essere Active. Puoi fare riferimento a un asset nel prompt con token come `asset1` o `asset 1`; il nodo li sostituisce con l'etichetta posizionale dell'asset (ad esempio "Image 2" o "Video 1"). | STRING | No | 1..9 slot (famiglia Seedance 2.0)<br>1..30 slot (Seedance 2.5) |
| `auto_downscale` | Ridimensiona automaticamente verso il basso i video di riferimento che superano il budget di pixel del modello per la risoluzione selezionata. Il rapporto d'aspetto viene preservato; i video già entro i limiti non vengono modificati. Predefinito: True. | BOOLEAN | No | true<br>false |
| `auto_upscale` | Ridimensiona automaticamente verso l'alto i video di riferimento che sono al di sotto del numero minimo di pixel del modello per la risoluzione selezionata. Il rapporto d'aspetto viene preservato; i video che già soddisfano il minimo non vengono modificati. Nota: il ridimensionamento verso l'alto di una sorgente a bassa risoluzione non aggiunge dettaglio reale e può produrre generazioni di qualità inferiore. Predefinito: False. Impostazione avanzata. | BOOLEAN | No | true<br>false |

**Nota:** Per eseguire il nodo è richiesto almeno un riferimento tra immagine, video o asset (Seedance 2.5 accetta anche riferimenti solo audio). I video e gli audio di riferimento devono durare ciascuno almeno 1.8 secondi, e la durata combinata di tutti i video di riferimento (e separatamente, di tutti gli audio di riferimento) non deve superare il numero massimo totale di secondi del modello selezionato. Le immagini di riferimento devono avere un rapporto d'aspetto compreso all'incirca tra 2:5 e 5:2 (da 0.4 a 2.5), devono essere almeno 300x300 pixel e vengono ridimensionate automaticamente verso il basso fino a un lato massimo di 6000 pixel. Le opzioni `task_type` "edit" e "extend" sono disponibili solo con Seedance 2.5 ed entrambe richiedono almeno un video di riferimento; quando si usa "edit", l'output mantiene la lunghezza e il rapporto d'aspetto del clip di origine e i widget `duration` e `ratio` vengono ignorati, mentre quando si usa "extend", l'output contiene solo il segmento appena generato per la durata impostata. Gli asset referenziati devono essere nello stato Active, altrimenti l'attività fallisce. Ogni esecuzione restituisce il proprio ID attività come `draft_task_id`, ma solo l'ID di un'esecuzione `Seedance 2.5 Draft` può essere renderizzato dal nodo ByteDance Seedance 2.5 Draft to Final Video, quindi con qualsiasi altro modello l'output deve essere lasciato non collegato, altrimenti l'esecuzione fallisce.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|-----------|
| `video` | Il video generato, scaricato dal provider una volta completata l'attività di generazione. Contiene audio quando la generazione audio è abilitata. | VIDEO |
| `draft_task_id` | ID attività restituito dall'esecuzione. Solo un'esecuzione `Seedance 2.5 Draft` produce una bozza che il nodo ByteDance Seedance 2.5 Draft to Final Video può renderizzare; con qualsiasi altro modello l'output deve essere lasciato non collegato, altrimenti l'esecuzione fallisce. | STRING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2ReferenceNodeV2/it.md)

---
**Source fingerprint (SHA-256):** `12fee29b280ff71e29f268f52131d1c15cf3066e0804356b735b61d97c80a6a9`
