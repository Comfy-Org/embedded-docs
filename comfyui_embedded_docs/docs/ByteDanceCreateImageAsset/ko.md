> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceCreateImageAsset/ko.md)

이 문서는 AI로 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 언제든지 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceCreateImageAsset/en.md)

이 노드는 ByteDance의 Seedance 2.0 서비스를 위한 개인 이미지 자산을 생성합니다. 입력 이미지를 업로드하고 지정된 자산 그룹에 등록합니다. 그룹 ID가 제공되지 않으면, 자산을 추가하기 전에 브라우저에서 실물 인증 절차를 시작하여 새 그룹을 생성합니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | 예 | | 개인 자산으로 등록할 이미지입니다. |
| `group_id` | STRING | 아니요 | | 동일 인물에 대한 반복적인 실물 인증을 건너뛰기 위해 기존 Seedance 자산 그룹 ID를 재사용합니다. 브라우저에서 실물 인증을 실행하고 새 그룹을 생성하려면 비워 두십시오(기본값: 비움). |

**이미지 제약 조건:**
*   이미지 너비는 300픽셀 이상 6000픽셀 이하여야 합니다.
*   이미지 높이는 300픽셀 이상 6000픽셀 이하여야 합니다.
*   이미지 종횡비는 0.4:1에서 2.5:1 사이여야 합니다.

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `asset_id` | STRING | 새로 생성된 이미지 자산의 고유 식별자입니다. |
| `group_id` | STRING | 자산 그룹의 식별자입니다. 제공된 `group_id` 또는 새로 생성된 ID가 됩니다. |