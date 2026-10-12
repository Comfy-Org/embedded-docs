# Combina Maschere

Questo nodo è specializzato nel combinare due input di maschera attraverso una varietà di operazioni come addizione, sottrazione e operazioni logiche, per produrre una nuova maschera modificata. Gestisce in modo astratto la manipolazione dei dati delle maschere per ottenere effetti di mascheramento complessi, fungendo da componente cruciale nei flussi di lavoro di modifica ed elaborazione delle immagini basati su maschere.

## Input

| Parametro | Descrizione | Tipo di dato |
| --- | --- | --- |
| `destination` | La maschera primaria che verrà modificata in base all'operazione con la maschera sorgente. Svolge un ruolo centrale nell'operazione di composizione, fungendo da base per le modifiche. | MASK |
| `source` | La maschera secondaria che verrà utilizzata insieme alla maschera di destinazione per eseguire l'operazione specificata, influenzando la maschera di output finale. | MASK |
| `x` | L'offset orizzontale in corrispondenza del quale la maschera sorgente verrà applicata alla maschera di destinazione, influenzando il posizionamento del risultato composito. | INT |
| `y` | L'offset verticale in corrispondenza del quale la maschera sorgente verrà applicata alla maschera di destinazione, influenzando il posizionamento del risultato composito. | INT |
| `operation` | Specifica il tipo di operazione da applicare tra la maschera di destinazione e la maschera sorgente, come 'add', 'subtract' o operazioni logiche, determinando la natura dell'effetto composito. | COMBO[STRING] |

## Output

| Parametro | Descrizione | Tipo di dato |
| --- | --- | --- |
| `mask` | La maschera risultante dopo aver applicato l'operazione specificata tra la maschera di destinazione e quella sorgente, che rappresenta il risultato composito. | MASK |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MaskComposite/it.md)
