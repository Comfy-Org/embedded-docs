# ByteDanceTextToVideoNode

Il nodo ByteDance Text to Video genera un video utilizzando i modelli ByteDance tramite un'API basata su un prompt testuale. Fornisci un prompt e scegli impostazioni come modello, risoluzione, rapporto d'aspetto e durata; il nodo invia la richiesta di generazione e restituisce il video generato.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `model` | Il modello ByteDance utilizzato per generare il video (predefinito: `"seedance-1-0-pro-fast-251015"`). | COMBO | Sì | `"seedance-1-5-pro-251215"`<br>`"seedance-1-0-pro-250528"`<br>`"seedance-1-0-pro-fast-251015"` |
| `prompt` | Il prompt testuale utilizzato per generare il video. | STRING | Sì | - |
| `resolution` | La risoluzione del video in output. | COMBO | Sì | `"480p"`<br>`"720p"`<br>`"1080p"` |
| `aspect_ratio` | Il rapporto d'aspetto del video in output. | COMBO | Sì | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"` |
| `duration` | La durata del video in output in secondi (predefinito: 5). | INT | Sì | da 3 a 12 |
| `seed` | Seed da utilizzare per la generazione (predefinito: 0). | INT | No | da 0 a 2147483647 |
| `camera_fixed` | Specifica se fissare la camera. La piattaforma aggiunge al prompt un'istruzione per fissare la camera, ma non garantisce l'effetto effettivo (predefinito: False). | BOOLEAN | No | - |
| `watermark` | Indica se aggiungere al video una filigrana "AI generated" (predefinito: False). | BOOLEAN | No | - |
| `generate_audio` | Questo parametro viene ignorato per qualsiasi modello tranne `seedance-1-5-pro-251215` (predefinito: False). | BOOLEAN | No | - |

**Vincoli dei parametri:**

- Il parametro `prompt` deve contenere almeno 1 carattere dopo la rimozione degli spazi bianchi.
- Il parametro `prompt` non può contenere i seguenti parametri testuali: "resolution", "ratio", "duration", "seed", "camerafixed", "watermark".
- Il nodo costruisce il prompt finale aggiungendo al testo del prompt le impostazioni selezionate `resolution`, `aspect_ratio`, `duration`, `seed`, `camera_fixed` e `watermark`.
- Il parametro `duration` è limitato a valori compresi tra 3 e 12 secondi. Per il modello `seedance-1-5-pro-251215`, la durata minima supportata è di 4 secondi.
- Il parametro `seed` accetta valori da 0 a 2,147,483,647.
- Il parametro `generate_audio` ha effetto solo quando il parametro `model` è impostato su `seedance-1-5-pro-251215`; viene ignorato per tutti gli altri modelli.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `output` | Il file video generato | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceTextToVideoNode/it.md)

---
**Source fingerprint (SHA-256):** `83b805b63e59a76cae378b0407b409e1bfe900677ef1e01fc836fede47283eee`
