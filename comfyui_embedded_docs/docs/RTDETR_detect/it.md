# RTDETR_detect

Il nodo RT-DETR Detect esegue il rilevamento di oggetti sulle immagini di input utilizzando un modello RT-DETR. Identifica gli oggetti, restituisce bounding box attorno a essi e assegna etichette in base alle classi del dataset COCO. È possibile filtrare i risultati per punteggio di confidenza, classe di oggetto e limitare il numero totale di rilevamenti.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model` | Il modello RT-DETR utilizzato per il rilevamento di oggetti. | MODEL | Sì | N/D |
| `image` | L'immagine o le immagini di input in cui rilevare gli oggetti. Il nodo elabora le immagini in batch fino a 32. | IMAGE | Sì | N/D |
| `threshold` | Il punteggio di confidenza minimo che un rilevamento deve avere per essere incluso nei risultati (predefinito: 0.5). | FLOAT | Sì | N/D |
| `class_name` | Filtra i rilevamenti per classe. Impostare su 'all' per disabilitare il filtro (predefinito: "all"). | COMBO | Sì | `"all"`<br>`"person"`<br>`"bicycle"`<br>`"car"`<br>`"motorcycle"`<br>`"airplane"`<br>`"bus"`<br>`"train"`<br>`"truck"`<br>`"boat"`<br>`"traffic light"`<br>`"fire hydrant"`<br>`"stop sign"`<br>`"parking meter"`<br>`"bench"`<br>`"bird"`<br>`"cat"`<br>`"dog"`<br>`"horse"`<br>`"sheep"`<br>`"cow"`<br>`"elephant"`<br>`"bear"`<br>`"zebra"`<br>`"giraffe"`<br>`"backpack"`<br>`"umbrella"`<br>`"handbag"`<br>`"tie"`<br>`"suitcase"`<br>`"frisbee"`<br>`"skis"`<br>`"snowboard"`<br>`"sports ball"`<br>`"kite"`<br>`"baseball bat"`<br>`"baseball glove"`<br>`"skateboard"`<br>`"surfboard"`<br>`"tennis racket"`<br>`"bottle"`<br>`"wine glass"`<br>`"cup"`<br>`"fork"`<br>`"knife"`<br>`"spoon"`<br>`"bowl"`<br>`"banana"`<br>`"apple"`<br>`"sandwich"`<br>`"orange"`<br>`"broccoli"`<br>`"carrot"`<br>`"hot dog"`<br>`"pizza"`<br>`"donut"`<br>`"cake"`<br>`"chair"`<br>`"couch"`<br>`"potted plant"`<br>`"bed"`<br>`"dining table"`<br>`"toilet"`<br>`"tv"`<br>`"laptop"`<br>`"mouse"`<br>`"remote"`<br>`"keyboard"`<br>`"cell phone"`<br>`"microwave"`<br>`"oven"`<br>`"toaster"`<br>`"sink"`<br>`"refrigerator"`<br>`"book"`<br>`"clock"`<br>`"vase"`<br>`"scissors"`<br>`"teddy bear"`<br>`"hair drier"`<br>`"toothbrush"` |
| `max_detections` | Numero massimo di rilevamenti da restituire per immagine. In ordine di punteggio di confidenza decrescente (predefinito: 100). | INT | Sì | N/D |

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `bboxes` | Un elenco di bounding box per ciascuna immagine di input. Ogni box contiene le coordinate (x, y, larghezza, altezza), un'etichetta di classe e un punteggio di confidenza. | BOUNDINGBOX |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RTDETR_detect/it.md)

---
**Source fingerprint (SHA-256):** `658a47cae788da207a52edc6bf8a428c9f3d8cf415e5f20f71d6125ad6d49734`
