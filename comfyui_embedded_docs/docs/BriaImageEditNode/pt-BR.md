# Bria Image Edit

O nó Bria FIBO Image Edit permite modificar uma imagem existente usando uma instrução de texto. Ele envia a imagem e seu prompt para a API da Bria, que usa o modelo FIBO para gerar uma nova versão editada da imagem com base na sua solicitação. Você também pode fornecer uma máscara para limitar as edições a uma área específica.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `model` | A versão do modelo a ser usada para edição de imagem. | COMBO | Sim | `"FIBO"` |
| `image` | A imagem de entrada que você deseja editar. | IMAGE | Sim | - |
| `prompt` | Instrução para editar a imagem (padrão: vazio). | STRING | Sim | - |
| `negative_prompt` | Texto descrevendo o que você não deseja que apareça na imagem editada (padrão: vazio). | STRING | Sim | - |
| `structured_prompt` | Uma string contendo o prompt de edição estruturado em formato JSON. Use este em vez do prompt usual para controle preciso e programático (padrão: vazio). | STRING | Sim | - |
| `seed` | Um número usado para inicializar a geração aleatória, garantindo resultados reproduzíveis (padrão: 1). | INT | Sim | 1 a 2147483647 |
| `guidance_scale` | Valores mais altos fazem a imagem seguir o prompt mais fielmente (padrão: 3.0). | FLOAT | Sim | 3.0 a 5.0 |
| `steps` | O número de etapas de remoção de ruído que o modelo executará (padrão: 50). | INT | Sim | 20 a 50 |
| `moderation` | Configurações de moderação. Selecionar `"true"` revela opções adicionais de moderação para conteúdo do prompt, entrada visual e saída visual. | DYNAMICCOMBO | Sim | `"false"`<br>`"true"` |
| `mask` | Se omitida, a edição se aplica a toda a imagem. | MASK | Não | - |

**Restrições Importantes:**

- É necessário fornecer pelo menos um dos inputs `prompt` ou `structured_prompt`. Eles não podem estar ambos vazios.
- Quando o parâmetro `moderation` estiver definido como `"true"`, três entradas booleanas adicionais ficam disponíveis: `prompt_content_moderation` (padrão: false), `visual_input_moderation` (padrão: false) e `visual_output_moderation` (padrão: true).

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `IMAGE` | A imagem editada retornada pela API da Bria. | IMAGE |
| `structured_prompt` | O prompt estruturado que foi usado ou gerado durante o processo de edição. | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaImageEditNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `e66aaa563a82407408f25b289011a491c8b158822fc2db8912daf73731750081`
