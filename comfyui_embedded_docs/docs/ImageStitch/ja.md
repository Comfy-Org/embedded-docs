このノードは、2つの画像を指定した方向（上、下、左、右）に結合することができ、サイズの調整や画像間の間隔設定をサポートしています。

## 入力

| パラメータ名 | データ型 | 入力タイプ | デフォルト値 | 範囲 | 説明 |
|------------|----------|------------|-------------|------|------|
| `image1` | IMAGE | 必須 | - | - | 結合する1枚目の画像 |
| `image2` | IMAGE | 任意 | None | - | 結合する2枚目の画像（指定しない場合は1枚目の画像のみを返す） |
| `direction` | STRING | 必須 | right | right/down/left/up | 2枚目の画像を結合する方向：right（右）、down（下）、left（左）、up（上） |
| `match_image_size` | BOOLEAN | 必須 | True | True/False | 2枚目の画像のサイズを1枚目の画像のサイズに合わせるかどうか |
| `spacing_width` | INT | 必須 | 0 | 0-1024 | 画像間の間隔の幅（偶数である必要があります） |
| `spacing_color` | STRING | 必須 | white | white/black/red/green/blue | 結合された画像間の間隔の色 |

> `spacing_color`について、"white/black"以外の色を使用する場合、`match_image_size`が`false`に設定されていると、パディング領域は黒で塗りつぶされます

## 出力

| 出力名 | データ型 | 説明 |
|--------|----------|------|
| `IMAGE` | IMAGE | 結合された画像 |

## ワークフロー例

以下のワークフローでは、異なるサイズの3つの入力画像を例として使用しています：

- image1: 500x300
- image2: 400x250
- image3: 300x300

![workflow](./asset/workflow.webp)

**1つ目のImage Stitchノード**

- `match_image_size`: false、画像は元のサイズのまま結合されます
- `direction`: up、`image2`は`image1`の上に配置されます
- `spacing_width`: 20
- `spacing_color`: black

出力画像1：

![output1](./asset/output-1.webp)

**2つ目のImage Stitchノード**

- `match_image_size`: true、2枚目の画像は1枚目の画像の高さまたは幅に合わせてサイズ調整されます
- `direction`: right、`image3`は右側に表示されます
- `spacing_width`: 20
- `spacing_color`: white

出力画像2：
![output2](./asset/output-2.webp)
