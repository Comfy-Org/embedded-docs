> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Hunyuan3Dv2Conditioning/ko.md)

Hunyuan3Dv2Conditioning 노드는 CLIP 비전 출력을 처리하여 비디오 모델을 위한 조건화 데이터를 생성합니다. 비전 출력에서 마지막 은닉 상태 임베딩을 추출하고 긍정적 및 부정적 조건화 쌍을 모두 생성합니다. 긍정적 조건화는 실제 임베딩을 사용하는 반면, 부정적 조건화는 동일한 형태의 0값 임베딩을 사용합니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `clip_vision_output` | CLIP_VISION_OUTPUT | 예 | - | 시각적 임베딩을 포함하는 CLIP 비전 모델의 출력 |

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | CLIP 비전 임베딩을 포함하는 긍정적 조건화 데이터 |
| `negative` | CONDITIONING | 긍정적 임베딩 형태와 일치하는 0값 임베딩을 포함하는 부정적 조건화 데이터 |