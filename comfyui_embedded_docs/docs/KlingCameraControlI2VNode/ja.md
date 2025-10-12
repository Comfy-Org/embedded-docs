> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingCameraControlI2VNode/ja.md)

Kling Image to Video Camera Control ノードは、静止画像をプロフェッショナルなカメラムーブメントを伴った映画的な動画に変換します。この特殊な画像変換ノードを使用すると、元の画像に焦点を合わせたまま、ズーム、回転、パン、チルト、一人称視点などの仮想カメラアクションを制御できます。カメラ制御は現在、kling-v1-5モデルで5秒間のプロモードでのみサポートされています。

## 入力

| パラメータ | データ型 | 必須 | 範囲 | 説明 |
|-----------|-----------|----------|-------|-------------|
| `start_frame` | IMAGE | はい | - | 参照画像 - URLまたはBase64エンコードされた文字列。10MBを超えず、解像度は300*300px以上、アスペクト比は1:2.5〜2.5:1の間である必要があります。Base64にはdata:imageプレフィックスを含めないでください。 |
| `prompt` | STRING | はい | - | 肯定的なテキストプロンプト |
| `negative_prompt` | STRING | はい | - | 否定的なテキストプロンプト |
| `cfg_scale` | FLOAT | いいえ | 0.0-1.0 | テキストガイダンスの強度を制御します（デフォルト: 0.75） |
| `aspect_ratio` | COMBO | いいえ | 複数オプション利用可能 | 動画のアスペクト比選択（デフォルト: 16:9） |
| `camera_control` | CAMERA_CONTROL | はい | - | Kling Camera Controls ノードを使用して作成できます。動画生成中のカメラの動きとモーションを制御します。 |

## 出力

| 出力名 | データ型 | 説明 |
|-------------|-----------|-------------|
| `video_id` | VIDEO | 生成された動画出力 |
| `duration` | STRING | 生成された動画の一意の識別子 |
| `duration` | STRING | 生成された動画の再生時間 |
