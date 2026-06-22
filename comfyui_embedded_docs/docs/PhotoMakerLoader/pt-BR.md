# PhotoMakerLoader

O nó PhotoMakerLoader carrega um modelo PhotoMaker a partir dos arquivos de modelo disponíveis. Ele lê o arquivo de modelo especificado e prepara o codificador de ID do PhotoMaker para uso em tarefas de geração de imagens baseadas em identidade. Este nó é marcado como experimental e destina-se a fins de teste.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `photomaker_model_name` | O nome do arquivo de modelo PhotoMaker a ser carregado. As opções disponíveis são determinadas pelos arquivos de modelo presentes na pasta `photomaker`. | STRING | Sim | Múltiplas opções disponíveis |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `photomaker_model` | O modelo PhotoMaker carregado contendo o codificador de ID, pronto para uso em operações de codificação de identidade. | PHOTOMAKER |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PhotoMakerLoader/pt-BR.md)

---
**Source fingerprint (SHA-256):** `4c55abacf8462d8de3d1f2a728d4b09ab1d1c8c6476d25cc4af5089508a721da`
