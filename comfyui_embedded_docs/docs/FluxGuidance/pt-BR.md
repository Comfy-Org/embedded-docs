> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxGuidance/pt-BR.md)

## Entradas

| Parâmetro | Tipo de Dados | Descrição |
|----------------|-----------|-------------|
| `conditioning` | CONDITIONING | Dados de condicionamento de entrada, tipicamente provenientes de etapas anteriores de codificação ou processamento |
| `guidance` | FLOAT | Controla a influência dos prompts de texto na geração da imagem, com faixa ajustável de 0.0 a 100.0 |

## Saídas

| Parâmetro | Tipo de Dados | Descrição |
|----------------|-----------|-------------|
| `CONDITIONING` | CONDITIONING | Dados de condicionamento atualizados, contendo o novo valor de `guidance` |
