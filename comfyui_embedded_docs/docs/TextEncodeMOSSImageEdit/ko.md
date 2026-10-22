# Text Encode MOSS-Image Edit

편집 지시문을 참조 이미지와 함께 MOSS-Image edit LoRA용 conditioning으로 인코딩합니다. 출력을 positive conditioning으로 연결하고, 동일한 참조를 사용하여 negative conditioning용으로 두 번째 인스턴스를 실행합니다. 참조는 입력된 크기 그대로 사용되므로 연결하기 전에 크기를 조정해야 합니다. 이 노드는 ComfyUI에서 실험적(experimental)으로 표시되어 있습니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
| --- | --- | --- | --- | --- |
| `clip` | 지시문을 토큰화하고 인코딩하는 CLIP 모델입니다. | CLIP | 예 | - |
| `prompt` | 편집을 설명하는 지시문입니다. 여러 줄 텍스트와 동적 프롬프트를 지원합니다. | STRING | 예 | 모든 텍스트 |
| `vae` | 참조 이미지를 참조 latent로 인코딩하는 데 사용되는 VAE입니다. | VAE | 예 | - |
| `edit_format` | 편집 LoRA가 학습된 레이아웃입니다. 참조 latent 메서드와 텍스트 인코더가 참조도 보는지 여부를 선택합니다. | COMBO | 예 | `"ai-toolkit"`<br>`"ai-toolkit (kv_cache off)"`<br>`"Moss-Image-Edit"` |
| `images` | 확장 가능한 슬롯: 하나 이상의 참조 이미지(`image_1`, `image_2`, ...)를 연결합니다. 각 이미지는 입력된 크기로 사용되며, 알파 채널이 제거되고 VAE로 인코딩되어 참조 latent가 됩니다. | IMAGE | 예 | 이미지 1개 이상 |

**참고:** `"ai-toolkit"` 및 `"ai-toolkit (kv_cache off)"`의 경우 텍스트 인코더도 모든 참조를 보며, 참조는 최대 384x384픽셀로 축소되고 프롬프트에서 `Picture N:` 마커가 앞에 붙습니다. 따라서 지시문에서 참조를 번호로 가리킬 수 있습니다. `"Moss-Image-Edit"`의 경우 참조는 참조 latent로만 모델에 전달되며, 텍스트 인코더는 지시문만 봅니다. `"ai-toolkit (kv_cache off)"`는 추가로 참조가 생성 중인 이미지에 계속 어텐션하도록 유지하므로, 매 샘플링 단계마다 다시 계산됩니다.

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
| --- | --- | --- |
| `conditioning` | 참조 latent와 해당 참조 latent 메서드가 첨부된 인코딩된 지시문입니다. | CONDITIONING |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeMOSSImageEdit/ko.md)

---
**Source fingerprint (SHA-256):** `30e4edbb129f647cdce4ec95f78c002ecdc9a4f8fc5a45f1477fdc555b541dae`
