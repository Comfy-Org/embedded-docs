# MagnificImageRelightNode

Il nodo Magnific Image Relight regola l'illuminazione di un'immagine di input. Può applicare un'illuminazione stilistica basata su un prompt testuale o trasferire le caratteristiche di illuminazione da un'immagine di riferimento opzionale. Il nodo offre vari controlli per mettere a punto luminosità, contrasto e atmosfera generale dell'output finale.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `image` | L'immagine di cui regolare l'illuminazione. È richiesta esattamente un'immagine. Le dimensioni minime sono 160x160 pixel. Le proporzioni devono essere comprese tra 1:3 e 3:1. | IMAGE | Sì | N/A |
| `prompt` | Guida descrittiva per l'illuminazione. Supporta la notazione di enfasi (1-1.4). Il valore predefinito è una stringa vuota. | STRING | No | N/A |
| `light_transfer_strength` | Intensità di applicazione del trasferimento della luce. Predefinito: 100. | INT | Sì | 0 to 100 |
| `style` | Preferenza stilistica dell'output. | COMBO | Sì | `"standard"`<br>`"darker_but_realistic"`<br>`"clean"`<br>`"smooth"`<br>`"brighter"`<br>`"contrasted_n_hdr"`<br>`"just_composition"` |
| `interpolate_from_original` | Limita la libertà di generazione per corrispondere più fedelmente all'originale. Predefinito: False. | BOOLEAN | Sì | N/A |
| `change_background` | Modifica lo sfondo in base al prompt/al riferimento. Predefinito: True. | BOOLEAN | Sì | N/A |
| `preserve_details` | Mantiene la texture e i dettagli fini dell'originale. Predefinito: True. | BOOLEAN | Sì | N/A |
| `advanced_settings` | Opzioni di regolazione fine per il controllo avanzato dell'illuminazione. Se impostato su `"enabled"`, diventano disponibili parametri aggiuntivi. | DYNAMICCOMBO | Sì | `"disabled"`<br>`"enabled"` |
| `reference_image` | Immagine di riferimento opzionale da cui trasferire l'illuminazione. Se fornita, è richiesta esattamente un'immagine. Le dimensioni minime sono 160x160 pixel. Le proporzioni devono essere comprese tra 1:3 e 3:1. | IMAGE | No | N/A |

**Nota sulle impostazioni avanzate:** Quando `advanced_settings` è impostato su `"enabled"`, diventano attivi i seguenti parametri annidati:

* `whites`: Regola i toni più chiari dell'immagine. Intervallo: da 0 a 100. Predefinito: 50.
* `blacks`: Regola i toni più scuri dell'immagine. Intervallo: da 0 a 100. Predefinito: 50.
* `brightness`: Regolazione della luminosità complessiva. Intervallo: da 0 a 100. Predefinito: 50.
* `contrast`: Regolazione del contrasto. Intervallo: da 0 a 100. Predefinito: 50.
* `saturation`: Regolazione della saturazione del colore. Intervallo: da 0 a 100. Predefinito: 50.
* `engine`: Selezione del motore di elaborazione. Opzioni: `"automatic"`, `"balanced"`, `"cool"`, `"real"`, `"illusio"`, `"fairy"`, `"colorful_anime"`, `"hard_transform"`, `"softy"`.
* `transfer_light_a`: L'intensità del trasferimento della luce. Opzioni: `"automatic"`, `"low"`, `"medium"`, `"normal"`, `"high"`, `"high_on_faces"`.
* `transfer_light_b`: Modifica anche l'intensità del trasferimento della luce. Può essere combinato con il controllo precedente per ottenere effetti vari. Opzioni: `"automatic"`, `"composition"`, `"straight"`, `"smooth_in"`, `"smooth_out"`, `"smooth_both"`, `"reverse_both"`, `"soft_in"`, `"soft_out"`, `"soft_mid"`, `"style_shift"`, `"strong_shift"`.
* `fixed_generation`: Garantisce un output coerente con le stesse impostazioni. Predefinito: True.

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `image` | L'immagine con l'illuminazione regolata. | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MagnificImageRelightNode/it.md)

---
**Source fingerprint (SHA-256):** `45fe68b21e1da7c367800915c803ad4cf1c5b80e9a2e91d80cae51b8a9531144`
