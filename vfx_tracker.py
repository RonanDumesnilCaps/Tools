import json
import argparse
from pathlib import Path

DATA_FILE = Path('vfx_data.json')

DEFAULT_DATA = {
    "shots": {}
}


def load_data():
    if DATA_FILE.exists():
        with DATA_FILE.open('r', encoding='utf-8') as f:
            return json.load(f)
    else:
        return DEFAULT_DATA.copy()


def save_data(data):
    with DATA_FILE.open('w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def add_shot(shot_id):
    data = load_data()
    if shot_id in data['shots']:
        print(f"Shot {shot_id} already exists.")
        return
    data['shots'][shot_id] = []
    save_data(data)
    print(f"Shot {shot_id} added.")


def add_task(shot_id, task_name):
    data = load_data()
    if shot_id not in data['shots']:
        print(f"Shot {shot_id} does not exist. Use add-shot to create it.")
        return
    data['shots'][shot_id].append({'name': task_name, 'status': 'todo'})
    save_data(data)
    print(f"Task '{task_name}' added to shot {shot_id}.")


def update_task(shot_id, task_index, status):
    data = load_data()
    if shot_id not in data['shots']:
        print(f"Shot {shot_id} does not exist.")
        return
    tasks = data['shots'][shot_id]
    if not (0 <= task_index < len(tasks)):
        print(f"Task index {task_index} out of range for shot {shot_id}.")
        return
    tasks[task_index]['status'] = status
    save_data(data)
    print(f"Task {task_index} in shot {shot_id} updated to {status}.")


def list_data():
    data = load_data()
    for shot_id, tasks in data['shots'].items():
        print(f"Shot {shot_id}:")
        for i, task in enumerate(tasks):
            print(f"  [{i}] {task['name']} - {task['status']}")


def main():
    parser = argparse.ArgumentParser(description="Simple VFX post-production tracker")
    subparsers = parser.add_subparsers(dest='command')

    parser_add_shot = subparsers.add_parser('add-shot', help='Add a new shot')
    parser_add_shot.add_argument('shot_id')

    parser_add_task = subparsers.add_parser('add-task', help='Add a task to a shot')
    parser_add_task.add_argument('shot_id')
    parser_add_task.add_argument('task_name')

    parser_update = subparsers.add_parser('update-task', help='Update task status')
    parser_update.add_argument('shot_id')
    parser_update.add_argument('task_index', type=int)
    parser_update.add_argument('status', choices=['todo', 'in_progress', 'done'])

    subparsers.add_parser('list', help='List all shots and tasks')

    args = parser.parse_args()

    if args.command == 'add-shot':
        add_shot(args.shot_id)
    elif args.command == 'add-task':
        add_task(args.shot_id, args.task_name)
    elif args.command == 'update-task':
        update_task(args.shot_id, args.task_index, args.status)
    elif args.command == 'list':
        list_data()
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
