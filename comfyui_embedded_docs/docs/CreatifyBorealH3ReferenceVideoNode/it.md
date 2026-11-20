# Creatify Boreal-H3 Reference to Video

Creatify Boreal-H3 Reference to Video genera un video con audio guidato da immagini, video e audio di riferimento, utilizzando il modello H3 post-addestrato di Creatify pensato per video pubblicitari. Assegna un nome ai riferimenti nel prompt come `@Image1`, `@Video1` e `@Audio1` per controllare il contributo di ciascuno.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `reference_images` | Slot espandibile per un massimo di 9 immagini di riferimento (`image_1` ... `image_9`), a cui si fa riferimento nel prompt come `@Image1` ... `@Image9` nell'ordine di connessione. È richiesta almeno un'immagine o un video e al massimo 12 riferimenti in totale. | IMAGE | No | Fino a 9 immagini |
| `reference_videos` | Slot espandibile per un massimo di 3 video di riferimento (`video_1` ... `video_3`), ciascuno lungo almeno 1 secondo. Il loro audio viene riutilizzato quando il prompt chiede di continuarlo; una nuova riga nel prompt lo sostituisce. Vengono addebitati in totale al massimo 15 secondi di video di riferimento. | VIDEO | No | Fino a 3 video |
| `reference_audios` | Slot espandibile per un massimo di 3 clip di riferimento (`audio_1` ... `audio_3`). Il parlato guida la voce anziché le parole, e la musica strumentale può diventare la colonna sonora. | AUDIO | No | Fino a 3 clip |
| `prompt` | Prompt testuale che descrive il video e fa riferimento ai riferimenti connessi. Deve contenere almeno un carattere che non sia uno spazio bianco. | STRING | Sì | Qualsiasi testo non vuoto |
| `resolution` | Risoluzione del video di output (predefinito: `"768p"`). | COMBO | Sì | `"768p"`<br>`"1088p"`<br>`"2k"` |
| `aspect_ratio` | Rapporto d'aspetto del video di output. `"auto"` segue la prima immagine di riferimento. Con solo video di riferimento a `"1088p"`, il nodo sceglie il rapporto supportato più vicino al primo video, che può differire dal suo rapporto esatto; alle altre risoluzioni `"auto"` viene passato a Creatify così com'è (predefinito: `"auto"`). | COMBO | Sì | `"auto"`<br>`"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"` |
| `duration` | Durata del video in secondi (predefinito: 5). A `"2k"` il massimo è 14 secondi. | INT | Sì | 1 a 15 (passo 1) |
| `prompt_enhancement` | Come Creatify riscrive il prompt prima del rendering: `"auto"` e `"ads"` lo trasformano in un prompt per video pubblicitario e possono aggiungere battute parlate, `"general"` lo riscrive per qualsiasi altro video, `"none"` lo renderizza così come scritto (predefinito: `"auto"`). | COMBO | Sì | `"auto"`<br>`"ads"`<br>`"general"`<br>`"none"` |
| `seed` | Il seed controlla se il nodo viene rieseguito. A Boreal-H3 non viene inviato alcun seed, quindi rieseguire con gli stessi input può produrre un video diverso (predefinito: 42). | INT | Sì | 0 a 2147483647 |

**Vincoli:** collegare almeno un'immagine o un video di riferimento; il solo audio non è accettato. Un tag di riferimento che punta oltre il numero di riferimenti connessi di quel tipo genera un errore, e lo stesso vale per più di 12 riferimenti in totale. Con `"1088p"` e `"auto"` e nessuna immagine di riferimento, il rapporto d'aspetto viene preso dal primo video di riferimento.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `VIDEO` | Il video generato con audio. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreatifyBorealH3ReferenceVideoNode/it.md)

---
**Source fingerprint (SHA-256):** `c6e60b83a8e02262fcbae7c04f4f379cf665a9e25b2fa00836047fe56d0fa064`
