# HeyGenImageToVideoNode

Trasforma un'immagine in un video con dialogo e audio sincronizzati usando HeyGen Video 1.0. L'immagine collegata viene utilizzata come primo fotogramma e il video generato mantiene il suo rapporto d'aspetto. Descrivi nel prompt ciò che dovrebbe accadere, incluse eventuali battute parlate. Il nodo carica l'immagine, crea il job video, attende che finisca e restituisce il video risultante.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `model` | Versione del modello utilizzata per la generazione. (predefinito: `"heygen-video-1"`) | DYNAMIC_COMBO | Sì | `"heygen-video-1"` |
| `image` | Primo fotogramma del video. È richiesta esattamente un'immagine; un batch viene rifiutato. Ritaglia l'immagine per cambiare la forma del video, perché l'output mantiene il rapporto d'aspetto di questa immagine. | IMAGE | Sì | 1 immagine, rapporto d'aspetto da 1:4 a 4:1 |
| `prompt` | Descrizione di ciò che accade nel video, incluse eventuali battute di dialogo. (predefinito: stringa vuota) | STRING | Sì | da 1 a 32000 caratteri |
| `duration` | Durata del video di output in secondi. (predefinito: 5) | INT | Sì | da 5 a 15 |
| `resolution` | Risoluzione di output. (predefinito: `"768p"`) | COMBO | Sì | `"768p"`<br>`"480p"`<br>`"2k"` |
| `seed` | Seed per la generazione. I risultati possono comunque variare tra esecuzioni con lo stesso seed. (predefinito: 42) | INT | Sì | da 0 a 4294967295 |

### Vincoli dei parametri

- **Immagine singola:** `image` deve contenere esattamente un'immagine. Il collegamento di un batch genera un errore.
- **Rapporto d'aspetto dell'immagine:** l'immagine non deve essere più larga di 4 volte la sua altezza né più alta di 4 volte la sua larghezza (tra 1:4 e 4:1); altrimenti l'esecuzione fallisce.
- **Prompt obbligatorio:** il prompt deve contenere almeno un carattere non di spaziatura e al massimo 32000 caratteri.
- **Seed:** il seed decide solo se il nodo viene rieseguito; i risultati non sono riproducibili con lo stesso seed.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `VIDEO` | Il video generato con dialogo e audio sincronizzati, al rapporto d'aspetto dell'immagine di input. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenImageToVideoNode/it.md)

---
**Source fingerprint (SHA-256):** `e15def8ce378572247be7dd197ac469fb655bcecf76521c8e9495bbad34e0284`
