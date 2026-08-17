# CLIPを読み込む

CLIPLoader ノードは、テキストエンコーダモデル（CLIP、T5 など）をファイルから読み込み、テキストプロンプトを数値表現に変換する必要がある他のノードで使用できるようにします。多種多様なモデルアーキテクチャをサポートしており、それぞれに特定のエンコーダタイプが必要です。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
|-----------|-------------|-----------|----------|-------|
| `clip_name` | 読み込むテキストエンコーダモデルのファイル名です。`ComfyUI/models/text_encoders/` ディレクトリ内のファイルである必要があります。 | COMBO | はい | `text_encoders` フォルダ内のファイル一覧 |
| `type` | 読み込むモデルのアーキテクチャタイプです。使用する特定のエンコーダーバリアントを決定します（デフォルト: `"stable_diffusion"`）。 | COMBO | はい | `"stable_diffusion"`<br>`"stable_cascade"`<br>`"sd3"`<br>`"stable_audio"`<br>`"mochi"`<br>`"ltxv"`<br>`"pixart"`<br>`"cosmos"`<br>`"lumina2"`<br>`"wan"`<br>`"hidream"`<br>`"chroma"`<br>`"ace"`<br>`"omnigen2"`<br>`"qwen_image"`<br>`"hunyuan_image"`<br>`"flux2"`<br>`"ovis"`<br>`"longcat_image"`<br>`"cogvideox"`<br>`"lens"`<br>`"pixeldit"`<br>`"ideogram4"`<br>`"boogu"`<br>`"krea2"`<br>`"joyimage"`<br>`"mage"`<br>`"minimax"` |
| `device` | モデルを読み込むデバイスです。`"default"` はデフォルトのデバイス（通常は利用可能な GPU）を使用し、`"cpu"` は CPU への読み込みを強制します。これは上級者向けのオプションです（デフォルト: `"default"`）。 | COMBO | いいえ | `"default"`<br>`"cpu"` |

### サポートされているタイプとエンコーダの対応

`type` パラメータは、特定のモデルアーキテクチャに対して適切なエンコーダを選択します。以下の一般的な対応は、ノードの説明に記載されています。

| タイプ | エンコーダ |
|------|---------|
| stable_diffusion | clip-l |
| stable_cascade | clip-g |
| sd3 | t5 xxl / clip-g / clip-l |
| stable_audio | t5 base |
| mochi | t5 xxl |
| cogvideox | t5 xxl（226トークンのパディング） |
| cosmos | 旧 t5 xxl |
| lumina2 | gemma 2 2B |
| wan | umt5 xxl |
| hidream | llama-3.1（推奨）または t5 |
| omnigen2 | qwen vl 2.5 3B |
| joyimage | qwen3-vl 8B |
| lens | gpt-oss-20b |
| pixeldit | gemma 2 2B elm |
| minimax | MiniMax H3 Qwen3-VL または Music3 Qwen/RVQ |

## 出力

| 出力名 | 説明 | データ型 |
|-------------|-------------|-----------|
| `clip` | 読み込まれたテキストエンコーダモデルです。テキストエンコーディングとコンディショニングのために、他のノードに接続する準備ができています。 | CLIP |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPLoader/ja.md)

---
**Source fingerprint (SHA-256):** `7c1586d01410d319468f7c8c153ef0717280804add868ba57bff0c6539fb5dd9`
