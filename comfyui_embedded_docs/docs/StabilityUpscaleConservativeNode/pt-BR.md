> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StabilityUpscaleConservativeNode/pt-BR.md)

Esta documentação foi gerada por IA. Se encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StabilityUpscaleConservativeNode/en.md)

Amplia a imagem com alterações mínimas para resolução 4K. Este nó utiliza o upscaling conservador da Stability AI para aumentar a resolução da imagem, preservando o conteúdo original e fazendo apenas alterações sutis.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `image` | IMAGE | Sim | - | A imagem de entrada a ser ampliada |
| `prompt` | STRING | Sim | - | O que você deseja ver na imagem de saída. Um prompt forte e descritivo que defina claramente elementos, cores e assuntos levará a melhores resultados. (padrão: string vazia) |
| `creativity` | FLOAT | Sim | 0.2-0.5 | Controla a probabilidade de criar detalhes adicionais que não são fortemente condicionados pela imagem inicial. (padrão: 0.35) |
| `seed` | INT | Sim | 0-4294967294 | A semente aleatória usada para criar o ruído. (padrão: 0) |
| `negative_prompt` | STRING | Não | - | Palavras-chave do que você NÃO deseja ver na imagem de saída. Este é um recurso avançado. (padrão: string vazia) |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `image` | IMAGE | A imagem ampliada em resolução 4K |

---
**Source fingerprint (SHA-256):** `0a6eed22a37c1019ee97035bba70660b9619b0d65e443111d1d330968ded009a`
