# PhotoMakerLoader

O nó PhotoMakerLoader carrega um modelo PhotoMaker a partir dos arquivos de modelo disponíveis. Ele lê o arquivo de modelo especificado e prepara o codificador ID do PhotoMaker para uso em tarefas de geração de imagens baseadas em identidade. Este nó é marcado como experimental e é destinado a fins de teste.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `photomaker_model_name` | O nome do arquivo de modelo PhotoMaker a ser carregado. As opções disponíveis são determinadas pelos arquivos de modelo presentes na pasta `photomaker`. | COMBO | Sim | Múltiplas opções disponíveis |

Nota: O arquivo de modelo selecionado deve existir na pasta `photomaker`. O nó gera um erro se o arquivo especificado não for encontrado.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `photomaker_model` | O modelo PhotoMaker carregado contendo o codificador ID, pronto para uso em operações de codificação de identidade. | PHOTOMAKER |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PhotoMakerLoader/pt-BR.md)

---
**Source fingerprint (SHA-256):** `1b26630fadbdc144cd42ca7393f743b079ee7463deb9c8b31b628b5dc7432317`
