# LTXV 가이드 자르기

`LTXVCropGuides` 노드는 키프레임 정보를 제거하고 잠재 변수(latent)의 크기를 조정하여 비디오 생성용 conditioning 및 latent 입력을 처리합니다. 이 노드는 키프레임 구간을 제외하도록 latent 이미지와 노이즈 마스크를 잘라내고, positive 및 negative conditioning 입력에서 키프레임 인덱스를 제거합니다. 이를 통해 키프레임 안내가 필요하지 않은 비디오 생성 워크플로우에 데이터를 준비합니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
| --- | --- | --- | --- | --- |
| `positive` | 생성을 위한 안내 정보가 포함된 positive conditioning 입력 | CONDITIONING | 예 | - |
| `negative` | 생성 시 피해야 할 내용에 대한 안내 정보가 포함된 negative conditioning 입력 | CONDITIONING | 예 | - |
| `latent` | 이미지 샘플과 노이즈 마스크 데이터가 포함된 잠재 변수 표현 | LATENT | 예 | - |

참고: positive conditioning에 키프레임 인덱스가 없으면 이 노드는 positive, negative, latent 입력을 변경하지 않고 그대로 반환합니다.

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
| --- | --- | --- |
| `positive` | 키프레임 인덱스와 가이드 어텐션 항목이 제거된 처리된 positive conditioning | CONDITIONING |
| `negative` | 키프레임 인덱스와 가이드 어텐션 항목이 제거된 처리된 negative conditioning | CONDITIONING |
| `latent` | 키프레임 구간이 제거되어 샘플과 노이즈 마스크가 조정된, 잘려진 잠재 변수 표현 | LATENT |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVCropGuides/ko.md)

---
**Source fingerprint (SHA-256):** `83e08bad281902e765ec18e06144b6a5fa730be2533932daa1d4076e6390b1e1`
