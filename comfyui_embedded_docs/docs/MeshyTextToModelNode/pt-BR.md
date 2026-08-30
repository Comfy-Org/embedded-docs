# Meshy: Texto para Modelo

O nó Meshy: Text to Model usa a API Meshy para gerar um modelo 3D a partir de uma descrição em texto. Ele envia uma solicitação para a API com seu prompt e configurações, aguarda a conclusão da geração e baixa os arquivos de modelo resultantes.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `modelo` | Especifica a versão do modelo de IA a ser usada para a geração. | COMBO | Sim | `"meshy-7"`<br>`"meshy-6"`<br>`"latest"` |
| `prompt` | A descrição em texto do modelo 3D que você deseja gerar. Deve ter entre 1 e 600 caracteres. | STRING | Sim | 1 - 600 caracteres |
| `estilo` | O estilo artístico para o modelo 3D gerado. | COMBO | Sim | `"realistic"` |
| `deve_refazer_malha` | Quando definido como falso, retorna uma malha triangular não processada. Selecionar "true" revela parâmetros adicionais para topologia e contagem de polígonos alvo. | DYNAMIC_COMBO | Sim | `"true"`<br>`"false"` |
| `topology` | O tipo de polígono alvo para o modelo remalhado. Este parâmetro só está disponível quando `should_remesh` está definido como "true". | COMBO | Não* | `"triangle"`<br>`"quad"` |
| `target_polycount` | O número alvo de polígonos para o modelo remalhado. O padrão é 300000. Este parâmetro só está disponível quando `should_remesh` está definido como "true". | INT | Não* | 100 - 300000 |
| `modo_de_simetria` | Controla a simetria no modelo gerado. Este é um parâmetro avançado. | COMBO | Sim | `"auto"`<br>`"on"`<br>`"off"` |
| `modo_de_pose` | Especifica o modo de pose para o modelo gerado. Uma string vazia significa que nenhuma pose específica é solicitada. Este é um parâmetro avançado. | COMBO | Sim | `""`<br>`"A-pose"`<br>`"T-pose"` |
| `semente` | A semente (seed) controla se o nó deve ser executado novamente; os resultados são não determinísticos independentemente da semente. O padrão é 0. | INT | Sim | 0 - 2147483647 |
| `ultra_mode` | Execute uma passagem extra de refinamento para geometria de maior fidelidade com detalhes de superfície mais finos. O padrão é false. | BOOLEAN | Sim | true<br>false |

*Nota: Os parâmetros `topology` e `target_polycount` estão disponíveis condicionalmente. Eles só aparecem quando o parâmetro `should_remesh` está definido como "true".

Quando `ultra_mode` está ativado, o parâmetro `model` deve ser definido como `"meshy-7"` ou `"latest"`.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `arquivo_do_modelo` | O nome do arquivo do modelo GLB gerado. Esta saída é fornecida para compatibilidade reversa. | STRING |
| `meshy_task_id` | O identificador único para a tarefa da API Meshy. | MESHY_TASK_ID |
| `GLB` | O arquivo do modelo 3D gerado no formato GLB. | FILE3DGLB |
| `FBX` | O arquivo do modelo 3D gerado no formato FBX. | FILE3DFBX |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyTextToModelNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `131f17bfb788f206e15c1d48c877e822114902fadf073a6f9fb25e8340421122`
