> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingLipSyncTextToVideoNode/ja.md)

Kling Lip Sync Text to Videoノードは、ビデオファイル内の口の動きをテキストプロンプトに合わせて同期させます。入力ビデオを受け取り、キャラクターの口の動きが提供されたテキストに合うように調整された新しいビデオを生成します。このノードは音声合成を使用して、自然な見た目の音声同期を作成します。

## 入力

| パラメータ | データ型 | 必須 | 範囲 | 説明 |
|-----------|-----------|----------|-------|-------------|
| `動画` | VIDEO | はい | - | リップシンク用の入力ビデオファイル |
| `テキスト` | STRING | はい | - | リップシンクビデオ生成用のテキスト内容。modeがtext2videoの場合に必須です。最大長は120文字です。 |
| `音声` | COMBO | いいえ | "Melody"<br>"Bella"<br>"Aria"<br>"Ethan"<br>"Ryan"<br>"Dorothy"<br>"Nathan"<br>"Lily"<br>"Aaron"<br>"Emma"<br>"Grace"<br>"Henry"<br>"Isabella"<br>"James"<br>"Katherine"<br>"Liam"<br>"Mia"<br>"Noah"<br>"Olivia"<br>"Sophia" | リップシンクオーディオ用の音声選択（デフォルト: "Melody"） |
| `話速` | FLOAT | いいえ | 0.8-2.0 | 話速。有効範囲: 0.8〜2.0、小数点第1位まで正確。（デフォルト: 1） |

**ビデオ要件:**

- ビデオファイルは100MBを超えないこと
- 高さ/幅は720pxから1920pxの間であること
- 長さは2秒から10秒の間であること

## 出力

| 出力名 | データ型 | 説明 |
|-------------|-----------|-------------|
| `動画ID` | VIDEO | リップシンクされたオーディオ付きの生成ビデオ |
| `再生時間` | STRING | 生成されたビデオの一意の識別子 |
| `duration` | STRING | 生成されたビデオの長さ情報 |
