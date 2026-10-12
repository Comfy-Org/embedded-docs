# Bria Cambia stagione

Questo nodo sposta un'immagine in una stagione diversa utilizzando Bria. L'intera scena viene renderizzata nuovamente, quindi lo scenario può cambiare oltre alla stagione stessa. Bria renderizza nuovamente l'intero fotogramma a circa 1 megapixel, quindi il risultato non è allineato a livello di pixel con l'input.

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `image` | L'immagine da spostare in un'altra stagione. Qualsiasi canale alpha viene rimosso prima che l'immagine venga inviata. | IMAGE | Sì | - |
| `season` | Stagione da applicare. | COMBO | Sì | `"spring"`<br>`"summer"`<br>`"autumn"`<br>`"winter"` |
| `moderation` | Impostazioni di moderazione. Seleziona se le opzioni di moderazione dei contenuti sono configurate per questa richiesta. | DYNAMIC_COMBO | Sì | `"false"`<br>`"true"` |

### Input di moderazione

Queste opzioni compaiono quando `moderation` è impostato su `"true"`.

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `visual_input_moderation` | Abilita la moderazione dei contenuti sull'immagine di input (predefinito: false). | BOOLEAN | No | true<br>false |
| `visual_output_moderation` | Abilita la moderazione dei contenuti sull'immagine di output generata (predefinito: false). | BOOLEAN | No | true<br>false |

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `IMAGE` | L'immagine renderizzata nuovamente nella stagione selezionata. | IMAGE |
| `structured_prompt` | Descrizione strutturata dell'immagine modificata, per una modifica successiva con Bria FIBO Image Edit. | STRING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaReseason/it.md)

---
**Source fingerprint (SHA-256):** `3bb9ee1c00c91759cc6f972e2ba8708ae73a186f4b66bf6669937e561efad0a4`
