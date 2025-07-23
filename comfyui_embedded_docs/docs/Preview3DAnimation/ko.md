Load3D 노드는 3D 모델 파일을 불러오고 처리하는 핵심 노드입니다. 노드를 불러올 때 `ComfyUI/input/3d/` 폴더에서 사용 가능한 3D 리소스를 자동으로 가져오며, 업로드 기능을 통해 지원되는 3D 파일을 업로드하여 미리보기할 수도 있습니다.

**지원 포맷**
현재 이 노드는 `.gltf`, `.glb`, `.obj`, `.fbx`, `.stl` 등 다양한 3D 파일 포맷을 지원합니다.

**3D 노드 설정**
3D 노드와 관련된 일부 설정은 ComfyUI의 설정 메뉴에서 조정할 수 있습니다. 자세한 내용은 아래 문서를 참고하세요:

[설정 메뉴](https://docs.comfy.org/interface/settings/3d)

일반적인 노드 출력 외에도 Load3D에는 미리보기 영역 메뉴에 다양한 3D 뷰 관련 기능이 있습니다.

## 입력

| 파라미터명      | 타입           | 설명                                                        | 기본값 | 범위         |
|---------------|---------------|-------------------------------------------------------------|--------|--------------|
| model_file    | File Selection | 3D 모델 파일 경로, 업로드 지원, 기본적으로 `ComfyUI/input/3d/`에서 파일을 읽음 | -      | 지원 포맷    |
| width         | INT            | 캔버스 렌더링 너비                                           | 1024   | 1-4096       |
| height        | INT            | 캔버스 렌더링 높이                                           | 1024   | 1-4096       |

## 출력

| 출력명           | 데이터 타입      | 설명                                                        |
|-----------------|----------------|-------------------------------------------------------------|
| image           | IMAGE          | 캔버스에 렌더링된 이미지                                    |
| mask            | MASK           | 현재 모델 위치가 포함된 마스크                              |
| mesh_path       | STRING         | 모델 파일 경로(`ComfyUI/input` 폴더 내 경로)                |
| normal          | IMAGE          | 노멀 맵                                                     |
| lineart         | IMAGE          | 라인아트 이미지 출력, `edge_threshold`는 캔버스의 모델 메뉴에서 조정 가능 |
| camera_info     | LOAD3D_CAMERA  | 카메라 정보                                                 |
| recording_video | VIDEO          | 녹화 영상(녹화가 있을 때만)                                 |

모든 출력 미리보기:
![뷰 조작 데모](../Load3D/asset/load3d_outputs.webp)

## 모델 캔버스(Canvas) 영역 설명

Load3D 노드의 Canvas 영역에는 다양한 뷰 조작 기능이 포함되어 있습니다:

- 미리보기 뷰 설정(그리드, 배경색, 미리보기)
- 카메라 제어: FOV, 카메라 타입 조정
- 전체 조명 강도: 조명 강도 조절
- 비디오 녹화: 영상 녹화 및 내보내기
- 모델 내보내기: `GLB`, `OBJ`, `STL` 포맷 지원
- 기타

![Load 3D 노드 UI](../Load3D/asset/load3d_ui.jpg)

1. Load3D 노드의 여러 메뉴 및 숨겨진 메뉴
2. 미리보기 창 크기 조정 및 캔버스 비디오 녹화 메뉴
3. 3D 뷰 조작 축
4. 미리보기 썸네일
5. 미리보기 크기 설정, 크기를 설정한 후 창 크기를 조절해 미리보기 표시를 조정

### 1. 뷰 조작

<video controls width="640" height="360">
  <source src="../Load3D/asset/view_operations.mp4" type="video/mp4">
  사용 중인 브라우저는 동영상 재생을 지원하지 않습니다.
</video>

뷰 조작 방법:

- 마우스 왼쪽 클릭 + 드래그: 뷰 회전
- 마우스 오른쪽 클릭 + 드래그: 뷰 이동
- 마우스 휠 또는 가운데 클릭: 확대/축소
- 좌표축: 뷰 전환

### 2. 왼쪽 메뉴 기능

![Menu](../Load3D/asset/menu.webp)

미리보기 영역에서는 일부 뷰 조작 관련 메뉴가 메뉴 버튼에 숨겨져 있습니다. 메뉴 버튼을 클릭하면 다양한 메뉴가 펼쳐집니다.

- 1. 장면(Scene): 미리보기 창 그리드, 배경색, 썸네일 설정
- 2. 모델(Model): 모델 렌더링 모드, 텍스처, 위 방향 설정
- 3. 카메라(Camera): 직교 뷰와 원근 뷰 전환, 시야각(FOV) 설정
- 4. 빛(Light): 전체 조명 강도
- 5. 내보내기(Export): GLB, OBJ, STL 포맷으로 내보내기

#### 장면(Scene)

![scene menu](../Load3D/asset/menu_scene.webp)

장면 메뉴는 장면의 기본 설정 기능을 제공합니다

1. 그리드 표시/숨기기
2. 배경색 설정
3. 배경 이미지 업로드
4. 썸네일 숨기기

#### 모델(Model)

![Menu_Scene](../Load3D/asset/menu_model.webp)

모델 메뉴는 모델 관련 기능을 제공합니다

1. **위 방향(Up direction)**: 모델의 어느 축이 위 방향인지 지정
2. **렌더링 모드(Material mode)**: 원본, 노멀, 와이어프레임, 라인아트 전환

#### 카메라(Camera)

![menu_modelmenu_camera](../Load3D/asset/menu_camera.webp)

이 메뉴는 직교 뷰와 원근 뷰 전환, 시야각(FOV) 설정을 제공합니다

1. **카메라(Camera)**: 직교 뷰와 원근 뷰 전환
2. **FOV**: 시야각 조절

#### 빛(Light)

![menu_modelmenu_camera](../Load3D/asset/menu_light.webp)

이 메뉴에서 전체 조명 강도를 빠르게 조절할 수 있습니다

#### 내보내기(Export)

![menu_export](../Load3D/asset/menu_export.webp)

이 메뉴는 모델을 다른 포맷(GLB, OBJ, STL)으로 변환 및 내보내기 기능을 제공합니다

### 3. 오른쪽 메뉴 기능

<video controls width="640" height="360">
  <source src="../Load3D/asset/recording.mp4" type="video/mp4">
  사용 중인 브라우저는 동영상 재생을 지원하지 않습니다.
</video>

오른쪽 메뉴의 주요 기능 두 가지:

1. **뷰 비율 재설정**: 버튼을 클릭하면 설정한 너비와 높이에 맞춰 캔버스 비율이 조정됩니다
2. **비디오 녹화**: 현재 3D 뷰 조작을 비디오로 녹화하고, 불러오기 및 후속 노드에 `recording_video`로 출력할 수 있습니다
