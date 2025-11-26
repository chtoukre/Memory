import time
import os
import argparse
import random
import csv
from datetime import datetime, date

def get_project_root():
    """
    Retourne le dossier racine du projet.
    On part du fichier courant: .../modules/chiffres.py -> racine = dossier parent de 'modules'.
    Si ton script n'est pas dans modules/, ça reste le dossier du script.
    """
    return os.path.dirname(os.path.abspath(__file__))

def ensure_results_folder():
    """
    Crée (si besoin) le dossier results/chiffre et le retourne.
    """
    # si ton script est dans modules/chiffres.py et que tu veux la racine au-dessus :
    root = os.path.dirname(get_project_root())  # parent du dossier du script
    results_dir = os.path.join(root, "results", "chiffre")
    os.makedirs(results_dir, exist_ok=True)
    return results_dir

def get_summary_filepath(results_dir):
    return os.path.join(results_dir, "memoire_summary.csv")

def get_attempt_index_for_today(summary_path, today_str):
    attempt_index = 0
    if not os.path.exists(summary_path):
        return 0
    with open(summary_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row.get('date') == today_str:
                try:
                    idx = int(row.get('attempt_day', 0))
                    if idx >= attempt_index:
                        attempt_index = idx + 1
                except:
                    pass
    return attempt_index

def memory_test(length=9, display_time=10, repetitions=30):
    print("===== TEST DE MÉMOIRE - SÉQUENCES DE CHIFFRES =====\n")

    # dossier results/chiffre
    results_dir = ensure_results_folder()

    summary_path = get_summary_filepath(results_dir)

    today_str = date.today().isoformat()
    attempt_day = get_attempt_index_for_today(summary_path, today_str)

    # nom du fichier détail
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    detail_filename = f"memoire_detail_{timestamp}_attempt{attempt_day}.csv"
    detail_path = os.path.join(results_dir, detail_filename)

    # créer fichier détail
    with open(detail_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([
            'timestamp', 'date', 'time', 'exercise_index',
            'length', 'display_time',
            'target_sequence', 'user_sequence',
            'correct_in_order', 'errors'
        ])

    correct_list = []

    for i in range(1, repetitions + 1):
        sequence = [random.randint(0, 9) for _ in range(length)]

        print(f"\nExercice {i}/{repetitions}")
        print(" ".join(str(n) for n in sequence))
        time.sleep(display_time)
        os.system('cls' if os.name == 'nt' else 'clear')

        user_input = input("Ta réponse : ")
        try:
            user_sequence = [int(x) for x in user_input.split()]
        except:
            user_sequence = []

        correct = 0
        for j in range(min(len(sequence), len(user_sequence))):
            if sequence[j] == user_sequence[j]:
                correct += 1
            else:
                break

        errors = length - correct
        correct_list.append(correct)

        with open(detail_path, 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            now = datetime.now()
            writer.writerow([
                now.isoformat(timespec='seconds'),
                today_str,
                now.time().strftime("%H:%M:%S"),
                i,
                length,
                display_time,
                " ".join(str(n) for n in sequence),
                " ".join(str(n) for n in user_sequence),
                correct,
                errors
            ])

    # résumé
    mean_correct = sum(correct_list) / len(correct_list) if correct_list else 0
    sorted_c = sorted(correct_list)
    if sorted_c:
        mid = len(sorted_c)//2
        median_correct = sorted_c[mid] if len(sorted_c)%2 else (sorted_c[mid-1]+sorted_c[mid])/2
    else:
        median_correct = 0
    note = (mean_correct/length)*100 if length > 0 else 0

    summary_exists = os.path.exists(summary_path)

    with open(summary_path, 'a', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=[
            'timestamp','date','time','attempt_day',
            'length','display_time','repetitions',
            'note_percent','mean_correct','median_correct'
        ])
        if not summary_exists:
            writer.writeheader()

        now = datetime.now()
        writer.writerow({
            'timestamp': now.isoformat(timespec='seconds'),
            'date': today_str,
            'time': now.time().strftime("%H:%M:%S"),
            'attempt_day': attempt_day,
            'length': length,
            'display_time': display_time,
            'repetitions': repetitions,
            'note_percent': f"{note:.2f}",
            'mean_correct': f"{mean_correct:.2f}",
            'median_correct': f"{median_correct:.2f}"
        })

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-l","--length",type=int,default=9)
    parser.add_argument("-t","--time",type=int,default=10)
    parser.add_argument("-n","--repetitions",type=int,default=30)
    args = parser.parse_args()
    memory_test(args.length,args.time,args.repetitions)

