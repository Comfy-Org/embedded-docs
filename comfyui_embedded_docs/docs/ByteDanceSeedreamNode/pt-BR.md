> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceSeedreamNode/pt-BR.md)

O nó ByteDance Seedream 4.5 e 5.0 oferece geração unificada de texto para imagem e capacidades precisas de edição de frase única em resoluções de até 4K. Ele pode criar novas imagens a partir de prompts de texto ou editar imagens existentes usando instruções textuais. O nó suporta tanto a geração de uma única imagem quanto a geração sequencial de múltiplas imagens relacionadas.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `model` | STRING | Sim | Ver Descrição | O modelo Seedream a ser usado para geração. Os modelos disponíveis incluem variantes seedream-4-0, seedream-4-5 e seedream-5-0. |
| `prompt` | STRING | Sim | - | Prompt de texto para criar ou editar uma imagem. Deve ter pelo menos 1 caractere. |
| `image` | IMAGE | Não | - | Imagem(ns) de entrada para geração imagem-para-imagem. Imagem(ns) de referência para geração de referência única ou múltipla. Máximo de 10 imagens de referência para a maioria dos modelos, ou 14 para seedream-5-0-260128. |
| `size_preset` | STRING | Não | Múltiplas opções disponíveis | Escolha um tamanho recomendado. Selecione Personalizado para usar a largura e altura abaixo. Padrão: primeiro predefinido de RECOMMENDED_PRESETS_SEEDREAM_4. |
| `width` | INT | Não | 1024 a 6240 (passo 2) | Largura personalizada para a imagem. O valor só funciona se `size_preset` estiver definido como `Personalizado`. Padrão: 2048. |
| `height` | INT | Não | 1024 a 4992 (passo 2) | Altura personalizada para a imagem. O valor só funciona se `size_preset` estiver definido como `Personalizado`. Padrão: 2048. |
| `sequential_image_generation` | STRING | Não | "desabilitado"<br>"automático" | Modo de geração de imagens em grupo. "desabilitado" gera uma única imagem. "automático" permite que o modelo decida se deve gerar múltiplas imagens relacionadas (ex: cenas de história, variações de personagens). Padrão: "desabilitado". |
| `max_images` | INT | Não | 1 a 15 (passo 1) | Número máximo de imagens a serem geradas quando sequential_image_generation='automático'. O total de imagens (entrada + geradas) não pode exceder 15. Padrão: 1. |
| `seed` | INT | Não | 0 a 2147483647 (passo 1) | Semente a ser usada para geração. Padrão: 0. |
| `watermark` | BOOLEAN | Não | - | Se deve adicionar uma marca d'água "gerado por IA" à imagem. Padrão: Falso. |
| `fail_on_partial` | BOOLEAN | Não | - | Se ativado, interrompe a execução se alguma imagem solicitada estiver faltando ou retornar um erro. Padrão: Verdadeiro. |

**Observações sobre as restrições dos parâmetros:**
- A resolução mínima da imagem depende do modelo selecionado: 3,68MP para modelos seedream-4-5 e seedream-5-0, 0,92MP para modelos seedream-4-0.
- A resolução máxima da imagem é 10,4MP para modelos seedream-5-0 e 16,78MP para outros modelos.
- As imagens de referência devem ter uma proporção de aspecto entre 1:3 e 3:1.
- Quando `sequential_image_generation` está definido como "automático", o número total de imagens de entrada mais `max_images` não pode exceder 15.
- Os parâmetros `width` e `height` são usados apenas quando `size_preset` está definido como "Personalizado".

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `IMAGE` | IMAGE | Imagem(ns) gerada(s) com base nos parâmetros de entrada e no prompt. Retorna um tensor de imagem única ou um lote de tensores de imagem se múltiplas imagens forem geradas. |

---
**Source fingerprint (SHA-256):** `ce130246026e0f5036e137bea4e193f51097e0812459586dcbeb87ef01975630`
