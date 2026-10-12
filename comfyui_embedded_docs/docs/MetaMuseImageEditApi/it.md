# Meta Muse Image Modifica

Modifica o combina fino a 10 immagini di riferimento utilizzando un prompt testuale e il modello Muse Image di Meta. Descrivi la modifica desiderata nel prompt e, quando necessario, fai riferimento alle immagini di riferimento come `@Image1`, `@Image2`, e così via. Il nodo carica le immagini di riferimento, chiama l'API Meta Muse Image e restituisce il risultato modificato come immagine.

## Input

Il nodo è controllato da un selettore `model`. Gli input specifici del modello descritti di seguito compaiono quando viene selezionato un modello, e il numero di immagini di riferimento che colleghi può essere aumentato o ridotto secondo necessità.

### Input comuni

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `model` | Modello da utilizzare. | DYNAMIC_COMBO | Sì | "muse-image-1.0" |

### Input di muse-image-1.0

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Istruzioni di modifica. Supporta riferimenti in stile `@Image1` alle immagini di input. Predefinito: stringa vuota. Il prompt deve contenere almeno un carattere. | STRING | Sì | Qualsiasi testo con una lunghezza minima di 1 carattere |
| `aspect_ratio` | Rapporto d'aspetto dell'output. Le immagini vengono renderizzate a circa 2,5 megapixel (1:1 è 1600x1600, 16:9 è 2048x1152); "auto" mantiene il rapporto d'aspetto dell'input. | COMBO | Sì | "auto"<br>"1:1"<br>"3:2"<br>"2:3"<br>"4:3"<br>"3:4"<br>"5:4"<br>"4:5"<br>"16:9"<br>"9:16"<br>"21:9"<br>"9:21"<br>"2:1"<br>"1:2" |
| `reasoning_strength` | Quanto il modello ragiona, pianifica e si autocorregge prima del rendering. | COMBO | Sì | "high"<br>"low" |
| `enable_web_search` | Consente al modello di cercare sul web fatti e informazioni in tempo reale mentre pianifica l'immagine. Predefinito: true. | BOOLEAN | Sì | true o false (predefinito: true) |
| `enable_image_search` | Consente al modello di cercare immagini di riferimento mentre pianifica l'immagine. Predefinito: true. | BOOLEAN | Sì | true o false (predefinito: true) |
| `enable_shell` | Consente al modello di eseguire codice durante la pianificazione, per layout, grafici e diagrammi precisi; quando è disattivato, quantità e allineamento sono approssimativi. Predefinito: true. | BOOLEAN | Sì | true o false (predefinito: true) |
| `seed` | Seed per determinare se il nodo deve essere rieseguito; l'API non ha un seed, quindi i risultati effettivi sono non deterministici indipendentemente da questo valore. Predefinito: 42. | INT | Sì | da 0 a 2147483647 (passo 1) |

### Input di riferimento

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `images` | Slot espandibile: collega da 1 a 10 immagini di riferimento (`image_1` fino a `image_10`) da modificare o combinare. Fai riferimento ad esse nel prompt come `@Image1`, `@Image2`, ..., numerate in ordine di input; un input in batch conta una volta per immagine. | IMAGE | Sì | da 1 a 10 immagini di riferimento |

Nota: il prompt non può essere vuoto e ogni riferimento `@ImageN` che contiene deve corrispondere a una delle immagini collegate in ordine di input (ad esempio, `@Image1` è la prima immagine di riferimento collegata). Se il prompt fa riferimento a un numero di immagine non collegata, o se vengono collegate più di 10 immagini di riferimento, il nodo genera un errore.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|-----------|
| `image` | L'immagine modificata o combinata restituita dal modello Muse Image. Se l'API restituisce più immagini, vengono restituite come batch. | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MetaMuseImageEditApi/it.md)

---
**Source fingerprint (SHA-256):** `5c009ca45199f9c70465f12d48a46b685abebd0194c3d437121b9df0636dbea7`
