# Carregar Latent

O nó LoadLatent carrega representações latentes previamente salvas de arquivos `.latent` no diretório de entrada. Ele lê os dados do tensor latente do arquivo selecionado e aplica os ajustes de escala necessários antes de retornar os dados latentes para uso em outros nós.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `latent` | Seleciona qual arquivo `.latent` carregar entre os arquivos disponíveis no diretório de entrada | COMBO | Sim | Todos os arquivos `.latent` no diretório de entrada (lista dinâmica, ordenada alfabeticamente) |

Nota: A lista de arquivos disponíveis é gerada dinamicamente e inclui apenas arquivos que terminam em `.latent` e que estão presentes no diretório de entrada. Se o arquivo selecionado não existir mais, o nó o reporta como um arquivo latente inválido.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `LATENT` | Retorna os dados da representação latente carregados do arquivo selecionado como um tensor de ponto flutuante. Se o arquivo não contiver o marcador `latent_format_version_0`, o tensor é escalado por 1/0,18215 antes de ser retornado; arquivos que contêm o marcador são retornados na escala em que foram armazenados. | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadLatent/pt-BR.md)

---
**Source fingerprint (SHA-256):** `0938214361687a3a98e03878b8cbc0240100cbeacc0b157c4a299e59e7728a13`
