Load3DAnimation 节点用于加载和处理 3D 模型文件的核心节点，在加载节点时会自动获取  `ComfyUI/input/3d/`  可用的 3D 资源，你也可以通过上传功能将受支持的 3D 文件上传然后进行预览。

> - 该节点功能大部分与 Load 3D 节点相同，但这个节点支持加载带有动画的模型加载，可以在节点中预览对应的动画
> - 本篇文档内容与 Load3D 节点相同，因为除了动画预览播放外他们的能力都是相同的。

**支持格式**
目前该节点支持多种 3D 文件格式，包括 `.gltf`、`.glb`、`.obj`、`.fbx` 和 `.stl`。

**3D 节点预设**
3D 节点的一些相关偏好设置可以在 ComfyUI 的设置菜单中进行设置，请参考下面的文档了解对应的设置
[设置菜单](https://docs.comfy.org/zh-CN/interface/settings/3d)

除了常规的节点输出之外， Load3D 有许多相关的 3D 视图相关操作是位于预览区域菜单, 3D 节点

## 输入

| 参数名        | 类型        | 描述                     | 默认值 | 范围         |
|--------------|------------|--------------------------|--------|--------------|
| 模型文件   | 文件选择    | 3D 模型文件路径，支持上传，默认读取 `ComfyUI/input/3d/` 下的模型文件 | -      | 受支持格式文件 |
| 宽度        | INT        | 画布渲染宽度                 | 1024   | 1-4096       |
| 高度       | INT        | 画布渲染高度                 | 1024   | 1-4096       |

## 输出

| 参数名称         | 数据类型        | 说明                             |
| --------------- | ------------- | -------------------------------- |
| image           | IMAGE         | 画布渲染渲染图像                    |
| mask            | MASK          | 包含当前模型位置的遮罩               |
| mesh_path       | STRING        | 模型文件路径在`ComfyUI/input` 文件夹下的路径               |
| normal          | IMAGE         | 法线贴图                          |
| lineart         | IMAGE         | 线稿图像输出，对应的 `edge_threshold` 可在画布的模型菜单中进行调节                      |
| camera_info     | LOAD3D_CAMERA | 相机信息                         |
| recording_video | VIDEO         | 录制视频（仅当有录制视频存在时）     |

对应所有的输出预览如下：
![视图操作演示](../Load3D/asset/load3d_outputs.webp)

## 模型画布(Canvas)区说明

Load 3D 节点的 Canvas 区域包含了诸多的视图操作，包括：

- 预览视图设置（网格、背景色、预览视图）
- 相机控制: 控制FOV、相机类型
- 全局光照强度: 调节光照强度
- 视频录制: 录制视频并导出视频
- 模型导出: 支持`GLB`、`OBJ`、`STL` 格式
- 等

![Load 3D 节点UI](../Load3D/asset/load3d_ui.jpg)

1. 包含了 Load 3D 节点的多个菜单以及隐藏菜单
2. 重新`缩放预览窗口大小`以及进行`画布视频录制`菜单
3. 3D 视图操作轴
4. 预览缩略图
5. 预览尺寸设置，通过设置尺寸然后再缩放窗口大小来缩放预览视图显示

### 1. 视图操作

<video controls width="640" height="360">
  <source src="../Load3D/asset/view_operations.mp4" type="video/mp4">
  您的浏览器不支持视频播放。
</video>

视图控制操作：

- 鼠标左键点击 + 拖拽： 视图旋转控制
- 鼠标右键 + 拖拽： 平移视图
- 鼠标中键： 缩放控制
- 坐标轴： 切换视图

### 2. 左侧菜单功能

![Menu](../Load3D/asset/menu.webp)

在预览区域，有些视图操作相关的菜单被隐藏在了菜单里，点击菜单按钮可以展开对应不同的菜单

- 1. 场景（Scene）: 包含预览窗口网格、背景色、缩略图设置
- 2. 模型（Model）: 模型渲染模式、纹理材质、上方向设置
- 3. 摄像机（Camera）: 轴测视图和透视视图切换、透视视角大小设置
- 4. 灯光（Light）: 场景全局光照强度
- 5. 导出（Export）: 导出模型为其它格式（GLB、OBJ、STL）

#### 场景（Scene）

![scene menu](../Load3D/asset/menu_scene.webp)

场景菜单提供了对场景的一些基础设置功能

1. 显示 / 隐藏网格
2. 设置背景色
3. 点击上传设置背景图片
4. 隐藏缩略预览图

#### 模型(Model)

![Menu_Scene](../Load3D/asset/menu_model.webp)

模型菜单提供了一些模型的相关功能

1. **上方向(Up direction)**: 确定模型的哪个轴为上方向
2. **渲染模式（Material mode）**: 模型渲染模式切换 原始（Original）、法线(Normal)、线框(Wireframe)、线稿(Lineart)

#### 摄像机（Camera）

![menu_modelmenu_camera](../Load3D/asset/menu_camera.webp)

该菜单提供了轴测视图和透视视图切换、透视视角大小设置

1. **相机（Camera）**: 在轴测视图和正交视图之间快速切换
2. **视场角(FOV)**: 调整 FOV 视角角度

#### 灯光（Light）

![menu_modelmenu_camera](../Load3D/asset/menu_light.webp)

通过该菜单可以快速调节模型场景的全局光照强度

#### 导出（Export）

![menu_export](../Load3D/asset/menu_export.webp)

该菜单提供了一个快速转换模型格式并导出的能力

### 3. 右侧菜单功能

<video controls width="640" height="360">
  <source src="../Load3D/asset/recording.mp4" type="video/mp4">
  您的浏览器不支持视频播放。
</video>

右侧菜单的两个主要功能为：

1. **重设视图比例**： 点击按钮后视图将根据设定好的宽高按比例调整画布渲染区域比例
2. **视频录制**： 允许你将当前的 3D 视图操作录制为视频，允许导入，并可以作为 `recording_video` 输出给后续节点
