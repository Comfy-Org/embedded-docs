# Bria Rimuovi Sfondo Immagine

Questo nodo rimuove lo sfondo da un'immagine utilizzando il servizio Bria RMBG 2.0. Invia l'immagine a un'API esterna per l'elaborazione e restituisce il risultato con lo sfondo rimosso.

## Input

Il selettore `moderation` mostra ulteriori opzioni di moderazione quando è impostato su `"true"`.

### Input comuni

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `image` | L'immagine di input da cui verrà rimosso lo sfondo. | IMAGE | Sì | - |
| `moderation` | Impostazioni di moderazione. Se impostato su `"true"`, diventano disponibili ulteriori opzioni di moderazione. | DYNAMIC_COMBO | Sì | `"false"`<br>`"true"` |
| `seed` | Il seed controlla se il nodo deve essere rieseguito; i risultati non sono deterministici indipendentemente dal seed. Predefinito: `0`. | INT | Sì | 0 a 2147483647 |

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
**Source fingerprint (SHA-256):** `f62dcd5c9406ec09f5aab44585dd7f25ae0f7d9a934faa10a58e46ef116df110`
