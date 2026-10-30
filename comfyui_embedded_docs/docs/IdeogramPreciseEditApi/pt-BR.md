# Ideogram 4.5 Edição Precisa

Edite uma imagem guiado por um prompt de texto com a edição precisa do Ideogram 4.5: apenas o que o prompt solicita é alterado, os pixels não tocados permanecem idênticos e a saída mantém o tamanho da imagem 1. A imagem 1 é a imagem a ser editada e até 4 imagens adicionais podem ser conectadas como referências. Uma única região da imagem 1 também pode ser editada isoladamente, selecionada por uma máscara ou por caixas delimitadoras, o que retorna a imagem em tamanho total.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `modelo` | Modelo a usar. (padrão: `"ideogram-4.5"`) | DYNAMIC_COMBO | Sim | `"ideogram-4.5"` |
| `images` | Slot expansível: a imagem 1 é a imagem a ser editada e as imagens 2 a 5 são referências opcionais (`image_1` ... `image_5`). Refira-se a elas no prompt como @Image1, @Image2, ...; uma entrada em lote conta uma vez por imagem. Cada imagem deve ter uma proporção de aspecto entre 1:6 e 6:1, exceto que a imagem 1 não é verificada quanto à proporção enquanto uma janela de contexto estiver em uso. | IMAGE | Sim | 1 a 5 imagens |
| `prompt` | Instruções de edição. Suporta referências no estilo @Image1 para as imagens conectadas. (padrão: string vazia) | STRING | Sim | 1 a 10000 caracteres |
| `quality` | Nível de qualidade. Níveis mais altos custam mais e demoram mais. (padrão: `"medium"`) | COMBO | Sim | `"very_low"`<br>`"low"`<br>`"medium"`<br>`"high"` |
| `seed` | Semente para geração. As mesmas imagens, prompt, configurações e semente produzem o mesmo resultado. (padrão: 42) | INT | Sim | 0 a 2147483647 |
| `context_window` | Região da imagem 1 a ser editada. `"none"` edita a imagem inteira. `"auto"` edita uma região ao redor de `context_window_mask` e `"custom"` a região de `context_window_bboxes`; ambos mantêm a imagem 1 em tamanho total e deixam o restante da imagem inalterado. (padrão: `"none"`) | COMBO | Não | `"none"`<br>`"auto"`<br>`"custom"` |
| `context_window_bboxes` | Região da imagem 1 a ser editada, por exemplo, a saída de Create Bounding Boxes. Obrigatório quando `context_window` é `"custom"`; não usado caso contrário. Várias caixas são mescladas em uma região, que é expandida para pelo menos 256 pixels por lado e uma proporção de aspecto de 6:1. A região pode ter até 4608 pixels por lado e cerca de 4 MP (por exemplo, 2048x2048). | BOUNDING_BOX | Não | - |
| `context_window_mask` | As áreas brancas indicam o que editar; a região de edição é posicionada ao redor delas. Obrigatório quando `context_window` é `"auto"`; não usado caso contrário. A máscara deve conter áreas brancas (editar) e pretas (manter). | MASK | Não | - |

### Restrições dos parâmetros

- **Contagem de imagens:** pelo menos 1 e no máximo 5 imagens; uma entrada em lote conta uma vez por imagem. A imagem 1 é a imagem a ser editada e as imagens 2 a 5 são referências. Com `context_window_mask`, no máximo 4 imagens são aceitas, ou seja, a imagem 1 e 3 referências.
- **Tamanho da saída:** o resultado mantém o tamanho da imagem 1, portanto este nó não tem entradas de tamanho, largura ou altura. Isso também vale quando uma região é editada, caso em que a imagem completa retorna com apenas a região alterada.
- **Proporção de aspecto da imagem:** cada imagem não pode ser mais larga que 6x sua altura nem mais alta que 6x sua largura (entre 1:6 e 6:1). A imagem 1 fica isenta enquanto `context_window` for `"auto"` ou `"custom"`, porque apenas sua região selecionada é enviada.
- **Tamanho da origem da região:** com uma janela de contexto em uso, a imagem 1 pode ter até 8192x8192 pixels (cerca de 67 MP); origens maiores geram um erro. Sem uma janela de contexto, imagens maiores que cerca de 4 MP ou 4608 px no lado maior são reduzidas antes de serem enviadas.
- **Limites da região:** uma região de `context_window_bboxes` pode ter até 4608 pixels por lado e cerca de 4 MP; caixas que ficam inteiramente fora da imagem 1 geram um erro.
- **Tags de prompt:** `@ImageN` é correspondido sem diferenciar maiúsculas de minúsculas e não deve exceder o número de imagens conectadas; o prompt não pode ser composto apenas de espaços em branco e deve ter no máximo 10000 caracteres.
- **Limite de upload:** a imagem 1, a máscara e as referências juntas devem caber no upload de 50 MB do Ideogram; a imagem 1 é recodificada como JPEG quando necessário e o nó gera um erro se ainda assim não couber.
- **Segurança de conteúdo:** se o filtro de segurança de conteúdo do Ideogram bloquear o resultado, o nó gera um erro em vez de retornar uma imagem.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `IMAGE` | A imagem editada como um lote, no tamanho da imagem 1. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/IdeogramPreciseEditApi/pt-BR.md)

---
**Source fingerprint (SHA-256):** `84f042739a8d7bc1a4b268f6175be6a598b67d32b9311fdf204a923472f5fcc9`
