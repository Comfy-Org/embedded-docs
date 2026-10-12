# Campiona Frame Video

Il nodo `VideoFrameSample` estrae un numero fisso di fotogrammi da un video utilizzando una delle quattro strategie. Per le strategie contigue "head" e "tail", l'output è un riferimento video lazy (i fotogrammi non vengono decodificati); per le strategie non contigue "uniform" e "random", vengono decodificati solo i fotogrammi selezionati.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `video` | Video di input. | VIDEO | Sì | – |
| `num_frames` | Numero di fotogrammi da campionare (predefinito: 16). | INT | Sì | 1 – 9999 |
| `strategy` | uniform: distribuiti uniformemente, head: primi N, tail: ultimi N, random: casuali ordinati (predefinito: "uniform"). | COMBO | Sì | "uniform"<br>"head"<br>"tail"<br>"random" |
| `seed` | Seme casuale, usato solo con la strategia "random" (predefinito: 0). | INT | Sì | 0 – 18446744073709551615 |

- `num_frames` viene automaticamente limitato al conteggio totale dei fotogrammi del video di input.
- Il parametro `seed` non ha effetto se `strategy` non è impostato su `"random"`.
- Quando `strategy` è `"uniform"` e `num_frames` è 1, viene selezionato il fotogramma centrale del video.
- Un valore `strategy` non riconosciuto genera un errore.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|-----------|
| `video` | Video campionato. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VideoFrameSample/it.md)

---
**Source fingerprint (SHA-256):** `727504a9cf7fe5505c33da071cb8f21a38e1b7c0f964c5da172d9cedfc2f2300`
