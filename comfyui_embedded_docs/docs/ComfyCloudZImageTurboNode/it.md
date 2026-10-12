# Comfy Cloud Z-Image Turbo da testo a immagine [BETA]

Questo nodo genera un'immagine da un prompt testuale usando il modello Z-Image Turbo, che completa in appena 8 passaggi. La generazione viene eseguita in remoto sulle GPU di Comfy Cloud e viene fatturata in base alla durata di esecuzione, il che lo rende una delle opzioni più rapide ed economiche disponibili qui per iterare su idee di immagini. Una volta terminata la generazione, il nodo scarica l'immagine finita per utilizzarla nel flusso di lavoro. Questo nodo fa parte del set di nodi Comfy Cloud, contrassegnato come BETA: le opzioni possono essere aggiunte o rimosse e un flusso di lavoro può essere ritirato.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `prompt` | Prompt testuale che descrive l'immagine da generare. Accetta input su più righe e viene ripulito dagli spazi bianchi prima dell'invio. Non deve essere vuoto dopo la rimozione degli spazi bianchi. Predefinito: "" (vuoto). | STRING | Sì | 1 - 4096 caratteri |
| `seed` | Seme casuale utilizzato per controllare la riproducibilità della generazione. Cambiandolo si produce una variazione diversa. Include un'opzione di controllo dopo la generazione. Predefinito: 42. | INT | No | 0 - 18446744073709551615 |
| `aspect_ratio` | Rapporto d'aspetto dell'immagine generata. Predefinito: "1:1". | COMBO | No | "1:1"<br>"3:4"<br>"2:3"<br>"3:2"<br>"4:3"<br>"16:9"<br>"9:16"<br>"21:9" |
| `megapixels` | Budget totale di pixel. 1.0 corrisponde a circa 1024x1024 con rapporto quadrato. Predefinito: 1.0. | FLOAT | No | 0.1 - 16.0<br>(passo di 0.1) |

Nota: i valori di input vengono convalidati prima dell'invio della generazione. Il `prompt` deve contenere tra 1 e 4.096 caratteri dopo la rimozione degli spazi bianchi, `aspect_ratio` deve essere una delle opzioni elencate e `megapixels` deve essere inserito in incrementi di 0.1.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `IMAGE` | L'immagine generata, restituita come tensore immagine, pronta per ulteriori nodi di elaborazione o salvataggio delle immagini. | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyCloudZImageTurboNode/it.md)

---
**Source fingerprint (SHA-256):** `9c78bf9aca5800212d1c5a8f9581dc6c154a82220cd60a8b55ebe74111d2f542`
