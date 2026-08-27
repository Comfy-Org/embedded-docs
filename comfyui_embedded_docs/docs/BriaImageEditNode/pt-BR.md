# Bria Image Edit

O nó Bria FIBO Image Edit edita uma imagem existente usando uma instrução de texto. Ele envia a imagem e o prompt para a API da Bria, onde o modelo FIBO cria uma versão editada. Uma máscara opcional pode limitar as alterações a uma área específica.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `modelo` | A versão do modelo a ser usada para edição de imagem. | COMBO | Sim | `"FIBO"` |
| `imagem` | A imagem de entrada que você deseja editar. | IMAGE | Sim | - |
| `prompt` | Instrução para editar a imagem (padrão: vazio). | STRING | Sim | - |
| `prompt_negativo` | Texto descrevendo o que você não deseja que apareça na imagem editada (padrão: vazio). | STRING | Sim | - |
| `prompt_estruturado` | Uma string contendo o prompt estruturado de edição em formato JSON. Use isto em vez do prompt usual para controle preciso e programático (padrão: vazio). | STRING | Sim | - |
| `semente` | Número usado para inicializar a geração aleatória, garantindo resultados reproduzíveis (padrão: 1). | INT | Sim | 1 a 2147483647 |
| `escala_de_guia` | Valores mais altos fazem a imagem seguir o prompt mais fielmente (padrão: 3). | FLOAT | Sim | 3.0 a 5.0 |
| `passos` | O número de etapas de remoção de ruído realizadas pelo modelo (padrão: 50). | INT | Sim | 20 a 50 |
| `moderação` | Configurações de moderação. Selecionar `"true"` revela opções adicionais de moderação. | DYNAMIC_COMBO | Sim | `"false"`<br>`"true"` |
| `máscara` | Se omitida, a edição se aplica à imagem inteira. | MASK | Não | - |

### Entradas de moderação

Quando `moderation` está definido como `"true"`, estas entradas adicionais ficam disponíveis:

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `prompt_content_moderation` | Se deve moderar o texto do prompt para conteúdo impróprio (padrão: false). | BOOLEAN | Não | `true`<br>`false` |
| `visual_input_moderation` | Se deve moderar a imagem de entrada para conteúdo impróprio (padrão: false). | BOOLEAN | Não | `true`<br>`false` |
| `visual_output_moderation` | Se deve moderar a imagem de saída editada para conteúdo impróprio (padrão: true). | BOOLEAN | Não | `true`<br>`false` |

**Restrições importantes:**

- Pelo menos um entre `prompt` ou `structured_prompt` deve ser não vazio. Se ambos estiverem vazios, o nó gera um erro.
- Quando `moderation` está definido como `"true"`, as três entradas de moderação acima são exibidas.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `IMAGE` | A imagem editada retornada pela API da Bria. | IMAGE |
| `prompt_estruturado` | O prompt estruturado usado ou gerado durante o processo de edição. | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaImageEditNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `e66aaa563a82407408f25b289011a491c8b158822fc2db8912daf73731750081`
