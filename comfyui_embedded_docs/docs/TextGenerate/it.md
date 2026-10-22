# Genera Testo

Il nodo TextGenerate usa un modello CLIP per creare testo basato sul prompt dell'utente. Può facoltativamente usare immagini, video o audio come contesto aggiuntivo per guidare la generazione del testo. Puoi controllare la lunghezza dell'output, abilitare una modalità thinking per i modelli supportati e scegliere se usare il campionamento casuale con varie impostazioni oppure generare testo senza campionamento.

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `sampling_mode` | Controlla se viene usato il campionamento casuale durante la generazione del testo. Quando è impostato su "on", diventano disponibili parametri di campionamento aggiuntivi. Quando è impostato su "off", il nodo genera testo senza campionamento casuale. | DYNAMIC_COMBO | Sì | `"on"`<br>`"off"` |
| `clip` | Il modello CLIP usato per tokenizzare il prompt e generare testo. | CLIP | Sì | N/A |
| `prompt` | Il prompt testuale che guida la generazione. Questo campo supporta più righe e prompt dinamici. Il valore predefinito è una stringa vuota. | STRING | Sì | N/A |
| `image` | Un'immagine opzionale che può essere usata insieme al prompt testuale per influenzare il testo generato. | IMAGE | No | N/A |
| `video` | Fotogrammi video come batch di immagini. Si presume siano a 24 FPS; vengono sottocampionati internamente a 1 FPS. | IMAGE | No | N/A |
| `audio` | Un input audio opzionale che può essere usato insieme al prompt testuale per influenzare il testo generato. | AUDIO | No | N/A |
| `max_length` | Il numero massimo di token che il modello genererà. Il valore predefinito è 512. | INT | Sì | 1 a 32768 |
| `thinking` | Opera in modalità thinking se il modello la supporta. Il valore predefinito è False. | BOOLEAN | No | True or False |
| `use_default_template` | Usa il prompt/template di sistema integrato se il modello ne ha uno. Il valore predefinito è True. Questo è un parametro avanzato. | BOOLEAN | No | True or False |
| `mtp` | Decodifica speculativa con la testa multi-token-prediction del checkpoint. Non ha effetto senza pesi MTP. `"auto"` adatta profondità e ampiezza della bozza in base alle corrispondenze di token osservate e al costo di esecuzione, `"2"`–`"5"` fissano una profondità costante, le modalità `tree` fissano sia l'ampiezza sia la profondità. L'output campionato rimane correttamente distribuito ma differisce dall'output non-MTP per lo stesso seed (predefinito: `"auto"`). | COMBO | No | `"auto"`<br>`"off"`<br>`"2"`<br>`"3"`<br>`"4"`<br>`"5"`<br>`"tree2s1"`<br>`"tree2s2"`<br>`"tree3s1"`<br>`"tree4s1m8"` |
| `system_prompt` | Sostituisce il prompt di sistema nel template chat del modello. Viene ignorato quando il template predefinito non viene usato. Collega un input STRING invece di digitare nel nodo (predefinito: vuoto). | STRING | No | N/A |

### Parametri di campionamento (quando `sampling_mode` è "on")

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `temperature` | Controlla la casualità dell'output. Valori più bassi rendono l'output più prevedibile, valori più alti lo rendono più creativo. Il valore predefinito è 0.7. | FLOAT | Sì | 0.01 a 2.0 |
| `top_k` | Limita il pool di campionamento ai K token successivi più probabili. Un valore di 0 disabilita questo filtro. Il valore predefinito è 64. | INT | Sì | 0 a 1000 |
| `top_p` | Usa il campionamento nucleare: mantiene il più piccolo insieme di token più probabili la cui probabilità cumulativa raggiunge questo valore. Il valore predefinito è 0.95. | FLOAT | Sì | 0.0 a 1.0 |
| `min_p` | Imposta una soglia minima di probabilità affinché i token siano considerati. Il valore predefinito è 0.05. | FLOAT | Sì | 0.0 a 1.0 |
| `repetition_penalty` | Penalizza i token già generati per ridurre le ripetizioni. Un valore di 1.0 non applica alcuna penalità. Il valore predefinito è 1.05. | FLOAT | Sì | 0.0 a 5.0 |
| `seed` | Un numero usato per inizializzare il generatore di numeri casuali per risultati riproducibili. Il valore predefinito è 0. | INT | Sì | 0 a 18446744073709551615 |
| `presence_penalty` | Penalizza i nuovi token in base al fatto che siano già comparsi nel testo finora, incoraggiando il modello a parlare di nuovi argomenti. Il valore predefinito è 0.0. | FLOAT | No | 0.0 a 5.0 |

**Nota:** I parametri di campionamento riportati sopra sono attivi e visibili nell'interfaccia del nodo solo quando `sampling_mode` è impostato su "on". Quando `sampling_mode` è impostato su "off", non è disponibile alcun parametro di campionamento e il nodo genera testo senza campionamento casuale.

**Nota:** Quando il testo generato contiene un blocco di ragionamento (si apre con `<think>` o il prompt termina con esso), il ragionamento viene restituito separatamente: `generated_text` contiene la risposta e `thinking` contiene il ragionamento con il tag di apertura rimosso. Altrimenti `generated_text` contiene tutto ciò che il modello ha prodotto e `thinking` è vuoto.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `generated_text` | Il testo generato dal modello in base al prompt di input e all'immagine, video o audio opzionali, con qualsiasi blocco di ragionamento separato nell'output `thinking`. | STRING |
| `thinking` | Il blocco di ragionamento prodotto dal modello, con il tag di apertura `<think>` rimosso. Vuoto quando il modello non ha prodotto alcun blocco di ragionamento. | STRING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextGenerate/it.md)

---
**Source fingerprint (SHA-256):** `e0854b0ce5a41e195a2634f4739c22c7dd0df1f2309cb8a02b506b8791bf3bee`
