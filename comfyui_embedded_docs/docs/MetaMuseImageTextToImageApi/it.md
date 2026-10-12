# Meta Muse Image da testo a immagine

Meta Muse Image Text to Image genera immagini da un prompt testuale usando il modello Muse Image di Meta. Il modello ragiona sul prompt prima del rendering e può utilizzare la ricerca web, la ricerca di immagini e l'esecuzione di codice durante la pianificazione dell'immagine. Il nodo chiama l'API Muse Image e restituisce l'immagine o le immagini risultanti.

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `model` | Modello da usare. | DYNAMIC_COMBO | Sì | `"muse-image-1.0"` |

Selezionando un modello nell'elenco vengono mostrate le impostazioni supportate da quel modello. L'unico modello disponibile è `muse-image-1.0`; le sue impostazioni sono elencate di seguito.

### Input di muse-image-1.0

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `prompt` | Prompt che descrive l'immagine. Il modello ragiona sul prompt e può usare la ricerca web e la ricerca di immagini integrate prima del rendering. | STRING | Sì | Testo multiriga, minimo 1 carattere |
| `aspect_ratio` | Rapporto d'aspetto dell'output. Le immagini vengono renderizzate a circa 2,5 megapixel (1:1 è 1600x1600, 16:9 è 2048x1152); "auto" lascia che il modello scelga dal prompt. | COMBO | Sì | `"auto"`<br>`"1:1"`<br>`"3:2"`<br>`"2:3"`<br>`"4:3"`<br>`"3:4"`<br>`"5:4"`<br>`"4:5"`<br>`"16:9"`<br>`"9:16"`<br>`"21:9"`<br>`"9:21"`<br>`"2:1"`<br>`"1:2"` |
| `reasoning_strength` | Quanto il modello riflette, pianifica e si auto-perfeziona prima del rendering. | COMBO | Sì | `"high"`<br>`"low"` |
| `enable_web_search` | Consente al modello di cercare sul web fatti e informazioni in tempo reale durante la pianificazione dell'immagine. | BOOLEAN | No | True<br>False (predefinito: True) |
| `enable_image_search` | Consente al modello di cercare immagini di riferimento durante la pianificazione dell'immagine. | BOOLEAN | No | True<br>False (predefinito: True) |
| `enable_shell` | Consente al modello di eseguire codice durante la pianificazione, per layout, grafici e diagrammi precisi; quando è disattivato, quantità e allineamento sono approssimativi. | BOOLEAN | No | True<br>False (predefinito: True) |
| `seed` | Seed per determinare se il nodo deve essere rieseguito; l'API non ha un seed, quindi i risultati effettivi sono non deterministici indipendentemente da questo valore. | INT | Sì | 0 – 2147483647 (predefinito: 42) |

Nota: il prompt deve contenere almeno un carattere. Quando `aspect_ratio` è impostato su "auto", non viene inviata alcuna dimensione esplicita all'API e il modello decide la dimensione dell'output dal prompt. Il parametro `seed` controlla solo quando il nodo viene rieseguito; non viene inviato all'API, quindi i risultati generati sono non deterministici.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `image` | L'immagine generata restituita dall'API, decodificata e fornita come immagine in batch. Se la risposta dell'API contiene più immagini, vengono combinate in un unico batch. | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MetaMuseImageTextToImageApi/it.md)

---
**Source fingerprint (SHA-256):** `59ebd72fab3db44a35ceac723606de4eabb5fe2b690d0b701db50e0e22a9e699`
