# Runway Immagine a Video (Gen3a Turbo)

Il nodo Runway Image to Video (Gen3a Turbo) genera un video da un singolo fotogramma iniziale utilizzando il modello Gen3a Turbo di Runway. Riceve un prompt testuale e un fotogramma immagine iniziale, quindi crea una sequenza video in base alla durata e al rapporto d'aspetto specificati. La generazione viene elaborata in remoto tramite l'API di Runway. Questo nodo è contrassegnato come deprecato.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `prompt` | Prompt testuale per la generazione (predefinito: "") | STRING | Sì | N/A |
| `start_frame` | Fotogramma iniziale da utilizzare per il video | IMAGE | Sì | N/A |
| `duration` | Durata del video generato, in secondi (predefinito: "5") | COMBO | Sì | `"5"`<br>`"10"` |
| `ratio` | Rapporto d'aspetto del video generato (predefinito: "768:1280") | COMBO | Sì | `"768:1280"`<br>`"1280:768"` |
| `seed` | Seme casuale per la generazione (predefinito: 0) | INT | Sì | da 0 a 4294967295 |

**Vincoli sui parametri:**

- Il `prompt` deve contenere almeno un carattere (non può essere vuoto).
- Il parametro `start_frame` accetta una singola immagine (massimo 1).
- Il parametro `start_frame` non deve superare i 7999 x 7999 pixel di dimensione.
- Il parametro `start_frame` deve avere un rapporto d'aspetto compreso tra 1:2 e 2:1 (da 0.5 a 2.0).

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `output` | La sequenza video generata | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RunwayImageToVideoNodeGen3a/it.md)

---
**Source fingerprint (SHA-256):** `ff66cbdfa80aabeaf96d43e7822dd0c700ee027d13fb430a9dc2079e1a23f38e`
