> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PhotoMakerLoader/pt-BR.md)

O nó PhotoMakerLoader carrega um modelo PhotoMaker a partir dos arquivos de modelo disponíveis. Ele lê o arquivo de modelo especificado e prepara o codificador de ID do PhotoMaker para uso em tarefas de geração de imagens baseadas em identidade. Este nó é marcado como experimental e destina-se a fins de teste.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Faixa | Descrição |
|-----------|---------------|-------------|-------|-----------|
| `photomaker_model_name` | STRING | Sim | Múltiplas opções disponíveis | O nome do arquivo de modelo PhotoMaker a ser carregado. As opções disponíveis são determinadas pelos arquivos de modelo presentes na pasta `photomaker`. |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|---------------|---------------|-----------|
| `photomaker_model` | PHOTOMAKER | O modelo PhotoMaker carregado contendo o codificador de ID, pronto para uso em operações de codificação de identidade. |

---
**Source fingerprint (SHA-256):** `4c55abacf8462d8de3d1f2a728d4b09ab1d1c8c6476d25cc4af5089508a721da`
