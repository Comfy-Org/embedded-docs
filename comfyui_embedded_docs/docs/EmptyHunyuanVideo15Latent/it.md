# Video latent Hunyuan 1.5 vuoto

Questo nodo crea un tensore latente vuoto formattato specificamente per l'uso con il modello HunyuanVideo 1.5. Genera un punto di partenza vuoto per la generazione video allocando un tensore di zeri con il numero corretto di canali e le dimensioni spaziali per lo spazio latente del modello.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `width` | La larghezza del fotogramma video in pixel. | INT | Sì | - |
| `height` | L'altezza del fotogramma video in pixel. | INT | Sì | - |
| `length` | Il numero di fotogrammi nella sequenza video. | INT | Sì | - |
| `batch_size` | Il numero di campioni video da generare in un batch (predefinito: 1). | INT | No | - |

**Nota:** Le dimensioni spaziali del tensore latente generato vengono calcolate dividendo i valori di input `width` e `height` per 16 (questo nodo usa un fattore di scala spaziale di 16 anziché 8). La dimensione temporale (fotogrammi) viene calcolata come `((length - 1) // 4) + 1`. Questi calcoli usano la divisione intera, quindi `width` e `height` dovrebbero essere multipli di 16 per evitare troncamenti.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `samples` | Un tensore latente vuoto con dimensioni adatte al modello HunyuanVideo 1.5. Il tensore ha una forma `[batch_size, 32, ((length - 1) // 4) + 1, height // 16, width // 16]`. L'output include anche un valore `downscale_ratio_spacial` pari a 16. | LATENT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyHunyuanVideo15Latent/it.md)

---
**Source fingerprint (SHA-256):** `ce7ec75e8433c778d175a3e2ea260a4397aa5507428908b9a32f50fbe9e184c6`
