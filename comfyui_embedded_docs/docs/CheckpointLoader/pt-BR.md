> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CheckpointLoader/pt-BR.md)

O nó CheckpointLoader carrega um checkpoint de modelo pré-treinado junto com seu arquivo de configuração. Ele recebe um arquivo de configuração e um arquivo de checkpoint como entradas e retorna os componentes do modelo carregado, incluindo o modelo principal, o modelo CLIP e o modelo VAE para uso no fluxo de trabalho.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `config_name` | STRING | Sim | Arquivos de configuração disponíveis | O arquivo de configuração que define a arquitetura e as configurações do modelo |
| `ckpt_name` | STRING | Sim | Arquivos de checkpoint disponíveis | O arquivo de checkpoint contendo os pesos e parâmetros do modelo treinado |

**Observação:** Este nó exige que tanto um arquivo de configuração quanto um arquivo de checkpoint sejam selecionados. O arquivo de configuração deve corresponder à arquitetura do arquivo de checkpoint que está sendo carregado.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `MODEL` | MODEL | O componente principal do modelo carregado, pronto para inferência |
| `CLIP` | CLIP | O componente do modelo CLIP carregado para codificação de texto |
| `VAE` | VAE | O componente do modelo VAE carregado para codificação e decodificação de imagens |

**Observação Importante:** Este nó foi marcado como obsoleto e pode ser removido em versões futuras. Considere usar nós de carregamento alternativos para novos fluxos de trabalho.

---
**Source fingerprint (SHA-256):** `9977bda5e124a9d10566839cbee868c74fab120c454141f27ce145efa60105e9`
