# Carregar CLIP

O nó CLIPLoader carrega um modelo de codificador de texto (CLIP, T5 ou similar) de um arquivo, disponibilizando-o para uso em outros nós que precisam converter prompts de texto em representações numéricas. Ele suporta uma ampla variedade de arquiteturas de modelo, cada uma exigindo um tipo específico de codificador.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `clip_name` | O nome do arquivo do modelo de codificador de texto a ser carregado. Este deve ser um arquivo localizado no diretório `ComfyUI/models/text_encoders/` ou `ComfyUI/models/clip/`. | STRING | Sim | Lista de arquivos encontrados na pasta `text_encoders` |
| `type` | O tipo de arquitetura do modelo que está sendo carregado. Isso determina qual variante específica do codificador usar. O padrão é `"stable_diffusion"`. | STRING | Sim | `"stable_diffusion"`<br>`"stable_cascade"`<br>`"sd3"`<br>`"stable_audio"`<br>`"mochi"`<br>`"ltxv"`<br>`"pixart"`<br>`"cosmos"`<br>`"lumina2"`<br>`"wan"`<br>`"hidream"`<br>`"chroma"`<br>`"ace"`<br>`"omnigen2"`<br>`"qwen_image"`<br>`"hunyuan_image"`<br>`"flux2"`<br>`"ovis"`<br>`"longcat_image"`<br>`"cogvideox"` |
| `device` | O dispositivo no qual carregar o modelo. `"default"` usa a GPU se disponível, enquanto `"cpu"` força o carregamento na CPU. Esta é uma opção avançada (padrão: `"default"`). | STRING | Não | `"default"`<br>`"cpu"` |

### Mapeamentos Suportados de Tipo para Codificador

O parâmetro `type` seleciona o codificador correto para uma determinada arquitetura de modelo. A seguir estão os mapeamentos comuns:

| Tipo | Codificador |
|------|-------------|
| stable_diffusion | clip-l |
| stable_cascade | clip-g |
| sd3 | t5 xxl / clip-g / clip-l |
| stable_audio | t5 base |
| mochi | t5 xxl |
| cogvideox | t5 xxl (preenchimento de 226 tokens) |
| cosmos | t5 xxl antigo |
| lumina2 | gemma 2 2B |
| wan | umt5 xxl |
| hidream | llama-3.1 (recomendado) ou t5 |
| omnigen2 | qwen vl 2.5 3B |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `clip` | O modelo de codificador de texto carregado, pronto para ser conectado a outros nós para codificação de texto e condicionamento. | CLIP |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPLoader/pt-BR.md)

---
**Source fingerprint (SHA-256):** `1051bfe5570dff81719682cb09938bae4c03e94e0e72f7a2be84867cccb48017`
