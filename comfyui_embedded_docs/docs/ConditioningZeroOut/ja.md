このノードは、コンディショニングデータ構造内の特定の要素をゼロにし、後続の処理ステップでの影響を効果的に中和します。コンディショニングの内部表現を直接操作する必要がある高度なコンディショニング操作用に設計されています。

## 入力

| パラメータ | Comfy dtype                | 説明 |
|-----------|----------------------------|-------------|
| `CONDITIONING` | CONDITIONING | 修正されるコンディショニングデータ構造。このノードは、各コンディショニングエントリ内の 'pooled_output' 要素をゼロにします（存在する場合）。 |

## 出力

| パラメータ | Comfy dtype                | 説明 |
|-----------|----------------------------|-------------|
| `CONDITIONING` | CONDITIONING | 'pooled_output' 要素がゼロに設定された修正済みのコンディショニングデータ構造。 |
