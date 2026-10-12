# Composito Latent Mascherato

Il nodo LatentCompositeMasked è progettato per fondere due rappresentazioni latenti tra loro in coordinate specificate, usando facoltativamente una maschera per una composizione più controllata. Questo nodo consente la creazione di immagini latenti complesse sovrapponendo parti di un'immagine su un'altra, con la possibilità di ridimensionare l'immagine sorgente per una corrispondenza perfetta.

## Input

| Parametro | Descrizione | Tipo di dato |
| --- | --- | --- |
| `destination` | La rappresentazione latente su cui verrà composta un'altra rappresentazione latente. Funge da livello di base per l'operazione di composizione. | `LATENT` |
| `source` | La rappresentazione latente da comporre sulla destinazione. Questo livello sorgente può essere ridimensionato e posizionato in base ai parametri specificati. | `LATENT` |
| `x` | La coordinata x nella rappresentazione latente di destinazione in cui verrà posizionata la sorgente. Consente un posizionamento preciso del livello sorgente. | `INT` |
| `y` | La coordinata y nella rappresentazione latente di destinazione in cui verrà posizionata la sorgente, consentendo un posizionamento accurato della sovrapposizione. | `INT` |
| `resize_source` | Un flag booleano che indica se la rappresentazione latente sorgente deve essere ridimensionata per corrispondere alle dimensioni della destinazione prima della composizione. | `BOOLEAN` |
| `mask` | Una maschera opzionale che può essere usata per controllare la fusione della sorgente sulla destinazione. La maschera definisce quali parti della sorgente saranno visibili nella composizione finale. | `MASK` |

## Output

| Parametro | Descrizione | Tipo di dato |
| --- | --- | --- |
| `latent` | La rappresentazione latente risultante dopo aver composto la sorgente sulla destinazione, usando potenzialmente una maschera per una fusione selettiva. | `LATENT` |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentCompositeMasked/it.md)
