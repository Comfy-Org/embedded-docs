> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Load3D/pt-BR.md)

O nó Load3D é um nó principal para carregar e processar arquivos de modelos 3D. Ao carregar o nó, ele recupera automaticamente os recursos 3D disponíveis de `ComfyUI/input/3d/`. Você também pode enviar arquivos 3D suportados para visualização usando a função de upload.

**Formatos Suportados**
Atualmente, este nó suporta vários formatos de arquivo 3D, incluindo `.gltf`, `.glb`, `.obj`, `.fbx` e `.stl`.

**Preferências do Nó 3D**
Algumas preferências relacionadas para nós 3D podem ser configuradas no menu de configurações do ComfyUI. Consulte a seguinte documentação para as configurações correspondentes:

[Menu de Configurações](https://docs.comfy.org/interface/settings/3d)

Além das saídas regulares do nó, o Load3D possui muitas configurações relacionadas à visualização 3D no menu da tela.

## Entradas

| Nome do Parâmetro | Tipo          | Descrição                                                     | Padrão | Intervalo      |
|-------------------|---------------|---------------------------------------------------------------|--------|----------------|
| model_file        | Seleção de Arquivo | Caminho do arquivo de modelo 3D, suporta upload, padrão é ler arquivos de modelo de `ComfyUI/input/3d/` | -      | Formatos suportados |
| width             | INT           | Largura de renderização da tela                               | 1024   | 1-4096         |
| height            | INT           | Altura de renderização da tela                                | 1024   | 1-4096         |

## Saídas

| Nome do Parâmetro | Tipo de Dado   | Descrição                                                         |
|-------------------|----------------|-------------------------------------------------------------------|
| image             | IMAGE          | Imagem renderizada da tela                                        |
| mask              | MASK           | Máscara contendo a posição atual do modelo                        |
| mesh_path         | STRING         | Caminho do arquivo do modelo                                      |
| normal            | IMAGE          | Mapa normal                                                       |
| lineart           | IMAGE          | Saída de imagem de arte linear, o `edge_threshold` correspondente pode ser ajustado no menu do modelo da tela |
| camera_info       | LOAD3D_CAMERA  | Informações da câmera                                             |
| recording_video   | VIDEO          | Vídeo gravado (apenas quando a gravação existe)                   |

Visualização de todas as saídas:
![Demonstração de Operação de Visualização](./asset/load3d_outputs.webp)

## Descrição da Área da Tela

A área da Tela do nó Load3D contém inúmeras operações de visualização, incluindo:

- Configurações de visualização de pré-visualização (grade, cor de fundo, visualização de pré-visualização)
- Controle de câmera: Controlar FOV, tipo de câmera
- Intensidade de iluminação global: Ajustar a intensidade da luz
- Gravação de vídeo: Gravar e exportar vídeos
- Exportação de modelo: Suporta formatos `GLB`, `OBJ`, `STL`
- E muito mais

![Interface do Nó Load 3D](./asset/load3d_ui.jpg)

1. Contém vários menus e menus ocultos do nó Load 3D
2. Menu para `redimensionar janela de pré-visualização` e `gravação de vídeo da tela`
3. Eixo de operação da visualização 3D
4. Miniatura de pré-visualização
5. Configurações de tamanho da pré-visualização, dimensionar a exibição da visualização de pré-visualização definindo dimensões e redimensionando a janela

### 1. Operações de Visualização

<video controls width="640" height="360">
  <source src="./asset/view_operations.mp4" type="video/mp4">
  Seu navegador não suporta a reprodução de vídeo.
</video>

Operações de controle de visualização:

- Clique esquerdo + arrastar: Girar a visualização
- Clique direito + arrastar: Mover a visualização
- Rolar o scroll do meio ou clique do meio + arrastar: Aumentar/diminuir zoom
- Eixo de coordenadas: Alternar visualizações

### 2. Funções do Menu Esquerdo

![Menu](./asset/menu.webp)

Na tela, algumas configurações estão ocultas no menu. Clique no botão do menu para expandir diferentes menus

- 1. Cena: Contém grade da janela de pré-visualização, cor de fundo, configurações de pré-visualização
- 2. Modelo: Modo de renderização do modelo, materiais de textura, configurações de direção para cima
- 3. Câmera: Alternar entre visualizações ortográfica e perspectiva, e definir o tamanho do ângulo de perspectiva
- 4. Luz: Intensidade de iluminação global da cena
- 5. Exportar: Exportar modelo para outros formatos (GLB, OBJ, STL)

#### Cena

![menu da cena](./asset/menu_scene.webp)

O menu Cena fornece algumas funções básicas de configuração de cena

1. Mostrar/Ocultar grade
2. Definir cor de fundo
3. Clique para enviar uma imagem de fundo
4. Ocultar a pré-visualização

#### Modelo

![Menu_Cena](./asset/menu_model.webp)

O menu Modelo fornece algumas funções relacionadas ao modelo

1. **Direção para cima**: Determinar qual eixo é a direção para cima do modelo
2. **Modo de material**: Alternar modos de renderização do modelo - Original, Normal, Wireframe, Lineart

#### Câmera

![menu_modelo_menu_camera](./asset/menu_camera.webp)

Este menu fornece a alternância entre visualizações ortográfica e perspectiva, e configurações de tamanho do ângulo de perspectiva

1. **Câmera**: Alternar rapidamente entre visualizações ortográfica e perspectiva
2. **FOV**: Ajustar o ângulo FOV

#### Luz

![menu_modelo_menu_camera](./asset/menu_light.webp)

Através deste menu, você pode ajustar rapidamente a intensidade de iluminação global da cena

#### Exportar

![menu_exportar](./asset/menu_export.webp)

Este menu fornece a capacidade de converter e exportar rapidamente formatos de modelo

### 3. Funções do Menu Direito

<video controls width="640" height="360">
  <source src="https://raw.githubusercontent.com/Comfy-Org/embedded-docs/refs/heads/main/comfyui_embedded_docs/docs/Load3d/asset/view_operations.mp4" type="video/mp4">
  Seu navegador não suporta a reprodução de vídeo.
</video>

O menu direito tem duas funções principais:

1. **Redefinir proporção da visualização**: Após clicar no botão, a visualização ajustará a proporção da área de renderização da tela de acordo com a largura e altura definidas
2. **Gravação de vídeo**: Permite gravar as operações atuais da visualização 3D como vídeo, permite importação e pode ser emitido como `recording_video` para nós subsequentes