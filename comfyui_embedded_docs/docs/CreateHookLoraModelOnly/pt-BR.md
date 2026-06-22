# Criar Hook LoRA (MO)

Este nó cria um hook LoRA (Adaptação de Baixo Posto) que se aplica apenas ao componente do modelo, deixando o componente CLIP completamente inalterado. Ele carrega um arquivo LoRA e o aplica com uma intensidade especificada ao modelo, enquanto define a intensidade do CLIP como zero. O nó pode ser encadeado com hooks anteriores para construir pipelines de modificação complexas.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `lora_name` | O nome do arquivo LoRA a ser carregado da pasta loras | STRING | Sim | Múltiplas opções disponíveis |
| `força_modelo` | O multiplicador de intensidade para aplicar o LoRA ao componente do modelo (padrão: 1.0) | FLOAT | Sim | -20.0 a 20.0 |
| `hooks_anteriores` | Hooks anteriores opcionais para encadear com este hook | HOOKS | Não | - |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `hooks` | O hook LoRA criado que pode ser aplicado ao processamento do modelo | HOOKS |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateHookLoraModelOnly/pt-BR.md)

---
**Source fingerprint (SHA-256):** `10adbdfc2e37fcf317e93130f87d9a7038d00b091cb6d1b45f4658c81632ef80`
