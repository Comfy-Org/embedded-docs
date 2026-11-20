# Ideogram 4.5 Edição Precisa

Edite uma imagem guiada por um prompt de texto com a edição precisa do Ideogram 4.6 ou 4.5: apenas o que o prompt solicita é alterado. Uma edição de região mantém a imagem 1 em seu tamanho e resolução exatos. Uma edição da imagem inteira reduz a escala da imagem 1 antes do upload quando ela está acima do limite do modelo, então o resultado pode ser menor que a entrada: 16,7 MP ou 8192 pixels por lado no 4.6, cerca de 4 MP ou 4608 pixels por lado no 4.5. A imagem 1 é a imagem a ser editada e até 4 imagens adicionais podem ser conectadas como referências. Uma única região da imagem 1 também pode ser editada isoladamente, selecionada por uma máscara ou por caixas delimitadoras, o que retorna a imagem em tamanho integral.

## Entradas

Selecionar um `model` determina quais entradas aparecem. Ambos os modelos editam uma região por meio de `context_window`, mas o 4.6 recebe sua máscara em `mask`, enquanto o 4.5 a recebe em `context_window_mask`, e o 4.6 usa `"auto"` como padrão em vez de `"none"`.

### Entradas comuns

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `model` | Modelo a usar. `"ideogram-4.6"` lida com origens maiores e regiões mais amplas; `"ideogram-4.5"` é o modelo anterior (padrão: `"ideogram-4.6"`). | DYNAMIC_COMBO | Sim | `"ideogram-4.6"`<br>`"ideogram-4.5"` |
| `images` | Slot expansível: a imagem 1 é a imagem a ser editada e as imagens 2 a 5 são referências opcionais (`image_1` ... `image_5`). Consulte-as no prompt como @Image1, @Image2, ...; uma entrada em lote conta uma vez por imagem. Cada imagem deve ter uma proporção entre 1:6 e 6:1, exceto que a imagem 1 não é verificada quanto à proporção enquanto uma janela de contexto estiver em uso. | IMAGE | Sim | 1 a 5 imagens |
| `prompt` | Instruções de edição. Suporta referências no estilo @Image1 para as imagens conectadas (padrão: string vazia). | STRING | Sim | 1 a 10000 caracteres |
| `quality` | Nível de qualidade. Níveis mais altos custam mais e demoram mais (padrão: `"medium"`). | COMBO | Sim | `"very_low"`<br>`"low"`<br>`"medium"`<br>`"high"` |
| `seed` | Semente para geração. No 4.6, as mesmas imagens, o mesmo prompt, as mesmas configurações e a mesma semente fornecem o mesmo resultado ou um resultado muito semelhante; no 4.5, fornecem o mesmo resultado (padrão: 42). | INT | Sim | 0 a 2147483647 |

### Entradas do Ideogram 4.6

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `context_window` | Região da imagem 1 a editar. `"auto"` edita a região ao redor da máscara e mantém a imagem 1 em tamanho integral, ou a imagem inteira quando nenhuma máscara está conectada; `"none"` edita a imagem inteira; `"custom"` edita a região definida por `context_window_bboxes` e mantém a imagem 1 em tamanho integral (padrão: `"auto"`). Um `mask` conectado é enviado nos três modos, incluindo `"none"`. | COMBO | Não | `"none"`<br>`"auto"`<br>`"custom"` |
| `context_window_bboxes` | Região da imagem 1 a editar, por exemplo, a saída de Create Bounding Boxes. Obrigatório quando `context_window` é `"custom"`; não é usado caso contrário. Várias caixas são mescladas em uma única região, que é expandida para pelo menos 256 pixels por lado e esticada mais apenas quando necessário para permanecer dentro da proporção máxima de 6:1. A região pode ter até 8192 pixels por lado e cerca de 16,7 MP (por exemplo, 4096x4096); a área é verificada após cada lado ser arredondado para cima para um múltiplo de 32, então uma região de 4097x4095 é rejeitada mesmo que sua área bruta esteja abaixo de 16,7 MP. | BOUNDING_BOX | Não | - |
| `mask` | As áreas brancas marcam o que editar; a região de edição é posicionada ao redor delas. A máscara deve conter áreas brancas (editar) e pretas (manter). Ela é enviada sempre que estiver conectada, em todos os modos de `context_window`, e reduz o limite de imagens para 4 (consulte as restrições abaixo). | MASK | Não | - |

