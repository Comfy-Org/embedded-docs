# Tripo P1: Imagem para Modelo

Tripo P1: Image to Model converte uma única imagem 2D em um modelo 3D usando a API Tripo P1. Ele é otimizado para gerar malhas low-poly prontas para jogos e permite escolher entre uma malha somente com geometria ou um modelo texturizado com mapas PBR. O modelo finalizado é retornado como um arquivo GLB.

## Entradas

### Entradas comuns

Estes parâmetros estão sempre disponíveis.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `output_mode` | Escolhe o tipo de resultado. "Geometry only" retorna uma malha sem textura; "Textured" adiciona mapas de cor/PBR e revela configurações extras de textura. | DYNAMIC_COMBO | Sim | `"Geometry only"`<br>`"Textured"` |
| `image` | A imagem 2D de origem usada para gerar o modelo 3D. Uma única imagem é necessária; o nó gera um erro se nenhuma for fornecida. | IMAGE | Sim | - |
| `enable_image_autofix` | Pré-processa a imagem de entrada para melhorar a qualidade da geração. (padrão: False) | BOOLEAN | Não | True<br>False |
| `face_limit` | Contagem alvo de faces, 48-20000. -1 permite que o Tripo escolha de forma adaptativa. (padrão: -1) | INT | Não | -1 a 20000 |
| `model_seed` | Semente usada para a geração da geometria para que os resultados possam ser reproduzidos. (padrão: 42) | INT | Não | 0 a 2147483647 |
| `auto_size` | Dimensiona a saída para aproximar metros do mundo real. (padrão: False) | BOOLEAN | Não | True<br>False |
| `export_uv` | Desdobramento UV durante a geração. Desative para execuções mais rápidas somente com geometria. (padrão: True) | BOOLEAN | Não | True<br>False |
| `compress_geometry` | Aplica compressão de geometria meshopt (EXT_meshopt_compression). Arquivos menores, mas a pré-visualização 3D do ComfyUI não consegue exibi-los; descomprima antes de editar. (padrão: False) | BOOLEAN | Não | True<br>False |

### Entradas do Geometry only

Nenhum parâmetro adicional. A saída é uma malha sem textura.

### Entradas do Textured

Estes parâmetros aparecem quando `output_mode` é definido como "Textured".

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `pbr` | Inclui mapas PBR. Quando ativado, a textura base também é forçada. (padrão: True) | BOOLEAN | Sim | True<br>False |
| `texture_quality` | detailed = texturas HD, extreme = texturas Ultra 8K. (padrão: "standard") | COMBO | Sim | `"standard"`<br>`"detailed"`<br>`"extreme"` |
| `texture_alignment` | Prioriza a fidelidade visual à imagem de origem ou o alinhamento à geometria da malha. (padrão: "original_image") | COMBO | Sim | `"original_image"`<br>`"geometry"` |
| `orientation` | Rotaciona a saída para corresponder à imagem de origem. Aplica-se apenas quando texturizado. (padrão: "default") | COMBO | Sim | `"default"`<br>`"align_image"` |
| `texture_seed` | Semente usada para a geração da textura para que resultados texturizados possam ser reproduzidos. (padrão: 42) | INT | Sim | 0 a 2147483647 |

Observação: quando `output_mode` é "Geometry only", a texturização é desativada para a solicitação. No modo "Textured", uma textura de cor é sempre solicitada; desativar `pbr` remove os mapas PBR, mas mantém a textura de cor base, enquanto ativar `pbr` força a textura base também. `texture_alignment` e `orientation` só estão disponíveis no modo "Textured".

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `model_file` | Uma string contendo o nome do arquivo de modelo gerado (`<task_id>.glb`). Mantido apenas para compatibilidade retroativa. | STRING |
| `model task_id` | O ID de tarefa exclusivo retornado pela API Tripo para o trabalho de geração concluído. | MODEL_TASK_ID |
| `GLB` | O modelo 3D gerado no formato GLB. | FILE3DGLB |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoP1ImageToModelNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `1369da2ef732556896bce3415e7b99023f310544b8077ea4c6b1730bec59ee99`
