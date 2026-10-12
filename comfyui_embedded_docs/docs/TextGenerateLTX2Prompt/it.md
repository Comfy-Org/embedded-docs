# TextGenerateLTX2Prompt

Il nodo TextGenerateLTX2Prompt espande un breve prompt utente in una descrizione audiovisiva dettagliata adatta a generare video con la serie LTX-2 di modelli video. Aggiunge automaticamente istruzioni di sistema specifiche per l'attività, invia il prompt formattato a un modello linguistico e restituisce il testo migliorato. Quando viene fornita un'immagine di riferimento opzionale, il nodo passa alla modalità da immagine a video ed espande il prompt partendo dal contenuto di quell'immagine.

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `clip` | Il modello CLIP usato per la codifica del testo. Il nodo controlla il nome del tokenizer del modello per selezionare le istruzioni corrispondenti: i modelli basati su Gemma 4 usano il formato LTX-2.4, mentre gli altri modelli usano il formato LTX-2 (Gemma 3). | CLIP | Sì | - |
| `prompt` | L'input testuale grezzo che descrive la scena o il concetto da espandere in un prompt dettagliato per la generazione video. | STRING | Sì | - |
| `image` | Un'immagine di input opzionale usata come primo frame del video. Quando fornita, il nodo passa alla modalità da immagine a video e usa un prompt di sistema che espande il prompt utente in base al contenuto dell'immagine. | IMAGE | No | - |
| `video` | Un input video opzionale usato come contesto aggiuntivo. Passato al modello linguistico come batch di immagini; si presume a 24 FPS e viene sottocampionato internamente a 1 FPS. | IMAGE | No | - |
| `audio` | Un input audio opzionale che può essere usato come contesto aggiuntivo per la generazione. | AUDIO | No | - |
| `max_length` | Il numero massimo di token che al modello linguistico è consentito generare (predefinito: 512). | INT | Sì | 1 to 32768 |
| `sampling_mode` | Controlla se viene usato il campionamento casuale durante la generazione del testo. Quando è impostato su `"on"`, i parametri di campionamento sottostanti diventano disponibili; con `"off"` il nodo genera testo senza campionamento casuale. | DYNAMIC_COMBO | Sì | `"on"`<br>`"off"` |
| `thinking` | Quando abilitato, al modello viene chiesto di ragionare prima di rispondere. Qualsiasi blocco di ragionamento viene restituito sull'output `thinking` invece che in `generated_text` (predefinito: False). | BOOLEAN | No | True/False |
| `use_default_template` | Quando abilitato, il nodo usa il template di chat predefinito per la formattazione (predefinito: True). Impostazione avanzata. | BOOLEAN | No | True/False |
| `mtp` | Decodifica speculativa con la testa di previsione multi-token del checkpoint. Non ha alcun effetto senza i pesi MTP. `"auto"` adatta la profondità della bozza, `"2"`–`"5"` la fissano. L'output campionato rimane correttamente distribuito ma differisce dall'output non-MTP per lo stesso seed (predefinito: `"auto"`). | COMBO | No | `"auto"`<br>`"off"`<br>`"2"`<br>`"3"`<br>`"4"`<br>`"5"` |
| `system_prompt` | Sostituisce il prompt di sistema LTX-2 integrato. Quando lasciato vuoto, il nodo usa le proprie istruzioni: il prompt di sistema da immagine a video quando è collegata un'`image`, altrimenti il prompt di sistema da testo a video. Collega un input STRING invece di digitare nel nodo (predefinito: vuoto). | STRING | No | - |

### Parametri di campionamento (quando `sampling_mode` è "on")

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `temperature` | Controlla la casualità dell'output. Valori più bassi rendono l'output più prevedibile, valori più alti lo rendono più creativo (predefinito: 0.7). | FLOAT | Sì | 0.01 to 2.0 |
| `top_k` | Limita il pool di campionamento ai K token successivi più probabili. Un valore di 0 disabilita questo filtro (predefinito: 64). | INT | Sì | 0 to 1000 |
| `top_p` | Usa il campionamento nucleus: mantiene il più piccolo insieme di token più probabili la cui probabilità cumulativa raggiunge questo valore. (predefinito: 0.95) | FLOAT | Sì | 0.0 to 1.0 |
| `min_p` | Imposta una soglia minima di probabilità affinché i token siano considerati (predefinito: 0.05). | FLOAT | Sì | 0.0 to 1.0 |
| `repetition_penalty` | Penalizza i token già generati per ridurre le ripetizioni. Un valore di 1.0 non applica alcuna penalità (predefinito: 1.05). | FLOAT | Sì | 0.0 to 5.0 |
| `seed` | Un numero usato per inizializzare il generatore di numeri casuali per risultati riproducibili (predefinito: 0). | INT | Sì | 0 to 18446744073709551615 |
| `presence_penalty` | Penalizza i nuovi token in base al fatto che siano già comparsi nel testo finora, incoraggiando il modello a parlare di nuovi argomenti (predefinito: 0.0). | FLOAT | No | 0.0 to 5.0 |

**Nota:** I parametri di campionamento sopra riportati sono attivi e visibili nell'interfaccia del nodo solo quando `sampling_mode` è impostato su "on". Quando è impostato su "off", non è disponibile alcun parametro di campionamento e il nodo genera testo senza campionamento casuale.

**Nota:** Il comportamento del nodo cambia in base ai suoi input:

- Se viene fornita un'`image`, il prompt generato viene formattato per un'attività da immagine a video usando un prompt di sistema che descrive come espandere il prompt in base al contenuto dell'immagine. Se non viene fornita alcuna immagine, la formattazione è per un'attività da testo a video usando un prompt di sistema che espande il prompt in una descrizione dettagliata per la generazione video.
- Se il nome del tokenizer CLIP contiene "gemma4", il nodo usa i prompt di sistema LTX-2.4 e il formato di chat Gemma 4. Altrimenti, usa i prompt di sistema LTX-2 (Gemma 3) e il formato di chat.
- Quando `thinking` è abilitato con un modello Gemma 4, il modello viene aperto sul suo canale di ragionamento; quando è disabilitato, il modello viene aperto direttamente sul canale della risposta finale. Per i modelli non Gemma 4, `thinking` viene passato al passo di generazione sottostante.
- Un `system_prompt` sostituisce le istruzioni integrate per la modalità selezionata (da immagine a video o da testo a video); quando è vuoto, viene usato il prompt integrato.
- Qualsiasi blocco di ragionamento viene restituito sull'output `thinking` invece che in `generated_text`.
- Se il modello linguistico non produce testo utilizzabile, il nodo restituisce invece il `prompt` originale.

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `generated_text` | Il prompt avanzato per la generazione video prodotto dal modello linguistico, con qualsiasi blocco di ragionamento separato nell'output `thinking`. Se il risultato è vuoto, viene restituito il prompt utente originale. | STRING |
| `thinking` | Il blocco di ragionamento prodotto dal modello, con il tag di apertura `<think>` rimosso. Vuoto quando il modello non ha prodotto alcun blocco di ragionamento; con i modelli Gemma 4 ci si aspetta un blocco di ragionamento solo quando `thinking` è abilitato. | STRING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextGenerateLTX2Prompt/it.md)

---
**Source fingerprint (SHA-256):** `a601a8bff65e8ee148d09f04ac0afc201dbc9ba5e09a65856400e9be37e085bb`
