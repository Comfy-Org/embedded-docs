# Ideogram 4.5 Edição Precisa

## Entradas

A seleção de um `model` determina quais entradas aparecem. Ambos os modelos editam uma região por meio de `context_window`, mas o 4.6 recebe sua máscara em `mask`, enquanto o 4.5 a recebe em `context_window_mask`, e o 4.6 usa `"auto"` como padrão em vez de `"none"`.

### Entradas comuns

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `model` | Modelo a usar. `"ideogram-4.6"` lida com fontes maiores e regiões mais amplas; `"ideogram-4.5"` é o modelo anterior (padrão: `"ideogram-4.6"`). | DYNAMIC_COMBO | Sim | `"ideogram-4.6"`<br>`"ideogram-4.5"` |
| `images` | Slot expansível: a imagem 1 é a imagem a editar e as imagens 2 a 5 são referências opcionais (`image_1` ... `image_5`). Consulte-as no prompt como @Image1, @Image2, ...; uma entrada em lote conta uma vez por imagem. Cada imagem deve ter uma proporção entre 1:6 e 6:1, exceto que a imagem 1 não passa pela verificação de proporção enquanto uma janela de contexto estiver em uso. | IMAGE | Sim | 1 a 5 imagens |
| `prompt` | Instruções de edição. Suporta referências no estilo @Image1 para as imagens conectadas (padrão: string vazia). | STRING | Sim | 1 a 10000 caracteres |
| `quality` | Nível de qualidade. Níveis mais altos custam mais e demoram mais (padrão: `"medium"`). | COMBO | Sim | `"very_low"`<br>`"low"`<br>`"medium"`<br>`"high"` |
| `seed` | Semente para geração. As mesmas imagens, prompt, configurações e semente geram o mesmo resultado ou um resultado muito semelhante (padrão: 42). | INT | Sim | 0 a 2147483647 |

### Entradas do Ideogram 4.6

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `context_window` | Região da imagem 1 a editar. `"auto"` edita a região ao redor da máscara e mantém a imagem 1 em tamanho real, ou a imagem inteira quando nenhuma máscara está conectada; `"none"` edita a imagem inteira; `"custom"` edita a região de `context_window_bboxes` e mantém a imagem 1 em tamanho real (padrão: `"auto"`). | COMBO | Não | `"none"`<br>`"auto"`<br>`"custom"` |
| `context_window_bboxes` | Região da imagem 1 a editar, por exemplo, a saída de Create Bounding Boxes. Obrigatório quando `context_window` é `"custom"`; não usado caso contrário. Várias caixas são mescladas em uma única região, que é expandida para pelo menos 256 pixels por lado e uma proporção de 6:1. A região pode ter até 8192 pixels por lado e cerca de 16,7 MP (ex.: 4096x4096). | BOUNDING_BOX | Não | - |
| `mask` | O branco marca o que editar; a região de edição é posicionada ao redor dele. A máscara deve conter áreas brancas (editar) e pretas (manter). Ela é enviada sempre que estiver conectada, em todos os modos de `context_window`, e reduz o limite de imagens para 4 (consulte as restrições abaixo). | MASK | Não | - |

### Entradas do Ideogram 4.5

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `context_window` | Região da imagem 1 a editar. `"none"` edita a imagem inteira. `"auto"` edita uma região ao redor de `context_window_mask`, e `"custom"` edita a região de `context_window_bboxes`; ambos mantêm a imagem 1 em tamanho real e deixam o restante da imagem inalterado (padrão: `"none"`). | COMBO | Não | `"none"`<br>`"auto"`<br>`"custom"` |
| `context_window_bboxes` | Região da imagem 1 a editar, por exemplo, a saída de Create Bounding Boxes. Obrigatório quando `context_window` é `"custom"`; não usado caso contrário. A região pode ter até 4608 pixels por lado e cerca de 4 MP (ex.: 2048x2048). | BOUNDING_BOX | Não | - |
| `context_window_mask` | O branco marca o que editar; a região de edição é posicionada ao redor dele. Obrigatória quando `context_window` é `"auto"`; não usada caso contrário. A máscara deve conter áreas brancas (editar) e pretas (manter). | MASK | Não | - |

### Restrições dos parâmetros

- **Contagem de imagens:** pelo menos 1 e no máximo 5 imagens; uma entrada em lote conta uma vez por imagem. Sempre que uma máscara estiver conectada, no máximo 4 imagens são aceitas, ou seja, a imagem 1 e 3 referências.
- **Tamanho da saída:** o nó não tem entradas de tamanho, largura ou altura. Uma edição de região retorna a imagem completa no tamanho da imagem 1. Uma edição da imagem inteira retorna o tamanho da imagem 1 conforme enviada: no 4.6, uma imagem acima de 16,7 MP ou 8192 pixels por lado é reduzida primeiro, e no 4.5 o mesmo acontece acima de cerca de 4 MP ou 4608 pixels por lado.
- **Tamanho da origem da região:** com uma janela de contexto em uso, a imagem 1 pode ter até 8192x8192 pixels (cerca de 67 MP); origens maiores lançam um erro.
- **Limites da região:** uma região de `context_window_bboxes` pode ter até 8192 pixels por lado e cerca de 16,7 MP no 4.6, e até 4608 pixels por lado e cerca de 4 MP no 4.5. Caixas que ficam inteiramente fora da imagem 1 lançam um erro.
- **Tags do prompt:** `@ImageN` é correspondido sem diferenciar maiúsculas de minúsculas e não deve exceder o número de imagens conectadas; o prompt não pode ser composto apenas por espaços em branco e deve ter no máximo 10000 caracteres.
- **Limite de upload:** a imagem 1, a máscara e as referências juntas devem caber no upload de 50 MB do Ideogram; a imagem 1 é recodificada como JPEG quando necessário e o nó lança um erro se ela ainda não couber.
- **Segurança de conteúdo:** se o filtro de segurança de conteúdo do Ideogram bloquear o resultado, o nó lança um erro em vez de retornar uma imagem.

## Saídas

| Nome da saída | Descrição | Tipo de dados |
|-------------|-------------|-----------|
| `IMAGE` | A imagem editada como lote, no tamanho da imagem 1. Uma edição de imagem inteira no 4.6 volta menor quando a fonte passa de 16.7 MP ou 8192 pixels por lado. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/IdeogramPreciseEditApi/pt-BR.md)

---
**Source fingerprint (SHA-256):** `84f042739a8d7bc1a4b268f6175be6a598b67d32b9311fdf204a923472f5fcc9`
