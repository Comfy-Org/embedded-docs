> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RTDETR_detect/pt-BR.md)

O nó RT-DETR Detect realiza detecção de objetos em imagens de entrada usando um modelo RT-DETR. Ele identifica objetos, desenha caixas delimitadoras ao redor deles e os rotula de acordo com as classes do conjunto de dados COCO. Você pode filtrar os resultados por pontuação de confiança, classe do objeto e limitar o número total de detecções.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Faixa | Descrição |
|-----------|---------------|-------------|-------|-----------|
| `model` | MODEL | Sim | N/A | O modelo RT-DETR usado para detecção de objetos. |
| `image` | IMAGE | Sim | N/A | A(s) imagem(ns) de entrada para detectar objetos. O nó processa imagens em lotes de até 32. |
| `threshold` | FLOAT | Não | N/A | A pontuação mínima de confiança que uma detecção deve ter para ser incluída nos resultados (padrão: 0,5). |
| `class_name` | COMBO | Não | `"all"`<br>`"person"`<br>`"bicycle"`<br>`"car"`<br>`"motorcycle"`<br>`"airplane"`<br>`"bus"`<br>`"train"`<br>`"truck"`<br>`"boat"`<br>`"traffic light"`<br>`"fire hydrant"`<br>`"stop sign"`<br>`"parking meter"`<br>`"bench"`<br>`"bird"`<br>`"cat"`<br>`"dog"`<br>`"horse"`<br>`"sheep"`<br>`"cow"`<br>`"elephant"`<br>`"bear"`<br>`"zebra"`<br>`"giraffe"`<br>`"backpack"`<br>`"umbrella"`<br>`"handbag"`<br>`"tie"`<br>`"suitcase"`<br>`"frisbee"`<br>`"skis"`<br>`"snowboard"`<br>`"sports ball"`<br>`"kite"`<br>`"baseball bat"`<br>`"baseball glove"`<br>`"skateboard"`<br>`"surfboard"`<br>`"tennis racket"`<br>`"bottle"`<br>`"wine glass"`<br>`"cup"`<br>`"fork"`<br>`"knife"`<br>`"spoon"`<br>`"bowl"`<br>`"banana"`<br>`"apple"`<br>`"sandwich"`<br>`"orange"`<br>`"broccoli"`<br>`"carrot"`<br>`"hot dog"`<br>`"pizza"`<br>`"donut"`<br>`"cake"`<br>`"chair"`<br>`"couch"`<br>`"potted plant"`<br>`"bed"`<br>`"dining table"`<br>`"toilet"`<br>`"tv"`<br>`"laptop"`<br>`"mouse"`<br>`"remote"`<br>`"keyboard"`<br>`"cell phone"`<br>`"microwave"`<br>`"oven"`<br>`"toaster"`<br>`"sink"`<br>`"refrigerator"`<br>`"book"`<br>`"clock"`<br>`"vase"`<br>`"scissors"`<br>`"teddy bear"`<br>`"hair drier"`<br>`"toothbrush"` | Filtra detecções por classe. Defina como 'all' para desabilitar a filtragem (padrão: "all"). |
| `max_detections` | INT | Não | N/A | Número máximo de detecções a retornar por imagem. Em ordem decrescente de pontuação de confiança (padrão: 100). |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|---------------|---------------|-----------|
| `bboxes` | BOUNDINGBOX | Uma lista de caixas delimitadoras para cada imagem de entrada. Cada caixa contém coordenadas (x, y, largura, altura), um rótulo de classe e uma pontuação de confiança. |