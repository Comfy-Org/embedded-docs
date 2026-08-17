# 기본 가이드

BasicGuider 노드는 샘플링 과정을 위한 간단한 가이드 메커니즘을 생성합니다. 모델과 컨디셔닝 데이터를 입력으로 받아 샘플링 중 생성 과정을 안내하는 데 사용할 수 있는 가이더 객체를 생성합니다. 이 노드는 제어된 생성을 위해 필요한 기본적인 가이드 기능을 제공합니다.

## 입력

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `model` | 가이드에 사용할 모델 | MODEL | 예 | - |
| `conditioning` | 생성 과정을 안내하는 컨디셔닝 데이터 | CONDITIONING | 예 | - |

## 출력

| Output Name | Description | Data Type |
| --- | --- | --- |
| `GUIDER` | 샘플링 과정 중 생성을 안내하는 데 사용할 수 있는 가이더 객체 | GUIDER |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BasicGuider/ko.md)

---
**Source fingerprint (SHA-256):** `8ea6b56be58ae99baaf13a04c4fadbf8ad921801d8f2ce2aecce768cc34a3b20`
