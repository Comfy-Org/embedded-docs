> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageAddNoise/pt-BR.md)

Esta documentação foi gerada por IA. Se você encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageAddNoise/en.md)

O nó ImageAddNoise adiciona ruído aleatório a uma imagem de entrada. Ele usa uma semente aleatória específica para gerar padrões de ruído consistentes e permite controlar a intensidade do efeito de ruído. A imagem resultante mantém as mesmas dimensões da entrada, mas com textura visual adicionada.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `imagem` | IMAGE | Sim | - | A imagem de entrada à qual o ruído será adicionado |
| `semente` | INT | Sim | 0 a 18446744073709551615 | A semente aleatória usada para criar o ruído (padrão: 0) |
| `intensidade` | FLOAT | Sim | 0.0 a 1.0 | Controla a intensidade do efeito de ruído (padrão: 0.5) |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `imagem` | IMAGE | A imagem de saída com ruído adicionado aplicado |

---
**Source fingerprint (SHA-256):** `8abfc64500e5ff8fe7589763a07c15d771e9a5a6a61bae9ec4d819be9bf71810`
