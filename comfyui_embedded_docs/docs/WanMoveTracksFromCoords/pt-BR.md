# WanMoveTracksFromCoords

O nó WanMoveTracksFromCoords cria trilhas de movimento a partir de uma string formatada em JSON contendo coordenadas. Ele converte os dados de coordenadas em um formato de tensor que pode ser usado por outros nós de processamento de vídeo e pode, opcionalmente, aplicar uma máscara para controlar a visibilidade das trilhas ao longo do tempo.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `track_coords` | Uma string formatada em JSON contendo os dados de coordenadas das trilhas. O valor padrão é uma lista vazia (`"[]"`). | STRING | Não | N/A |
| `track_mask` | Uma máscara opcional. Quando fornecida, o nó a utiliza para determinar a visibilidade de cada trilha por quadro. Quando não fornecida, todas as trilhas são consideradas visíveis em todos os quadros. | MASK | Não | N/A |

**Observação:** O parâmetro `track_coords` espera uma estrutura JSON específica. Deve ser uma lista de trilhas, em que cada trilha é uma lista de quadros, e cada quadro é um objeto com coordenadas `x` e `y`. O número de quadros deve ser consistente em todas as trilhas.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `tracks` | Os dados de trilha gerados, contendo as coordenadas do caminho e as informações de visibilidade de cada trilha. | TRACKS |
| `track_length` | O número total de quadros nas trilhas geradas. | INT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanMoveTracksFromCoords/pt-BR.md)

---
**Source fingerprint (SHA-256):** `125187c96332fa81f0a30bcc4c927f405b56b578638ea565642a2b88dff808b7`
