# 학습 데이터셋 저장

이 노드는 준비된 학습 데이터셋을 컴퓨터의 하드 드라이브에 저장합니다. 이미지 잠재(latent)와 해당 텍스트 컨디셔닝을 포함하는 인코딩된 데이터를 입력받아, 관리하기 쉽도록 샤드(shard)라고 하는 여러 개의 작은 파일로 정리합니다. 이 노드는 datasets 디렉토리에 폴더를 자동으로 생성하고, 샤드 데이터 파일과 데이터셋을 설명하는 메타데이터 파일을 모두 저장합니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
| --- | --- | --- | --- | --- |
| `latents` | MakeTrainingDataset에서 생성된 잠재(latent) dict 목록입니다. | LATENT | 예 | 해당 없음 |
| `conditioning` | MakeTrainingDataset에서 생성된 컨디셔닝 리스트로 이루어진 목록입니다. | CONDITIONING | 예 | 해당 없음 |
| `folder_name` | datasets 디렉토리 안에서 데이터셋을 저장할 폴더 이름입니다. 'project/run1'과 같은 하위 폴더도 허용됩니다. (기본값: "training_dataset") | STRING | 예 | 해당 없음 |
| `shard_size` | 샤드 파일당 샘플 수입니다. (기본값: 1000) | INT | 예 | 1~100000 |

**참고:** `latents` 목록의 항목 수는 `conditioning` 목록의 항목 수와 정확히 일치해야 합니다. 이 개수가 일치하지 않으면 노드에서 오류가 발생합니다. `folder_name`은 datasets 디렉토리의 하위 폴더를 지정해야 합니다. datasets 루트 폴더 자체나 이를 벗어나는 경로(예: '..' 또는 절대 경로)는 거부됩니다.

## 출력

이 노드는 출력 데이터를 생성하지 않습니다. datasets 디렉토리의 선택한 폴더 안에 번호가 매겨진 샤드 파일(예: `shard_0000.pkl`)과 `metadata.json` 파일로 데이터셋을 저장합니다.

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveTrainingDataset/ko.md)

---
**Source fingerprint (SHA-256):** `6d7b63a24ac42907b0f4a1358712cd0ed085982ecd308bce87e5376d9bbc2274`
