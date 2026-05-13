> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerEulerCFGpp/pt-BR.md)

O nó SamplerEulerCFGpp fornece um método de amostragem Euler CFG++ para gerar saídas. Este nó oferece duas versões diferentes de implementação do amostrador Euler CFG++ que podem ser selecionadas de acordo com a preferência do usuário.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `versão` | STRING | Sim | `"regular"`<br>`"alternative"` | A versão de implementação do amostrador Euler CFG++ a ser usada (padrão: "regular") |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `sampler` | SAMPLER | Retorna uma instância configurada do amostrador Euler CFG++ |

---
**Source fingerprint (SHA-256):** `f01732fc39a76fca697aaddefc8cec58d54ba9761eb8d93da806ddd162d42513`
