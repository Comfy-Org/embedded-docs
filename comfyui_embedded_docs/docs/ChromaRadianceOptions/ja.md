# ChromaRadianceオプション

ChromaRadianceOptions ノードを使用すると、Chroma Radiance モデルの高度な設定を構成できます。既存のモデルをラップし、シグマ値に基づいてノイズ除去プロセス中に特定のオプションを適用することで、NeRF タイルサイズやその他のラディアンス関連パラメータを細かく制御できます。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
|-----------|------|----------|------|------|
| `model` | Chroma Radiance オプションを適用するモデル | MODEL | はい | - |
| `preserve_wrapper` | 有効にすると、既存のモデル関数ラッパーがあればそれに委譲します。通常は有効のままにしてください。(デフォルト: True) | BOOLEAN | いいえ | - |
| `start_sigma` | これらのオプションが有効になる最初のシグマ値。(デフォルト: 1.0) | FLOAT | いいえ | 0.0 to 1.0 |
| `end_sigma` | これらのオプションが有効になる最後のシグマ値。(デフォルト: 0.0) | FLOAT | いいえ | 0.0 to 1.0 |
| `nerf_tile_size` | デフォルトの NeRF タイルサイズを上書きできます。-1 はデフォルト (32) を使用することを意味します。0 は非タイルモードを使用することを意味します (多くの VRAM を必要とする場合があります)。(デフォルト: -1) | INT | いいえ | -1 and above |
| `force_sequential_txt_ids` | ゼロではなく、連続したテキストトークン ID の使用を強制します。2026-05-22 から 2026-06-01 までのチェックポイントで、この方法でトレーニングされているが、状態辞書に __sequential__ キーが含まれていない場合に使用してください。(デフォルト: False) | BOOLEAN | いいえ | - |

**注:** Chroma Radiance オプションは、現在のシグマ値が `end_sigma` と `start_sigma` の間（両端を含む）にある場合にのみ有効になります。`nerf_tile_size` パラメータは、0 以上に設定した場合にのみ適用されます。`force_sequential_txt_ids` パラメータは、True に設定した場合にのみ適用されます。

## 出力

| 出力名 | 説明 | データ型 |
|--------|------|----------|
| `model` | Chroma Radiance オプションが適用された変更済みモデル | MODEL |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ChromaRadianceOptions/ja.md)

---
**Source fingerprint (SHA-256):** `761f1946fe1fd77158e97f6f34d002e2445cc00e008741f8c37cde5673900409`
