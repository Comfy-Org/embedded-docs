# EmptyMiniMaxH3LatentAV

Questo nodo crea un latente vuoto che combina sia informazioni video sia audio per il modello MiniMax H3. Si definiscono larghezza, altezza e lunghezza del contenuto, e il nodo produce un latente vuoto che il modello può usare come punto di partenza per la generazione. La durata (`length`) viene regolata automaticamente per adattarsi alla griglia di fotogrammi richiesta dal modello, pari a 17k+5 fotogrammi a 24 fps.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `width` | La larghezza del latente in pixel. I valori devono essere multipli di 32. Predefinito: 1344. | INT | Sì | 32 - MAX_RESOLUTION (passo 32) |
| `height` | L'altezza del latente in pixel. I valori devono essere multipli di 32. Predefinito: 768. | INT | Sì | 32 - MAX_RESOLUTION (passo 32) |
| `length` | Numero di fotogrammi a 24 fps, arrotondato per eccesso alla griglia 17k+5 del modello (124 = ~5 s; l'intervallo addestrato è ~124-362, valori più lunghi non sono testati). Predefinito: 124. | INT | Sì | 5 - 3600 (passo 17) |

Nota: il valore `length` viene arrotondato per eccesso al successivo numero di fotogrammi che rientra nella griglia 17k+5 del modello (17 x k + 5 fotogrammi, come 5, 22, 39, 56, 73, 90, 107, 124 e così via). I valori `width` e `height` devono essere multipli di 32. La risoluzione massima è il valore definito dal sistema in ComfyUI.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `latent` | Il latente congiunto video+audio vuoto generato per MiniMax H3, dimensionato in base ai valori di input `width`, `height` e `length`. | LATENT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyMiniMaxH3LatentAV/it.md)

---
**Source fingerprint (SHA-256):** `ee24f4ac630858d87b9b98bb402689a5790e0ed882ec47dffe7b497216e37a5c`
