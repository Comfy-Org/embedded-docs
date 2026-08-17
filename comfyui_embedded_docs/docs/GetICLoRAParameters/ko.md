# IC-LoRA 파라미터 가져오기

## 개요

이 노드는 LoRA가 로드된 모델의 메타데이터에서 IC-LoRA 매개변수를 추출합니다. safetensors 메타데이터를 읽어 참조 다운스케일 계수(reference downscale factor)와 같은 값을 찾은 후, 이를 구조화된 매개변수 객체로 출력합니다. 이 객체는 특수 가이드 처리를 위해 LTXVAddGuide 노드에 연결할 수 있습니다. 메타데이터가 없거나 참조 다운스케일 계수를 읽을 수 없는 경우 값은 기본적으로 1로 설정됩니다. 값을 찾은 경우에는 반올림된 후 최소값 1로 제한됩니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
| --- | --- | --- | --- | --- |
| `iclora_model` | 메타데이터를 추출할 특정 IC-LoRA에 대한 LoRA 로더의 직접 출력입니다. | MODEL | 예 | N/A |

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
| --- | --- | --- |
| `iclora_parameters` | LoRA 메타데이터에서 추출한 IC-LoRA 매개변수입니다(예: reference_downscale_factor). LoRA가 가이드에 대한 특별 처리를 요구하는 경우 LTXVAddGuide에 연결하십시오. | IC_LORA_PARAMETERS |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GetICLoRAParameters/ko.md)

---
**Source fingerprint (SHA-256):** `5f6becad0c7673b8cde1e099bd7ba5be7106da958b8967f8e693ba2a704baaef`
