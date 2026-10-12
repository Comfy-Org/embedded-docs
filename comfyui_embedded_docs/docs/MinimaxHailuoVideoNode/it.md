# MiniMax Hailuo 02 Video

Genera video da prompt testuali utilizzando il modello MiniMax Hailuo-02. Opzionalmente, puoi fornire un'immagine iniziale da utilizzare come primo fotogramma, creando un video che continua da quell'immagine.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Range |
|-----------|-------------|--------------|--------------|-------|
| `prompt_text` | Prompt testuale per guidare la generazione del video (predefinito: vuoto). | STRING | Sì | - |
| `seed` | Il seme casuale utilizzato per creare il rumore (predefinito: 0). | INT | No | 0 to 18446744073709551615 |
| `first_frame_image` | Immagine opzionale da usare come primo fotogramma per generare un video. | IMAGE | No | - |
| `prompt_optimizer` | Ottimizza il prompt per migliorare la qualità della generazione quando necessario (predefinito: True). | BOOLEAN | No | True<br>False |
| `duration` | La durata del video di output in secondi (predefinito: 6). | COMBO | No | 6<br>10 |
| `resolution` | Le dimensioni di visualizzazione del video. 1080p corrisponde a 1920x1080, 768p corrisponde a 1366x768 (predefinito: "768P"). | COMBO | No | "768P"<br>"1080P" |

**Nota:** Quando `resolution` è impostato su "1080P", `duration` è limitato a 6 secondi. Quando `first_frame_image` non è fornito, `prompt_text` non deve essere vuoto.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `output` | Il file video generato. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuoVideoNode/it.md)

---
**Source fingerprint (SHA-256):** `f371aae15cfbe7353236bc679c8a6d558703c5037e49ab7ddb9bdf5c50ef0995`
