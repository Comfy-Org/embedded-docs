# 체크포인트 로드

```markdown
확산 모델 체크포인트 파일을 로드하고 이를 세 가지 핵심 구성 요소, 즉 잠재 공간(latent) 노이즈 제거에 사용되는 메인 모델, CLIP 텍스트 인코더, VAE 이미지 인코더/디코더로 분해합니다. 이 노드는 `ComfyUI/models/checkpoints` 폴더와 `extra_model_paths.yaml` 파일에 구성된 추가 경로에 있는 모든 모델 파일을 자동으로 감지합니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
| --- | --- | --- | --- | --- |
| `ckpt_name` | 로드할 체크포인트(모델) 이름입니다. 체크포인트 모델 파일 이름을 선택하며, 이에 따라 이후 이미지 생성에 사용될 AI 모델이 결정됩니다. | STRING | 예 | 체크포인트 폴더의 모든 모델 파일 |

**참고:** ComfyUI 실행 중에 새 모델 파일이 추가된 경우, 브라우저를 새로고침(Ctrl+R)해야 드롭다운 목록에 새 파일이 표시됩니다.

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
| --- | --- | --- |
| `MODEL` | 잠재 공간(latent) 노이즈 제거에 사용되는 모델입니다. 이미지 생성에 사용되는 핵심 확산 모델입니다. | MODEL |
| `CLIP` | 텍스트 프롬프트를 인코딩하여 텍스트 설명을 AI가 이해할 수 있는 정보로 변환하는 데 사용되는 CLIP 모델입니다. | CLIP |
| `VAE` | 이미지를 잠재 공간(latent space)으로 인코딩하고 다시 이미지로 디코딩하는 데 사용되는 VAE 모델입니다. | VAE |
```

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CheckpointLoaderSimple/ko.md)

---
**Source fingerprint (SHA-256):** `db99a8ba83a586491463df0d4e99ba5f77d4511c6d8337a721d76edd3450f310`
