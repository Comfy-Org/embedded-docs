# 潜在空間結合

LatentConcat ノードは、2 つの潜在サンプルを選択した次元に沿って結合します。2 つの latent 入力を x、y、または t 軸に沿って連結し、どちらのサンプルを先に配置するかを制御するオプションがあります。このノードは、連結を実行する前に、2 番目の入力のバッチサイズを最初の入力に一致するように自動的に調整します。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
| --- | --- | --- | --- | --- |
| `samples1` | 連結する最初の latent サンプル | LATENT | はい | - |
| `samples2` | 連結する 2 番目の latent サンプル | LATENT | はい | - |
| `dim` | latent サンプルを連結する次元を指定します。x、y、t を指定すると、結果内で `samples1` が `samples2` の前に配置されます。-x、-y、-t を指定すると、`samples2` が `samples1` の前に配置されます。次元の対応は次のとおりです。x = 幅、y = 高さ、t = 時間/フレーム | COMBO | はい | `"x"`<br>`"-x"`<br>`"y"`<br>`"-y"`<br>`"t"`<br>`"-t"` |

**注:** 2 番目の latent サンプル（`samples2`）は、連結前に最初の latent サンプル（`samples1`）のバッチサイズに一致するよう自動的に調整されます。

## 出力

| 出力名 | 説明 | データ型 |
| --- | --- | --- |
| `output` | 指定された次元に沿って 2 つの入力サンプルを結合した結果の latent サンプル | LATENT |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentConcat/ja.md)

---
**Source fingerprint (SHA-256):** `dfe27f76ad12e16623d62c9e7f0b2772df6ecadb543a4eee430bc38ab04a12f2`
