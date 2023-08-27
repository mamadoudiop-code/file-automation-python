import shutil
import os
import time
import logging

# Configuration de la journalisation
logging.basicConfig(filename='backup_log.txt', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def backup_files(source_dir, backup_dir):
    try:
        # Vérification si le répertoire de sauvegarde existe, sinon le créer
        if not os.path.exists(backup_dir):
            os.makedirs(backup_dir)

        # Copie des fichiers du répertoire source vers le répertoire de sauvegarde
        for filename in os.listdir(source_dir):
            source_path = os.path.join(source_dir, filename)
            backup_path = os.path.join(backup_dir, filename)

            # Vérification si le fichier existe déjà dans le répertoire de sauvegarde
            if os.path.exists(backup_path):
                logging.warning(f'Le fichier {filename} existe déjà dans le répertoire de sauvegarde.')
                continue

            shutil.copy2(source_path, backup_path)
            logging.info(f'Le fichier {filename} a été sauvegardé avec succès.')

    except Exception as e:
        logging.error(f'Une erreur est survenue lors de la sauvegarde : {str(e)}')

if __name__ == "__main__":
    source_directory = "source-directory"
    backup_directory = "save-directory"

    while True:
        backup_files(source_directory, backup_directory)
        logging.info('Sauvegarde effectuée.')

        # Temporisation pour la prochaine sauvegarde (par exemple, toutes les 24 heures)
        time.sleep(24 * 60 * 60)  # 24 heures en secondes
