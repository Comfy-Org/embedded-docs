# MiniMax Hailuo 비디오

MiniMax Hailuo-02 모델을 사용하여 텍스트 프롬프트에서 비디오를 생성합니다. 선택적으로 시작 이미지를 첫 번째 프레임으로 제공하여 해당 이미지에서 이어지는 비디오를 만들 수 있습니다.

## 입력

| 매개변수 | 설명 | 데이터 유형 | 필수 여부 | 범위 |
|-----------|-------------|-----------|----------|-------|
| `prompt_text` | 비디오 생성을 안내하는 텍스트 프롬프트입니다. | STRING | 예 | - |
| `seed` | 노이즈를 생성하는 데 사용되는 무작위 시드입니다 (기본값: 0). | INT | 아니요 | 0 to 18446744073709551615 |
| `first_frame_image` | 비디오 생성을 위해 첫 번째 프레임으로 사용할 선택적 이미지입니다. | IMAGE | 아니요 | - |
| `prompt_optimizer` | 필요 시 생성 품질을 향상시키기 위해 프롬프트를 최적화합니다 (기본값: True). | BOOLEAN | 아니요 | - |
| `duration` | 출력 비디오의 길이(초)입니다 (기본값: 6). | COMBO | 아니요 | `6`<br>`10` |
| `resolution` | 비디오 디스플레이의 해상도입니다. 1080p는 1920x1080, 768p는 1366x768입니다 (기본값: "768P"). | COMBO | 아니요 | `"768P"`<br>`"1080P"` |

**참고 사항:**
- `first_frame_image`가 제공되지 않으면 `prompt_text`는 비어 있지 않은 문자열이어야 합니다.
- MiniMax-Hailuo-02 모델을 1080P 해상도로 사용할 때 비디오 길이는 6초로 제한됩니다.

## 출력

| 출력 이름 | 설명 | 데이터 유형 |
|-------------|-------------|-----------|
| `output` | 생성된 비디오 파일입니다. | VIDEO |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuoVideoNode/ko.md)

---
**Source fingerprint (SHA-256):** `f371aae15cfbe7353236bc679c8a6d558703c5037e49ab7ddb9bdf5c50ef0995`
