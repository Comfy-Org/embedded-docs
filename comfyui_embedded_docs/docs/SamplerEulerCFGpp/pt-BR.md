> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerEulerCFGpp/pt-BR.md)

O nó SamplerEulerCFGpp fornece um método de amostragem Euler CFG++ para gerar saídas. Este nó oferece duas versões de implementação diferentes do amostrador Euler CFG++ que podem ser selecionadas com base na preferência do usuário.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `version` | STRING | Sim | `"regular"`<br>`"alternative"` | A versão de implementação do amostrador Euler CFG++ a ser utilizada |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `sampler` | SAMPLER | Retorna uma instância configurada do amostrador Euler CFG++ |
