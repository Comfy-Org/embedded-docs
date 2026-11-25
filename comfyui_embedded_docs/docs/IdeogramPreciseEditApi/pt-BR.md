# Ideogram 4.5 Edição Precisa

Edite uma imagem guiada por um prompt de texto com a edição precisa do Ideogram 4.6 ou 4.5: apenas o que o prompt solicita é alterado. Uma edição de região mantém a imagem 1 no tamanho e na resolução exatos. Uma edição da imagem inteira reduz a imagem 1 antes do upload quando ela está acima do limite do modelo, portanto o resultado pode ser menor que a entrada: 16,7 MP ou 8192 pixels por lado no 4.6, cerca de 4 MP ou 4608 pixels por lado no 4.5. A imagem 1 é a imagem a ser editada, e até 4 imagens adicionais podem ser conectadas como referências. Uma única região da imagem 1 também pode ser editada isoladamente, selecionada por uma máscara ou por caixas delimitadoras, o que retorna a imagem em tamanho total.

## Entradas

A seleção de um `model` determina quais entradas aparecem. Ambos os modelos editam uma região por meio de `context_window`, mas o 4.6 recebe sua máscara em `mask`, enquanto o 4.5 a recebe em `context_window_mask`, e o 4.6 usa `"auto"` como padrão em vez de `"none"`.

### Entradas comuns

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `modelo` | Modelo a usar. `"ideogram-4.6"` lida com fontes maiores e regiões mais amplas; `"ideogram-4.5"` é o modelo anterior (padrão: `"ideogram-4.6"`). | DYNAMIC_COMBO | Sim | `"ideogram-4.6"`<br>`"ideogram-4.5"` |
| `images` | Slot expansível: a imagem 1 é a imagem a ser editada, e as imagens 2 a 5 são referências opcionais (`image_1` ... `image_5`). Refira-se a elas no prompt como @Image1, @Image2, ...; uma entrada em lote conta uma vez por imagem. Cada imagem deve ter uma proporção entre 1:6 e 6:1, exceto que a imagem 1 não passa por verificação de proporção enquanto uma janela de contexto estiver em uso. | IMAGE | Sim | 1 a 5 imagens |
| `prompt` | Instruções de edição. Oferece suporte a referências no estilo @Image1 para as imagens conectadas (padrão: string vazia). | STRING | Sim | 1 a 10000 caracteres |
| `quality` | Nível de qualidade. Níveis mais altos custam mais e demoram mais (padrão: `"medium"`). | COMBO | Sim | `"very_low"`<br>`"low"`<br>`"medium"`<br>`"high"` |
| `seed` | Semente para geração. No 4.6, as mesmas imagens, o mesmo prompt, as mesmas configurações e a mesma semente produzem o mesmo resultado ou um resultado muito semelhante; no 4.5, produzem o mesmo resultado (padrão: 42). | INT | Sim | 0 a 2147483647 |

### Entradas do Ideogram 4.6

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `context_window` | Região da imagem 1 a ser editada. `"auto"` edita a região ao redor da máscara e mantém a imagem 1 em tamanho total, ou a imagem inteira quando nenhuma máscara está conectada; `"none"` edita a imagem inteira; `"custom"` edita a região de `context_window_bboxes` e mantém a imagem 1 em tamanho total (padrão: `"auto"`). Uma `mask` conectada é enviada nos três modos, incluindo `"none"`. | COMBO | Não | `"none"`<br>`"auto"`<br>`"custom"` |
| `context_window_bboxes` | Região da imagem 1 a ser editada, por exemplo, a saída do nó Create Bounding Boxes. Obrigatório quando `context_window` é `"custom"`; não é usado de outra forma. Várias caixas são mescladas em uma única região, que é ampliada para pelo menos 256 pixels por lado e ampliada ainda mais apenas quando necessário para permanecer dentro da proporção máxima de 6:1. A região pode ter até 8192 pixels por lado e cerca de 16,7 MP (por exemplo, 4096x4096); a área é verificada após cada lado ser arredondado para cima até um múltiplo de 32, então uma região de 4097x4095 é rejeitada mesmo que sua área bruta esteja abaixo de 16,7 MP. | BOUNDING_BOX | Não | - |
| `mask` | O branco marca o que editar; a região de edição é posicionada ao redor dele. A máscara deve conter áreas brancas (editar) e pretas (manter). Ela é enviada sempre que estiver conectada, em todos os modos de `context_window`, e reduz o limite de imagens para 4 (consulte as restrições abaixo). | MASK | Não | - |

