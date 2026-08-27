# LatentConcat

O nó LatentConcat combina duas amostras latentes unindo-as ao longo de uma dimensão escolhida. Ele recebe duas entradas latentes e as concatena ao longo do eixo x, y ou t, com a opção de controlar qual amostra vem primeiro. O nó ajusta automaticamente o tamanho do lote da segunda entrada para corresponder ao da primeira antes de realizar a concatenação.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `amostras1` | A primeira amostra latente a ser concatenada | LATENT | Sim | - |
| `amostras2` | A segunda amostra latente a ser concatenada | LATENT | Sim | - |
| `dimensão` | A dimensão ao longo da qual as amostras latentes serão concatenadas. Valores positivos (x, y, t) colocam samples1 antes de samples2 no resultado. Valores negativos (-x, -y, -t) colocam samples2 antes de samples1. O mapeamento das dimensões é: x = largura, y = altura, t = tempo/quadros | COMBO | Sim | `"x"`<br>`"-x"`<br>`"y"`<br>`"-y"`<br>`"t"`<br>`"-t"` |

**Observação:** A segunda amostra latente (`samples2`) é automaticamente repetida conforme necessário para corresponder ao tamanho do lote da primeira amostra latente (`samples1`) antes da concatenação.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `output` | As amostras latentes concatenadas resultantes da combinação das duas amostras de entrada ao longo da dimensão especificada | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentConcat/pt-BR.md)

---
**Source fingerprint (SHA-256):** `dfe27f76ad12e16623d62c9e7f0b2772df6ecadb543a4eee430bc38ab04a12f2`
