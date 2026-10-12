# ViduMultiFrameVideoNode

Questo nodo genera un video creando transizioni tra più keyframe. Parte da un'immagine iniziale e anima una sequenza di immagini finali e prompt definiti dall'utente, producendo come output un singolo file video.

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `model` | Il modello Vidu da usare per la generazione video. | COMBO | Sì | "viduq2-pro"<br>"viduq2-turbo" |
| `start_image` | L'immagine del fotogramma iniziale. Le proporzioni devono essere comprese tra 1:4 e 4:1. | IMAGE | Sì | Proporzioni da 1:4 a 4:1 |
| `seed` | Un valore seed per la generazione di numeri casuali, per garantire risultati riproducibili (predefinito: 1). | INT | Sì | 0 a 2147483647 |
| `resolution` | La risoluzione del video in output. | COMBO | Sì | "720p"<br>"1080p" |
| `frames` | Numero di transizioni tra keyframe (2-9). Selezionando un valore vengono mostrati dinamicamente gli input richiesti per ogni fotogramma. | DYNAMIC_COMBO | Sì | "2"<br>"3"<br>"4"<br>"5"<br>"6"<br>"7"<br>"8"<br>"9" |

### Input dei fotogrammi (condivisi da tutte le opzioni del numero di fotogrammi)

Quando `frames` è impostato su un numero, i seguenti tre input vengono mostrati per ogni fotogramma `i` da 1 a quel numero. Ad esempio, scegliendo "3" vengono aggiunti `prompt1` / `end_image1` / `duration1`, `prompt2` / `end_image2` / `duration2` e `prompt3` / `end_image3` / `duration3`.

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `prompt{i}` | Prompt testuale per la transizione del fotogramma {i}. Campo di testo multiriga. Massimo 2000 caratteri. | STRING | Sì | Fino a 2000 caratteri |
| `end_image{i}` | Immagine del fotogramma finale per il segmento {i}. Le proporzioni devono essere comprese tra 1:4 e 4:1. | IMAGE | Sì | Proporzioni da 1:4 a 4:1 |
| `duration{i}` | Durata del segmento {i} in secondi (predefinita: 4). | INT | Sì | Da 2 a 7 |

**Note:**

- Tutti gli input sono obbligatori. `seed` ha un valore predefinito ma è comunque un input obbligatorio.
- `start_image` e ogni `end_image{i}` devono avere proporzioni comprese tra 1:4 e 4:1.
- Ogni `prompt{i}` ha una lunghezza massima di 2000 caratteri.
- Ogni `duration{i}` deve essere compresa tra 2 e 7 secondi.
- Il numero di fotogrammi può essere compreso tra 2 e 9, quindi gli indici dei fotogrammi possibili vanno da 1 a 9.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `output` | Il file video generato contenente tutte le transizioni animate. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ViduMultiFrameVideoNode/it.md)

---
**Source fingerprint (SHA-256):** `ad877532ba27444938b7b2e4634ac7f8a47db0f7fb53967d874ad38b44336dcf`
