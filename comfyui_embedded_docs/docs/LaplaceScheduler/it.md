# LaplaceScheduler

Il nodo LaplaceScheduler genera una sequenza di valori sigma seguendo una distribuzione di Laplace per l'uso nel campionamento diffusionale. Crea una pianificazione dei livelli di rumore che diminuiscono gradualmente da un valore massimo a uno minimo, usando i parametri della distribuzione di Laplace per controllare la progressione. Questo scheduler è comunemente usato nei flussi di lavoro di campionamento personalizzati per definire la pianificazione del rumore per i modelli di diffusione.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `steps` | Numero di passaggi di campionamento nella pianificazione (predefinito: 20) | INT | Sì | 1 to 10000 |
| `sigma_max` | Valore sigma massimo all'inizio della pianificazione (predefinito: 14.614642) | FLOAT | Sì | 0.0 to 5000.0 |
| `sigma_min` | Valore sigma minimo alla fine della pianificazione (predefinito: 0.0291675) | FLOAT | Sì | 0.0 to 5000.0 |
| `mu` | Parametro di media per la distribuzione di Laplace (predefinito: 0.0) | FLOAT | Sì | -10.0 to 10.0 |
| `beta` | Parametro di scala per la distribuzione di Laplace (predefinito: 0.5) | FLOAT | Sì | 0.0 to 10.0 |

Nota: `sigma_max`, `sigma_min`, `mu` e `beta` sono parametri avanzati.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `SIGMAS` | Una sequenza di valori sigma che segue una pianificazione con distribuzione di Laplace | SIGMAS |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LaplaceScheduler/it.md)

---
**Source fingerprint (SHA-256):** `8e5ca00f4797f863a2cf8b9b115ec27beb7f65981cbb04eb036150402fc19389`
