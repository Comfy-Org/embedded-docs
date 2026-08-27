# BakeAmbientOcclusion

Bakes an ambient-occlusion map from a high-poly mesh into the UV layout of a low-poly mesh. The output is a grayscale image in which white texels are open and dark texels are in crevices; it is meant for the Apply Texture To Mesh node's occlusion input. Connect the UV-unwrapped low-poly mesh and the high-poly mesh it was decimated from.

ハイポリメッシュからアンビエントオクルージョンマップをベイクし、ローポリメッシュのUVレイアウトに焼き付けます。出力はグレースケール画像で、白いテクセルは開放領域、暗いテクセルは隙間やくぼみを示します。これは Apply Texture To Mesh ノードのオクルージョン入力用です。UV展開済みのローポリメッシュと、そのローポリメッシュのデシメーション元であるハイポリメッシュを接続してください。

## Inputs / 入力

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `low_poly` | The UV-unwrapped low-poly mesh to bake into. Must have UVs; the node raises an error if they are missing. | MESH | Yes | - |
| `high_poly` | The high-poly mesh that the low-poly was decimated from, used as the source geometry for occlusion. | MESH | Yes | - |
| `resolution` | Texture resolution in pixels; each texel receives an occlusion value. Default: 1024. | INT | Yes | 64 to 8192 (step 64) |
| `samples` | Rays per texel. More = smoother, slower. Raise if grainy. Default: 64. | INT | Yes | 4 to 1024 (step 4) |
| `max_distance` | Ray length, as a fraction of the bounding box diagonal. Smaller = tighter, more local occlusion. Default: 0.5. | FLOAT | Yes | 0.01 to 2.0 (step 0.01) |
| `strength` | Scales the occlusion. >1 darkens, <1 lightens. Default: 1.0. | FLOAT | Yes | 0.0 to 2.0 (step 0.05) |
| `bias` | Ray origin lift off the surface, as a fraction of the bounding box diagonal. Raise if even surfaces show dark blotches/holes. Default: 0.01. | FLOAT | Yes | 0.0001 to 0.2 (step 0.0005) |

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
|-----------|-------------|-----------|----------|-------|
| `low_poly` | ベイク先となるUV展開済みローポリメッシュ。UVが必要です。UVがない場合、ノードはエラーを発生させます。 | MESH | はい | - |
| `high_poly` | ローポリのデシメーション元であるハイポリメッシュ。オクルージョンのソースジオメトリとして使用されます。 | MESH | はい | - |
| `resolution` | テクスチャ解像度（ピクセル単位）。各テクセルにオクルージョン値が割り当てられます。デフォルト: 1024。 | INT | はい | 64 to 8192 (step 64) |
| `samples` | テクセルあたりのレイ数。多いほど滑らかになりますが、遅くなります。ざらつきが目立つ場合は増やしてください。デフォルト: 64。 | INT | はい | 4 to 1024 (step 4) |
| `max_distance` | レイの長さ。バウンディングボックスの対角線に対する比率です。小さいほど密着した局所的なオクルージョンになります。デフォルト: 0.5。 | FLOAT | はい | 0.01 to 2.0 (step 0.01) |
| `strength` | オクルージョンをスケーリングします。1より大きいと暗く、1より小さいと明るくなります。デフォルト: 1.0。 | FLOAT | はい | 0.0 to 2.0 (step 0.05) |
| `bias` | サーフェスからのレイ起点の浮き上がり量。バウンディングボックスの対角線に対する比率です。平面にもかかわらず暗い斑点や穴が見られる場合は増やしてください。デフォルト: 0.01。 | FLOAT | はい | 0.0001 to 0.2 (step 0.0005) |

Note: `low_poly` must have UV coordinates — this node never unwraps the mesh. If `high_poly` contains only one batch item, it is reused for every batch item of `low_poly`; batch items of `low_poly` with no faces are skipped and replaced with an all-white image, with a warning logged.

注記: `low_poly` にはUV座標が必要です。このノードはメッシュをUV展開しません。`high_poly` にバッチ項目が1つしかない場合、`low_poly` のすべてのバッチ項目に対してそれが再利用されます。面がない `low_poly` のバッチ項目はスキップされ、警告がログに記録されたうえで全白画像に置き換えられます。

## Outputs / 出力

| Output Name | Description | Data Type |
|-------------|-------------|-----------|
| `occlusion` | Grayscale ambient-occlusion image with values in [0,1] (white = open, dark = crevices), one image per batch item of `low_poly`. Intended for the Apply Texture To Mesh node's occlusion input (packed into the ORM map / occlusionTexture). | IMAGE |

| 出力名 | 説明 | データ型 |
|-------------|-------------|-----------|
| `occlusion` | 値が[0,1]のグレースケールのアンビエントオクルージョン画像（白=開放、暗=くぼみ）。`low_poly` のバッチ項目ごとに1枚の画像が生成されます。Apply Texture To Mesh ノードのオクルージョン入力（ORMマップ / occlusionTexture にパックされる）を想定しています。 | IMAGE |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BakeAmbientOcclusion/ja.md)

---
**Source fingerprint (SHA-256):** `63ea6ce5289728d351fdd7d722e9a299ebb1283e1128262a817466ec6d23786a`
