> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, fique à vontade para contribuir. [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MultiGPU_WorkUnits/pt-BR.md)

## Visão geral

O nó MultiGPU CFG Split permite que o trabalho de difusão seja dividido entre várias GPUs instaladas no mesmo computador. O ganho de velocidade depende do workflow, mas já foram medidos aumentos de até 1.95x em workflows comuns.

## Detalhes importantes

Não é possível misturar tipos diferentes de GPU. As GPUs instaladas precisam ser iguais, por exemplo 2x 5090 ou 2x 5080.

O ComfyUI detecta automaticamente várias GPUs instaladas durante a inicialização.

## GPUs compatíveis

Qualquer configuração homogênea com duas GPUs baseadas em arquitetura Ampere ou mais recente, por exemplo 2 x 3090 ou 2 x RTX6000 Pro.

## Modelos compatíveis

* LTX-2.3  
* WAN 2.2  
* FLUX.2 Klein - versões base  
* Z-Image  
* Stable Diffusion 3.5 Large  
* Hunyuan Video  
* Qwen-Image-Edit-2511  
* Hunyuan-3D-v2.1  
* SDXL

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `model` | MODEL | Sim | N/A | O modelo que será preparado para usar o MultiGPU CFG Split antes da amostragem. |
| `max_gpus` | INT | Sim | Mínimo: 1<br>Passo: 1<br>Padrão: 2 | O número máximo de GPUs idênticas usadas para dividir a carga de trabalho. Ajuste esse valor para a quantidade de GPUs iguais instaladas no sistema. |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `MODEL` | MODEL | O modelo preparado para MultiGPU CFG Split, pronto para amostragem acelerada. |

## Posicionamento do nó e notas do workflow

![image1.png](./asset/image1.png)

O campo `max_gpus` deve ser definido com a quantidade máxima de GPUs idênticas instaladas no sistema.

**Posicionamento do nó:** o MultiGPU CFG Split precisa ficar entre o nó de carregamento do modelo e o nó de amostragem. Se houver outros nós conectados à saída de modelo do carregador, o MultiGPU CFG Split deve ser o último nó dessa cadeia antes do nó de amostragem.

![image2.png](./asset/image2.png)

**Requisitos do workflow:** este nó divide o workflow de difusão no nível do CFG. Por isso, o CFG do workflow precisa ser maior que 1. Workflows destilados que exigem CFG = 1 não mostram ganho de desempenho ao usar o MultiGPU CFG Split com várias GPUs.

## Verificação do uso de múltiplas GPUs

Ao executar um workflow com o MultiGPU CFG Split ativado, você pode abrir o Gerenciador de Tarefas do Windows e selecionar a categoria de desempenho.

![image3.webp](./asset/image3.webp)  

![image4.png](./asset/image4.webp)

Você deve ver atividade nas duas GPUs instaladas enquanto o sampler estiver rodando no workflow.

## Workflow de exemplo com múltiplas GPUs: (Wan 2.2 FP8)

[Workflow de exemplo (Wan 2.2 FP8)](https://raw.githubusercontent.com/Comfy-Org/embedded-docs/refs/heads/main/comfyui_embedded_docs/docs/MultiGPU_WorkUnits/asset/video_wan2_2_14B_t2v_mGPU.json)

---
**Source fingerprint (SHA-256):** `7293ee785e29aea9a1a70a10444b99e89fb23c866505628ec57c209a2b8aaee0`
