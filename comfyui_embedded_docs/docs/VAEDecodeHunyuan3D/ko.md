# VAEDecodeHunyuan3D

VAEDecodeHunyuan3D 노드는 VAE 디코더를 사용하여 잠재 표현을 3D 복셀 데이터로 변환합니다. 구성 가능한 청크 분할 및 해상도 설정을 통해 VAE 모델로 잠재 샘플을 처리하여 3D 응용 프로그램에 적합한 체적 데이터를 생성합니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
| --- | --- | --- | --- | --- |
| `samples` | 3D 복셀 데이터로 디코딩될 잠재 표현입니다. | LATENT | 예 | - |
| `vae` | 잠재 샘플을 디코딩하는 데 사용되는 VAE 모델입니다. | VAE | 예 | - |
| `num_chunks` | 메모리 관리를 위해 처리를 분할할 청크 수입니다 (기본값: 8000). | INT | 예 | 1000-500000 |
| `octree_resolution` | 3D 복셀 생성에 사용되는 옥트리 구조의 해상도입니다 (기본값: 256). | INT | 예 | 16-512 |

참고: `num_chunks`와 `octree_resolution`은 고급 매개변수입니다.

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
| --- | --- | --- |
| `voxels` | 디코딩된 잠재 표현에서 생성된 3D 복셀 데이터입니다. | VOXEL |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEDecodeHunyuan3D/ko.md)

---
**Source fingerprint (SHA-256):** `740e328e9e7817aa1a029c5fadddf5457c91bbb5ac12c7e8af2cd81bee6184a7`
