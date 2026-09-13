# Criar Imagem em Camadas

## Entradas

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-----------|---------------|-------------|-----------|
| `layers` | Pilha de camadas a compor; crie-a com Add Layer. Os itens são empilhados por z_index, quadros em lote dentro de um item se expandem para camadas consecutivas, e o posicionamento, a opacidade e o modo de mesclagem do item definem a composição inicial. Sem uma tela de documento explícita, o tamanho é a extensão máxima possível das camadas posicionadas. Uma composição salva que corresponda às entradas atuais tem prioridade. | LAYERS | Sim | Máximo de 50 camadas |
| `compositor` | Composição em camadas salva pelo editor do compositor. | COMPOSITOR | Não | Nenhum |

**Notas sobre restrições:**

- A pilha de camadas suporta no máximo 50 camadas expandidas; fornecer mais gera um erro.
- No momento, apenas itens de camada raster têm suporte; outros tipos de item geram um erro.
- A versão do documento `layers` deve ser 1; outras versões geram um erro.
- O estado salvo de `compositor` só é reproduzido quando suas impressões digitais de entrada registradas correspondem à pilha de camadas atual. Se não corresponderem, o nó recorre à composição a partir das propriedades das camadas e marca o estado salvo como obsoleto.
- A opacidade da camada é limitada ao intervalo de 0.0 a 1.0.
- O posicionamento horizontal e vertical da camada (`x`, `y`) é limitado ao limite máximo de resolução.
- A largura e a altura da camada recorrem ao tamanho natural da imagem quando definidas como zero ou menos, e são limitadas ao limite máximo de resolução.
- O tamanho da tela composta não deve exceder o limite máximo de resolução.
- Quando nenhuma camada é fornecida, uma imagem de espaço reservado 64x64 é retornada.

## Saídas

| Nome da saída | Descrição | Tipo de dados |
|---------------|-----------|---------------|
| `IMAGE` | Imagem composta. Possui um canal alfa quando a composição tem áreas transparentes (por exemplo, fundo oculto); caso contrário, RGB simples. | IMAGE |
| `MASK` | Transparência da composição (1 = totalmente transparente). Todos os valores são zero quando a composição é opaca. | MASK |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageCompositor/pt-BR.md)

---
**Source fingerprint (SHA-256):** `76e5e57ade89f9ee172c5e1f0b82579d846d15bafb52b2052246f1f2ad7f0034`
