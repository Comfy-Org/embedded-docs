# Adicionar Ruído à Imagem

O nó ImageAddNoise adiciona ruído aleatório a uma imagem de entrada. Ele usa uma semente aleatória especificada para gerar padrões de ruído consistentes e permite controlar a intensidade do efeito de ruído. A imagem resultante mantém as mesmas dimensões da entrada, mas com textura visual adicionada.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `image` | A imagem de entrada à qual o ruído será adicionado | IMAGE | Sim | - |
| `seed` | A semente aleatória usada para criar o ruído (padrão: 0). Este parâmetro oferece suporte à funcionalidade "control after generate". | INT | Sim | 0 a 18446744073709551615 |
| `strength` | Controla a intensidade do efeito de ruído (padrão: 0.5, passo: 0.01) | FLOAT | Sim | 0.0 a 1.0 |

**Nota:** Os valores de ruído são adicionados à imagem e o resultado é limitado ao intervalo de 0.0–1.0. Se a imagem de entrada tiver um canal alfa (4 canais), o canal alfa original é preservado sem alterações — o ruído é aplicado apenas aos canais de cor.

## Saídas

| Nome de Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `image` | A imagem de saída com o ruído adicionado aplicado | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageAddNoise/pt-BR.md)

---
**Source fingerprint (SHA-256):** `e6b9815e7c075c7ee97c924c22a92dfef6d9c65b97b6e65b0f9e1c96628f39f2`
