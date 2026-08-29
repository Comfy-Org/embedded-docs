# Comparar Imagens

O nó Image Compare fornece uma interface visual para comparar duas imagens lado a lado usando um controle deslizante arrastável. Ele é projetado como um nó de saída, ou seja, não envia dados para outros nós, mas exibe as imagens diretamente na interface do usuário para inspeção.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `imagem_a` | A primeira imagem a ser comparada. | IMAGE | Não | - |
| `imagem_b` | A segunda imagem a ser comparada. | IMAGE | Não | - |
| `compare_view` | O controle que ativa a visualização de comparação com controle deslizante na interface. | IMAGECOMPARE | Sim | - |

**Observação:** Este é um nó de saída. Embora `image_a` e `image_b` sejam opcionais, pelo menos uma imagem deve ser fornecida para que o nó tenha um efeito visível. O nó exibirá uma área vazia para qualquer entrada de imagem que não estiver conectada.

## Saídas

Este é um nó de saída e não produz nenhuma saída de dados para uso em outros nós. Sua função é exibir as imagens fornecidas na interface do ComfyUI.

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageCompare/pt-BR.md)

---
**Source fingerprint (SHA-256):** `bc065572c5631ed80c0590aabae775c51d0f607895a87cb2cca78037ab9a6638`
