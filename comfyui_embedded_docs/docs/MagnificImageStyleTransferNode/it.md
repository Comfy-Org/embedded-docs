# MagnificImageStyleTransferNode

This node applies the visual style from a reference image to your input image. It uses an external AI service to process the images, allowing you to control the strength of the style transfer and the preservation of the original image's structure.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `image` | L'immagine a cui applicare il trasferimento di stile. | IMAGE | Sì | - |
| `reference_image` | L'immagine di riferimento da cui estrarre lo stile. | IMAGE | Sì | - |
| `prompt` | Un prompt testuale opzionale per guidare il trasferimento di stile. | STRING | No | - |
| `style_strength` | Percentuale dell'intensità dello stile (predefinito: 100). | INT | No | 0 to 100 |
| `structure_strength` | Mantiene la struttura dell'immagine originale (predefinito: 50). | INT | No | 0 to 100 |
| `flavor` | Variante del trasferimento di stile. | COMBO | No | "faithful"<br>"gen_z"<br>"psychedelia"<br>"detaily"<br>"clear"<br>"donotstyle"<br>"donotstyle_sharp" |
| `engine` | Selezione del motore di elaborazione. | COMBO | No | "balanced"<br>"definio"<br>"illusio"<br>"3d_cartoon"<br>"colorful_anime"<br>"caricature"<br>"real"<br>"super_real"<br>"softy" |
| `portrait_mode` | Abilita la modalità ritratto per miglioramenti del viso. | COMBO | No | "disabled"<br>"enabled" |
| `portrait_style` | Stile visivo applicato alle immagini ritratto. Questo input è disponibile solo quando `portrait_mode` è impostato su "enabled". | COMBO | No | "standard"<br>"pop"<br>"super_pop" |
| `portrait_beautifier` | Intensità di abbellimento del viso sui ritratti. Questo input è disponibile solo quando `portrait_mode` è impostato su "enabled". | COMBO | No | "none"<br>"beautify_face"<br>"beautify_face_max" |
| `fixed_generation` | Quando è disabilitato, aspettati che ogni generazione introduca un certo grado di casualità, portando a risultati più vari (predefinito: True). | BOOLEAN | No | - |

**Vincoli:**

* Sono richiesti esattamente un `image` e un `reference_image`.
* Entrambe le immagini devono avere un rapporto d'aspetto compreso tra 1:3 e 3:1.
* Entrambe le immagini devono avere un'altezza e una larghezza minime di 160 pixel.
* I parametri `portrait_style` e `portrait_beautifier` sono attivi solo quando `portrait_mode` è impostato su "enabled".

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `image` | L'immagine risultante dopo l'applicazione del trasferimento di stile. | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MagnificImageStyleTransferNode/it.md)

---
**Source fingerprint (SHA-256):** `edffec024ebe7cbf7c42008e14c1b99d6fafcf5b9da62b0b560d194a585dc9ad`
