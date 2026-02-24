> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftStyleV3RealisticImage/pt-BR.md)

Este nó cria uma configuração de estilo de imagem realista para uso com a API do Recraft. Ele permite que você selecione o estilo `realistic_image` e escolha entre várias opções de subestilo para personalizar a aparência da saída.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `substyle` | STRING | Sim | Múltiplas opções disponíveis | O subestilo específico a ser aplicado ao estilo `realistic_image`. Se definido como "None", nenhum subestilo será aplicado. |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `recraft_style` | STYLEV3 | Retorna um objeto de configuração de estilo do Recraft contendo o estilo `realistic_image` e as configurações do subestilo selecionado. |
