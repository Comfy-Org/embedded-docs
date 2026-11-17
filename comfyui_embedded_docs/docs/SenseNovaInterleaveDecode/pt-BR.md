# SenseNova Interleave Decode

Converta o histórico de intercalação deixado pelo SenseNova Conditioning em texto, imagens e raciocínio utilizáveis. Execute-o ao final do loop, com o parâmetro End Loop accumulate desativado, para coletar tudo o que o modelo produziu em uma única passagem.

## Entradas

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `clip` | Modelo CLIP SenseNova usado para decodificar os tokens gerados. | CLIP | Sim | - |
| `conditioning` | Condicionamento de intercalação do SenseNova Conditioning. | CONDITIONING | Sim | - |
| `samples` | Último latente de pixel do KSampler, necessário quando o loop terminou em uma solicitação de imagem. | LATENT | Não | - |

**Restrições e comportamento:**

* O condicionamento deve vir do SenseNova Conditioning na tarefa `interleave` ou `self-correction`; qualquer outra coisa gera um erro.
* Quando o modelo estiver aguardando uma imagem, conecte a saída LATENT do sampler a `samples`.
* Imagens de referência conectadas no início da execução são excluídas da saída, e os consumidores de imagem são ignorados quando nenhuma imagem foi gerada.

## Saídas

| Nome da saída | Descrição | Tipo de dados |
|-------------|-------------|-----------|
| `text` | Texto decodificado do histórico de intercalação, com marcadores de imagem substituídos por linhas em branco. | STRING |
| `images` | As imagens que o modelo gerou durante a execução. | IMAGE |
| `thinking` | O texto de raciocínio do modelo, quando ele produziu um. | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SenseNovaInterleaveDecode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `62c7ded50c1348e2242319209729a17d543d80e4d01ddf173cf8b77e4fd0be50`
