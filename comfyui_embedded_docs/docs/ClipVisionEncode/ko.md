> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPVisionEncode/ko.md)

`CLIP Vision Encode` 노드는 ComfyUI의 이미지 인코딩 노드로, CLIP Vision 모델을 통해 입력 이미지를 시각적 특징 벡터로 변환합니다. 이 노드는 이미지와 텍스트 이해를 연결하는 중요한 브릿지 역할을 하며, 다양한 AI 이미지 생성 및 처리 워크플로우에서 널리 사용됩니다.

**노드 기능**

- **이미지 특징 추출**: 입력 이미지를 고차원 특징 벡터로 변환합니다.
- **멀티모달 연결**: 이미지와 텍스트의 공동 처리를 위한 기반을 제공합니다.
- **조건부 생성**: 이미지 기반 조건부 생성을 위한 시각적 조건을 제공합니다.

## 입력

| 매개변수명     | 데이터 타입    | 설명                                                         |
| -------------- | -----------  | ------------------------------------------------------------ |
| `clip_vision`  | CLIP_VISION  | CLIP Vision 모델로, 일반적으로 CLIPVisionLoader 노드를 통해 로드됩니다. |
| `image`        | IMAGE        | 인코딩할 입력 이미지입니다.                                   |
| `crop`         | 드롭다운     | 이미지 자르기 방법입니다. 옵션: center (중앙 자르기), none (자르지 않음) |

## 출력

| 출력명              | 데이터 타입          | 설명                 |
| ------------------- | ------------------ | -------------------- |
| CLIP_VISION_OUTPUT  | CLIP_VISION_OUTPUT | 인코딩된 시각적 특징입니다. |

이 출력 객체에는 다음이 포함됩니다:

- `last_hidden_state`: 마지막 은닉 상태
- `image_embeds`: 이미지 임베딩 벡터
- `penultimate_hidden_states`: 마지막에서 두 번째 은닉 상태
- `mm_projected`: 멀티모달 투영 결과 (사용 가능한 경우)