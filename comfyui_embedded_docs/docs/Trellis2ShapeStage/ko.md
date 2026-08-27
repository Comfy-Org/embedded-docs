# Trellis2ShapeStage

이 노드는 Trellis2 파이프라인의 첫 번째 형상 생성 샘플링 패스를 설정합니다. VaeDecodeStructureTrellis2가 생성한 밀집 구조 복셀을 입력받아, 채워진 복셀의 희소 좌표를 추출하고, 빈 희소 latent를 생성한 다음, 샘플링 메타데이터를 컨디셔닝에 첨부하여 모델이 샘플링 중에 이를 읽을 수 있게 합니다. 업샘플링 후의 두 번째 형상 패스에는 Trellis2UpsampleStage를 대신 사용해야 합니다. 이 노드는 캐스케이드와 두 번째 패스 단계 설정을 결합합니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
|-----------|-------------|-----------|----------|-------|
| `positive` | 형상 단계를 준비할 positive 컨디셔닝입니다. 표준 Trellis2 컨디셔닝이거나 투영 특징 팩을 제공하는 Pixal3D 컨디셔닝일 수 있습니다. 투영 특징이 있는 경우 선택된 단계에 대해 계산되어 출력 컨디셔닝에 첨부됩니다. | CONDITIONING | 예 | 모든 Trellis2 또는 Pixal3D 컨디셔닝 |
| `negative` | 형상 단계를 준비할 negative 컨디셔닝입니다. positive 컨디셔닝과 동일한 형상 단계 메타데이터가 첨부됩니다. | CONDITIONING | 예 | 모든 Trellis2 또는 Pixal3D 컨디셔닝 |
| `voxel` | VaeDecodeStructureTrellis2가 생성한 밀집 구조 복셀입니다. | VOXEL | 예 | 모든 복셀 그리드; 그리드 해상도(축당 복셀 수)가 파이프라인 단계를 선택합니다. |

### 참고

- 복셀 그리드 해상도가 파이프라인 단계를 선택합니다. 해상도가 32 이하이면 `shape_generation_512` 모드와 `shape_512` 단계를 사용하고, 32보다 크면 `shape_generation` 모드와 `shape_1024` 단계를 사용합니다.
- 복셀에는 채워진 복셀이 하나 이상 포함되어야 합니다. 빈 복셀이면 오류가 발생합니다. 복셀에서 파생된 배치 인덱스는 0 이상이고 연속적이어야 합니다.
- `positive` 컨디셔닝에 `proj_feat_pack`이 포함되어 있으면(Pixal3D 컨디셔닝에서 제공된 경우) 선택된 단계에 대한 투영 특징이 계산되고 출력 latent의 모델 프레임이 `y_up`으로 설정됩니다. 그렇지 않으면 투영 특징이 첨부되지 않고 모델 프레임이 `z_up`으로 설정됩니다.

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
|-------------|-------------|-----------|
| `positive` | 형상 단계 메타데이터(생성 모드, 희소 좌표, 배치별 좌표 개수, 그리고 소스 컨디셔닝이 제공하는 경우 투영 특징)가 첨부된 positive 컨디셔닝입니다. | CONDITIONING |
| `negative` | 동일한 형상 단계 메타데이터가 첨부된 negative 컨디셔닝입니다. | CONDITIONING |
| `latent` | 빈 희소 latent 텐서(형태: 배치 크기, 32, 토큰 수, 1)와 함께 추출된 희소 좌표, 배치별 좌표 개수, 좌표 해상도, 타입 마커 `trellis2`, 모델 프레임 방향을 포함합니다. | LATENT |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Trellis2ShapeStage/ko.md)

---
**Source fingerprint (SHA-256):** `7dbee8a5b6ef7111f07def4dbe1cc4908533e00ffcb775f5a284099360c7eed3`
