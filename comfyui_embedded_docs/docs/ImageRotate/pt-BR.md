> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageRotate/pt-BR.md)

O nó ImageRotate gira uma imagem de entrada por ângulos especificados. Ele suporta quatro opções de rotação: sem rotação, 90 graus no sentido horário, 180 graus e 270 graus no sentido horário. A rotação é realizada usando operações eficientes de tensor que mantêm a integridade dos dados da imagem.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Faixa | Descrição |
|-----------|---------------|-------------|-------|-----------|
| `imagem` | IMAGE | Sim | - | A imagem de entrada a ser girada |
| `rotação` | STRING | Sim | "none"<br>"90 degrees"<br>"180 degrees"<br>"270 degrees" | O ângulo de rotação a ser aplicado à imagem (padrão: "none") |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|---------------|---------------|-----------|
| `imagem` | IMAGE | A imagem de saída girada |

---
**Source fingerprint (SHA-256):** `068946b31ebe87b2524a1e628b5bc0a3da7367d7252fa7afafe96bcbb174747d`
