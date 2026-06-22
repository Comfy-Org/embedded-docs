# Criar Hook Modelo como LoRA (MO)

Esta documentação foi gerada por IA. Se você encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateHookModelAsLoraModelOnly/en.md)

Este nó cria um hook que aplica um modelo LoRA (Adaptação de Baixa Classificação) para modificar apenas o componente de modelo de uma rede neural. Ele carrega um arquivo de checkpoint e o aplica com uma intensidade especificada ao modelo, deixando o componente CLIP inalterado. Este é um nó experimental que estende a funcionalidade da classe base CreateHookModelAsLora.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `ckpt_name` | O arquivo de checkpoint a ser carregado como modelo LoRA. As opções disponíveis dependem do conteúdo da pasta de checkpoints. | STRING | Sim | Múltiplas opções disponíveis |
| `força_modelo` | O multiplicador de intensidade para aplicar a LoRA ao componente do modelo (padrão: 1.0) | FLOAT | Sim | -20.0 a 20.0 |
| `hooks_anteriores` | Hooks anteriores opcionais para encadear com este hook | HOOKS | Não | - |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `hooks` | O grupo de hooks criado contendo a modificação do modelo LoRA | HOOKS |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateHookModelAsLoraModelOnly/pt-BR.md)

---
**Source fingerprint (SHA-256):** `adbeaede65aa89d48c59225ca1c8edc4c9394a364f93a00dae4a83a2270f093b`
