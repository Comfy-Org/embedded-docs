사중 CLIP 로더 QuadrupleCLIPLoader는 ComfyUI의 핵심 노드 중 하나로, HiDream I1 버전 모델 지원을 위해 처음 추가되었습니다. 이 노드가 누락된 경우, ComfyUI를 최신 버전으로 업데이트하여 노드 지원을 확인하십시오.

이 노드는 4개의 CLIP 모델을 필요로 하며, 각각 `clip_name1`, `clip_name2`, `clip_name3`, `clip_name4`라는 4개의 매개변수에 해당하며, 후속 노드에서 사용할 CLIP 모델 출력을 제공합니다.

이 노드는 `ComfyUI/models/text_encoders` 폴더에 있는 모델을 감지하며,
또한 extra_model_paths.yaml 파일에 설정된 추가 경로의 모델도 읽습니다.
모델을 추가한 후에는 **ComfyUI 인터페이스를 다시 로드**해야 해당 폴더의 모델 파일을 읽을 수 있습니다.
