# LatentCut

O nó LatentCut extrai uma seção específica de amostras latentes ao longo de uma dimensão escolhida. Ele recorta uma porção da representação latente especificando a dimensão (x, y ou t), a posição inicial e quanto extrair. O nó oferece suporte a indexação positiva e negativa e ajusta automaticamente a quantidade de extração para que permaneça dentro dos limites disponíveis.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `samples` | As amostras latentes de entrada das quais extrair | LATENT | Sim | - |
| `dim` | A dimensão ao longo da qual recortar as amostras latentes. "x" recorta ao longo do último eixo (normalmente largura), "y" ao longo do penúltimo eixo (normalmente altura) e "t" ao longo do antepenúltimo eixo (normalmente quadros em latentes de vídeo) | COMBO | Sim | "x"<br>"y"<br>"t" |
| `index` | A posição inicial para o corte (padrão: 0). Valores positivos contam a partir do início; valores negativos contam a partir do fim. O nó limita o índice para permanecer dentro do intervalo válido das amostras latentes | INT | Sim | -16384 a 16384 |
| `amount` | O número de elementos a extrair ao longo da dimensão especificada (padrão: 1). Deve ser pelo menos 1. O nó reduz automaticamente esse valor se ele exceder os dados disponíveis após a posição inicial | INT | Sim | 1 a 16384 |

Nota: Os valores de `index` e `amount` são ajustados para se adequar ao tamanho real do latente ao longo da dimensão selecionada. Se `index` for maior que o tamanho da dimensão, ele é limitado à última posição válida. Se `index` for negativo, ele é limitado ao tamanho da dimensão em termos absolutos, e `amount` é limitado para não ultrapassar o fim dos dados.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `output` | A porção extraída das amostras latentes | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentCut/pt-BR.md)

---
**Source fingerprint (SHA-256):** `7682de2644a4b85dba0571406f9f9802eca7caab09dc2ccf1ac91dc13b41bcdf`
