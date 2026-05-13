> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateHookModelAsLoraModelOnly/ko.md)

이 문서는 AI가 생성했습니다. 오류를 발견하거나 개선 제안이 있으시면 언제든지 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateHookModelAsLoraModelOnly/en.md)

이 노드는 LoRA(저차원 적응) 모델을 적용하여 신경망의 모델 구성 요소만 수정하는 훅을 생성합니다. 체크포인트 파일을 로드하고 지정된 강도로 모델에 적용하며, CLIP 구성 요소는 변경하지 않습니다. 이는 기본 CreateHookModelAsLora 클래스의 기능을 확장한 실험적 노드입니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `체크포인트 파일명` | STRING | 예 | 여러 옵션 사용 가능 | LoRA 모델로 로드할 체크포인트 파일입니다. 사용 가능한 옵션은 체크포인트 폴더 내용에 따라 달라집니다. |
| `모델 강도` | FLOAT | 예 | -20.0 ~ 20.0 | 모델 구성 요소에 LoRA를 적용할 강도 승수입니다(기본값: 1.0) |
| `이전 후크` | HOOKS | 아니요 | - | 이 훅과 연결할 이전 훅(선택 사항) |

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `hooks` | HOOKS | LoRA 모델 수정이 포함된 생성된 훅 그룹입니다. |

---
**Source fingerprint (SHA-256):** `adbeaede65aa89d48c59225ca1c8edc4c9394a364f93a00dae4a83a2270f093b`
