# Carregar CLIP

O nó CLIPLoader carrega um modelo codificador de texto (CLIP, T5 ou similar) a partir de um arquivo, disponibilizando-o para uso em outros nós que precisam converter prompts de texto em representações numéricas. Ele suporta uma ampla variedade de arquiteturas de modelo, cada uma exigindo um tipo específico de codificador.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `clip_name` | O nome do arquivo do modelo codificador de texto a ser carregado. Este deve ser um arquivo localizado no diretório `ComfyUI/models/text_encoders/`. | STRING | Sim | Lista de arquivos encontrados na pasta `text_encoders` |
| `type` | O tipo de arquitetura do modelo sendo carregado. Isso determina qual variante específica de codificador usar (padrão: `"stable_diffusion"`). | COMBO | Sim | `"stable_diffusion"`<br>`"stable_cascade"`<br>`"sd3"`<br>`"stable_audio"`<br>`"mochi"`<br>`"ltxv"`<br>`"pixart"`<br>`"cosmos"`<br>`"lumina2"`<br>`"wan"`<br>`"hidream"`<br>`"chroma"`<br>`"ace"`<br>`"omnigen2"`<br>`"qwen_image"`<br>`"hunyuan_image"`<br>`"flux2"`<br>`"ovis"`<br>`"longcat_image"`<br>`"cogvideox"`<br>`"lens"`<br>`"pixeldit"`<br>`"ideogram4"`<br>`"boogu"`<br>`"krea2"`<br>`"joyimage"`<br>`"mage"`<br>`"minimax"`<br>`"yue2"` |
| `device` | O dispositivo no qual carregar o modelo. `"default"` usa a GPU se disponível, enquanto `"cpu"` força o carregamento na CPU. Esta é uma opção avançada (padrão: `"default"`). | COMBO | Não | `"default"`<br>`"cpu"` |

### Mapeamentos de tipo para codificador suportados

O parâmetro `type` seleciona o codificador correto para uma determinada arquitetura de modelo. A seguir estão mapeamentos comuns:

| Tipo | Codificador |
|------|---------|
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
| joyimage | qwen3-vl 8B |
| lens | gpt-oss-20b |
| pixeldit | gemma 2 2B elm |
| minimax | MiniMax H3 Qwen3-VL ou Music3 Qwen/RVQ |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `CLIP` | O modelo codificador de texto carregado, pronto para ser conectado a outros nós para codificação de texto e condicionamento. | CLIP |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ClipLoader/pt-BR.md)

---
**Source fingerprint (SHA-256):** `6df608d500520d9414acd82d9fd509b1e211a8385202cefd5579e8a8f397bc64`
