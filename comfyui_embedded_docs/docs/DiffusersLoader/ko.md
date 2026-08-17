# Diffusers 로드

`DiffusersLoader` 노드는 더 이상 사용되지 않습니다(deprecated). 이 노드는 Hugging Face diffusers 형식으로 저장된 사전 학습된 모델을 불러와 파이프라인에 필요한 세 가지 표준 구성 요소인 MODEL, CLIP, VAE를 반환합니다. 노드는 구성된 diffusers 폴더에서 유효한 모델 디렉터리(`model_index.json` 파일이 포함된 폴더)를 자동으로 검색하고, 로드할 모델을 선택할 수 있게 해 줍니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
|-----------|-------------|-----------|----------|-------|
| `model_path` | 로드할 diffusers 모델 디렉터리 경로입니다. 노드는 구성된 diffusers 폴더를 검색하고 `model_index.json` 파일이 포함된 모든 디렉터리를 나열합니다. | COMBO | 예 | 구성된 diffusers 폴더에서 자동으로 채워짐(`model_index.json` 파일이 포함된 모든 하위 디렉터리) |

참고: 선택한 경로는 발견된 모델 목록과 대조하여 검증됩니다. 경로가 더 이상 목록에 없거나 모델 디렉터리를 찾을 수 없으면 오류와 함께 로드가 실패합니다.

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
|-------------|-------------|-----------|
| `MODEL` | diffusers 형식에서 로드된 모델 구성 요소입니다. | MODEL |
| `CLIP` | diffusers 형식에서 로드된 CLIP 텍스트 인코딩 모델 구성 요소입니다. | CLIP |
| `VAE` | diffusers 형식에서 로드된 VAE(변분 오토인코더) 구성 요소입니다. | VAE |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DiffusersLoader/ko.md)

---
**Source fingerprint (SHA-256):** `75238342d05eac7528f981a2d4544accb6053891cd078a77751cc838054225d4`
