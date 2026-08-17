# Kling 비디오 생성 (텍스트 → 비디오)

Kling Text to Video 노드는 Kling 비디오 생성 서비스를 사용하여 텍스트 프롬프트를 짧은 비디오 클립으로 변환합니다. 긍정 및 부정 프롬프트와 함께 화면 비율, 구성 척도, 생성 모드 등의 설정을 제공하면 노드는 생성된 비디오와 해당 식별자 및 지속 시간을 반환합니다.

## 입력

| 매개변수 | 설명 | 데이터 유형 | 필수 | 범위 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 원하는 비디오 내용을 설명하는 긍정 텍스트 프롬프트입니다. 여러 줄 입력이 가능합니다. 비워 둘 수 없습니다. | STRING | 예 | 최대 2500자 |
| `negative_prompt` | 비디오에서 피해야 할 내용을 설명하는 부정 텍스트 프롬프트입니다. 여러 줄 입력이 가능합니다. 비워 둘 수 있습니다. | STRING | 예 | 최대 2500자 |
| `cfg_scale` | 비디오가 프롬프트를 얼마나 밀접하게 따르는지 제어하는 구성 척도 값입니다(기본값: 1.0). | FLOAT | 아니요 | 0.0~1.0 |
| `aspect_ratio` | 비디오 화면 비율 설정입니다(기본값: "16:9"). | COMBO | 아니요 | `"16:9"`<br>`"9:16"`<br>`"1:1"` |
| `mode` | 모드 / 지속 시간 / 모델 이름 형식에 따라 비디오 생성에 사용할 구성입니다(기본값: "pro mode / 5s duration / kling-v2-5-turbo"). 5초 모드는 USD 0.35, 10초 모드는 USD 0.70입니다. | COMBO | 아니요 | `"pro mode / 5s duration / kling-v2-5-turbo"`<br>`"pro mode / 10s duration / kling-v2-5-turbo"` |

## 출력

| 출력 이름 | 설명 | 데이터 유형 |
|-------------|-------------|-----------|
| `output` | 생성된 비디오 출력입니다. | VIDEO |
| `video_id` | 생성된 비디오의 고유 식별자입니다. | STRING |
| `duration` | 생성된 비디오의 지속 시간 정보입니다. | STRING |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingTextToVideoNode/ko.md)

---
**Source fingerprint (SHA-256):** `6a63b0b8bc45dc5a6300cdfe7a373399eeead36de6727f7aae2c026ba0deaea8`
