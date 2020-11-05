from pathlib import Path
import pendulum

def rename(name: str) -> None:
    #  print(path.)
    p = Path('.')
    old = p / f'{name}.pdf'
    dt = pendulum.tomorrow()
    new = p / f'{name}{dt.isoformat()[0:10]}.pdf'
    if not old.exists():
        print(f'file {old} does not exist!')
        return
    if new.exists():
        print(f'file {new} has existed!')
        return
    old.rename(new)

if __name__ == "__main__":
    files = ['math', 'english', 'general']
    for f in files:
        rename(f)
