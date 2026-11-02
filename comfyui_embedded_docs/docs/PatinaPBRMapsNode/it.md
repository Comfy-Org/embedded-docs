# Patina PBR Material Maps

Deriva un insieme di mappe di materiale PBR da un'immagine di texture esistente: basecolor, normal, roughness, metalness e height. Abilitare solo le mappe necessarie, poiché ogni mappa abilitata aumenta il costo. Usalo per completare una texture che non ha ancora mappe di materiale, oppure per ricostruire una singola mappa danneggiata.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `image` | La fotografia o il rendering da cui derivare le mappe PBR. | IMAGE | Sì | - |
| `basecolor` | Genera la mappa basecolor (albedo). Predefinito: True. | BOOLEAN | Sì | true<br>false |
| `normal` | Genera la mappa normal. Predefinito: True. | BOOLEAN | Sì | true<br>false |
| `roughness` | Genera la mappa roughness. Predefinito: False. | BOOLEAN | Sì | true<br>false |
| `metalness` | Genera la mappa metalness. Predefinito: False. | BOOLEAN | Sì | true<br>false |
| `height` | Genera la mappa height (displacement). Predefinito: False. | BOOLEAN | Sì | true<br>false |
| `seed` | Seme per un denoising riproducibile. Predefinito: 42. | INT | Sì | 0 a 2147483646 |
| `safety_checker` | Esegue il controllo di sicurezza dei contenuti del provider sulla richiesta. Impostazione avanzata. Predefinito: False. | BOOLEAN | Sì | true<br>false |
| `auto_downscale` | Ridimensiona automaticamente verso il basso un'immagine di input il cui lato più lungo supera 2048 pixel, il limite di input del modello, preservando le proporzioni; le immagini più piccole vengono lasciate invariate. Disabilitalo per generare invece un errore sulle immagini sovradimensionate. Impostazione avanzata. Predefinito: True. | BOOLEAN | No | true<br>false |

**Vincoli e comportamento:**

* È necessario abilitare almeno una mappa; in caso contrario l'esecuzione non riesce.
* L'immagine di input è limitata a 2048 pixel sul lato più lungo; consenti a `auto_downscale` di ridurla, altrimenti l'esecuzione non riesce su un'immagine sovradimensionata.
* Ogni mappa disabilitata restituisce comunque un output, ma come immagine segnaposto 1x1; collega quindi solo gli output che hai effettivamente generato.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `basecolor` | La mappa basecolor (albedo) generata, oppure un segnaposto 1x1 quando quella mappa è disabilitata. | IMAGE |
| `normal` | La mappa normal generata, oppure un segnaposto 1x1 quando quella mappa è disabilitata. | IMAGE |
| `roughness` | La mappa roughness generata, oppure un segnaposto 1x1 quando quella mappa è disabilitata. | IMAGE |
| `metalness` | La mappa metalness generata, oppure un segnaposto 1x1 quando quella mappa è disabilitata. | IMAGE |
| `height` | La mappa height (displacement) generata, oppure un segnaposto 1x1 quando quella mappa è disabilitata. | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PatinaPBRMapsNode/it.md)

---
**Source fingerprint (SHA-256):** `813c5bb3336c5ca54a9ca9ee95e84e7f27791170650248d0169acee39c4b3ce1`
