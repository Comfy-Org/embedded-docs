# 빈 잠재 비디오 (LTXV)

```markdown
EmptyLTXVLatentVideo 노드는 비디오 생성을 위한 빈 잠재 텐서를 생성합니다. 지정된 너비, 높이, 길이 및 배치 크기로 0으로 채워진 잠재 표현을 생성하며, LTXV 비디오 워크플로에서 시작점으로 사용할 준비가 되어 있습니다. 잠재 표현은 비디오를 압축된 형태로 저장합니다: 공간 차원은 32로 나누어지고 프레임 수는 8분의 1로 감소합니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 여부 | 범위 |
| --- | --- | --- | --- | --- |
| `width` | 잠재 비디오의 너비(픽셀 단위, 기본값: 768, 간격: 32) | INT | 예 | 64 to MAX_RESOLUTION |
| `height` | 잠재 비디오의 높이(픽셀 단위, 기본값: 512, 간격: 32) | INT | 예 | 64 to MAX_RESOLUTION |
| `length` | 잠재 비디오의 프레임 수(기본값: 97, 간격: 8) | INT | 예 | 1 to MAX_RESOLUTION |
| `batch_size` | 배치에서 생성할 잠재 비디오의 수(기본값: 1) | INT | 아니오 | 1 to 4096 |

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
| --- | --- | --- |
| `samples` | 0으로 채워진 빈 잠재 텐서입니다. 잠재 표현에는 너비와 높이에 적용된 공간 다운스케일링을 설명하는 `downscale_ratio_spacial` 값 32도 포함되어 있습니다. | LATENT |
```

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyLTXVLatentVideo/ko.md)

---
**Source fingerprint (SHA-256):** `0b1e57baf9730d852b03b6bccbb8a033e2be9b9cd2420a0aa3638c31f6d3cd26`