### Entradas do Ideogram 4.5

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `context_window` | Região da imagem 1 a ser editada. `"none"` edita a imagem inteira. `"auto"` edita uma região ao redor de `context_window_mask`, e `"custom"`, a região de `context_window_bboxes`; ambos mantêm a imagem 1 em tamanho total e deixam o restante da imagem inalterado (padrão: `"none"`). | COMBO | Não | `"none"`<br>`"auto"`<br>`"custom"` |
| `context_window_bboxes` | Região da imagem 1 a ser editada, por exemplo, a saída do nó Create Bounding Boxes. Obrigatório quando `context_window` é `"custom"`; não é usado de outra forma. Várias caixas são mescladas em uma única região, que é ampliada para pelo menos 256 pixels por lado e ampliada ainda mais apenas quando necessário para permanecer dentro da proporção máxima de 6:1, então uma caixa pequena como 32x32 também edita os pixels ao seu redor. A região pode ter até 4608 pixels por lado e cerca de 4 MP (por exemplo, 2048x2048), verificada após cada lado ser arredondado para cima até um múltiplo de 32. | BOUNDING_BOX | Não | - |
| `context_window_mask` | O branco marca o que editar; a região de edição é posicionada ao redor dele. Obrigatório quando `context_window` é `"auto"`; não é usado de outra forma. A máscara deve conter áreas brancas (editar) e pretas (manter). | MASK | Não | - |

### Restrições de parâmetros

- **Contagem de imagens:** pelo menos 1 e no máximo 5 imagens; uma entrada em lote conta uma vez por imagem. Quando o nó usa uma máscara, no máximo 4 imagens são aceitas, ou seja, a imagem 1 e 3 referências. No 4.6, uma `mask` conectada é usada em todos os modos; no 4.5, a máscara é `context_window_mask` e é usada apenas em `"auto"`, portanto `"none"` e `"custom"` ainda aceitam 5 imagens com uma máscara conectada.
- **Tamanho da saída:** o nó não tem entradas de tamanho, largura ou altura. Uma edição de região retorna a imagem completa no tamanho da imagem 1. Uma edição da imagem inteira retorna o tamanho da imagem 1 conforme enviada: no 4.6, uma imagem acima de 16,7 MP ou 8192 pixels por lado é reduzida primeiro, e no 4.5 o mesmo acontece acima de cerca de 4 MP ou 4608 pixels por lado, e sua área é medida após cada lado ser arredondado para cima até um múltiplo de 32, então uma imagem logo abaixo de 4 MP, como 2049x2047, também é reduzida.
- **Tamanho da origem da região:** com uma janela de contexto em uso, a imagem 1 pode ter até 67.108.864 pixels no total (cerca de 67 MP), por exemplo, 8192x8192 ou 10000x5000; o limite é sobre a área, não sobre um lado.
- **Limites de região:** uma região de `context_window_bboxes` pode ter até 8192 pixels por lado e cerca de 16,7 MP no 4.6, e até 4608 pixels por lado e cerca de 4 MP no 4.5. As caixas geram um erro quando a região mesclada fica fora da imagem 1 ou excede o limite de lado, área ou proporção 6:1 do modelo, então uma caixa de 4096x4096 falha no 4.5 mesmo dentro de uma imagem 8192x8192. Uma caixa à esquerda da imagem e outra à direita dela são mescladas em uma região que abrange a imagem, o que é aceitável.
- **Tags no prompt:** `@ImageN` é correspondido sem diferenciar maiúsculas de minúsculas e não deve exceder o número de imagens conectadas; o prompt não pode conter apenas espaços em branco e deve ter no máximo 10000 caracteres.
- **Limite de upload:** a imagem 1, a máscara e as referências juntas devem caber no upload de 50 MB do Ideogram. Uma edição no 4.6 e uma edição de região no 4.5 recodificam a imagem 1 como JPEG quando os arquivos não cabem e geram um erro se ainda assim não couberem; uma edição da imagem inteira no 4.5 sempre envia PNG e não tem esse mecanismo alternativo.
- **Segurança de conteúdo:** se o filtro de segurança de conteúdo do Ideogram bloquear o resultado, o nó gera um erro em vez de retornar uma imagem.

## Saídas

| Nome da saída | Descrição | Tipo de dados |
|-------------|-------------|-----------|
| `IMAGE` | A imagem editada como um lote, no tamanho da imagem 1. Uma edição da imagem inteira retorna menor quando a origem está acima do limite de upload: 16,7 MP ou 8192 pixels por lado no 4.6, cerca de 4 MP ou 4608 pixels por lado no 4.5. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/IdeogramPreciseEditApi/pt-BR.md)

---
**Source fingerprint (SHA-256):** `9218070f5e55b3bd8da0701d4b4ea969cb7b1c2ebfc06669a523e64ce4bcf342`
