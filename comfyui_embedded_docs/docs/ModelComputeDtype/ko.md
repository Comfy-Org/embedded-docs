# ModelComputeDtype

ModelComputeDtype 노드는 처리 중에 모델이 사용하는 계산 데이터 유형(정밀도)을 변경합니다. 입력 모델의 복사본을 만들고 선택한 정밀도 설정을 적용하므로, 하드웨어에 따라 메모리 사용량과 성능을 최적화하는 데 도움이 될 수 있습니다. 이는 다양한 정밀도 구성을 디버깅하고 테스트하는 데 유용합니다.

## 입력

| 매개변수 | 설명 | 데이터 유형 | 필수 | 범위 |
| --- | --- | --- | --- | --- |
| `model` | 새 계산 데이터 유형으로 수정할 입력 모델 | MODEL | 예 | - |
| `dtype` | 모델에 적용할 계산 데이터 유형(기본값: "default"). 이 매개변수는 UI에서 고급 설정으로 표시됩니다. | COMBO | 예 | "default"<br>"fp32"<br>"fp16"<br>"bf16" |

## 출력

| 출력 이름 | 설명 | 데이터 유형 |
| --- | --- | --- |
| `model` | 새 계산 데이터 유형이 적용된 수정된 모델 | MODEL |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelComputeDtype/ko.md)

---
**Source fingerprint (SHA-256):** `ad9c39e1217fd2e343ad4f49df9d1acabbc4708966dadec5340bb975adb59854`
