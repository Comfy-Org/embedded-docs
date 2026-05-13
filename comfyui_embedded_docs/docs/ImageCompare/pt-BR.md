> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageCompare/pt-BR.md)

O nó Image Compare fornece uma interface visual para comparar duas imagens lado a lado usando um controle deslizante ajustável. Ele foi projetado como um nó de saída, ou seja, não transmite dados para outros nós, mas exibe as imagens diretamente na interface do usuário para inspeção.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `image_a` | IMAGE | Não | - | A primeira imagem a ser comparada. |
| `image_b` | IMAGE | Não | - | A segunda imagem a ser comparada. |
| `compare_view` | IMAGECOMPARE | Sim | - | O controle que habilita a visualização de comparação com controle deslizante na interface. |

**Observação:** Este nó é um nó de saída. Embora `image_a` e `image_b` sejam opcionais, pelo menos uma imagem deve ser fornecida para que o nó tenha um efeito visível. O nó exibirá uma área vazia para qualquer entrada de imagem que não estiver conectada.

## Saídas

Este nó é um nó de saída e não produz nenhuma saída de dados para uso em outros nós. Sua função é exibir as imagens fornecidas na interface do ComfyUI.

---
**Source fingerprint (SHA-256):** `2bc980cd20aad3cf60300868599bbce8eaba1cdb21880d2b3f4cd628108d8139`
