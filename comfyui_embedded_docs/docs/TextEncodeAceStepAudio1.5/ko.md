# TextEncodeAceStepAudio1.5

TextEncodeAceStepAudio1.5 노드는 AceStepAudio 1.5 모델과 함께 사용할 텍스트 및 오디오 관련 메타데이터를 준비합니다. 설명 태그, 가사 및 음악 매개변수를 입력받은 다음, CLIP 모델을 사용하여 오디오 생성에 적합한 컨디셔닝 형식으로 변환합니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
| --- | --- | --- | --- | --- |
| `clip` | 입력 텍스트를 토큰화하고 인코딩하는 데 사용되는 CLIP 모델입니다. | CLIP | 예 | N/A |
| `tags` | 장르, 분위기 또는 악기 등 오디오를 설명하는 태그입니다. 여러 줄 입력과 동적 프롬프트를 지원합니다. | STRING | 예 | N/A |
| `lyrics` | 오디오 트랙의 가사입니다. 여러 줄 입력과 동적 프롬프트를 지원합니다. | STRING | 예 | N/A |
| `seed` | 재현 가능한 생성을 위한 무작위 시드 값입니다. control_after_generate 위젯이 포함되어 있습니다. 기본값: 0. | INT | 아니오 | 0 to 18446744073709551615 |
| `bpm` | 생성된 오디오의 분당 비트 수(BPM)입니다. 기본값: 120. | INT | 아니오 | 10 to 300 |
| `duration` | 원하는 오디오 길이(초)입니다. 기본값: 120.0. | FLOAT | 아니오 | 0.0 to 2000.0 |
| `timesignature` | 음악 박자표입니다. | COMBO | 아니오 | `"2"`<br>`"3"`<br>`"4"`<br>`"6"` |
| `language` | 입력 텍스트의 언어입니다. 기본값: "en". | COMBO | 아니오 | `"ar"`<br>`"az"`<br>`"bg"`<br>`"bn"`<br>`"ca"`<br>`"cs"`<br>`"da"`<br>`"de"`<br>`"el"`<br>`"en"`<br>`"es"`<br>`"fa"`<br>`"fi"`<br>`"fr"`<br>`"he"`<br>`"hi"`<br>`"hr"`<br>`"ht"`<br>`"hu"`<br>`"id"`<br>`"is"`<br>`"it"`<br>`"ja"`<br>`"ko"`<br>`"la"`<br>`"lt"`<br>`"ms"`<br>`"ne"`<br>`"nl"`<br>`"no"`<br>`"pa"`<br>`"pl"`<br>`"pt"`<br>`"ro"`<br>`"ru"`<br>`"sa"`<br>`"sk"`<br>`"sr"`<br>`"sv"`<br>`"sw"`<br>`"ta"`<br>`"te"`<br>`"th"`<br>`"tl"`<br>`"tr"`<br>`"uk"`<br>`"ur"`<br>`"vi"`<br>`"yue"`<br>`"zh"`<br>`"unknown"` |
| `keyscale` | 음악의 조와 음계(장조 또는 단조)입니다. | COMBO | 아니오 | `"C major"`<br>`"C# major"`<br>`"Db major"`<br>`"D major"`<br>`"D# major"`<br>`"Eb major"`<br>`"E major"`<br>`"F major"`<br>`"F# major"`<br>`"Gb major"`<br>`"G major"`<br>`"G# major"`<br>`"Ab major"`<br>`"A major"`<br>`"A# major"`<br>`"Bb major"`<br>`"B major"`<br>`"C minor"`<br>`"C# minor"`<br>`"Db minor"`<br>`"D minor"`<br>`"D# minor"`<br>`"Eb minor"`<br>`"E minor"`<br>`"F minor"`<br>`"F# minor"`<br>`"Gb minor"`<br>`"G minor"`<br>`"G# minor"`<br>`"Ab minor"`<br>`"A minor"`<br>`"A# minor"`<br>`"Bb minor"`<br>`"B minor"` |
| `generate_audio_codes` | 오디오 코드를 생성하는 LLM을 활성화합니다. 느릴 수 있지만 생성된 오디오의 품질이 향상됩니다. 모델에 오디오 참조를 제공하는 경우 이 기능을 해제하십시오. 기본값: True. | BOOLEAN | 아니오 | N/A |
| `cfg_scale` | 분류기-프리 가이던스(Classifier-Free Guidance) 스케일입니다. 값이 높을수록 출력이 프롬프트를 더 밀접하게 따릅니다. 기본값: 2.0. | FLOAT | 아니오 | 0.0 to 100.0 |
| `temperature` | 샘플링 온도입니다. 값이 낮을수록 출력이 더 결정론적으로 변합니다. 기본값: 0.85. | FLOAT | 아니오 | 0.0 to 2.0 |
| `top_p` | 핵 샘플링 확률(top-p)입니다. 기본값: 0.9. | FLOAT | 아니오 | 0.0 to 2000.0 |
| `top_k` | 고려할 최고 확률 토큰의 수(top-k)입니다. 기본값: 0. | INT | 아니오 | 0 to 100 |
| `min_p` | 토큰 샘플링을 위한 최소 확률 임계값(min-p)입니다. 기본값: 0.000. | FLOAT | 아니오 | 0.0 to 1.0 |

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
| --- | --- | --- |
| `CONDITIONING` | 인코딩된 텍스트와 AceStepAudio 1.5 모델을 위한 오디오 매개변수가 포함된 컨디셔닝 데이터입니다. | CONDITIONING |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeAceStepAudio1.5/ko.md)

---
**Source fingerprint (SHA-256):** `4bc97ec6220514b71fafde610339f2dca4ded26f68b541ed43ea492f127321f8`
