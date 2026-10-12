# Runway Immagine a Video (Gen4 Turbo)

Il nodo Runway Image to Video (Gen4 Turbo) genera un video da un singolo frame iniziale utilizzando il modello Gen4 Turbo di Runway. Riceve un prompt testuale e un frame immagine iniziale, quindi crea una sequenza video in base alle impostazioni di durata e rapporto d'aspetto fornite. Il nodo gestisce il caricamento del frame iniziale all'API di Runway e restituisce il video generato.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `prompt` | Prompt testuale per la generazione (predefinito: stringa vuota) | STRING | Sì | - |
| `start_frame` | Frame iniziale da utilizzare per il video | IMAGE | Sì | - |
| `duration` | Durata del video in secondi | COMBO | Sì | `"5"`<br>`"10"` |
| `ratio` | Rapporto d'aspetto per il video generato (predefinito: "1280:720") | COMBO | Sì | `"1280:720"`<br>`"720:1280"`<br>`"1104:832"`<br>`"832:1104"`<br>`"960:960"`<br>`"1584:672"` |
| `seed` | Seed casuale per la generazione (predefinito: 0) | INT | No | 0 to 4294967295 |

**Vincoli sui parametri:**

- L'immagine `start_frame` deve avere dimensioni non superiori a 7999x7999 pixel
- L'immagine `start_frame` deve avere un rapporto d'aspetto compreso tra 0.5 e 2.0
- Il `prompt` deve contenere almeno un carattere

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `output` | Il video generato in base al frame di input e al prompt | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RunwayImageToVideoNodeGen4/it.md)

---
**Source fingerprint (SHA-256):** `1cbf70391f1dfd0f40a3085dad68b98ec20e964eab7d4a17b2fb3cd07a035277`
