# Convert SDR to HDR

O nó **Convert SDR to HDR** expande imagens sRGB de faixa dinâmica padrão para Rec.2020 HLG HDR. Ele mantém a aparência existente da imagem e mapeia seu brilho para uma faixa mais ampla, portanto o resultado deve ser salvo com um espaço de cor HDR selecionado. O alfa é preservado sem alterações.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `image` | A(s) imagem(ns) SDR em sRGB a serem expandidas para HDR. | IMAGE | Sim | - |
| `algorithm` | Algoritmo de expansão HDR. Selecionar um algoritmo revela seus parâmetros (`target_luminance`). | DYNAMIC_COMBO | Sim | `"lottes"` |

### Entradas do lottes

Estes parâmetros aparecem quando `algorithm` é definido como `"lottes"`.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `target_luminance` | Alvo de branco de pico em nits. 0 mantém a renderização calibrada. Imagens escuras não são normalizadas para este pico. (padrão: 650.0) | FLOAT | Sim | 0.0 a 10000.0 (passo 1.0) |

Cada imagem do lote é convertida separadamente: a codificação sRGB é invertida para luz linear, o brilho é expandido com uma curva racional no estilo Lottes combinada com uma curva de ganho logarítmico monotônica calibrada, e o resultado é recodificado como Rec.2020 HLG. Como a saída é HDR, o nó de salvamento deve usar o espaço de cor `HDR`; salvá-la como sRGB renderiza o brilho incorretamente.

HLG assume um monitor de referência de 1000 nits, portanto valores de `target_luminance` abaixo de 1000 mantêm essa referência e um valor de `0` deixa a renderização calibrada intacta. Imagens de canal único são expandidas para três canais antes da conversão, e o canal alfa é copiado sem alterações.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `IMAGE` | A(s) imagem(ns) HDR Rec.2020 HLG. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageSDRToHDR/pt-BR.md)

---
**Source fingerprint (SHA-256):** `51eb0beac3d48345a30ba66d80d95873384cf5155fc06c33353b6d1dc029658a`
