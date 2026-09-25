# ByteDance Seedance 2.0 첫-마지막 프레임에서 비디오 생성

이 노드는 ByteDance Seedance 모델을 사용하여 필수인 첫 프레임 이미지와 선택적인 마지막 프레임 이미지로부터 비디오를 생성합니다. 텍스트 프롬프트로 비디오를 설명하며, 첫 프레임은 비디오의 시작을, 마지막 프레임은 끝을 안내합니다. Seedance 2.5 및 Seedance 2.0 제품군(Seedance 2.0, Seedance 2.0 Fast, Seedance 2.0 Mini)을 지원합니다. `Seedance 2.5 Draft` 모델을 선택하면 대신 빠른 480p 미리보기를 렌더링합니다. 결과로 생성된 `draft_task_id`를 ByteDance Seedance 2.5 Draft to Final Video 노드에 연결하여 1080p 최종본을 렌더링하세요.

## 입력

### 공통 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
|-----------|-------------|-----------|----------|-------|
| `model` | 최신 모델인 Seedance 2.5는 최대 30초 길이의 비디오와 mp4/mov 출력을 지원합니다. Seedance 2.5 Draft는 빠른 480p 미리보기를 생성하며, 해당 `draft_task_id` 출력을 ByteDance Seedance 2.5 Draft to Final Video 노드에서 사용하면 1080p 최종본을 렌더링합니다. Seedance 2.0은 최대 품질과 4k를 지원합니다. Fast는 속도 최적화에, Mini는 가장 빠르고 저렴한 생성에 적합합니다. 모델을 선택하면 아래에 모델별 입력이 표시됩니다. | DYNAMIC_COMBO | 예 | `"Seedance 2.5"`<br>`"Seedance 2.5 Draft"`<br>`"Seedance 2.0"`<br>`"Seedance 2.0 Fast"`<br>`"Seedance 2.0 Mini"` |
| `first_frame` | 비디오의 첫 프레임 이미지입니다. | IMAGE | 아니요 | - |
| `last_frame` | 비디오의 마지막 프레임 이미지입니다. | IMAGE | 아니요 | - |
| `first_frame_asset_id` | 첫 프레임으로 사용할 Seedance asset_id입니다. `first_frame` 이미지 입력과 함께 사용할 수 없습니다. 기본값은 빈 문자열입니다. | STRING | 아니요 | - |
| `last_frame_asset_id` | 마지막 프레임으로 사용할 Seedance asset_id입니다. `last_frame` 이미지 입력과 함께 사용할 수 없습니다. 기본값은 빈 문자열입니다. | STRING | 아니요 | - |
| `seed` | 시드는 노드의 재실행 여부를 제어합니다. 시드와 관계없이 결과는 비결정적입니다. 기본값은 0입니다. | INT | 예 | 0 ~ 2147483647 |
| `watermark` | 비디오에 워터마크를 추가할지 여부입니다. 기본값은 False입니다. | BOOLEAN | 예 | False<br>True |

### Seedance 2.5 입력

이 입력은 `Seedance 2.5`를 선택하면 표시됩니다.

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 비디오 생성을 위한 텍스트 프롬프트입니다. 대사를 이중 따옴표로 묶으면 생성되는 대화를 유도할 수 있습니다. | STRING | 예 | - |
| `resolution` | 출력 비디오의 해상도입니다. 기본값은 720p입니다. | COMBO | 예 | `"480p"`<br>`"720p"`<br>`"1080p"` |
| `duration` | 출력 비디오의 길이(초)입니다(4-30). 기본값은 5입니다. | INT | 예 | 4 ~ 30 |
| `generate_audio` | 출력 비디오의 오디오 생성을 활성화합니다. 기본값은 True입니다. | BOOLEAN | 예 | False<br>True |
| `output_format` | 출력 비디오의 컨테이너 형식입니다. 기본값은 mp4입니다. | COMBO | 예 | `"mp4"` |

### Seedance 2.5 Draft 입력

