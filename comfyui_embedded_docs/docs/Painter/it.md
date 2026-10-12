# Painter

Il nodo Painter fornisce una tela interattiva per creare o modificare immagini e maschere direttamente all'interno di ComfyUI. Consente di partire da una tela vuota o da un'immagine esistente, disegnarci sopra usando uno strumento pennello e restituisce sia l'immagine risultante sia una maschera alfa corrispondente. La maschera definisce le aree disegnate, che vengono poi composte sopra l'immagine di base o il colore di sfondo.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `image` | Immagine di base opzionale su cui disegnare. Se non viene fornita, viene creata una tela vuota usando il colore di sfondo, la larghezza e l'altezza specificati. | IMAGE | No | - |
| `mask` | I dati di disegno, generalmente generati dal widget interattivo integrato del nodo. Questo parametro è gestito dallo strumento di disegno dell'interfaccia utente e non è destinato a essere collegato a un socket standard. | STRING | Sì | - |
| `width` | La larghezza della tela in pixel, utilizzata quando non viene fornita un'immagine di base (`image`). Il valore deve essere un multiplo di 64. Il valore predefinito è 512. | INT | Sì | 64 to 4096 |
| `height` | L'altezza della tela in pixel, utilizzata quando non viene fornita un'immagine di base (`image`). Il valore deve essere un multiplo di 64. Il valore predefinito è 512. | INT | Sì | 64 to 4096 |
| `bg_color` | Il colore di sfondo per la tela, specificato come codice esadecimale (ad es., #000000). Viene utilizzato solo quando non viene fornita un'immagine di base (`image`). Il valore predefinito è nero (#000000). | COLOR | Sì | - |

**Nota:** L'input `mask` è progettato per funzionare con il widget UI specializzato del nodo. Quando si disegna sulla tela, il widget compila automaticamente questo valore. Gli input `width` e `height` sono nascosti nell'interfaccia utente standard ma definiscono le dimensioni della tela quando si crea una nuova immagine. Se viene fornita un'immagine di base (`image`), le sue dimensioni hanno la precedenza sulle impostazioni `width` e `height`.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `IMAGE` | L'immagine finale composta. È il risultato della fusione delle aree disegnate (dalla `mask`) sopra l'immagine di base fornita (`image`) o lo sfondo colorato. | IMAGE |
| `MASK` | La maschera del canale alfa (trasparenza) estratta dal disegno. Le aree bianche rappresentano le regioni disegnate, mentre le aree nere rappresentano lo sfondo non modificato. | MASK |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Painter/it.md)

---
**Source fingerprint (SHA-256):** `217a6d8abbad02cb43cab18d0a592bdd5bfbfe321a742d0c14e8f4e1fa5e2630`
