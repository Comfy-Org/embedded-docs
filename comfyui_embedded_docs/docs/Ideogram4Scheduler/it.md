# Ideogram 4 Scheduler

Il nodo Ideogram 4 Scheduler genera una sequenza di valori sigma (livelli di rumore) per il processo di campionamento della diffusione, basandosi sulla schedulazione di riferimento di Ideogram 4. Crea una schedulazione del rumore personalizzata che si adatta alle dimensioni dell'immagine e consente una messa a punto tramite parametri statistici.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `steps` | Il numero di passaggi di campionamento per cui generare la schedulazione (predefinito: 20). L'output contiene `steps + 1` valori sigma. | INT | Sì | Da 1 a 200 |
| `width` | La larghezza dell'immagine in pixel (predefinito: 1024). La risoluzione relativa a un riferimento di 512×512 sposta la schedulazione del rumore. | INT | Sì | Da 256 a 8192 (passo: 16) |
| `height` | L'altezza dell'immagine in pixel (predefinito: 1024). La risoluzione relativa a un riferimento di 512×512 sposta la schedulazione del rumore. | INT | Sì | Da 256 a 8192 (passo: 16) |
| `mu` | Il parametro della media per la distribuzione logit-normale, che controlla il livello di rumore centrale. Combinato con il termine di risoluzione per formare lo spostamento logSNR (predefinito: 0.0). | FLOAT | Sì | Da -10.0 a 10.0 (passo: 0.05) |
| `std` | Il parametro della deviazione standard per la distribuzione logit-normale, che controlla la dispersione dei livelli di rumore (predefinito: 1.75). | FLOAT | Sì | Da 0.1 a 5.0 (passo: 0.05) |

Nota: la schedulazione è derivata da una distribuzione logit-normale sul tempo di riferimento. Un termine di risoluzione pari a `0.5 * log((width × height) / (512 × 512))` viene aggiunto a `mu`, quindi immagini più grandi o più piccole spostano la schedulazione rispetto a un riferimento di 512×512 allo stesso valore di `mu`.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `SIGMAS` | Un tensore di valori sigma che rappresenta la schedulazione del rumore, con lunghezza pari a `steps + 1`. I valori diminuiscono da rumore alto a rumore basso, con il valore finale impostato a 0.0 per un denoising completo. | SIGMAS |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Ideogram4Scheduler/it.md)

---
**Source fingerprint (SHA-256):** `af0749713ce223d2246fc24b5100f18aa68d56746480990282899c223578b8f4`
