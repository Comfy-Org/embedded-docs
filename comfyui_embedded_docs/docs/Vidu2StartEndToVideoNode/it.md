# Vidu2 Generazione Video da Frame Iniziale/Finale

Questo nodo genera un video interpolando tra un frame iniziale e un frame finale forniti, guidato da un prompt testuale. Utilizza un modello Vidu specificato per creare una transizione fluida tra le due immagini per una durata impostata.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `model` | Il modello Vidu da utilizzare per la generazione del video. | COMBO | Sì | `"viduq2-pro-fast"`<br>`"viduq2-pro"`<br>`"viduq2-turbo"` |
| `first_frame` | L'immagine iniziale per la sequenza video. È consentita una sola immagine. | IMAGE | Sì | - |
| `end_frame` | L'immagine finale per la sequenza video. È consentita una sola immagine. | IMAGE | Sì | - |
| `prompt` | Descrizione del prompt (max 2000 caratteri). | STRING | Sì | - |
| `duration` | La durata del video generato in secondi (predefinito: 5). | INT | No | da 2 a 8 |
| `seed` | Un numero utilizzato per inizializzare la generazione casuale per ottenere risultati riproducibili (predefinito: 1). | INT | No | da 0 a 2147483647 |
| `resolution` | La risoluzione di output del video generato. | COMBO | No | `"720p"`<br>`"1080p"` |
| `movement_amplitude` | L'ampiezza del movimento degli oggetti nel frame. | COMBO | No | `"auto"`<br>`"small"`<br>`"medium"`<br>`"large"` |

**Nota:** Le immagini `first_frame` e `end_frame` devono avere rapporti d'aspetto simili. Il nodo verifica che i loro rapporti d'aspetto siano compresi in un intervallo relativo da 0,8 a 1,25. È consentita una sola immagine per ciascun input.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|-----------|
| `output` | Il file video generato. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Vidu2StartEndToVideoNode/it.md)

---
**Source fingerprint (SHA-256):** `01316d15f95f264cadfb33978565fc320a9f42917693faa87c1367c0f31ca400`
