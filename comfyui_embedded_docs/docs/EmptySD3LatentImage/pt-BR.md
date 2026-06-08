O nó EmptySD3LatentImage cria um tensor de imagem latente em branco formatado especificamente para modelos Stable Diffusion 3. Ele gera um tensor preenchido com zeros que possui as dimensões e a estrutura corretas esperadas pelos pipelines SD3. Isso é comumente usado como ponto de partida para fluxos de trabalho de geração de imagens.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `largura` | A largura da imagem latente de saída em pixels (padrão: 1024) | INT | Sim | 16 a MAX_RESOLUTION (passo: 16) |
| `altura` | A altura da imagem latente de saída em pixels (padrão: 1024) | INT | Sim | 16 a MAX_RESOLUTION (passo: 16) |
| `tamanho_do_lote` | O número de imagens latentes a serem geradas em um lote (padrão: 1) | INT | Sim | 1 a 4096 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `LATENT` | Um tensor latente contendo amostras em branco com dimensões compatíveis com SD3. O tensor possui 16 canais e é reduzido espacialmente por um fator de 8 em comparação com a largura e altura de entrada. | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptySD3LatentImage/pt-BR.md)

---
**Source fingerprint (SHA-256):** `21eb5b6385b9b0db95d48fa2f4b85eafe44f865af11ee194945ab7ffe54b6acc`
