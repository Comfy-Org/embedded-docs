> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ViduReferenceVideoNode/ko.md)

Vidu Reference Video 노드는 여러 참조 이미지와 텍스트 프롬프트에서 비디오를 생성합니다. AI 모델을 사용하여 제공된 이미지와 설명을 기반으로 일관된 비디오 콘텐츠를 만듭니다. 이 노드는 지속 시간, 화면 비율, 해상도 및 움직임 제어를 포함한 다양한 비디오 설정을 지원합니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | 예 | `"vidu_q1"`<br>`"vidu_q2"`<br>`"vidu_q3"`<br>`"vidu_q4"`<br>`"vidu_q5"`<br>`"vidu_q6"`<br>`"vidu_q7"`<br>`"vidu_q8"`<br>`"vidu_q9"`<br>`"vidu_q10"`<br>`"vidu_q11"`<br>`"vidu_q12"`<br>`"vidu_q13"`<br>`"vidu_q14"`<br>`"vidu_q15"`<br>`"vidu_q16"`<br>`"vidu_q17"`<br>`"vidu_q18"`<br>`"vidu_q19"`<br>`"vidu_q20"`<br>`"vidu_q21"`<br>`"vidu_q22"`<br>`"vidu_q23"`<br>`"vidu_q24"`<br>`"vidu_q25"`<br>`"vidu_q26"`<br>`"vidu_q27"`<br>`"vidu_q28"`<br>`"vidu_q29"`<br>`"vidu_q30"`<br>`"vidu_q31"`<br>`"vidu_q32"`<br>`"vidu_q33"`<br>`"vidu_q34"`<br>`"vidu_q35"`<br>`"vidu_q36"`<br>`"vidu_q37"`<br>`"vidu_q38"`<br>`"vidu_q39"`<br>`"vidu_q40"`<br>`"vidu_q41"`<br>`"vidu_q42"`<br>`"vidu_q43"`<br>`"vidu_q44"`<br>`"vidu_q45"`<br>`"vidu_q46"`<br>`"vidu_q47"`<br>`"vidu_q48"`<br>`"vidu_q49"`<br>`"vidu_q50"`<br>`"vidu_q51"`<br>`"vidu_q52"`<br>`"vidu_q53"`<br>`"vidu_q54"`<br>`"vidu_q55"`<br>`"vidu_q56"`<br>`"vidu_q57"`<br>`"vidu_q58"`<br>`"vidu_q59"`<br>`"vidu_q60"`<br>`"vidu_q61"`<br>`"vidu_q62"`<br>`"vidu_q63"`<br>`"vidu_q64"`<br>`"vidu_q65"`<br>`"vidu_q66"`<br>`"vidu_q67"`<br>`"vidu_q68"`<br>`"vidu_q69"`<br>`"vidu_q70"`<br>`"vidu_q71"`<br>`"vidu_q72"`<br>`"vidu_q73"`<br>`"vidu_q74"`<br>`"vidu_q75"`<br>`"vidu_q76"`<br>`"vidu_q77"`<br>`"vidu_q78"`<br>`"vidu_q79"`<br>`"vidu_q80"`<br>`"vidu_q81"`<br>`"vidu_q82"`<br>`"vidu_q83"`<br>`"vidu_q84"`<br>`"vidu_q85"`<br>`"vidu_q86"`<br>`"vidu_q87"`<br>`"vidu_q88"`<br>`"vidu_q89"`<br>`"vidu_q90"`<br>`"vidu_q91"`<br>`"vidu_q92"`<br>`"vidu_q93"`<br>`"vidu_q94"`<br>`"vidu_q95"`<br>`"vidu_q96"`<br>`"vidu_q97"`<br>`"vidu_q98"`<br>`"vidu_q99"`<br>`"vidu_q100"` | 비디오 생성을 위한 모델 이름 (기본값: "vidu_q1") |
| `images` | IMAGE | 예 | - | 일관된 주제를 가진 비디오를 생성하기 위한 참조로 사용할 이미지 (최대 7개 이미지) |
| `prompt` | STRING | 예 | - | 비디오 생성을 위한 텍스트 설명 |
| `duration` | INT | 아니오 | 5-5 | 출력 비디오의 지속 시간(초) (기본값: 5) |
| `seed` | INT | 아니오 | 0-2147483647 | 비디오 생성을 위한 시드 (0은 무작위) (기본값: 0) |
| `aspect_ratio` | COMBO | 아니오 | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"`<br>`"21:9"`<br>`"9:21"` | 출력 비디오의 화면 비율 (기본값: "16:9") |
| `resolution` | COMBO | 아니오 | `"480p"`<br>`"720p"`<br>`"1080p"`<br>`"1440p"`<br>`"2160p"` | 지원되는 값은 모델 및 지속 시간에 따라 다를 수 있음 (기본값: "1080p") |
| `movement_amplitude` | COMBO | 아니오 | `"auto"`<br>`"low"`<br>`"medium"`<br>`"high"` | 프레임 내 객체의 움직임 진폭 (기본값: "auto") |

**제약 사항 및 한계:**

- `prompt` 필드는 필수이며 비워둘 수 없음
- 참조용 이미지는 최대 7개까지 허용
- 각 이미지는 1:4에서 4:1 사이의 화면 비율을 가져야 함
- 각 이미지는 최소 128x128 픽셀의 크기를 가져야 함
- 지속 시간은 5초로 고정됨

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `output` | VIDEO | 참조 이미지와 프롬프트를 기반으로 생성된 비디오 |
