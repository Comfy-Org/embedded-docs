# Bria Rimuovi Sfondo Immagine

Questo nodo rimuove lo sfondo da un'immagine utilizzando il servizio Bria RMBG 2.0 o RMBG 3.0. Invia l'immagine a un'API esterna per l'elaborazione e restituisce il risultato con lo sfondo rimosso.

## Input

Il selettore `moderation` mostra ulteriori opzioni di moderazione quando è impostato su `"true"`.

### Input comuni

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `immagine` | L'immagine di input da cui verrà rimosso lo sfondo. | IMAGE | Sì | - |
| `moderazione` | Impostazioni di moderazione. Se impostato su `"true"`, diventano disponibili ulteriori opzioni di moderazione. | DYNAMIC_COMBO | Sì | `"false"`<br>`"true"` |
| `seed` | Il seed controlla se il nodo deve essere rieseguito; la stessa immagine dà sempre lo stesso risultato indipendentemente dal seed. Predefinito: `0`. | INT | Sì | 0 a 2147483647 |
| `modello` | Modello di rimozione dello sfondo. `"RMBG2"` è il predefinito; `"RMBG3"` usa il modello più recente Bria RMBG 3.0. | COMBO | No | `"RMBG2"`<br>`"RMBG3"` |

### Input per moderazione "true"

Questi parametri compaiono solo quando `moderation` è impostato su `"true"`. L'opzione `"false"` non aggiunge input aggiuntivi.

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `visual_input_moderation` | Abilita la moderazione dei contenuti visivi sull'immagine di input. Predefinito: `False`. | BOOLEAN | No | - |
| `visual_output_moderation` | Abilita la moderazione dei contenuti visivi sull'immagine di output. Predefinito: `True`. | BOOLEAN | No | - |

**Nota:** I parametri `visual_input_moderation` e `visual_output_moderation` dipendono dal parametro `moderation`. Sono attivi solo quando `moderation` è impostato su `"true"`.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `image` | L'immagine elaborata con lo sfondo rimosso. | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaRemoveImageBackground/it.md)

---
**Source fingerprint (SHA-256):** `82f7ec2ac2d1579a3da009b464bce7c56fa2d7b1f599744d6158177ecd462cb2`
