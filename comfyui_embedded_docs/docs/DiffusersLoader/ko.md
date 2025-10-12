> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DiffusersLoader/ko.md)

DiffusersLoader 노드는 diffusers 형식으로 사전 학습된 모델을 불러옵니다. 이 노드는 model_index.json 파일을 포함하는 유효한 diffusers 모델 디렉토리를 검색하여 이를 MODEL, CLIP, VAE 구성 요소로 불러와 파이프라인에서 사용할 수 있게 합니다. 이 노드는 더 이상 사용되지 않는(deprecated) 로더 범주에 속하며 Hugging Face diffusers 모델과의 호환성을 제공합니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `모델 경로` | STRING | 예 | 여러 옵션 사용 가능<br>(diffusers 폴더에서 자동으로 채워짐) | 불러올 diffusers 모델 디렉토리의 경로입니다. 이 노드는 구성된 diffusers 폴더에서 유효한 diffusers 모델을 자동으로 스캔하고 사용 가능한 옵션을 나열합니다. |

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `MODEL` | MODEL | diffusers 형식에서 불러온 모델 구성 요소 |
| `CLIP` | CLIP | diffusers 형식에서 불러온 CLIP 모델 구성 요소 |
| `VAE` | VAE | diffusers 형식에서 불러온 VAE (Variational Autoencoder) 구성 요소 |
