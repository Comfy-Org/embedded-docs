# Flux 3 Image

Flux 3 Image gera uma imagem com o FLUX 3 a partir de um prompt, ou edita e combina imagens de referência. Escreva o que você deseja como instrução, depois conecte até 10 imagens de referência e refira-se a elas no prompt como imagem 1, imagem 2 e assim por diante. O prompt é interpretado e expandido antes da geração, e o resultado é renderizado na proporção de aspecto e resolução escolhidas.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | O que gerar, ou a edição a ser feita. O prompt é interpretado e expandido antes da geração. Refira-se às imagens de referência conectadas como imagem 1, imagem 2 e assim por diante. (padrão: "") | STRING | Sim | 1 a 15000 caracteres |
| `images` | Slot expansível para imagens de referência; conecte até 10 no total. Cada imagem deve ter pelo menos 256x256 pixels, e sua proporção de aspecto não pode ser mais extrema que 64:1. | IMAGE | Não | 0 a 10 imagens |
| `bounding_boxes` | Caixas opcionais fornecidas pelo nó Create Bounding Boxes que posicionam objetos ou texto na saída. As posições são relativas à tela, então forneça ao nó a proporção de aspecto da saída. | ARRAY | Não | - |
| `aspect_ratio` | Proporção de aspecto da imagem gerada. "auto" segue a primeira imagem de referência, ou escolhe uma proporção a partir do prompt. (padrão: "auto") | COMBO | Sim | `"auto"`<br>`"21:9"`<br>`"2:1"`<br>`"16:9"`<br>`"3:2"`<br>`"7:5"`<br>`"4:3"`<br>`"5:4"`<br>`"1:1"`<br>`"4:5"`<br>`"3:4"`<br>`"5:7"`<br>`"2:3"`<br>`"9:16"`<br>`"1:2"`<br>`"9:21"` |
| `resolution` | Tamanho da saída na proporção de aspecto escolhida: 0.75K é cerca de 0,6 megapixels, 1K 1 MP, 1.5K 2,4 MP, 2K 4,2 MP, 4K 16,8 MP. (padrão: "2K") | COMBO | Sim | `"0.75K"`<br>`"1K"`<br>`"1.5K"`<br>`"2K"`<br>`"4K"` |
| `grounding` | Permite que o modelo pesquise o prompt com busca na web e de imagens antes de gerar. (padrão: True) | BOOLEAN | Sim | True<br>False |
| `safety_tolerance` | Tolerância de moderação, 0 é a mais rigorosa. (padrão: 4) | INT | Sim | 0 a 4 |
| `seed` | Semente para determinar se o nó deve ser executado novamente; o FLUX 3 escolhe sua própria semente, então os resultados reais são não determinísticos independentemente deste valor. (padrão: 42) | INT | Sim | 0 a 4294967295 |

`safety_tolerance` é uma entrada avançada, e `seed` inclui controles Control After Generate na interface.

As imagens de referência são carregadas antes do envio da solicitação. Um único slot pode conter um lote, e cada quadro de cada lote conta para o limite de 10 imagens.

As linhas de `bounding_boxes` são anexadas ao prompt, então o prompt e as descrições das caixas devem ter, juntos, 15000 caracteres ou menos.

O preço exibido depende de `resolution`: $0.05863 em 0.75K, $0.06864 em 1K, $0.1001 em 1.5K, $0.143 em 2K e $0.86801 em 4K.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `IMAGE` | A imagem gerada, baixada do resultado do FLUX 3. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Flux3ImageNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `f32a90887227f9ce9e6ed04a76cde452a70f36fb97d8c36d7c55140855c1f593`
