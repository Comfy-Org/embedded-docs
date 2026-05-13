> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftStyleV3RealisticImage/pt-BR.md)

Esta documentação foi gerada por IA. Se encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftStyleV3RealisticImage/en.md)

Este nó cria uma configuração de estilo para gerar imagens realistas usando a API do Recraft. Ele seleciona o estilo `realistic_image` e permite escolher um subestilo opcional para ajustar a aparência da saída.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Faixa | Descrição |
|-----------|---------------|-------------|-------|-----------|
| `substyle` | STRING | Sim | Múltiplas opções disponíveis (determinadas pela API Recraft) | O subestilo específico a ser aplicado ao estilo realistic_image. Se definido como "None", nenhum subestilo será aplicado. |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|---------------|---------------|-----------|
| `recraft_style` | STYLEV3 | Um objeto de configuração de estilo Recraft contendo o estilo `realistic_image` e as configurações do subestilo selecionado. Esta saída pode ser conectada a outros nós Recraft que aceitam uma entrada de estilo. |

---
**Source fingerprint (SHA-256):** `23eafae0a00f1806052a6583db791a5c1fd418ea940ed6463824dffe843ed0d7`
