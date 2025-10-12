> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanAnimateToVideo/ja.md)

WanAnimateToVideoノードは、ポーズ参照、顔の表情、背景要素など、複数の条件付け入力を組み合わせて動画コンテンツを生成します。様々な動画入力を処理し、フレーム間の時間的一貫性を維持しながら、首尾一貫したアニメーションシーケンスを作成します。このノードは潜在空間での操作を扱い、既存の動画をモーションパターンを継続することで拡張することができます。

## 入力

| パラメータ | データ型 | 必須 | 範囲 | 説明 |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | はい | - | 生成を目的のコンテンツに向けて導くためのポジティブ条件付け |
| `negative` | CONDITIONING | はい | - | 生成を望ましくないコンテンツから遠ざけるためのネガティブ条件付け |
| `vae` | VAE | はい | - | 画像データのエンコードとデコードに使用されるVAEモデル |
| `width` | INT | いいえ | 16 から MAX_RESOLUTION | 出力動画の幅（ピクセル単位）（デフォルト: 832, ステップ: 16） |
| `height` | INT | いいえ | 16 から MAX_RESOLUTION | 出力動画の高さ（ピクセル単位）（デフォルト: 480, ステップ: 16） |
| `length` | INT | いいえ | 1 から MAX_RESOLUTION | 生成するフレーム数（デフォルト: 77, ステップ: 4） |
| `batch_size` | INT | いいえ | 1 から 4096 | 同時に生成する動画の数（デフォルト: 1） |
| `clip_vision_output` | CLIP_VISION_OUTPUT | いいえ | - | 追加の条件付けのためのオプションのCLIPビジョンモデル出力 |
| `reference_image` | IMAGE | いいえ | - | 生成の開始点として使用される参照画像 |
| `face_video` | IMAGE | いいえ | - | 顔の表情のガイダンスを提供する動画入力 |
| `pose_video` | IMAGE | いいえ | - | ポーズとモーションのガイダンスを提供する動画入力 |
| `continue_motion_max_frames` | INT | いいえ | 1 から MAX_RESOLUTION | 前のモーションから継続する最大フレーム数（デフォルト: 5, ステップ: 4） |
| `background_video` | IMAGE | いいえ | - | 生成されたコンテンツと合成する背景動画 |
| `character_mask` | MASK | いいえ | - | 選択的処理のためのキャラクター領域を定義するマスク |
| `continue_motion` | IMAGE | いいえ | - | 時間的一貫性のために継続する前のモーションシーケンス |
| `video_frame_offset` | INT | いいえ | 0 から MAX_RESOLUTION | すべての入力動画でシークするフレーム数。チャンク単位でより長い動画を生成するために使用されます。動画を拡張するには、前のノードのvideo_frame_offset出力に接続してください。（デフォルト: 0, ステップ: 1） |

**パラメータの制約:**

- `pose_video`が提供され、`trim_to_pose_video`ロジックがアクティブな場合、出力の長さはポーズ動画の長さに合わせて調整されます
- `face_video`は処理時に自動的に512x512解像度にリサイズされます
- `continue_motion`フレームは`continue_motion_max_frames`パラメータによって制限されます
- 入力動画（`face_video`、`pose_video`、`background_video`、`character_mask`）は、処理前に`video_frame_offset`によってオフセットされます
- `character_mask`が1フレームのみを含む場合、すべてのフレームにわたって繰り返されます
- `clip_vision_output`が提供される場合、ポジティブ条件付けとネガティブ条件付けの両方に適用されます

## 出力

| 出力名 | データ型 | 説明 |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | 追加の動画コンテキストを持つ修正されたポジティブ条件付け |
| `negative` | CONDITIONING | 追加の動画コンテキストを持つ修正されたネガティブ条件付け |
| `latent` | LATENT | 潜在空間形式で生成された動画コンテンツ |
| `trim_latent` | INT | 下流処理のための潜在空間トリミング情報 |
| `trim_image` | INT | 参照モーションフレームのための画像空間トリミング情報 |
| `video_frame_offset` | INT | チャンク単位で動画生成を継続するための更新されたフレームオフセット |
