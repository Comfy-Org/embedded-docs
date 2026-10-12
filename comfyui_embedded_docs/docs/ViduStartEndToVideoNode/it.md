# ViduStartEndToVideoNode

Il nodo Vidu Start End To Video Generation crea un video generando frame tra un frame iniziale e un frame finale. Utilizza un prompt testuale per guidare il processo di generazione del video e supporta vari modelli video con impostazioni di risoluzione e movimento diverse. Il nodo verifica che i frame iniziale e finale abbiano rapporti d'aspetto compatibili prima dell'elaborazione.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `model` | Nome del modello | COMBO | Sì | `"viduq1"` |
| `first_frame` | Frame iniziale | IMAGE | Sì | - |
| `end_frame` | Frame finale | IMAGE | Sì | - |
| `prompt` | Una descrizione testuale per la generazione del video | STRING | No | - |
| `duration` | Durata del video di output in secondi (predefinito: 5, fissata a 5 secondi) | INT | No | 5-5 |
| `seed` | Seed per la generazione del video (0 per casuale) (predefinito: 0) | INT | No | 0-2147483647 |
| `resolution` | I valori supportati possono variare in base al modello e alla durata (predefinito: "1080p") | COMBO | No | `"1080p"` |
| `movement_amplitude` | L'ampiezza di movimento degli oggetti nel frame (predefinito: "auto") | COMBO | No | `"auto"`<br>`"small"`<br>`"medium"`<br>`"large"` |

**Nota:** I frame iniziali e finali devono avere rapporti d'aspetto compatibili (validati con tolleranza del rapporto min_rel=0.8, max_rel=1.25).

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `output` | Il file video generato | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ViduStartEndToVideoNode/it.md)

---
**Source fingerprint (SHA-256):** `5e8a566373fac84111e90d00c00a6932a23e827f9b4669950c223256c08dd96c`
