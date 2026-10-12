# ImageStitch

Questo nodo consente di unire due immagini tra loro in una direzione specificata (up, down, left, right), con supporto per l'adattamento delle dimensioni e la spaziatura tra le immagini.

## Input

| Nome parametro | Descrizione | Tipo di dati | Tipo di input | Predefinito | Intervallo |
| --- | --- | --- | --- | --- | --- |
| `image1` | La prima immagine da unire | IMAGE | Obbligatorio | - | - |
| `image2` | La seconda immagine da unire; se non viene fornita, restituisce solo la prima immagine | IMAGE | Opzionale | None | - |
| `direction` | La direzione in cui unire la seconda immagine: right, down, left o up | STRING | Obbligatorio | right | right/down/left/up |
| `match_image_size` | Indica se ridimensionare la seconda immagine per adattarla alle dimensioni della prima immagine | BOOLEAN | Obbligatorio | True | True/False |
| `spacing_width` | Larghezza della spaziatura tra le immagini; deve essere un numero pari | INT | Obbligatorio | 0 | 0-1024 |
| `spacing_color` | Colore della spaziatura tra le immagini unite | STRING | Obbligatorio | white | white/black/red/green/blue |

> Per `spacing_color`, quando si usano colori diversi da "white/black", se `match_image_size` è impostato su `false`, l'area di riempimento verrà riempita con il colore nero

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `IMAGE` | L'immagine unita | IMAGE |

## Esempio di workflow

Nel workflow seguente, utilizziamo 3 immagini di input di dimensioni diverse come esempio:

- image1: 500x300
- image2: 400x250
- image3: 300x300

![workflow](./asset/workflow.webp)

**Primo nodo Image Stitch**

- `match_image_size`: false, le immagini verranno unite alle loro dimensioni originali
- `direction`: up, `image2` verrà posizionata sopra `image1`
- `spacing_width`: 20
- `spacing_color`: black

Immagine di output 1:

![output1](./asset/output-1.webp)

**Secondo nodo Image Stitch**

- `match_image_size`: true, la seconda immagine verrà ridimensionata per corrispondere all'altezza o alla larghezza della prima immagine
- `direction`: right, `image3` apparirà sul lato destro
- `spacing_width`: 20
- `spacing_color`: white

Immagine di output 2:

![output2](./asset/output-2.webp)

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageStitch/it.md)