이 입력은 `Seedance 2.5 Draft`를 선택하면 표시됩니다. 매개변수 구성은 위의 Seedance 2.5와 동일하지만, `resolution`은 `"480p"`만 제공합니다(기본값 `"480p"`).

### Seedance 2.0 입력

이 입력은 `Seedance 2.0`을 선택하면 표시됩니다.

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 비디오 생성을 위한 텍스트 프롬프트입니다. | STRING | 예 | - |
| `resolution` | 출력 비디오의 해상도입니다. | COMBO | 예 | `"480p"`<br>`"720p"`<br>`"1080p"`<br>`"4k"` |
| `ratio` | 출력 비디오의 화면 비율입니다. 기본값은 `adaptive`이며, 입력 프레임의 화면 비율에 가장 가까운 지원 비율을 사용합니다. | COMBO | 예 | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | 출력 비디오의 길이(초)입니다(4-15). 기본값은 7입니다. | INT | 예 | 4 ~ 15 |
| `generate_audio` | 출력 비디오의 오디오 생성을 활성화합니다. 기본값은 True입니다. | BOOLEAN | 예 | False<br>True |

### Seedance 2.0 Fast 및 Seedance 2.0 Mini 입력

`Seedance 2.0 Fast`와 `Seedance 2.0 Mini`에서 공유됩니다.

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 비디오 생성을 위한 텍스트 프롬프트입니다. | STRING | 예 | - |
| `resolution` | 출력 비디오의 해상도입니다. | COMBO | 예 | `"480p"`<br>`"720p"` |
| `ratio` | 출력 비디오의 화면 비율입니다. 기본값은 `adaptive`이며, 입력 프레임의 화면 비율에 가장 가까운 지원 비율을 사용합니다. | COMBO | 예 | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | 출력 비디오의 길이(초)입니다(4-15). 기본값은 7입니다. | INT | 예 | 4 ~ 15 |
| `generate_audio` | 출력 비디오의 오디오 생성을 활성화합니다. 기본값은 True입니다. | BOOLEAN | 예 | False<br>True |

**매개변수 제약 조건**

- 첫 프레임은 `first_frame` 이미지 또는 `first_frame_asset_id` 중 하나로 반드시 제공해야 합니다. 둘 다 제공하면 오류가 발생하며, 둘 다 제공하지 않아도 오류가 발생합니다.
- `last_frame` 및 `last_frame_asset_id` 입력은 선택 사항이지만, 동일한 프레임에 대해 둘 다 제공할 수 없습니다.
- Asset ID는 존재하는 활성 Seedance Image 에셋을 참조해야 합니다.
- `prompt` 입력은 필수이며 비워 둘 수 없습니다.
- `draft_task_id` 출력은 `Seedance 2.5 Draft`에서만 생성됩니다. 다른 모델에서는 연결하지 않은 상태로 두어야 하며, 그렇지 않으면 실행이 실패합니다.
- `Seedance 2.5`에서는 출력 화면 비율이 항상 adaptive이며 첫 프레임 자체의 화면 비율을 따르므로 `ratio` 입력이 표시되지 않습니다.
- Seedance 2.0 제품군 모델과 로컬 프레임 이미지를 사용하는 경우, 이미지는 생성 전에 중앙 크롭되고 대상 출력 해상도 및 비율에 맞게 크기 조정됩니다. `ratio`가 `adaptive`이면 입력 이미지에 가장 가까운 지원 비율이 사용됩니다.
- 로컬 프레임 이미지는 지원되는 화면 비율과 치수에 대해 검증되며, 너무 큰 이미지는 다운스케일됩니다.

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
|-------------|-------------|-----------|
| `output` | 생성된 비디오입니다. | VIDEO |
| `draft_task_id` | 드래프트 실행의 작업 ID입니다. Seedance 2.5 Draft 모델만 이 출력을 생성합니다. ByteDance Seedance 2.5 Draft to Final Video 노드에 연결하여 1080p 최종본을 렌더링하세요. | STRING |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2FirstLastFrameNode/ko.md)

---
**Source fingerprint (SHA-256):** `363f1baac1685c2dada0e64a0b339f6ab2671161dccb002eb81f6b4f0d0aa243`
