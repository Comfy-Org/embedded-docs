# CLIP 로드

CLIPLoader 노드는 파일에서 텍스트 인코더 모델(CLIP, T5 또는 유사 모델)을 로드하여, 텍스트 프롬프트를 숫자 표현으로 변환해야 하는 다른 노드에서 사용할 수 있도록 제공합니다. 다양한 모델 아키텍처를 지원하며, 각 아키텍처는 특정 인코더 유형이 필요합니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
|-----------|-------------|-----------|----------|-------|
| `clip_name` | 로드할 텍스트 인코더 모델의 파일 이름입니다. 이 파일은 `ComfyUI/models/text_encoders/` 디렉터리에 있어야 합니다. | COMBO | 예 | `text_encoders` 폴더에서 찾은 파일 목록 |
| `type` | 로드 중인 모델의 아키텍처 유형입니다. 이 값은 사용할 특정 인코더 변형을 결정합니다(기본값: `"stable_diffusion"`). | COMBO | 예 | `"stable_diffusion"`<br>`"stable_cascade"`<br>`"sd3"`<br>`"stable_audio"`<br>`"mochi"`<br>`"ltxv"`<br>`"pixart"`<br>`"cosmos"`<br>`"lumina2"`<br>`"wan"`<br>`"hidream"`<br>`"chroma"`<br>`"ace"`<br>`"omnigen2"`<br>`"qwen_image"`<br>`"hunyuan_image"`<br>`"flux2"`<br>`"ovis"`<br>`"longcat_image"`<br>`"cogvideox"`<br>`"lens"`<br>`"pixeldit"`<br>`"ideogram4"`<br>`"boogu"`<br>`"krea2"`<br>`"joyimage"`<br>`"mage"`<br>`"minimax"` |
| `device` | 모델을 로드할 장치입니다. `"default"`는 기본 장치(일반적으로 GPU 사용 가능 시 GPU)를 사용하며, `"cpu"`는 CPU 로딩을 강제합니다. 이는 고급 옵션입니다(기본값: `"default"`). | COMBO | 아니요 | `"default"`<br>`"cpu"` |

### 지원되는 유형-인코더 매핑

`type` 매개변수는 주어진 모델 아키텍처에 대해 올바른 인코더를 선택합니다. 다음 일반적인 매핑은 노드 설명에 나열되어 있습니다.

| 유형 | 인코더 |
|------|---------|
| stable_diffusion | clip-l |
| stable_cascade | clip-g |
| sd3 | t5 xxl / clip-g / clip-l |
| stable_audio | t5 base |
| mochi | t5 xxl |
| cogvideox | t5 xxl (226-토큰 패딩) |
| cosmos | old t5 xxl |
| lumina2 | gemma 2 2B |
| wan | umt5 xxl |
| hidream | llama-3.1(권장) 또는 t5 |
| omnigen2 | qwen vl 2.5 3B |
| joyimage | qwen3-vl 8B |
| lens | gpt-oss-20b |
| pixeldit | gemma 2 2B elm |
| minimax | MiniMax H3 Qwen3-VL 또는 Music3 Qwen/RVQ |

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
|-------------|-------------|-----------|
| `clip` | 로드된 텍스트 인코더 모델로, 텍스트 인코딩 및 컨디셔닝을 위해 다른 노드에 연결할 준비가 되었습니다. | CLIP |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPLoader/ko.md)

---
**Source fingerprint (SHA-256):** `7c1586d01410d319468f7c8c153ef0717280804add868ba57bff0c6539fb5dd9`
