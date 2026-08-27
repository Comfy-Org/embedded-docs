# LatentCut

O nó LatentCut extrai uma seção específica de amostras latentes ao longo de uma dimensão escolhida. Ele permite recortar uma parte da representação latente especificando a dimensão (x, y ou t), a posição inicial e a quantidade a extrair. O nó lida tanto com indexação positiva quanto negativa e ajusta automaticamente a quantidade extraída para permanecer dentro dos limites disponíveis.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `amostras` | As amostras latentes de entrada das quais extrair | LATENT | Sim | - |
| `dimensão` | A dimensão ao longo da qual cortar as amostras latentes. "x" corta ao longo do último eixo (normalmente largura), "y" ao longo do penúltimo eixo (normalmente altura) e "t" ao longo do antepenúltimo eixo (normalmente quadros em latentes de vídeo) | COMBO | Sim | "x"<br>"y"<br>"t" |
| `índice` | A posição inicial para o corte (padrão: 0). Valores positivos contam a partir do início, valores negativos contam a partir do final. O nó limita automaticamente o índice para permanecer dentro do intervalo válido das amostras latentes | INT | Sim | -16384 a 16384 |
| `quantidade` | O número de elementos a extrair ao longo da dimensão especificada (padrão: 1). O nó reduz automaticamente esse valor se ele exceder os dados disponíveis além do índice inicial | INT | Sim | 1 a 16384 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `output` | A parte extraída das amostras latentes | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentCut/pt-BR.md)

---
**Source fingerprint (SHA-256):** `7682de2644a4b85dba0571406f9f9802eca7caab09dc2ccf1ac91dc13b41bcdf`
