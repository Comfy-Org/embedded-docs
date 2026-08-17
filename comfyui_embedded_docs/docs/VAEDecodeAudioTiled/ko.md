# VAE 오디오 디코드 (타일)

이 노드는 VAE(Variational Autoencoder)를 사용하여 압축된 오디오 표현(잠재 샘플)을 오디오 파형으로 다시 변환합니다. 메모리 사용을 관리하기 위해 데이터를 더 작고 겹치는 섹션(타일)으로 처리하므로 긴 오디오 시퀀스를 처리하는 데 적합합니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
| --- | --- | --- | --- | --- |
| `samples` | 디코딩할 오디오의 압축된 잠재 표현입니다. | LATENT | 예 | N/A |
| `vae` | 디코딩을 수행하는 데 사용되는 VAE 모델입니다. | VAE | 예 | N/A |
| `tile_size` | 각 처리 타일의 크기입니다. 오디오는 메모리를 절약하기 위해 이 길이의 섹션으로 디코딩됩니다(기본값: 512). | INT | 예 | 32 to 8192 |
| `overlap` | 인접한 타일이 겹치는 샘플 수입니다. 타일 경계에서 아티팩트를 줄이는 데 도움이 됩니다(기본값: 64). | INT | 예 | 0 to 1024 |

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
| --- | --- | --- |
| `output` | 디코딩된 오디오 파형입니다. | AUDIO |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEDecodeAudioTiled/ko.md)

---
**Source fingerprint (SHA-256):** `5ddedf218ba27ab9f463646c1e5288091172f2d7fae8f2980bb2b5e4d3dca89c`
