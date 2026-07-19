# WanMoveTracksFromCoords

O nó WanMoveTracksFromCoords cria trilhas de movimento a partir de uma string formatada em JSON contendo coordenadas. Ele converte os dados de coordenadas em um formato de tensor que pode ser utilizado por outros nós de processamento de vídeo e, opcionalmente, pode aplicar uma máscara para controlar a visibilidade das trilhas ao longo do tempo.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `track_coords` | Uma string formatada em JSON contendo os dados de coordenadas para as trilhas. O valor padrão é uma lista vazia (`"[]"`). | STRING | Não | N/A |
| `track_mask` | Uma máscara opcional. Quando fornecida, o nó a utiliza para determinar a visibilidade de cada trilha por quadro. | MASK | Não | N/A |

**Nota:** A entrada `track_coords` espera uma estrutura JSON específica. Deve ser uma lista de trilhas, onde cada trilha é uma lista de quadros, e cada quadro é um objeto com coordenadas `x` e `y`. O número de quadros deve ser consistente em todas as trilhas.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `tracks` | Os dados de trilha gerados, contendo as coordenadas do caminho e informações de visibilidade para cada trilha. | TRACKS |
| `track_length` | O número total de quadros nas trilhas geradas. | INT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanMoveTracksFromCoords/pt-BR.md)

---
**Source fingerprint (SHA-256):** `106b05b3bdb5ede6e31216b9f3c14160630df0eee1f4e8a645c2b6cf9fbecf8c`
