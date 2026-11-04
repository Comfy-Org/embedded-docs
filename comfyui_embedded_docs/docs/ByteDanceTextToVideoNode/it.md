# ByteDance Testo in Video

Il nodo ByteDance Text to Video genera un video utilizzando i modelli ByteDance tramite un'API basata su un prompt testuale. Fornisci un prompt e scegli impostazioni come modello, risoluzione, rapporto d'aspetto e durata; il nodo invia la richiesta di generazione e restituisce il video generato.

**Nota:** questo nodo è contrassegnato come deprecato nel codice sorgente.

**Nota:** BytePlus dismette il modello Seedance 1.5 Pro l'11 novembre 2026, quindi questo nodo non lo offre più e i workflow salvati con esso smettono di funzionare. Usa invece `seedance-1-0-pro-250528`, `seedance-1-0-pro-fast-251015` o il [nodo partner Seedance 2.5](https://docs.comfy.org/it/tutorials/partner-nodes/bytedance/seedance-2-5).

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `model` | Il modello ByteDance utilizzato per generare il video (predefinito: `"seedance-1-0-pro-fast-251015"`). | COMBO | Sì | `"seedance-1-0-pro-250528"`<br>`"seedance-1-0-pro-fast-251015"` |
| `prompt` | Il prompt testuale utilizzato per generare il video. | STRING | Sì | - |
| `resolution` | La risoluzione del video in output. | COMBO | Sì | `"480p"`<br>`"720p"`<br>`"1080p"` |
| `aspect_ratio` | Il rapporto d'aspetto del video in output. | COMBO | Sì | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"` |
| `duration` | La durata del video in output in secondi (predefinito: 5). | INT | Sì | da 3 a 12 |
| `seed` | Seed da utilizzare per la generazione (predefinito: 0). | INT | No | da 0 a 2147483647 |
| `camera_fixed` | Specifica se fissare la camera. La piattaforma aggiunge al prompt un'istruzione per fissare la camera, ma non garantisce l'effetto effettivo (predefinito: False). | BOOLEAN | No | - |
| `watermark` | Indica se aggiungere al video una filigrana "AI generated" (predefinito: False). | BOOLEAN | No | - |
| `generate_audio` | Aggiunge una traccia audio generata dall'IA. Gli altri modelli ignorano questo input (predefinito: False). | BOOLEAN | No | - |

**Vincoli dei parametri:**

- Il parametro `prompt` deve contenere almeno 1 carattere dopo la rimozione degli spazi bianchi.
- Il parametro `prompt` non può contenere i seguenti parametri testuali: "resolution", "ratio", "duration", "seed", "camerafixed", "watermark".
- Il nodo costruisce il prompt finale aggiungendo al testo del prompt le impostazioni selezionate `resolution`, `aspect_ratio`, `duration`, `seed`, `camera_fixed` e `watermark`.
- Il parametro `duration` è limitato a valori compresi tra 3 e 12 secondi.
- Il parametro `seed` accetta valori da 0 a 2,147,483,647.
- Il parametro `generate_audio` è accettato per compatibilità, ma gli altri modelli lo ignorano.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `output` | Il file video generato | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceTextToVideoNode/it.md)

---
**Source fingerprint (SHA-256):** `d26d13c99a25bb14a0b1c1f3bae2dea1b30bf35f886331f26ef72e64ca357ef5`
