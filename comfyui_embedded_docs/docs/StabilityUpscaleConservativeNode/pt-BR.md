> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StabilityUpscaleConservativeNode/pt-BR.md)

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Sim | - | A imagem de entrada a ser ampliada |
| `prompt` | STRING | Sim | - | O que você deseja ver na imagem de saída. Um prompt forte e descritivo que defina claramente elementos, cores e assuntos levará a melhores resultados. (padrão: string vazia) |
| `creativity` | FLOAT | Sim | 0.2-0.5 | Controla a probabilidade de criar detalhes adicionais não fortemente condicionados pela imagem inicial. (padrão: 0.35) |
| `seed` | INT | Sim | 0-4294967294 | A semente aleatória usada para criar o ruído. (padrão: 0) |
| `negative_prompt` | STRING | Não | - | Palavras-chave do que você não deseja ver na imagem de saída. Este é um recurso avançado. (padrão: string vazia) |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `image` | IMAGE | A imagem ampliada em resolução 4K |