### Entradas do Ideogram 4.5

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `context_window` | Região da imagem 1 a editar. `"none"` edita a imagem inteira. `"auto"` edita uma região ao redor de `context_window_mask` e `"custom"` a região definida por `context_window_bboxes`; ambos mantêm a imagem 1 em tamanho integral e deixam o restante da imagem inalterado (padrão: `"none"`). | COMBO | Não | `"none"`<br>`"auto"`<br>`"custom"` |
| `context_window_bboxes` | Região da imagem 1 a editar, por exemplo, a saída de Create Bounding Boxes. Obrigatório quando `context_window` é `"custom"`; não é usado caso contrário. Várias caixas são mescladas em uma única região, que é expandida para pelo menos 256 pixels por lado e esticada mais apenas quando necessário para permanecer dentro da proporção máxima de 6:1, então uma caixa pequena como 32x32 também edita os pixels ao redor. A região pode ter até 4608 pixels por lado e cerca de 4 MP (por exemplo, 2048x2048), verificada após cada lado ser arredondado para cima para um múltiplo de 32. | BOUNDING_BOX | Não | - |
| `context_window_mask` | As áreas brancas marcam o que editar; a região de edição é posicionada ao redor delas. Obrigatório quando `context_window` é `"auto"`; não é usado caso contrário. A máscara deve conter áreas brancas (editar) e pretas (manter). | MASK | Não | - |

### Restrições de parâmetros

- **Contagem de imagens:** pelo menos 1 e no máximo 5 imagens; uma entrada em lote conta uma vez por imagem. Quando o nó usa uma máscara, no máximo 4 imagens são aceitas, ou seja, a imagem 1 e 3 referências. No 4.6, um `mask` conectado é usado em todos os modos; no 4.5, a máscara é `context_window_mask` e é usada apenas em `"auto"`, então `"none"` e `"custom"` ainda aceitam 5 imagens com uma máscara conectada.
- **Tamanho da saída:** o nó não tem entradas de tamanho, largura ou altura. Uma edição de região retorna a imagem completa no tamanho da imagem 1. Uma edição da imagem inteira retorna o tamanho da imagem 1 conforme enviada: no 4.6, uma imagem acima de 16,7 MP ou 8192 pixels por lado é reduzida primeiro; no 4.5, o mesmo ocorre acima de cerca de 4 MP ou 4608 pixels por lado.
- **Tamanho da origem da região:** com uma janela de contexto em uso, a imagem 1 pode ter até 67.108.864 pixels no total (cerca de 67 MP), por exemplo 8192x8192 ou 10000x5000; o limite é sobre a área, não sobre um lado.
- **Limites da região:** uma região de `context_window_bboxes` pode ter até 8192 pixels por lado e cerca de 16,7 MP no 4.6, e até 4608 pixels por lado e cerca de 4 MP no 4.5. As caixas geram erro somente quando a região mesclada fica fora da imagem 1, então uma caixa à esquerda da imagem e outra à direita dela se mesclam em uma região que abrange a imagem.
- **Tags do prompt:** `@ImageN` é correspondido sem diferenciar maiúsculas de minúsculas e não deve exceder o número de imagens conectadas; o prompt não pode ser vazio nem conter apenas espaços em branco e deve ter no máximo 10000 caracteres.
- **Limite de upload:** a imagem 1, a máscara e as referências juntas devem caber no upload de 50 MB do Ideogram. Uma edição no 4.6 e uma edição de região no 4.5 recodificam a imagem 1 como JPEG quando os arquivos não cabem e geram um erro se ainda não couberem; uma edição da imagem inteira no 4.5 sempre envia PNG e não tem esse recurso alternativo.
- **Segurança de conteúdo:** se o filtro de segurança de conteúdo do Ideogram bloquear o resultado, o nó gera um erro em vez de retornar uma imagem.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `IMAGE` | A imagem editada como um lote, no tamanho da imagem 1. Uma edição da imagem inteira retorna menor quando a origem está acima do orçamento de upload: 16,7 MP ou 8192 pixels por lado no 4.6, cerca de 4 MP ou 4608 pixels por lado no 4.5. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/IdeogramPreciseEditApi/pt-BR.md)

---
**Source fingerprint (SHA-256):** `84f042739a8d7bc1a4b268f6175be6a598b67d32b9311fdf204a923472f5fcc9`
