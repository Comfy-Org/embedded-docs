# Trellis2TextureStage

## 입력

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `positive` | 텍스처 생성 패스에 사용되는 포지티브 컨디셔닝입니다. 텍스처 단계 메타데이터가 여기에 첨부됩니다. | CONDITIONING | 예 | - |
| `negative` | 텍스처 생성 패스에 사용되는 네거티브 컨디셔닝입니다. 텍스처 단계 메타데이터가 여기에 첨부됩니다. | CONDITIONING | 예 | - |
| `shape_latent` | Trellis2ShapeStage 또는 Trellis2UpsampleStage에서 생성된 잠재 변수 사전(dict)입니다. `coords`(좌표 레이아웃, 형태 [N, 4])와 `samples`(복셀당 shape 잠재 변수)를 포함해야 하며, `coord_resolution`과 `model_frame`은 선택 사항입니다. | LATENT | 예 | - |

참고:
- `shape_latent`은(는) Trellis2ShapeStage 또는 Trellis2UpsampleStage의 출력이어야 합니다. 텍스처 패스에서 사용하는 좌표 레이아웃과 복셀당 shape 잠재 변수를 제공합니다.
- 좌표 레이아웃의 유효성이 검사됩니다. `coords`의 첫 번째 열에 있는 배치 ID는 음수가 아니고 연속적이어야 하며, 총 행 수가 좌표 개수와 일치해야 합니다.
- `positive`에 프로젝션 피처 팩(Pixal3D 컨디셔닝)이 포함되어 있고 `shape_latent`에 `coord_resolution`이 포함된 경우, 1024 텍스처 해상도의 프로젝션 피처가 계산되어 컨디셔닝에 첨부됩니다.
- 모델 프레임은 `shape_latent`에서 읽습니다. 없는 경우, 프로젝션 피처가 있으면 `"y_up"`으로, 그렇지 않으면 `"z_up"`으로 기본 설정됩니다.

## 출력

| Output Name | Description | Data Type |
|-------------|-------------|-----------|
| `positive` | 텍스처 단계 메타데이터가 첨부된 포지티브 컨디셔닝입니다(해당되는 경우 생성 모드, 좌표, 좌표 개수, shape 잠재 변수, 모델 프레임, 프로젝션 피처 포함). | CONDITIONING |
| `negative` | 동일한 텍스처 단계 메타데이터가 첨부된 네거티브 컨디셔닝입니다. | CONDITIONING |
| `latent` | 입력 shape 잠재 변수와 동일한 좌표 레이아웃에 32개 채널을 가진 새로운 빈 희소 잠재 변수입니다. 해당 사전에는 `samples`, `type`("trellis2"), `coords`, `coord_counts`, `model_frame`이 포함되며, `coord_resolution`은 사용 가능한 경우 포함됩니다. | LATENT |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Trellis2TextureStage/ko.md)

---
**Source fingerprint (SHA-256):** `ae612021af7c74cd09206d905e7b800fa48367a22daf9b0335b444c854a78b1e`
