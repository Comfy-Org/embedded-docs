> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PixverseImageToVideoNode/ko.md)

# PixverseImageToVideoNode

입력 이미지와 텍스트 프롬프트를 기반으로 비디오를 생성합니다. 이 노드는 이미지를 입력받아 지정된 모션 및 품질 설정을 적용하여 정적 이미지를 움직이는 시퀀스로 변환함으로써 애니메이션 비디오를 생성합니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | 예 | - | 비디오로 변환할 입력 이미지 |
| `prompt` | STRING | 예 | - | 비디오 생성을 위한 프롬프트 |
| `quality` | COMBO | 예 | `res_540p`<br>`res_1080p` | 비디오 품질 설정 (기본값: res_540p) |
| `duration_seconds` | COMBO | 예 | `dur_2`<br>`dur_5`<br>`dur_10` | 생성된 비디오의 길이(초) |
| `motion_mode` | COMBO | 예 | `normal`<br>`fast`<br>`slow`<br>`zoom_in`<br>`zoom_out`<br>`pan_left`<br>`pan_right`<br>`pan_up`<br>`pan_down`<br>`tilt_up`<br>`tilt_down`<br>`roll_clockwise`<br>`roll_counterclockwise` | 비디오 생성에 적용되는 모션 스타일 |
| `seed` | INT | 예 | 0-2147483647 | 비디오 생성을 위한 시드 (기본값: 0) |
| `negative_prompt` | STRING | 아니요 | - | 이미지에서 원하지 않는 요소에 대한 선택적 텍스트 설명 |
| `pixverse_template` | CUSTOM | 아니요 | - | PixVerse 템플릿 노드에서 생성된, 생성 스타일에 영향을 주는 선택적 템플릿 |

**참고:** 1080p 품질을 사용하는 경우 모션 모드가 자동으로 normal로 설정되고 지속 시간이 5초로 제한됩니다. 5초 이외의 지속 시간을 사용하는 경우에도 모션 모드가 자동으로 normal로 설정됩니다.

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `output` | VIDEO | 입력 이미지와 매개변수를 기반으로 생성된 비디오 |

---
**Source fingerprint (SHA-256):** `7630c662a2506fb0c8be0cb9c6bfdfcf0fc06d2b6f16b8636664d587affededc`
