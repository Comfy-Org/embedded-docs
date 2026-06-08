Esta documentação foi gerada por IA. Se você encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TencentTextToModelNode/en.md)

Este nó utiliza a API Hunyuan3D Pro da Tencent para gerar um modelo 3D a partir de uma descrição textual. Ele envia uma requisição para criar uma tarefa de geração, consulta o resultado e baixa os arquivos finais do modelo nos formatos GLB e OBJ.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `modelo` | A versão do modelo Hunyuan3D a ser utilizada. A opção LowPoly não está disponível para o modelo `3.1`. | COMBO | Sim | `"3.0"`<br>`"3.1"` |
| `prompt` | A descrição textual do modelo 3D a ser gerado. Suporta até 1024 caracteres. | STRING | Sim | - |
| `número_de_faces` | O número alvo de faces para o modelo 3D gerado. Padrão: 500000. | INT | Sim | 3000 - 1500000 |
| `tipo_de_geração` | O tipo de modelo 3D a ser gerado. As opções disponíveis e seus parâmetros associados são:<br>- **Normal**: Gera um modelo padrão. Inclui um parâmetro `pbr` (padrão: `False`).<br>- **LowPoly**: Gera um modelo de baixa poligonagem. Inclui os parâmetros `polygon_type` (`"triangle"` ou `"quadrilateral"`) e `pbr` (padrão: `False`).<br>- **Geometry**: Gera um modelo apenas com geometria. | DYNAMICCOMBO | Sim | `"Normal"`<br>`"LowPoly"`<br>`"Geometry"` |
| `semente` | Um valor de semente para a geração. Os resultados não são determinísticos independentemente da semente. Definir uma nova semente controla se o nó deve ser executado novamente. Padrão: 0. | INT | Não | 0 - 2147483647 |

**Observação:** O parâmetro `generate_type` é dinâmico. Selecionar `"LowPoly"` revelará entradas adicionais para `polygon_type` e `pbr`. Selecionar `"Normal"` revelará uma entrada para `pbr`. Selecionar `"Geometry"` não revelará entradas adicionais.

**Restrição:** O tipo de geração `"LowPoly"` não pode ser usado com o modelo `"3.1"`.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `model_file` | Uma saída legada para compatibilidade com versões anteriores. | STRING |
| `GLB` | O modelo 3D gerado no formato de arquivo GLB. | FILE3DGLB |
| `OBJ` | O modelo 3D gerado no formato de arquivo OBJ. | FILE3DOBJ |
| `texture_image` | A imagem de textura extraída do arquivo OBJ gerado, se disponível. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TencentTextToModelNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `e35f5165941cc7761639dd72e78141326d37d5e169be9a0e326afcbcdc572b7d`
