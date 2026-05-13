> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanVideo15LatentUpscaleWithModel/pt-BR.md)

O nó **Hunyuan Video 15 Latent Upscale With Model** aumenta a resolução de uma representação latente de imagem. Ele primeiro redimensiona as amostras latentes para um tamanho especificado usando um método de interpolação escolhido e, em seguida, refina o resultado redimensionado usando um modelo de redimensionamento especializado Hunyuan Video 1.5 para melhorar a qualidade.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `modelo` | LATENT_UPSCALE_MODEL | Sim | N/A | O modelo de redimensionamento latente Hunyuan Video 1.5 usado para refinar as amostras redimensionadas. |
| `amostras` | LATENT | Sim | N/A | A representação latente da imagem a ser redimensionada. |
| `método_de_upscale` | COMBO | Não | `"nearest-exact"`<br>`"bilinear"`<br>`"area"`<br>`"bicubic"`<br>`"bislerp"` | O algoritmo de interpolação usado na etapa inicial de redimensionamento (padrão: `"bilinear"`). |
| `largura` | INT | Não | 0 a 16384 | A largura alvo para o latente redimensionado, em pixels. Um valor 0 calculará a largura automaticamente com base na altura alvo e na proporção original. A largura final da saída será um múltiplo de 16 (padrão: 1280). |
| `altura` | INT | Não | 0 a 16384 | A altura alvo para o latente redimensionado, em pixels. Um valor 0 calculará a altura automaticamente com base na largura alvo e na proporção original. A altura final da saída será um múltiplo de 16 (padrão: 720). |
| `corte` | COMBO | Não | `"disabled"`<br>`"center"` | Determina como o latente redimensionado é cortado para se ajustar às dimensões alvo. |

**Observação sobre Dimensões:** Se tanto `width` quanto `height` forem definidos como 0, o nó retorna as `samples` de entrada inalteradas. Se apenas uma dimensão for definida como 0, a outra dimensão é calculada para preservar a proporção original. As dimensões finais são sempre ajustadas para terem pelo menos 64 pixels e serem divisíveis por 16.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `LATENT` | LATENT | A representação latente da imagem redimensionada e refinada pelo modelo. |

---
**Source fingerprint (SHA-256):** `1de9e157c1a0433f1b3d5ff4d428a1aa392fd65da5e314e6e818ce66495d5ef4`
