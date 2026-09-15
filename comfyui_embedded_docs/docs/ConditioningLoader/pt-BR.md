# Carregar Condicionamento

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `conditioning_name` | O arquivo a ser carregado da pasta embeddings. A lista de opções é criada a partir dos arquivos disponíveis atualmente nessa pasta. | COMBO | Sim | Todos os arquivos na pasta embeddings |

**Observação:** O arquivo selecionado deve conter um tensor `conditioning`. Quaisquer chaves adicionais armazenadas no arquivo são restauradas: chaves numeradas (por exemplo, `key.0`, `key.1`) são agrupadas novamente em listas ordenadas, e outras chaves são restauradas como opções simples. Opções extras são lidas dos metadados `conditioning_options` do arquivo, quando presentes.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `CONDITIONING` | O condicionamento carregado do arquivo, juntamente com as opções restauradas. | CONDITIONING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningLoader/pt-BR.md)

---
**Source fingerprint (SHA-256):** `08fc58bcaa2309fcf03d4e4cc634b930aaf6ccf8097181fd3d45924abda144eb`
