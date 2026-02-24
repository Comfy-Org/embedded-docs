> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ControlNetApply/pt-BR.md)

O uso do ControlNet requer o pré-processamento das imagens de entrada. Como os nós iniciais do ComfyUI não vêm com pré-processadores e modelos ControlNet, primeiro instale os pré-processadores do ControlNet [baixe os pré-processadores aqui](https://github.com/Fannovel16/comfy_controlnet_preprocessors) e os modelos ControlNet correspondentes.

## Entradas

| Parâmetro | Tipo de Dados | Função |
| --- | --- | --- |
| `positive` | `CONDITIONING` | Dados de condicionamento positivo, provenientes do Codificador de Texto CLIP ou de outras entradas de condicionamento |
| `negative` | `CONDITIONING` | Dados de condicionamento negativo, provenientes do Codificador de Texto CLIP ou de outras entradas de condicionamento |
| `control_net` | `CONTROL_NET` | O modelo ControlNet a ser aplicado, normalmente inserido a partir do ControlNet Loader |
| `image` | `IMAGE` | Imagem para aplicação do ControlNet, precisa ser processada pelo pré-processador |
| `vae` | `VAE` | Entrada do modelo VAE |
| `strength` | `FLOAT` | Controla a intensidade dos ajustes da rede, faixa de valores 0~10. Valores recomendados entre 0.5~1.5 são razoáveis. Valores mais baixos permitem mais liberdade ao modelo, valores mais altos impõem restrições mais rígidas. Valores muito altos podem resultar em imagens estranhas. Você pode testar e ajustar este valor para refinar a influência da rede de controle. |
| `start_percent` | `FLOAT` | Valor 0.000~1.000, determina quando começar a aplicar o ControlNet como uma porcentagem, por exemplo, 0.2 significa que a orientação do ControlNet começará a influenciar a geração da imagem aos 20% do processo de difusão |
| `end_percent` | `FLOAT` | Valor 0.000~1.000, determina quando parar de aplicar o ControlNet como uma porcentagem, por exemplo, 0.8 significa que a orientação do ControlNet deixará de influenciar a geração da imagem aos 80% do processo de difusão |

### Saídas

| Parâmetro | Tipo de Dados | Função |
| --- | --- | --- |
| `positive` | `CONDITIONING` | Dados de condicionamento positivo processados pelo ControlNet, podem ser enviados para os próximos nós ControlNet ou K Sampler |
| `negative` | `CONDITIONING` | Dados de condicionamento negativo processados pelo ControlNet, podem ser enviados para os próximos nós ControlNet ou K Sampler |
