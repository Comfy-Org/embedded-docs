# Ideogram Vector Generate SVG

Este nó gera um SVG editável a partir de um prompt de texto com o Ideogram Vector, opcionalmente guiado por até 5 imagens de referência. O resultado é uma marcação vetorial, e não uma imagem raster, portanto as formas permanecem editáveis em um editor vetorial.

## Entradas

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `model` | Modelo a usar. Padrão: `"ideogram-vector-1"`. | DYNAMIC_COMBO | Sim | `"ideogram-vector-1"` |
| `images` | Imagens de referência opcionais. A imagem 1 é a fonte principal e as imagens 2 a 5 são referências extras; mencione-as no prompt como `@Image1`, `@Image2` e assim por diante. Uma entrada em lote conta uma vez por imagem. | AUTOGROW | Não | 0 a 5 imagens |
| `prompt` | Descrição do SVG. Suporta referências no estilo `@Image1` às imagens de entrada. | STRING | Sim | 1 a 9500 caracteres |
| `aspect_ratio` | `"auto"` segue a imagem 1 ou o prompt quando nenhuma imagem está conectada. Padrão: `"auto"`. | COMBO | Sim | `"auto"`<br>`"1:3"`<br>`"1:2"`<br>`"9:16"`<br>`"10:16"`<br>`"2:3"`<br>`"3:4"`<br>`"4:5"`<br>`"1:1"`<br>`"5:4"`<br>`"4:3"`<br>`"3:2"`<br>`"16:10"`<br>`"16:9"`<br>`"2:1"`<br>`"3:1"` |
| `quality` | Nível de qualidade. Níveis mais altos custam mais e demoram mais. Padrão: `"medium"`. | COMBO | Sim | `"low"`<br>`"medium"`<br>`"high"` |
| `seed` | Seed para geração. O mesmo prompt, imagens, configurações e seed produzem o mesmo SVG. Padrão: 42. | INT | Sim | 0 a 2147483647 |

**Restrições:**

* O prompt deve conter entre 1 e 9500 caracteres.
* `images` aceita no máximo 5 imagens, contadas por imagem quando a entrada está em lote, e cada imagem deve ter uma proporção de aspecto entre 1:6 e 6:1.
* Imagens cujo lado mais longo tenha mais de 2048 pixels são reduzidas antes do upload.
* Referenciar uma imagem que não está conectada, como `@Image4` com apenas duas imagens fornecidas, gera um erro.

## Saídas

| Nome da Saída | Descrição | Tipo de dados |
|-------------|-------------|-----------|
| `SVG` | O SVG gerado como marcação vetorial editável. | SVG |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/IdeogramVectorGenerateApi/pt-BR.md)

---
**Source fingerprint (SHA-256):** `5bd24ad48d6c26daf43f84544a9c22a18961dea645799104591f3785a851f819`
