# 🐍 Python File Organizer

> Organise automatiquement tous tes fichiers téléchargés par catégorie en **3 secondes**. Fini le chaos dans ton dossier Downloads !

[![Python Version](https://img.shields.io/badge/python-3.7%2B-blue)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![YouTube](https://img.shields.io/badge/YouTube-CodeAvecAbel-red)](https://youtube.com/@CodeAvecAbel)

---

## 🎥 Vidéo Tutoriel

**Regarde la vidéo complète sur YouTube pour comprendre le code ligne par ligne :**

[![Miniature YouTube](https://img.shields.io/badge/▶️-Regarder_sur_YouTube-red?style=for-the-badge)](lien-vers-ta-video)

---

## 📸 Avant / Après

### ❌ AVANT : Chaos complet
```
Downloads/
├── photo_vacances.jpg
├── rapport_2024.pdf
├── musique.mp3
├── screenshot_01.png
├── archive_projet.zip
├── facture_janvier.pdf
├── video_tuto.mp4
├── script.py
└── ... (100+ fichiers mélangés)
```

### ✅ APRÈS : Organisation parfaite (en 3 secondes)
```
Downloads/
├── Images/
│   ├── photo_vacances.jpg
│   └── screenshot_01.png
├── Documents/
│   ├── rapport_2024.pdf
│   └── facture_janvier.pdf
├── Videos/
│   └── video_tuto.mp4
├── Musique/
│   └── musique.mp3
├── Archives/
│   └── archive_projet.zip
└── Code/
    └── script.py
```

---

## ✨ Fonctionnalités

- ✅ **Automatique** : Organise tous tes fichiers en une seule commande
- ✅ **Intelligent** : Gère les doublons sans écraser tes fichiers
- ✅ **Personnalisable** : Ajoute tes propres catégories via JSON
- ✅ **Cross-platform** : Fonctionne sur Windows, Mac et Linux
- ✅ **Sans dépendances** : Utilise uniquement les bibliothèques Python standard
- ✅ **Rapide** : Traite des centaines de fichiers en quelques secondes
- ✅ **Sûr** : Ne supprime jamais tes fichiers, les déplace seulement

---

## 🚀 Installation

### Prérequis

- Python 3.7 ou supérieur
- C'est tout ! Aucune dépendance externe nécessaire

### Étapes

1. **Clone le dépôt** :
```bash
git clone https://github.com/ton-username/python-file-organizer.git
cd python-file-organizer
```

2. **C'est prêt !** Le script utilise uniquement les bibliothèques standard Python (os, shutil, pathlib, json)

---

## 📖 Utilisation

### Utilisation basique

Lance simplement le script :

```bash
python organiser_fichiers.py
```

Le script va :
1. Scanner ton dossier `Downloads`
2. Identifier chaque fichier par son extension
3. Créer des dossiers par catégorie
4. Déplacer chaque fichier dans le bon dossier
5. Afficher un résumé de l'organisation

### Exemple de sortie

```bash
🚀 Début de l'organisation...

✅ photo_vacances.jpg → Images/
✅ rapport_2024.pdf → Documents/
✅ musique.mp3 → Musique/
✅ archive.zip → Archives/
✅ script.py → Code/
⚠️  fichier_inconnu.xyz : pas de catégorie

🎉 5 fichiers organisés !
```

---

## ⚙️ Configuration

Le fichier `fichier.json` contient les catégories et extensions :

```json
{
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".svg", ".webp", ".bmp"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx", ".odt"],
    "Videos": [".mp4", ".avi", ".mkv", ".mov", ".wmv", ".flv"],
    "Musique": [".mp3", ".wav", ".flac", ".aac", ".ogg"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Code": [".py", ".js", ".html", ".css", ".json", ".xml"]
}
```

### Ajouter tes propres catégories

Tu veux une catégorie pour tes ebooks ? Ajoute simplement :

```json
{
    "Ebooks": [".epub", ".mobi", ".azw"],
    "Photos_RAW": [".raw", ".cr2", ".nef"],
    "3D": [".obj", ".fbx", ".blend"]
}
```

---

## 🛠️ Comment ça marche ?

### Architecture du code

```
1. Imports des bibliothèques (os, shutil, pathlib, json)
   ↓
2. Lecture du fichier JSON de configuration
   ↓
3. Récupération du chemin vers Downloads
   ↓
4. Pour chaque fichier dans Downloads :
   ├── Ignorer les dossiers
   ├── Extraire l'extension
   ├── Trouver la catégorie correspondante
   ├── Créer le dossier de destination si besoin
   ├── Gérer les doublons (renommer si nécessaire)
   └── Déplacer le fichier
   ↓
5. Afficher le résumé
```

### Gestion des doublons

Si un fichier du même nom existe déjà :
- `photo.jpg` → `photo_1.jpg`
- `photo_1.jpg` → `photo_2.jpg`
- etc.

Aucun fichier n'est jamais écrasé !

---

## 🎯 Cas d'usage

### Automatisation quotidienne

Ajoute le script à ton démarrage système ou crée une tâche planifiée :

**Windows (Task Scheduler) :**
```batch
python C:\chemin\vers\organiser_fichiers.py
```

**Mac/Linux (cron) :**
```bash
0 9 * * * /usr/bin/python3 /chemin/vers/organiser_fichiers.py
```

### Adaptation pour d'autres dossiers

Modifie la ligne dans le script :

```python
# Au lieu de Downloads
downloads = str(Path.home() / "Documents")  # Organise Documents
downloads = str(Path.home() / "Desktop")    # Organise Bureau
downloads = "/chemin/personnalise"          # N'importe quel dossier
```

---

## 📚 Apprendre avec ce projet

Ce projet est parfait pour apprendre :

| Concept | Ce que tu apprends |
|---------|-------------------|
| **Manipulation de fichiers** | `os.listdir()`, `os.path.join()`, `shutil.move()` |
| **Gestion des chemins** | `pathlib.Path`, compatibilité cross-platform |
| **Fichiers JSON** | Lire et parser du JSON avec Python |
| **Conditions et boucles** | `for`, `if`, gestion de la logique |
| **Gestion d'erreurs** | Vérifications, `exist_ok`, gestion des doublons |
| **Bonnes pratiques** | Séparation config/code, code propre et commenté |

---

## 🤝 Contribution

Les contributions sont les bienvenues ! Voici comment participer :

### Signaler un bug

Ouvre une [issue](https://github.com/ton-username/python-file-organizer/issues) avec :
- Description du problème
- Système d'exploitation
- Version de Python
- Message d'erreur si applicable

### Proposer une amélioration

Tu as une idée ? Ouvre une [issue](https://github.com/ton-username/python-file-organizer/issues) ou directement une Pull Request !

**Idées d'améliorations possibles :**
- [ ] Interface graphique (GUI)
- [ ] Mode "dry run" pour simuler sans déplacer
- [ ] Historique des opérations
- [ ] Support des règles complexes (taille, date)
- [ ] Notifications système
- [ ] Mode récursif (sous-dossiers)

---

## 📝 Changelog

### Version 1.0.0 (2025-02-21)
- ✨ Première version
- ✅ Organisation automatique par extension
- ✅ Configuration JSON
- ✅ Gestion des doublons
- ✅ Support multi-plateformes

---

## 🌟 Projets similaires

Si ce projet t'intéresse, tu aimeras peut-être :

- [Organize](https://github.com/tfeldmann/organize) - Outil plus avancé avec règles complexes
- [PySort](https://github.com/example/pysort) - Tri avec interface graphique
- [File Juggler](https://www.filejuggler.com/) - Solution commerciale

---

## 📧 Contact

**Abel KPOKOUTA**

- 🎥 YouTube : [CodeAvecAbel](https://youtube.com/@codeavecabel?si=n0W74nEc4tDFsSMp)
- 💼 LinkedIn : [Abel KPOKOUTA](https://www.linkedin.com/in/abel-kocou-kpokouta-6a388739a)
- 🐙 GitHub : [@ton-username](https://github.com/Abel-Dev-KPOKOUTA)
- 📧 Email : kpokoutaabel@gmail.com

---

## 📜 Licence

Ce projet est sous licence MIT - tu es libre de l'utiliser, le modifier et le distribuer.

Voir le fichier [LICENSE](LICENSE) pour plus de détails.

---

## ❤️ Remerciements

Un grand merci à :
- La communauté YouTube **CodeAvecAbel**
- Tous ceux qui ont regardé la vidéo et donné leur feedback
- Toi, pour utiliser ce script ! 🎉

---

## ⭐ Soutien

Si ce projet t'a été utile :
- ⭐ **Donne une étoile** au dépôt
- 🔔 **Abonne-toi** à la [chaîne YouTube](https://youtube.com/@codeavecabel?si=n0W74nEc4tDFsSMp)
- 📢 **Partage** avec tes amis développeurs
- 💬 **Laisse un commentaire** sur la vidéo

---

<div align="center">

**Fait avec ❤️ par Abel KPOKOUTA**

[🎥 YouTube](https://youtube.com/@codeavecabel?si=n0W74nEc4tDFsSMp) • [💼 LinkedIn](https://www.linkedin.com/in/abel-kocou-kpokouta-6a388739a) • [🐙 GitHub](https://github.com/Abel-Dev-KPOKOUTA)

</div>
