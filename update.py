from pathlib import Path
import pendulum
import argparse

def rename(name: str, args) -> None:
    #  print(path.)
    p = Path('.')
    old = p / f'{name}.pdf'
    dt = pendulum.today().add(days=args.offset[0])
    new = p / f'{name}{dt.isoformat()[0:10]}.pdf'
    if not old.exists():
        print(f'file {old} does not exist!')
        return
    if new.exists():
        print(f'file {new} has existed!')
        return
    old.rename(new)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = 'update file')
    parser.add_argument('offset', metavar='N', type=int, nargs=1, help='offset of the date')
    args = parser.parse_args()
    files = ['math', 'english', 'general']
    for f in files:
        rename(f, args)
