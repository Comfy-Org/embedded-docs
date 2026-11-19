# Ideogram 4.5 Edição Precisa

Edite uma imagem guiada por um prompt de texto com a edição precisa do Ideogram 4.6 ou 4.5: apenas o que o prompt pede é alterado, os pixels não tocados permanecem idênticos, e a saída mantém o tamanho da imagem 1. A imagem 1 é a imagem a ser editada, e até 4 imagens adicionais podem ser conectadas como referências. Uma única região da imagem 1 também pode ser editada isoladamente, selecionada por uma máscara ou por caixas delimitadoras, o que retorna a imagem no tamanho original.

## Entradas

Selecionar um `model` determina quais entradas aparecem. Ambos os modelos editam uma região por meio de `context_window`, mas o 4.6 recebe sua máscara em `mask`, enquanto o 4.5 a recebe em `context_window_mask`, e o 4.6 usa `"auto"` por padrão em vez de `"none"`.

### Entradas comuns

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `model` | Modelo a usar. `"ideogram-4.6"` lida com fontes maiores e regiões mais amplas; `"ideogram-4.5"` é o modelo anterior (padrão: `"ideogram-4.6"`). | DYNAMIC_COMBO | Sim | `"ideogram-4.6"`<br>`"ideogram-4.5"` |
| `images` | Slot expansível: a imagem 1 é a imagem a ser editada e as imagens 2 a 5 são referências opcionais (`image_1` ... `image_5`). Refira-se a elas no prompt como @Image1, @Image2, ...; uma entrada em lote conta uma vez por imagem. Cada imagem deve ter uma proporção entre 1:6 e 6:1, exceto que a imagem 1 não passa pela verificação de proporção enquanto uma janela de contexto estiver em uso. | IMAGE | Sim | 1 a 5 imagens |
| `prompt` | Instruções de edição. Suporta referências no estilo @Image1 para as imagens conectadas (padrão: string vazia). | STRING | Sim | 1 a 10000 caracteres |
| `quality` | Nível de qualidade. Níveis mais altos custam mais e demoram mais (padrão: `"medium"`). | COMBO | Sim | `"very_low"`<br>`"low"`<br>`"medium"`<br>`"high"` |
| `seed` | Semente para geração. As mesmas imagens, prompt, configurações e semente produzem o mesmo resultado (padrão: 42). | INT | Sim | 0 a 2147483647 |

### Entradas do Ideogram 4.6

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `context_window` | Região da imagem 1 a editar. `"auto"` edita ao redor de `mask` e mantém a imagem 1 no tamanho original, ou a imagem inteira quando nenhuma máscara está conectada; `"none"` edita a imagem inteira mesmo com uma máscara; `"custom"` edita a região de `context_window_bboxes` e mantém a imagem 1 no tamanho original. Edições da imagem inteira reduzem primeiro imagens acima de 16.7 MP ou 8192 pixels por lado (padrão: `"auto"`). | COMBO | Não | `"none"`<br>`"auto"`<br>`"custom"` |
| `context_window_bboxes` | Região da imagem 1 a editar, por exemplo, a saída de Create Bounding Boxes. Obrigatório quando `context_window` é `"custom"`; não usado de outra forma. Várias caixas são mescladas em uma região, que é expandida para pelo menos 256 pixels por lado e uma proporção de 6:1. A região pode ter até 8192 pixels por lado e cerca de 16.7 MP (por exemplo, 4096x4096). | BOUNDING_BOX | Não | - |
| `mask` | As áreas brancas marcam o que editar; a região de edição é posicionada ao redor delas. A máscara deve conter áreas brancas (editar) e pretas (manter). Usada apenas quando `context_window` é `"auto"`. | MASK | Não | - |

### Entradas do Ideogram 4.5

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `context_window` | Região da imagem 1 a editar. `"none"` edita a imagem inteira. `"auto"` edita uma região ao redor de `context_window_mask` e `"custom"` a região de `context_window_bboxes`; ambos mantêm a imagem 1 no tamanho original e deixam o restante da imagem inalterado (padrão: `"none"`). | COMBO | Não | `"none"`<br>`"auto"`<br>`"custom"` |
| `context_window_bboxes` | Região da imagem 1 a editar, por exemplo, a saída de Create Bounding Boxes. Obrigatório quando `context_window` é `"custom"`; não usado de outra forma. A região pode ter até 4608 pixels por lado e cerca de 4 MP (por exemplo, 2048x2048). | BOUNDING_BOX | Não | - |
| `context_window_mask` | As áreas brancas marcam o que editar; a região de edição é posicionada ao redor delas. Obrigatório quando `context_window` é `"auto"`; não usado de outra forma. A máscara deve conter áreas brancas (editar) e pretas (manter). | MASK | Não | - |

### Restrições de parâmetros

- **Contagem de imagens:** pelo menos 1 e no máximo 5 imagens; uma entrada em lote conta uma vez por imagem. Com uma máscara, no máximo 4 imagens são aceitas, ou seja, a imagem 1 e 3 referências.
- **Tamanho da saída:** o resultado mantém o tamanho da imagem 1, portanto este nó não tem entradas de tamanho, largura ou altura. No 4.6, uma imagem acima de 16.7 MP ou 8192 pixels por lado é reduzida primeiro; no 4.5, o mesmo acontece acima de cerca de 4 MP ou 4608 pixels por lado.
- **Tamanho da fonte da região:** com uma janela de contexto em uso, a imagem 1 pode ter até 8192x8192 pixels (cerca de 67 MP); fontes maiores geram um erro.
- **Limites da região:** uma região de `context_window_bboxes` pode ter até 8192 pixels por lado e cerca de 16.7 MP no 4.6, e até 4608 pixels por lado e cerca de 4 MP no 4.5. Caixas que ficam inteiramente fora da imagem 1 geram um erro.
- **Tags do prompt:** `@ImageN` é correspondida sem diferenciar maiúsculas de minúsculas e não deve exceder o número de imagens conectadas; o prompt deve conter algo além de espaços em branco e ter no máximo 10000 caracteres.
- **Limite de upload:** a imagem 1, a máscara e as referências juntas devem caber no upload de 50 MB do Ideogram; a imagem 1 é recodificada como JPEG quando necessário, e o nó gera um erro se ela ainda não couber.
- **Segurança de conteúdo:** se o filtro de segurança de conteúdo do Ideogram bloquear o resultado, o nó gera um erro em vez de retornar uma imagem.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `IMAGE` | A imagem editada como um lote, no tamanho da imagem 1. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/IdeogramPreciseEditApi/pt-BR.md)

---
**Source fingerprint (SHA-256):** `84f042739a8d7bc1a4b268f6175be6a598b67d32b9311fdf204a923472f5fcc9`
