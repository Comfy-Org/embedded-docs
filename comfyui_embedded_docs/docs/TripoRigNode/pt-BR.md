# Tripo: Rig no modelo

Este nó recebe um modelo 3D Tripo existente e cria uma versão com rig dele, ou seja, o modelo recebe um esqueleto para que possa ser animado. Você fornece o ID da tarefa do modelo a receber rig, escolhe a versão do rig, o tipo de esqueleto, o estilo de nomenclatura dos ossos e o formato do arquivo de saída; o nó envia a tarefa para a Tripo, aguarda até que ela seja concluída e então retorna o resultado baixado.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `original_model_task_id` | O ID da tarefa do modelo 3D original a receber rig. Normalmente é o ID produzido por um nó anterior de geração de modelo Tripo. | MODEL_TASK_ID | Sim | - |
| `model_version` | Versão do modelo de rig a usar. v1.0: apenas personagens humanoides (bípedes), mais de 90 presets de animação. v2.5: criaturas não humanoides (quadrúpedes, hexápodes, octópodes, aviárias, serpentinas, aquáticas). Padrão: `v1.0-20240301`. | COMBO | Não | "v1.0-20240301"<br>"v2.5-20260210" |
| `rig_type` | Tipo de esqueleto. "auto" executa primeiro a verificação gratuita de rig da Tripo e usa o tipo recomendado. Padrão: "auto". | COMBO | Não | "auto"<br>"biped"<br>"quadruped"<br>"hexapod"<br>"octopod"<br>"avian"<br>"serpentine"<br>"aquatic" |
| `spec` | Nomenclatura dos ossos: nativa da Tripo ou compatível com Mixamo. A Tripo não consegue fazer retarget de seus presets de animação em um rig v1.0 criado com a especificação mixamo; use tripo para o Tripo: Retarget rigged model. Padrão: "tripo". | COMBO | Não | "tripo"<br>"mixamo" |
| `out_format` | Formato do arquivo de saída; o resultado chega na saída correspondente. Padrão: "glb". | COMBO | Não | "glb"<br>"fbx" |

**Nota:** A versão de modelo v1.0 (`v1.0-20240301`) só oferece suporte a esqueletos bípedes. Se um `rig_type` que não seja bípede for usado com essa versão, o nó gera um erro e instrui você a usar `v2.5-20260210` em vez disso.

**Nota:** Quando `rig_type` é "auto", a Tripo primeiro verifica se o modelo pode receber rig e escolhe o tipo de esqueleto recomendado. Se a Tripo informar que o modelo não pode receber rig, o nó falha com um erro.

**Nota:** O nó espera que a Tripo retorne um arquivo GLB ou FBX. Se a Tripo retornar qualquer outro tipo de arquivo, o nó gera um erro.

**Nota:** Somente a saída correspondente a `out_format` é preenchida: `GLB` quando `out_format` é "glb", e `FBX` quando `out_format` é "fbx". A outra saída 3D fica vazia.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `model_file` | O nome do arquivo do modelo com rig gerado (ID da tarefa mais extensão de formato). Mantido apenas para compatibilidade com versões anteriores. | STRING |
| `rig task_id` | O ID da tarefa para acompanhar o processo de geração de rig. | RIG_TASK_ID |
| `GLB` | O modelo com rig como um arquivo 3D GLB. Preenchido quando `out_format` é "glb". | FILE3DGLB |
| `FBX` | O modelo com rig como um arquivo 3D FBX. Preenchido quando `out_format` é "fbx". | FILE3DFBX |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoRigNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `b9c1b6d27b6278bcee4fc22e11c11e65cd22ea92cab3fc6c74f84d3deb2024d6`
