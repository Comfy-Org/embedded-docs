# Creatify Boreal-H3 Video

Creatify Boreal-H3 Video trasforma un prompt testuale in un video con audio, utilizzando il modello H3 post-addestrato di Creatify, progettato per video pubblicitari. Collega un primo frame per animare un'immagine statica e, facoltativamente, un ultimo frame per concludere l'inquadratura su un'immagine scelta.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `prompt` | Prompt testuale che descrive il video. Deve contenere almeno un carattere non di spaziatura. | STRING | Sì | Qualsiasi testo non vuoto |
| `first_frame` | Immagine da cui inizia il video. Quando è collegata, mantieni `aspect_ratio` su `"auto"` in modo che il video segua l'immagine. | IMAGE | No | - |
| `last_frame` | Immagine su cui termina il video. Richiede un `first_frame` collegato. | IMAGE | No | - |
| `resolution` | Risoluzione del video di output (predefinito: `"768p"`). | COMBO | Sì | `"768p"`<br>`"1088p"`<br>`"2k"` |
| `aspect_ratio` | Rapporto d'aspetto del video di output. `"auto"` segue il primo frame quando ne è collegato uno; in tal caso lascialo su `"auto"` (predefinito: `"auto"`). | COMBO | Sì | `"auto"`<br>`"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"` |
| `duration` | Durata del video in secondi (predefinito: 5). Con `"2k"` il massimo è 14 secondi. | INT | Sì | 1 a 15 (passo: 1) |
| `prompt_enhancement` | Come Creatify riscrive il prompt prima del rendering: `"auto"` e `"ads"` lo trasformano in un prompt per video pubblicitario e possono aggiungere frasi parlate, `"general"` lo riscrive per qualsiasi altro video, `"none"` lo genera così com'è scritto (predefinito: `"auto"`). | COMBO | Sì | `"auto"`<br>`"ads"`<br>`"general"`<br>`"none"` |
| `seed` | Il seed controlla se il nodo viene rieseguito. A Boreal-H3 non viene inviato alcun seed, quindi rieseguire con gli stessi input può produrre un video diverso (predefinito: 42). | INT | Sì | 0 a 2147483647 |

**Vincoli:** con un `first_frame` il rapporto d'aspetto proviene sempre dall'immagine, quindi qualsiasi altro valore di `aspect_ratio` genera un errore. Un `last_frame` senza un `first_frame` viene rifiutato, e una `duration` superiore a 14 secondi viene rifiutata con `"2k"`.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `VIDEO` | Il video generato con audio. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreatifyBorealH3VideoNode/it.md)

---
**Source fingerprint (SHA-256):** `535bcbeced69cffd4d0edca04f30dd00dac4ec728cd8eb638b4f9d9af8448336`
