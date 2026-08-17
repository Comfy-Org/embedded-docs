# Carregar Latent

---

O nó LoadLatent carrega representações latentes que foram salvas anteriormente como arquivos .latent no diretório de entrada. Ele lê os dados do tensor latente do arquivo selecionado e aplica os ajustes de escala necessários antes de retornar os resultados para uso em outros nós.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `latent` | Seleciona qual arquivo .latent carregar entre os arquivos disponíveis no diretório de entrada | COMBO | Sim | Todos os arquivos .latent no diretório de entrada |

Observação: Para arquivos .latent que não contêm o marcador `latent_format_version_0`, o tensor latente carregado é multiplicado por 1/0.18215 para que sua escala corresponda ao formato esperado pelos outros nós.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `LATENT` | Retorna os dados da representação latente carregados do arquivo selecionado | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadLatent/pt-BR.md)

---
**Source fingerprint (SHA-256):** `0938214361687a3a98e03878b8cbc0240100cbeacc0b157c4a299e59e7728a13`
