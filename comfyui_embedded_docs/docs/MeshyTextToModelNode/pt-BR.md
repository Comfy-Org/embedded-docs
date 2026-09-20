# Meshy: Texto para Modelo

O nó Meshy: Text to Model usa a API Meshy para gerar um modelo 3D a partir de uma descrição textual. Ele envia uma solicitação à API com seu prompt e configurações, depois aguarda a conclusão da geração e baixa os arquivos do modelo resultante.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-----------|---------------|-------------|-----------|
| `modelo` | Especifica a versão do modelo de IA a ser usada para geração. | COMBO | Sim | `"meshy-7.1"`<br>`"meshy-7"`<br>`"meshy-6"`<br>`"latest"` |
| `prompt` | A descrição textual do modelo 3D que você deseja gerar. Deve ter entre 1 e 600 caracteres. O padrão é uma string vazia. | STRING | Sim | 1 - 600 caracteres |
| `estilo` | O estilo artístico para o modelo 3D gerado. | COMBO | Sim | `"realistic"` |
| `deve_refazer_malha` | Quando definido como false, retorna uma malha triangular não processada. Selecionar "true" revela parâmetros adicionais para topologia e contagem de polígonos alvo. | DYNAMIC_COMBO | Sim | `"true"`<br>`"false"` |
| `topology` | O tipo de polígono alvo para o modelo remalhado. Este parâmetro só está disponível quando `should_remesh` está definido como "true". | COMBO | Não* | `"triangle"`<br>`"quad"` |
| `target_polycount` | O número alvo de polígonos para o modelo remalhado. O padrão é 300000. Este parâmetro só está disponível quando `should_remesh` está definido como "true". | INT | Não* | 100 - 300000 |
| `modo_de_simetria` | Controla a simetria no modelo gerado. Este é um parâmetro avançado. As opções são `"auto"`, `"on"` e `"off"`. | COMBO | Sim | `"auto"`<br>`"on"`<br>`"off"` |
| `modo_de_pose` | Especifica o modo de pose para o modelo gerado. Uma string vazia significa que nenhuma pose específica foi solicitada. Este é um parâmetro avançado. | COMBO | Sim | `""`<br>`"A-pose"`<br>`"T-pose"` |
| `semente` | A seed controla se o nó deve ser executado novamente; os resultados não são determinísticos independentemente da seed. O padrão é 0. | INT | Sim | 0 - 2147483647 |
| `ultra_mode` | Executa uma passagem extra de refinamento para geometria de maior fidelidade com detalhes de superfície mais finos. O padrão é false. | BOOLEAN | Sim | true<br>false |
| `ultra_resolution` | Resolução da passagem ultra: `"2k"` a executa em 2048³ e `"4k"` em 4096³ para o detalhe de superfície mais fino. `"4k"` requer o modelo `"meshy-7.1"` ou `"latest"`. Usado apenas quando `ultra_mode` está habilitado (padrão: `"2k"`). | COMBO | Não | `"2k"`<br>`"4k"` |

*Nota: Os parâmetros `topology` e `target_polycount` estão disponíveis condicionalmente. Eles só aparecem quando o parâmetro `should_remesh` está definido como "true".

Quando `ultra_mode` está habilitado, o parâmetro `model` deve ser definido como `"meshy-7.1"`, `"meshy-7"` ou `"latest"`; qualquer outro modelo gera um erro. Com `"meshy-7"` a passagem ultra sempre é executada em 2048³, e a resolução ultra `"4k"` requer `"meshy-7.1"` ou `"latest"`.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|---------------|-----------|---------------|
| `model_file` | O nome do arquivo do modelo GLB gerado. Esta saída é fornecida para compatibilidade com versões anteriores. | STRING |
| `meshy_task_id` | O identificador único da tarefa da API Meshy. | MESHY_TASK_ID |
| `GLB` | O arquivo de modelo 3D gerado no formato GLB. | FILE3DGLB |
| `FBX` | O arquivo de modelo 3D gerado no formato FBX. | FILE3DFBX |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyTextToModelNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `a02a5ae28bcae343c628d11ba3efa952b61b8bdf867669f58f1beb0f7c9e49f9`
