# HeyGen Video 1.0 da immagine a video

Anima un'immagine in un video con dialogo e audio sincronizzati usando HeyGen Video 1.0. L'immagine collegata viene usata come primo fotogramma e il video generato ne mantiene il rapporto d'aspetto. Descrivi cosa deve accadere, incluse eventuali battute parlate, nel prompt. Il nodo carica l'immagine, crea il job video, attende che termini e restituisce il video risultante.

## Ingressi

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `model` | Versione del modello usata per la generazione. (predefinito: `"heygen-video-1"`) | DYNAMIC_COMBO | Sì | `"heygen-video-1"` |
| `image` | Primo fotogramma del video. È richiesta esattamente un'immagine; un batch viene rifiutato. Ritaglia l'immagine per cambiare la forma del video, perché l'output mantiene il rapporto d'aspetto di questa immagine. | IMAGE | Sì | 1 immagine, rapporto d'aspetto da 1:4 a 4:1 |
| `prompt` | Descrizione di ciò che accade nel video, inclusi eventuali dialoghi. (predefinito: stringa vuota) | STRING | Sì | da 1 a 16000 caratteri |
| `duration` | Durata del video di output in secondi. Ignorata quando `auto_duration` è `"enabled"`. (predefinito: 5) | INT | Sì | da 5 a 30 |
| `resolution` | Risoluzione di output. 1080p e 2k vengono renderizzati solo in 16:9 o 9:16, quindi l'immagine deve avere quella forma; ritagliala prima. (predefinito: `"768p"`) | COMBO | Sì | `"768p"`<br>`"480p"`<br>`"1080p"`<br>`"2k"` |
| `seed` | Seed per la generazione. I risultati possono comunque variare tra un'esecuzione e l'altra con lo stesso seed. (predefinito: 42) | INT | Sì | da 0 a 4294967295 |
| `auto_duration` | Se abilitato, la durata del video segue il dialogo tra virgolette nel prompt (da 8 a 30 secondi) e `duration` viene ignorato. (predefinito: `"disabled"`) | COMBO | No | `"disabled"`<br>`"enabled"` |

### Vincoli sui parametri

- **Immagine singola:** `image` deve contenere esattamente un'immagine. Collegare un batch genera un errore.
- **Rapporto d'aspetto dell'immagine:** l'immagine non deve essere più larga di 4 volte la sua altezza né più alta di 4 volte la sua larghezza (tra 1:4 e 4:1); altrimenti l'esecuzione fallisce.
- **Prompt obbligatorio:** il prompt deve contenere almeno un carattere non di spaziatura e al massimo 16000 caratteri.
- **Alte risoluzioni:** `resolution` `"1080p"` e `"2k"` richiedono un'immagine in 16:9 o 9:16, perché il video mantiene il rapporto d'aspetto dell'immagine. Ritaglia l'immagine per altre forme.
- **Seed:** il seed decide solo se il nodo viene eseguito nuovamente; i risultati non sono riproducibili con lo stesso seed.

## Uscite

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `VIDEO` | Il video generato con dialogo e audio sincronizzati, con il rapporto d'aspetto dell'immagine di input. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenImageToVideoNode/it.md)

---
**Source fingerprint (SHA-256):** `e711d1d84c6c73a2ee177903f982042086a57b3e1afff8390c6e5b3bcd09c914`
