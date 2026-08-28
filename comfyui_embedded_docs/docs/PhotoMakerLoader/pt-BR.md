# PhotoMakerLoader

O nó PhotoMakerLoader carrega um modelo PhotoMaker dos arquivos de modelo disponíveis. Ele lê o arquivo de modelo especificado e prepara o codificador de ID do PhotoMaker para uso em tarefas de geração de imagens baseadas em identidade. Este nó está marcado como experimental e destina-se a fins de teste.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `photomaker_model_name` | O nome do arquivo de modelo PhotoMaker a ser carregado. As opções disponíveis são determinadas pelos arquivos de modelo presentes na pasta `photomaker`. | COMBO | Sim | Várias opções disponíveis (preenchidas dinamicamente a partir da pasta `photomaker`) |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `photomaker_model` | O modelo PhotoMaker carregado contendo o codificador de ID, pronto para uso em operações de codificação de identidade. | PHOTOMAKER |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PhotoMakerLoader/pt-BR.md)

---
**Source fingerprint (SHA-256):** `1b26630fadbdc144cd42ca7393f743b079ee7463deb9c8b31b628b5dc7432317`
