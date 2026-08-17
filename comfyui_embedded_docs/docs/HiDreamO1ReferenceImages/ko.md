# HiDream-O1 Reference Images

## 개요

참조 이미지를 긍정 및 부정 컨디셔닝 모두에 첨부합니다. 이 노드를 사용하면 하나 이상의 참조 이미지를 제공하여 이미지 생성 프로세스를 안내할 수 있으며, 지시문 기반 편집 또는 피사체 기반 개인화에 사용할 수 있습니다.

## 입력

| 매개변수 | 설명 | 데이터 유형 | 필수 | 범위 |
| --- | --- | --- | --- | --- |
| `positive` | 참조 이미지를 첨부할 긍정 컨디셔닝입니다. | CONDITIONING | 예 | - |
| `negative` | 참조 이미지를 첨부할 부정 컨디셔닝입니다. | CONDITIONING | 예 | - |
| `images` | 참조 이미지입니다. 이미지 1개는 지시문 기반 편집을 의미하고, 2~10개는 다중 참조를 의미합니다. | IMAGE | 예 | 이미지 1~10개 |

**`images` 매개변수 참고 사항:** 이 입력은 자동으로 증가하며 1~10개의 이미지를 허용합니다. 이미지는 `image_1`부터 `image_10`까지 레이블이 지정됩니다. 최소 1개의 이미지를 제공해야 합니다. 이미지 수에 따라 작동 모드가 결정됩니다. 단일 이미지는 편집 지시문에 사용되고, 여러 이미지(2~10개)는 피사체 기반 개인화에 사용됩니다.

## 출력

| 출력 이름 | 설명 | 데이터 유형 |
| --- | --- | --- |
| `positive` | 참조 이미지가 첨부된 긍정 컨디셔닝입니다. | CONDITIONING |
| `negative` | 참조 이미지가 첨부된 부정 컨디셔닝입니다. | CONDITIONING |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HiDreamO1ReferenceImages/ko.md)

---
**Source fingerprint (SHA-256):** `f05f6be19df8b8697a98507163e8f60fd0cf2048c81f92597d2ae0a3395b8c6d`
