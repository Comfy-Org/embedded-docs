# ModelAttentionBackend

Este nó permite escolher qual backend de atenção um modelo usa para seus cálculos de atenção. Ele cria uma cópia do modelo e substitui a função de atenção selecionada, o que pode afetar o desempenho ou o comportamento. Se o backend escolhido não estiver disponível, ele volta automaticamente para a atenção PyTorch e registra um aviso.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `model` | O modelo ao qual o backend de atenção selecionado será aplicado. | MODEL | Sim |  |
| `attention` | O backend de atenção a ser usado (padrão: "pytorch attention"). Se o backend selecionado não estiver disponível, a atenção PyTorch será usada como fallback. | STRING | Sim | "pytorch attention"<br>"comfy kitchen attention" |

Nota: A opção "comfy kitchen attention" só é listada quando o módulo de atenção comfy kitchen int8 está disponível no ambiente atual.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `MODEL` | Um clone do modelo de entrada com o backend de atenção selecionado aplicado. | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelAttentionBackend/pt-BR.md)

---
**Source fingerprint (SHA-256):** `4ba613cc0bf5b3e7f9effa895b98b3a3bd302e5d20e9d7e18d1633906c783244`
