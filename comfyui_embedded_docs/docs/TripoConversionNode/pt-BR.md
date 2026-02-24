> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoConversionNode/pt-BR.md)

O TripoConversionNode converte modelos 3D entre diferentes formatos de arquivo usando a API Tripo. Ele recebe um ID de tarefa de uma operação Tripo anterior e converte o modelo resultante para o formato desejado, com várias opções de exportação.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `original_model_task_id` | MODEL_TASK_ID,RIG_TASK_ID,RETARGET_TASK_ID | Sim | MODEL_TASK_ID<br>RIG_TASK_ID<br>RETARGET_TASK_ID | O ID da tarefa de uma operação Tripo anterior (geração de modelo, rigging ou retargeting) |
| `format` | COMBO | Sim | GLTF<br>USDZ<br>FBX<br>OBJ<br>STL<br>3MF | O formato de arquivo de destino para o modelo 3D convertido |
| `quad` | BOOLEAN | Não | Verdadeiro/Falso | Se deve converter triângulos para quadriláteros (padrão: Falso) |
| `face_limit` | INT | Não | -1 a 500000 | Número máximo de faces no modelo de saída, use -1 para sem limite (padrão: -1) |
| `texture_size` | INT | Não | 128 a 4096 | Tamanho das texturas de saída em pixels (padrão: 4096) |
| `texture_format` | COMBO | Não | BMP<br>DPX<br>HDR<br>JPEG<br>OPEN_EXR<br>PNG<br>TARGA<br>TIFF<br>WEBP | Formato para as texturas exportadas (padrão: JPEG) |

**Observação:** O `original_model_task_id` deve ser um ID de tarefa válido de uma operação Tripo anterior (geração de modelo, rigging ou retargeting).

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| *Nenhuma saída nomeada* | - | Este nó processa a conversão de forma assíncrona e retorna o resultado através do sistema da API Tripo |
