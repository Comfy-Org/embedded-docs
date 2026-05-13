> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoraLoaderBypassModelOnly/pt-BR.md)

Esta documentação foi gerada por IA. Se você encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoraLoaderBypassModelOnly/en.md)

Este nó aplica uma LoRA (Adaptação de Baixo Posto) a um modelo para modificar seu comportamento, mas afeta apenas o componente do modelo em si. Ele carrega um arquivo LoRA especificado e ajusta os pesos do modelo com uma determinada intensidade, deixando outros componentes, como o codificador de texto CLIP, inalterados.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `model` | MODEL | Sim | - | O modelo base ao qual os ajustes da LoRA serão aplicados. |
| `lora_name` | STRING | Sim | (Lista de arquivos LoRA disponíveis) | O nome do arquivo LoRA a ser carregado e aplicado. As opções são preenchidas a partir dos arquivos no diretório `loras`. |
| `strength_model` | FLOAT | Sim | -100.0 a 100.0 | A intensidade do efeito da LoRA nos pesos do modelo. Um valor positivo aplica a LoRA, um valor negativo aplica o inverso e um valor 0 não tem efeito (padrão: 1.0). |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `model` | MODEL | O modelo modificado com os ajustes da LoRA aplicados aos seus pesos. |

---
**Source fingerprint (SHA-256):** `e0e1ad2d6481a1b9771d7eae833ffab0737a967d4af6e57b946d1b2223fe45bf`
