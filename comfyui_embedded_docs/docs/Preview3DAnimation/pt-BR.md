> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Preview3DAnimation/pt-BR.md)

O nó Preview3DAnimation é usado principalmente para visualizar saídas de modelos 3D. Este nó recebe duas entradas: uma é a `camera_info` do nó Load3D, e a outra é o caminho para o arquivo do modelo 3D. O caminho do arquivo do modelo deve estar localizado na pasta `ComfyUI/output`.

**Formatos Suportados**
Atualmente, este nó suporta múltiplos formatos de arquivo 3D, incluindo `.gltf`, `.glb`, `.obj`, `.fbx` e `.stl`.

**Preferências dos Nós 3D**
Algumas preferências relacionadas aos nós 3D podem ser configuradas no menu de configurações do ComfyUI. Consulte a seguinte documentação para as configurações correspondentes:
[Menu de Configurações](https://docs.comfy.org/interface/settings/3d)

## Entradas

| Nome do Parâmetro | Tipo           | Descrição                                  |
| -------------- | -------------- | -------------------------------------------- |
| camera_info    | LOAD3D_CAMERA  | Informações da câmera                           |
| model_file     | STRING  | Caminho do arquivo do modelo em `ComfyUI/output/`      |

## Descrição da Área da Tela

Atualmente, os nós relacionados a 3D no frontend do ComfyUI compartilham o mesmo componente de tela, portanto suas operações básicas são majoritariamente consistentes, exceto por algumas diferenças funcionais.

> O conteúdo e a interface a seguir são baseados principalmente no nó Load3D. Consulte a interface real do nó para funcionalidades específicas.

A área da Tela inclui várias operações de visualização, tais como:

- Configurações da visualização de prévia (grade, cor de fundo, visualização de prévia)
- Controle da câmera: FOV, tipo de câmera
- Intensidade da iluminação global: ajustar a iluminação
- Exportação do modelo: suporta formatos `GLB`, `OBJ`, `STL`
- etc.

![Interface do Nó Load 3D](../Preview3D/asset/preview3d_canvas.jpg)

1. Contém múltiplos menus e menus ocultos do nó Load 3D
2. Eixo de operação da visualização 3D

### 1. Operações de Visualização

<video controls width="640" height="360">
  <source src="https://raw.githubusercontent.com/Comfy-Org/embedded-docs/refs/heads/main/comfyui_embedded_docs/docs/Load3d/asset/view_operations.mp4" type="video/mp4">
  Seu navegador não suporta reprodução de vídeo.
</video>

Operações de controle da visualização:

- Clique esquerdo + arrastar: Girar a visualização
- Clique direito + arrastar: Mover a visualização
- Rolar roda do meio ou clique do meio + arrastar: Aproximar/afastar
- Eixo de coordenadas: Alternar entre visualizações

### 2. Funções do Menu Esquerdo

![Menu](https://raw.githubusercontent.com/Comfy-Org/embedded-docs/refs/heads/main/comfyui_embedded_docs/docs/Load3d/asset/menu.webp)

Na área de prévia, alguns menus de operação de visualização estão ocultos no menu. Clique no botão do menu para expandir diferentes menus.

- 1. Cena: Contém configurações de grade da janela de prévia, cor de fundo, miniaturas
- 2. Modelo: Configurações de modo de renderização do modelo, material de textura, direção para cima
- 3. Câmera: Alternar entre vistas ortográfica e em perspectiva, definir ângulo de perspectiva
- 4. Luz: Intensidade da iluminação global da cena
- 5. Exportar: Exportar modelo para outros formatos (GLB, OBJ, STL)

#### Cena

![menu da cena](https://raw.githubusercontent.com/Comfy-Org/embedded-docs/refs/heads/main/comfyui_embedded_docs/docs/Load3d/asset/menu_scene.webp)

O menu Cena fornece algumas funções básicas de configuração da cena:

1. Mostrar/Ocultar grade
2. Definir cor de fundo
3. Clicar para fazer upload de uma imagem de fundo
4. Ocultar miniatura de prévia

#### Modelo

![Menu_Cena](https://raw.githubusercontent.com/Comfy-Org/embedded-docs/refs/heads/main/comfyui_embedded_docs/docs/Load3d/asset/menu_model.webp)

O menu Modelo fornece algumas funções relacionadas ao modelo:

1. **Direção para cima**: Determinar qual eixo é a direção para cima do modelo
2. **Modo de material**: Alternar modos de renderização do modelo - Original, Normal, Wireframe, Lineart

#### Câmera

![menu_modelmenu_camera](https://raw.githubusercontent.com/Comfy-Org/embedded-docs/refs/heads/main/comfyui_embedded_docs/docs/Load3d/asset/menu_camera.webp)

Este menu fornece a alternância entre vistas ortográfica e em perspectiva, e configurações do tamanho do ângulo de perspectiva:

1. **Câmera**: Alternar rapidamente entre vistas ortográfica e em perspectiva
2. **FOV**: Ajustar o ângulo FOV

#### Luz

![menu_modelmenu_camera](https://raw.githubusercontent.com/Comfy-Org/embedded-docs/refs/heads/main/comfyui_embedded_docs/docs/Load3d/asset/menu_light.webp)

Através deste menu, você pode ajustar rapidamente a intensidade da iluminação global da cena

#### Exportar

![menu_exportar](https://raw.githubusercontent.com/Comfy-Org/embedded-docs/refs/heads/main/comfyui_embedded_docs/docs/Load3d/asset/menu_export.webp)

Este menu fornece a capacidade de converter e exportar rapidamente formatos de modelo
