# Higgsfield Genjutsu Motion Transfer

Il nodo **Higgsfield Genjutsu Motion Transfer** rielabora un video con nuovi personaggi, ambientazioni o stili presi da immagini di riferimento, mantenendo il movimento, il movimento della camera, la temporizzazione e l'audio della clip sorgente. Collega la clip da rielaborare e una o più immagini di riferimento che descrivono il nuovo aspetto, poi descrivi il risultato nel prompt. La richiesta viene inviata all'API di Higgsfield e viene restituito il video generato.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `model` | Modello da utilizzare. Selezionando un modello vengono visualizzati i parametri specifici: `video`, `reference_images`, `prompt`, `resolution` e `seed`. | DYNAMIC_COMBO | Sì | `"genjutsu-v1.0"` |
| `video` | Video sorgente di cui vengono mantenuti il movimento, il movimento della camera, la temporizzazione e l'audio. Almeno 4 secondi; vengono utilizzati solo i primi 30 secondi. | VIDEO | Sì | da 4 a 30 secondi |
| `reference_images` | Slot espandibile: collega da 1 a 8 immagini (`image_1`, `image_2`, ...) dei personaggi, delle ambientazioni o degli stili da utilizzare. Un input in batch viene conteggiato una volta per immagine. | IMAGE | Sì | da 1 a 8 immagini |
| `prompt` | Opzionale. Descrivi il risultato, ad esempio quale riferimento sostituisce quale persona, oppure una nuova ambientazione. (predefinito: vuoto) | STRING | Sì | Qualsiasi testo |
| `resolution` | Risoluzione del video in output. (predefinita: `"720p"`) | COMBO | Sì | `"480p"`<br>`"720p"`<br>`"1080p"` |
| `seed` | Il seed controlla se il nodo deve essere rieseguito; i risultati sono non deterministici indipendentemente dal seed. Questo parametro ha la funzionalità «controllo dopo la generazione» (predefinito: 42). | INT | Sì | da 0 a 2147483647 |

Il video sorgente viene convalidato prima che la richiesta venga inviata: una clip più corta di 4 secondi viene rifiutata, mentre una clip più lunga di 30 secondi viene tagliata ai primi 30 secondi. L'audio viene trasferito nel risultato. Le immagini di riferimento vengono caricate per prime e il numero totale di immagini in tutti gli slot collegati non può superare 8, anche se il nodo espone otto slot. La moderazione dei contenuti di Higgsfield può rifiutare l'input o il risultato, il che genera un errore invece di restituire un video.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `VIDEO` | Il file video con il nuovo stile. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HiggsfieldMotionTransferNode/it.md)

---
**Source fingerprint (SHA-256):** `f0c30fb93dd2af8d564335290fdb6ff61c38e36ab62cef9641fd1aa81cc10cd2`
