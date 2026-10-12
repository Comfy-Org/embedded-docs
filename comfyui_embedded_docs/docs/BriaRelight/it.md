# BriaRelight

Questo nodo modifica l'atmosfera e la direzione dell'illuminazione di un'immagine utilizzando Bria. L'immagine viene ri-renderizzata da Bria, quindi il risultato non è allineato pixel per pixel con l'input; l'intero fotogramma viene rigenerato a circa 1 megapixel.

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `image` | L'immagine di cui modificare l'illuminazione. Qualsiasi canale alpha viene eliminato prima che l'immagine venga caricata. | IMAGE | Sì | - |
| `light_type` | Atmosfera luminosa da applicare. | COMBO | Sì | `"midday"`<br>`"blue hour light"`<br>`"low-angle sunlight"`<br>`"sunrise light"`<br>`"spotlight on subject"`<br>`"overcast light"`<br>`"soft overcast daylight lighting"`<br>`"cloud-filtered lighting"`<br>`"fog-diffused lighting"`<br>`"moonlight lighting"`<br>`"starlight nighttime"`<br>`"soft bokeh lighting"`<br>`"harsh studio lighting"` |
| `light_direction` | Da dove proviene la luce. Le atmosfere con luce dura come midday, spotlight on subject e harsh studio lighting sono quelle che reagiscono maggiormente a questa impostazione. | COMBO | Sì | `"front"`<br>`"side"`<br>`"bottom"`<br>`"top-down"` |
| `moderation` | Impostazioni di moderazione. Seleziona `"true"` per mostrare le opzioni di moderazione, oppure `"false"` per eseguire senza di esse. | DYNAMIC_COMBO | Sì | `"false"`<br>`"true"` |

### Input di moderazione

Queste opzioni compaiono quando `moderation` è impostato su `"true"`.

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `visual_input_moderation` | Abilita la moderazione dei contenuti sull'immagine di input. Predefinito: false. | BOOLEAN | No | `true`<br>`false` |
| `visual_output_moderation` | Abilita la moderazione dei contenuti sull'immagine di output generata. Predefinito: false. | BOOLEAN | No | `true`<br>`false` |

Nota: Bria ri-renderizza l'intero fotogramma a circa 1 megapixel, quindi il risultato non è allineato pixel per pixel con l'input.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|-----------|
| `image` | L'immagine con illuminazione modificata restituita da Bria. | IMAGE |
| `structured_prompt` | Descrizione strutturata dell'immagine modificata, per una modifica successiva con Bria FIBO Image Edit. | STRING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaRelight/it.md)

---
**Source fingerprint (SHA-256):** `21fbe2186c99a7e8d99d5659ac25c3ab1a757492916dba4135487d4b293cb4f6`
