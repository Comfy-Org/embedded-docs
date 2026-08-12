# ImageCompositor

Este nó combina múltiplas camadas de imagem em uma única imagem composta. Ele recebe uma pilha de camadas criada com o nó Add Layer e, opcionalmente, uma composição salva do editor de compositor; em seguida, mescla as camadas usando suas configurações de posição, tamanho, rotação, opacidade e modo de mesclagem.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `layers` | Pilha de camadas para compor; crie-a com o nó Add Layer. Os itens são empilhados por `z_index`, quadros em lote dentro de um item se expandem em camadas consecutivas, e a posição, opacidade e o modo de mesclagem do item definem a composição inicial. Sem uma tela de documento explícita, o tamanho é uma extensão máxima de melhor esforço das camadas posicionadas. Uma composição salva que corresponda às entradas atuais tem prioridade. | LAYERS | Sim | Máximo de 50 camadas |
| `compositor` | Composição em camadas salva pelo editor de compositor. | COMPOSITOR | Não | Nenhum |

**Notas sobre restrições:**

- A pilha de camadas suporta no máximo 50 camadas (quadros expandidos); fornecer mais gera um erro.
- Apenas camadas rasterizadas são suportadas atualmente; outros tipos de item de camada geram um erro.
- A versão do documento de `layers` deve ser 1; outras versões geram um erro.
- O estado salvo do `compositor` só é reproduzido quando suas impressões digitais de entrada registradas correspondem à pilha de camadas atual. Se não corresponderem, o nó recorre à composição a partir das propriedades das camadas e marca o estado salvo como obsoleto.
- A opacidade da camada é limitada ao intervalo de 0.0 a 1.0.
- A posição horizontal/vertical da camada (`x`, `y`) é limitada ao limite máximo de resolução.
- A largura e a altura da camada voltam ao tamanho natural da imagem quando definidas como zero ou menos, e são limitadas ao limite máximo de resolução.
- O tamanho da tela composta não deve exceder o limite máximo de resolução.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `IMAGE` | Imagem composta. Carrega um canal alfa quando a composição possui áreas transparentes (por exemplo, fundo oculto); caso contrário, RGB simples. | IMAGE |
| `MASK` | Transparência da composição (1 = totalmente transparente). Todos os zeros quando a composição é opaca. | MASK |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageCompositor/pt-BR.md)

---
**Source fingerprint (SHA-256):** `1eca5c151b3737ccf76e6fd7a83cd1458b2acc314609753d597eec711bcf4bd8`
