# ビデオ三角形CFGガイダンス

VideoTriangleCFGGuidance ノードは、ビデオモデルに三角波状のクラシファイアフリーガイダンス（CFG）スケーリングパターンを適用します。最小CFG値と元のconditioningスケールの間で振動する三角波関数を使用して、conditioningスケールを時間の経過とともに変更します。これにより、動的なガイダンスパターンが生成され、ビデオ生成の一貫性と品質の向上に役立ちます。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
| --- | --- | --- | --- | --- |
| `model` | 三角波CFGガイダンスを適用するビデオモデル | MODEL | はい | - |
| `min_cfg` | 三角波パターンの最小CFGスケール値（デフォルト: 1.0） | FLOAT | はい | 0.0 - 100.0 |

## 出力

| 出力名 | 説明 | データ型 |
| --- | --- | --- |
| `model` | 三角波CFGガイダンスが適用された変更済みモデル | MODEL |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VideoTriangleCFGGuidance/ja.md)

---
**Source fingerprint (SHA-256):** `412d84d402f8c9a4852ee7b3f0ca0ab5650658fc26a37d10333a653e92e0294e`
