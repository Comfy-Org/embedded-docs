# Genera Tracce Video

Il nodo `GenerateTracks` crea molteplici percorsi di movimento paralleli (tracce) per la generazione video. Definisce un percorso principale da una posizione iniziale a una posizione finale, quindi genera un insieme di tracce che corrono parallele a questo percorso, distanziate uniformemente. È possibile controllare la forma del percorso (linea retta o curva di Bezier), la velocità di movimento lungo di esso e in quali fotogrammi le tracce sono visibili.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `width` | La larghezza del fotogramma video in pixel. Il valore predefinito è 832. | INT | Sì | 16 - 4096 |
| `height` | L'altezza del fotogramma video in pixel. Il valore predefinito è 480. | INT | Sì | 16 - 4096 |
| `start_x` | Coordinata X normalizzata (0-1) per la posizione iniziale. Il valore predefinito è 0.0. | FLOAT | Sì | 0.0 - 1.0 |
| `start_y` | Coordinata Y normalizzata (0-1) per la posizione iniziale. Il valore predefinito è 0.0. | FLOAT | Sì | 0.0 - 1.0 |
| `end_x` | Coordinata X normalizzata (0-1) per la posizione finale. Il valore predefinito è 1.0. | FLOAT | Sì | 0.0 - 1.0 |
| `end_y` | Coordinata Y normalizzata (0-1) per la posizione finale. Il valore predefinito è 1.0. | FLOAT | Sì | 0.0 - 1.0 |
| `num_frames` | Il numero totale di fotogrammi per cui generare le posizioni delle tracce. Il valore predefinito è 81. | INT | Sì | 1 - 1024 |
| `num_tracks` | Il numero di tracce parallele da generare. Il valore predefinito è 5. | INT | Sì | 1 - 100 |
| `track_spread` | Distanza normalizzata tra le tracce. Le tracce sono distribuite perpendicolarmente alla direzione del movimento. Il valore predefinito è 0.025. | FLOAT | Sì | 0.0 - 1.0 |
| `bezier` | Abilita il percorso a curva di Bezier usando il punto medio come punto di controllo. Il valore predefinito è False. | BOOLEAN | Sì | True / False |
| `mid_x` | Punto di controllo X normalizzato per la curva di Bezier. Usato solo quando `bezier` è abilitato. Il valore predefinito è 0.5. | FLOAT | Sì | 0.0 - 1.0 |
| `mid_y` | Punto di controllo Y normalizzato per la curva di Bezier. Usato solo quando `bezier` è abilitato. Il valore predefinito è 0.5. | FLOAT | Sì | 0.0 - 1.0 |
| `interpolation` | Controlla la temporizzazione/velocità del movimento lungo il percorso (predefinito: "linear"):<br>"linear" - velocità costante<br>"ease_in" - inizia lento e accelera<br>"ease_out" - inizia veloce e rallenta<br>"ease_in_out" - accelerazione e decelerazione fluide<br>"constant" - mantiene tutte le posizioni nel punto iniziale | COMBO | Sì | `"linear"`<br>`"ease_in"`<br>`"ease_out"`<br>`"ease_in_out"`<br>`"constant"` |
| `track_mask` | Maschera opzionale per indicare i fotogrammi visibili. Se fornita, i fotogrammi in cui la maschera ha un qualsiasi pixel diverso da zero vengono contrassegnati come visibili per tutte le tracce. | MASK | No | - |

**Nota:** I parametri `mid_x` e `mid_y` sono usati solo quando il parametro `bezier` è impostato su `True`. Quando `bezier` è `False`, il percorso è una linea retta dal punto iniziale a quello finale.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `TRACKS` | Un oggetto tracks contenente le coordinate del percorso generate e le informazioni di visibilità per tutte le tracce in tutti i fotogrammi. | TRACKS |
| `track_length` | Il numero di fotogrammi per cui sono state generate le tracce, corrispondente al valore di input `num_frames`. | INT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GenerateTracks/it.md)

---
**Source fingerprint (SHA-256):** `4bd4d03a84f4b7ea260555b43f217af0b90dd4ca5196aca94e8f3886875ab912`
