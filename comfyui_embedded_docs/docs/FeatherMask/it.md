# FeatherMask

Il nodo `FeatherMask` applica un effetto di sfumatura ai bordi di una maschera specificata, rendendo gradualmente più morbidi i bordi della maschera regolando la loro opacità in base alle distanze specificate da ciascun bordo. Questo crea un effetto bordo più morbido e uniformemente sfumato.

## Input

| Parametro | Descrizione | Tipo di dato |
| --- | --- | --- |
| `mask` | La maschera a cui applicare l'effetto di sfumatura. Determina l'area dell'immagine che sarà interessata dalla sfumatura. | MASK |
| `left` | Specifica la distanza dal bordo sinistro entro cui verrà applicato l'effetto di sfumatura. | INT |
| `top` | Specifica la distanza dal bordo superiore entro cui verrà applicato l'effetto di sfumatura. | INT |
| `right` | Specifica la distanza dal bordo destro entro cui verrà applicato l'effetto di sfumatura. | INT |
| `bottom` | Specifica la distanza dal bordo inferiore entro cui verrà applicato l'effetto di sfumatura. | INT |

## Output

| Parametro | Descrizione | Tipo di dato |
| --- | --- | --- |
| `mask` | L'output è una versione modificata della maschera di input con un effetto di sfumatura applicato ai suoi bordi. | MASK |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FeatherMask/it.md)
