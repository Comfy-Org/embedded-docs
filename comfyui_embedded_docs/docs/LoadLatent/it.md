# LoadLatent

Il nodo LoadLatent carica rappresentazioni latenti salvate in precedenza da file .latent nella directory di input. Legge i dati del tensore latente dal file selezionato e applica eventuali regolazioni di scala necessarie prima di restituire i dati latenti per l'uso in altri nodi.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `latent` | Seleziona quale file .latent caricare tra i file disponibili nella directory di input | COMBO | Sì | Tutti i file .latent nella directory di input (elenco dinamico, ordinato alfabeticamente) |

Nota: l'elenco dei file disponibili viene generato dinamicamente e include solo i file con estensione .latent presenti nella directory di input. Se il file selezionato non esiste più, il nodo lo segnala come file latente non valido.

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `LATENT` | Restituisce i dati della rappresentazione latente caricati dal file selezionato come tensore float. Se il file non contiene il marcatore `latent_format_version_0`, il tensore viene scalato di 1/0.18215 prima di essere restituito; i file che contengono il marcatore vengono restituiti alla loro scala memorizzata. | LATENT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadLatent/it.md)

---
**Source fingerprint (SHA-256):** `0938214361687a3a98e03878b8cbc0240100cbeacc0b157c4a299e59e7728a13`
