# WanSCAILToVideo

WanSCAILToVideo ノードは、ビデオ生成用のコンディショニングと空の潜在空間を準備します。参照画像、ポーズビデオ、CLIP vision 出力、前フレームチャンクなどのオプション入力を処理し、それらをビデオモデル用のポジティブおよびネガティブコンディショニングに埋め込みます。このノードは、変更されたコンディショニングと、指定されたビデオサイズの空の潜在テンソルを出力します。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
|-----------|-------------|-----------|----------|-------|
| `positive` | ポジティブコンディショニングの入力です。 | CONDITIONING | 必須 | - |
| `negative` | ネガティブコンディショニングの入力です。 | CONDITIONING | 必須 | - |
| `vae` | 画像とビデオフレームのエンコードに使用される VAE モデルです。 | VAE | 必須 | - |
| `width` | 出力ビデオの幅（ピクセル単位）（デフォルト: 512）。32刻みで調整可能です。 | INT | 必須 | 32 to MAX_RESOLUTION |
| `height` | 出力ビデオの高さ（ピクセル単位）（デフォルト: 896）。32刻みで調整可能です。 | INT | 必須 | 32 to MAX_RESOLUTION |
| `length` | ビデオのフレーム数（デフォルト: 81）。1から始まり4刻みで調整可能です。 | INT | 必須 | 1 to MAX_RESOLUTION |
| `batch_size` | バッチで生成するビデオの数（デフォルト: 1）。 | INT | 必須 | 1 to 4096 |
| `pose_strength` | ポーズ潜在表現の強度（デフォルト: 1.0）。 | FLOAT | 必須 | 0.0 to 10.0 |
| `pose_start` | ポーズコンディショニングの開始ステップ（デフォルト: 0.0）。 | FLOAT | 必須 | 0.0 to 1.0 |
| `pose_end` | ポーズコンディショニングの終了ステップ（デフォルト: 1.0）。 | FLOAT | 必須 | 0.0 to 1.0 |
| `video_frame_offset` | このチャンクが開始する累積出力フレームです。前のチャンクの `video_frame_offset` 出力から接続します（デフォルト: 0）。 | INT | 必須 | 0 to MAX_RESOLUTION |
| `previous_frame_count` | アンカーとして使用する `previous_frames` の末尾フレーム数です。SCAIL-2 は 5 で学習されています（81フレームチャンク、76フレームステップ）（デフォルト: 5）。 | INT | 必須 | 1 to MAX_RESOLUTION |
| `pose_video` | ポーズコンディショニングに使用するビデオです。メインビデオの半分の解像度にダウンスケールされます。 | IMAGE | 任意 | - |
| `pose_video_mask` | SCAIL-2 のみ。`pose_video` と同じ解像度の、ID ごとに色分けされた SAM3 マスクビデオです。 | IMAGE | 任意 | - |
| `replacement_mode` | SCAIL-2 のみ。False = アニメーションモード（`pose_video_mask` は黒い背景にしてください）。True = リプレイスメントモード（`pose_video_mask` は白い背景にしてください）。デフォルト: False。 | BOOLEAN | 任意 | - |
| `reference_image` | 参照画像です。最初の画像がプライマリ参照です（すべての ID をその上に合成します）。SCAIL-2 では、追加のバッチ画像は追加ビュー（背面、接写、遮蔽された背景）として使用され、それぞれに対応する `reference_image_mask` をその ID の色で指定する必要があります。 | IMAGE | 任意 | - |
| `reference_image_mask` | SCAIL-2 のみ。色分けされた参照マスクです。`reference_image` とバッチが一致します（最初はプライマリ参照マスク、残りは追加の `reference_image` 用の ID マスクです）。 | IMAGE | 任意 | - |
| `clip_vision_output` | コンディショニング用の CLIP vision 特徴量です。モデルは、アスペクト比へのストレッチリサイズを使用して学習されています。 | CLIP_VISION_OUTPUT | 任意 | - |
| `previous_frames` | SCAIL-2 のみ。前のチャンクの完全にデコードされた出力です。末尾の `previous_frame_count` フレームのみが拡張アンカーとして使用されます。 | IMAGE | 任意 | - |

**注記:**

- `pose_video` と `pose_video_mask` の入力は、`video_frame_offset` の位置からスライスされます。そのオフセットより先にフレームがないビデオは無視されます。その後、2つのうち短い方に合わせて一緒に切り詰められ、`length` フレームに制限されます。`pose_video` はエンコード前にメインビデオの半分の解像度にダウンスケールされます。
- `reference_image_mask` 入力は、`reference_image` も指定されている場合にのみ適用されます。`reference_image` バッチ内の各画像は、単一フレームの潜在参照として個別にエンコードされます。リプレイスメントモード（`replacement_mode=True`）では、参照画像は参照画像マスクをアルファマットとして使用し、黒い背景に合成されます。
- `clip_vision_output` が指定されている場合、ポジティブとネガティブの両方のコンディショニングに適用されます。
- `previous_frames` が指定されている場合、末尾の `previous_frame_count` フレームのみが拡張アンカーとして使用されます。出力潜在テンソルは、これらのフレームのエンコード結果で部分的に埋められ、ノイズマスクが潜在出力に含まれ、`video_frame_offset` は保持されたフレーム数を差し引いて調整されます（0 未満にはなりません）。

## 出力

| 出力名 | 説明 | データ型 |
|-------------|-------------|-----------|
| positive | 変更されたポジティブコンディショニングです。埋め込まれた参照画像の潜在表現、CLIP vision 出力、ポーズビデオの潜在表現、ドライビングマスク、参照マスク、または前フレームの潜在表現が含まれる可能性があります。 | CONDITIONING |
| negative | 変更されたネガティブコンディショニングです。埋め込まれた参照画像の潜在表現、CLIP vision 出力、ポーズビデオの潜在表現、ドライビングマスク、参照マスク、または前フレームの潜在表現が含まれる可能性があります。 | CONDITIONING |
| latent | 形状 `[batch_size, 16, ((length - 1) // 4) + 1, height // 8, width // 8]` の空の潜在テンソルです。`previous_frames` が指定されている場合、潜在テンソルはエンコードされた前フレームで部分的に埋められ、ノイズマスクが含まれます。 | LATENT |
| video_frame_offset | 調整後のオフセットに `length` を加えた値です。シーケンシャルなビデオ生成のために、次のチャンクに接続してください。 | INT |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanSCAILToVideo/ja.md)

---
**Source fingerprint (SHA-256):** `4a1a2201dfa94bd2f1330db02ec18a5e0a6aae9e9ac5ae97d456b7af1aa84b7b`
