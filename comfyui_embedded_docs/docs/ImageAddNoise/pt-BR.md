Esta documentação foi gerada por IA. Se você encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageAddNoise/en.md)

O nó ImageAddNoise adiciona ruído aleatório a uma imagem de entrada. Ele usa uma semente aleatória específica para gerar padrões de ruído consistentes e permite controlar a intensidade do efeito de ruído. A imagem resultante mantém as mesmas dimensões da entrada, mas com textura visual adicionada.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `imagem` | A imagem de entrada à qual o ruído será adicionado | IMAGE | Sim | - |
| `semente` | A semente aleatória usada para criar o ruído (padrão: 0) | INT | Sim | 0 a 18446744073709551615 |
| `intensidade` | Controla a intensidade do efeito de ruído (padrão: 0.5) | FLOAT | Sim | 0.0 a 1.0 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `imagem` | A imagem de saída com ruído adicionado aplicado | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageAddNoise/pt-BR.md)

---
**Source fingerprint (SHA-256):** `8abfc64500e5ff8fe7589763a07c15d771e9a5a6a61bae9ec4d819be9bf71810`
