# OpenAI ChatGPT

Ce nœud génère des réponses textuelles avec les modèles GPT d’OpenAI. Il envoie une invite textuelle et, facultativement, des images ou des fichiers comme contexte, puis renvoie la réponse sous forme de chaîne de caractères. Tous les réglages se trouvent dans le sélecteur `model` : la sélection d’un modèle affiche ses propres niveaux `reasoning_effort`, sa limite de jetons, sa graine et son prompt système, aucun nœud de configuration distinct n’est donc nécessaire. Ce nœud remplace l’ancien nœud OpenAI ChatGPT, que le code source marque désormais comme obsolète.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model` | Le modèle utilisé pour générer la réponse. Chaque modèle expose les niveaux `reasoning_effort` qu’il prend en charge (par défaut : `"gpt-6.2-sol"`). | DYNAMIC_COMBO | Oui | `"gpt-6.2-sol"`<br>`"gpt-6.2-astra"`<br>`"gpt-6-astra"`<br>`"gpt-6.1-sol"`<br>`"gpt-6.1-terra"`<br>`"gpt-6-sol"`<br>`"gpt-6-luna"`<br>`"gpt-5.6-sol"`<br>`"gpt-5.6-terra"`<br>`"gpt-5.6-luna"`<br>`"gpt-5.5-pro"`<br>`"gpt-5.5"` |
| `prompt` | Entrée texte pour le modèle (par défaut : chaîne vide). | STRING | Oui | - |
| `images` | Emplacement extensible : connectez 1..16 éléments (`image_1`, `image_2`, ...). Image(s) facultative(s) utilisée(s) comme contexte pour le modèle. | IMAGE | Non | 0 à 16 images |
| `files` | Fichier(s) facultatif(s) utilisé(s) comme contexte pour le modèle. Accepte les entrées du nœud OpenAI ChatGPT Input Files. | OPENAI_INPUT_FILES | Non | - |
| `reasoning_effort` | Dans quelle mesure le modèle raisonne avant de répondre. Les niveaux plus élevés consomment plus de jetons et prennent plus de temps. Les niveaux proposés dépendent du modèle sélectionné (par défaut : `"medium"`, `"high"` pour `gpt-5.5-pro`). | COMBO | Oui | Voir la liste par modèle ci-dessous |
| `max_output_tokens` | Nombre maximal de jetons à générer, y compris les jetons de raisonnement. Une valeur faible associée à un `reasoning_effort` élevé peut ne laisser aucune place pour la réponse (par défaut : 32768). | INT | Oui | 16 à 128000 |
| `seed` | La graine contrôle si le nœud doit être réexécuté ; les résultats sont non déterministes quelle que soit la graine (par défaut : 42). | INT | Oui | 0 à 2147483647 |
| `system_prompt` | Instructions fondamentales qui dictent le comportement du modèle (par défaut : chaîne vide). | STRING | Non | - |

### Niveaux d’effort de raisonnement par modèle

- `gpt-6.2-sol`, `gpt-6.2-astra`, `gpt-6-astra`, `gpt-6.1-sol` : `"low"`, `"medium"`, `"high"`, `"xhigh"`, `"max"`, par défaut `"medium"`.
- `gpt-6.1-terra`, `gpt-6-sol`, `gpt-6-luna`, `gpt-5.6-sol`, `gpt-5.6-terra`, `gpt-5.6-luna` : `"none"`, `"low"`, `"medium"`, `"high"`, `"xhigh"`, `"max"`, par défaut `"medium"`.
- `gpt-5.5-pro` : `"medium"`, `"high"`, `"xhigh"`, par défaut `"high"`.
- `gpt-5.5` : `"none"`, `"low"`, `"medium"`, `"high"`, `"xhigh"`, par défaut `"medium"`.

### Notes sur le comportement

- Seul le texte de la réponse est renvoyé. Les messages que le modèle émet dans sa phase de commentaire pendant la réflexion sont ignorés.
- Si le budget de jetons s’épuise avant que la réponse soit écrite, le nœud lève une erreur vous invitant à augmenter `max_output_tokens`.
- Les images sont envoyées à leur propre résolution avec le niveau de détail automatique de l’API ; les grandes images consomment donc plus de jetons.
- Chaque requête est stockée côté OpenAI, et le texte renvoyé concatène les parties de la réponse avec des retours à la ligne.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `output` | La réponse textuelle générée par le modèle OpenAI. | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIChatNodeV2/fr.md)

---
**Source fingerprint (SHA-256):** `129c13a6c7b76d142c0a23234ab5e707a1dd39a99055974277d46a39593aa7ba`
