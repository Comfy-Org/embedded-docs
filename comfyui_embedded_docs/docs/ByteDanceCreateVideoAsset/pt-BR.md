> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceCreateVideoAsset/pt-BR.md)

Este nó cria um ativo de vídeo pessoal para o Seedance 2.0. Ele faz upload do seu vídeo de entrada e o registra em um grupo de ativos especificado. Se você não fornecer um ID de grupo, ele o guiará por um processo de verificação de pessoa real no seu navegador para criar um novo grupo primeiro.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|---------------|-------------|-----------|-----------|
| `video` | VIDEO | Sim | - | Vídeo a ser registrado como ativo pessoal. |
| `group_id` | STRING | Não | - | Reutiliza um ID de grupo de ativos Seedance existente para evitar verificação humana repetida para a mesma pessoa. Deixe vazio para executar a autenticação de pessoa real no navegador e criar um novo grupo. (padrão: string vazia) |

**Restrições do Vídeo:**
*   **Duração:** Deve estar entre 2 e 15 segundos.
*   **Dimensões:** Largura e altura devem estar entre 300 e 6000 pixels.
*   **Proporção de Aspecto:** A proporção largura/altura deve estar entre 0,4 e 2,5.
*   **Total de Pixels:** O número total de pixels (largura × altura) deve estar entre 409.600 e 927.408.
*   **Taxa de Quadros:** Deve estar entre 24 e 60 quadros por segundo (FPS).

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|---------------|---------------|-----------|
| `asset_id` | STRING | O identificador único para o ativo de vídeo recém-criado. |
| `group_id` | STRING | O identificador do grupo de ativos que contém o novo vídeo. Será o `group_id` fornecido ou um recém-criado. |

---
**Source fingerprint (SHA-256):** `9da0872cf8df32765e3fb1eef50bc24f53b65e069d8ef2609de1075d89edd605`
